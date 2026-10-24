import importlib.util
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "orchestrate.py"
SPEC = importlib.util.spec_from_file_location("orchestrate", MODULE_PATH)
orchestrate = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(orchestrate)


def test_route_known_type():
    agents = orchestrate.load_json(orchestrate.AGENTS_PATH)
    assert orchestrate.route("gis", agents) == "gis_analyst"
    assert orchestrate.route("formula_verification", agents) == "mechanics_reviewer"


def test_ready_tasks_respect_dependencies():
    queue = {
        "tasks": [
            {"id": "A", "status": "COMPLETED", "depends_on": [], "priority": 1, "gate": 1},
            {"id": "B", "status": "PLANNED", "depends_on": ["A"], "priority": 1, "gate": 1},
            {"id": "C", "status": "PLANNED", "depends_on": ["B"], "priority": 1, "gate": 1},
        ]
    }
    assert [task["id"] for task in orchestrate.ready_tasks(queue)] == ["B"]
