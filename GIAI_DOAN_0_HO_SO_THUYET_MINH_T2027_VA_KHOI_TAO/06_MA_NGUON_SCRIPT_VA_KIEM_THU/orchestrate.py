"""Deterministic router for the guarded AUTO workflow.

The script does not call an LLM. It selects dependency-ready work, routes it
to a configured role, and records a reproducible handoff package for a host.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
QUEUE_PATH = ROOT / ".agents" / "task_queue.json"
AGENTS_PATH = ROOT / ".agents" / "agents.json"
STATE_PATH = ROOT / "AGENT_STATE.json"
HANDOFF_DIR = ROOT / "research_outputs" / "2026-10-13_152753" / "09_logs" / "handoffs"
TERMINAL = {"COMPLETED", "WAIVED"}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def route(task_type: str, agents: dict[str, Any]) -> str:
    for rule in agents["routing"]:
        if task_type in rule["match"]:
            return rule["to"]
    return agents["orchestrator"]


def dependency_ready(task: dict[str, Any], tasks: dict[str, dict[str, Any]]) -> bool:
    return all(tasks[dep]["status"] in TERMINAL for dep in task["depends_on"])


def ready_tasks(queue: dict[str, Any]) -> list[dict[str, Any]]:
    by_id = {task["id"]: task for task in queue["tasks"]}
    candidates = [
        task for task in queue["tasks"]
        if task["status"] in {"READY", "PLANNED"} and dependency_ready(task, by_id)
    ]
    return sorted(candidates, key=lambda item: (item["priority"], item["gate"], item["id"]))


def dispatch() -> dict[str, Any]:
    queue = load_json(QUEUE_PATH)
    agents = load_json(AGENTS_PATH)
    state = load_json(STATE_PATH)
    candidates = ready_tasks(queue)
    if not candidates:
        return {"status": "NO_READY_TASK", "reason": "dependencies, blockers, or completion"}

    task = candidates[0]
    assignee = route(task["type"], agents)
    timestamp = datetime.now(timezone.utc).isoformat()
    task["status"] = "DISPATCHED"
    task["assigned_to"] = assignee
    task["dispatched_at"] = timestamp
    handoff = {
        "task_id": task["id"],
        "title": task["title"],
        "gate": task["gate"],
        "task_type": task["type"],
        "assigned_to": assignee,
        "dependencies": task["depends_on"],
        "rules": [
            "Do not modify source/raw data.",
            "Record evidence and source locators.",
            "Do not mark an audit gate passed without checks.",
            "Write only to role-appropriate generated-output paths."
        ],
        "created_at": timestamp
    }
    HANDOFF_DIR.mkdir(parents=True, exist_ok=True)
    handoff_path = HANDOFF_DIR / f"{task['id']}_{assignee}.json"
    save_json(handoff_path, handoff)
    queue["handoff_log"].append({**handoff, "handoff_file": str(handoff_path.relative_to(ROOT))})
    state["execution"]["current_task"] = task["id"]
    state["execution"]["next_action"] = f"Execute {task['id']} with {assignee}"
    state["updated_at"] = timestamp
    state["handoff_log"].append({
        "timestamp": timestamp,
        "from": "general_contractor",
        "to": assignee,
        "task": task["id"],
        "status": "DISPATCHED"
    })
    save_json(QUEUE_PATH, queue)
    save_json(STATE_PATH, state)
    return {
        "status": "DISPATCHED",
        "task": task["id"],
        "agent": assignee,
        "handoff": handoff_path.relative_to(ROOT).as_posix(),
    }


def set_status(task_id: str, status_value: str, evidence: str | None) -> dict[str, Any]:
    allowed = {"READY", "IN_PROGRESS", "COMPLETED", "BLOCKED", "FAILED", "WAIVED"}
    if status_value not in allowed:
        raise ValueError(f"Unsupported status: {status_value}")
    queue = load_json(QUEUE_PATH)
    for task in queue["tasks"]:
        if task["id"] == task_id:
            task["status"] = status_value
            if evidence:
                task.setdefault("evidence", []).append(evidence)
            save_json(QUEUE_PATH, queue)
            return {"task": task_id, "status": status_value, "evidence": evidence}
    raise KeyError(f"Unknown task: {task_id}")


def status() -> dict[str, Any]:
    queue = load_json(QUEUE_PATH)
    counts: dict[str, int] = {}
    for task in queue["tasks"]:
        counts[task["status"]] = counts.get(task["status"], 0) + 1
    return {"counts": counts, "ready": [task["id"] for task in ready_tasks(queue)]}


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status")
    sub.add_parser("dispatch")
    update = sub.add_parser("set-status")
    update.add_argument("task_id")
    update.add_argument("status")
    update.add_argument("--evidence")
    args = parser.parse_args()
    if args.command == "status":
        result = status()
    elif args.command == "dispatch":
        result = dispatch()
    else:
        result = set_status(args.task_id, args.status, args.evidence)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
