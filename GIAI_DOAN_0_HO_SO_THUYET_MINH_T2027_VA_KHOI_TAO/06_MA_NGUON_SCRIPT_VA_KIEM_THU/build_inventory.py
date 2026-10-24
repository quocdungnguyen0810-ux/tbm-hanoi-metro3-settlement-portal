"""Create a reproducible inventory without modifying source files."""

from __future__ import annotations

import csv
import hashlib
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "research_outputs" / "2026-10-13_152753" / "01_project_inventory" / "File_Inventory.csv"
EXCLUDED_PARTS = {".git", "__pycache__", ".pytest_cache", "research_outputs"}


def classify(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in {".csv", ".tsv", ".xlsx", ".xls", ".xlsm"}:
        return "tabular_data"
    if suffix == ".pdf":
        return "reference_or_report"
    if suffix in {".md", ".txt", ".doc", ".docx", ".tex"}:
        return "document_or_manuscript"
    if suffix in {".json", ".xml", ".yaml", ".yml", ".toml"}:
        return "configuration_or_structured_data"
    if suffix in {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".svg"}:
        return "image_or_figure"
    if suffix in {".shp", ".dbf", ".shx", ".prj", ".gpkg", ".geojson"}:
        return "spatial_data"
    if suffix in {".py", ".ipynb", ".r"}:
        return "code_or_notebook"
    return "other"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def include(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    return not any(part in EXCLUDED_PARTS for part in relative.parts) and not path.name.startswith("~$")


def main() -> None:
    rows = []
    for path in sorted(item for item in ROOT.rglob("*") if item.is_file() and include(item)):
        stat = path.stat()
        relative = path.relative_to(ROOT).as_posix()
        rows.append({
            "file_name": path.name,
            "relative_path": relative,
            "file_type": classify(path),
            "size_bytes": stat.st_size,
            "modified_at": datetime.fromtimestamp(stat.st_mtime).isoformat(),
            "sha256": sha256(path),
            "expected_role": "source" if relative.startswith("research/") else "project_control_or_code",
            "readability": "direct",
            "processing_status": "unprocessed",
            "notes": ""
        })
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0].keys()) if rows else ["file_name"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} records to {OUTPUT.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
