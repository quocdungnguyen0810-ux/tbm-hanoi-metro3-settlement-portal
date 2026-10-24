"""Baseline freezing script for Gate 3 (WF-09)."""

import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "research_outputs" / "2026-10-13_152753" / "03_processed_data"
FROZEN_DIR = ROOT / "research_outputs" / "2026-10-13_152753" / "03_processed_data" / "frozen_baseline"
FROZEN_DIR.mkdir(parents=True, exist_ok=True)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def freeze():
    files_to_freeze = [
        "normalized_sources.csv",
        "normalized_parameters.csv"
    ]
    
    manifest = {
        "frozen_at": datetime.now(timezone.utc).isoformat(),
        "gate": "GATE_3_BASELINE_FREEZE",
        "files": []
    }
    
    checksum_lines = []
    
    for fname in files_to_freeze:
        src = SRC_DIR / fname
        dst = FROZEN_DIR / fname
        shutil.copy2(src, dst)
        digest = sha256(dst)
        manifest["files"].append({
            "name": fname,
            "sha256": digest,
            "size_bytes": dst.stat().st_size
        })
        checksum_lines.append(f"{digest}  {fname}")
        
    (FROZEN_DIR / "checksums.sha256").write_text("\n".join(checksum_lines) + "\n", encoding="utf-8")
    (FROZEN_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Successfully froze {len(files_to_freeze)} files to {FROZEN_DIR.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    freeze()
