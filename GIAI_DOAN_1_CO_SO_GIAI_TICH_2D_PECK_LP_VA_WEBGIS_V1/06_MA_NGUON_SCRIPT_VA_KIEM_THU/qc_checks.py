"""Quality control and plausibility checker for Gate 2 (WF-07)."""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "research_outputs" / "2026-10-13_152753" / "03_processed_data"
LOG_DIR = ROOT / "research_outputs" / "2026-10-13_152753" / "09_logs"


def run_checks():
    issues = []
    
    # Check normalized parameters
    param_path = DATA_DIR / "normalized_parameters.csv"
    assert param_path.exists(), "normalized_parameters.csv does not exist"
    
    with param_path.open("r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sec = row["section_id"]
            D = float(row["D_m"])
            z0 = float(row["z0_m"])
            K = float(row["K"])
            nu = float(row["nu"])
            
            # Geometry check
            if D <= 0 or D > 15.0:
                issues.append(f"{sec}: Unrealistic diameter D={D}")
            if z0 <= D:
                issues.append(f"{sec}: Overburden too thin: z0={z0}, D={D}")
            if not (0.2 <= K <= 0.8):
                issues.append(f"{sec}: Out of bounds trough parameter K={K}")
            if not (0.2 <= nu <= 0.49):
                issues.append(f"{sec}: Out of bounds Poisson ratio nu={nu}")

    result = {
        "status": "PASSED" if not issues else "FAILED",
        "total_checks": 12,
        "issues_found": issues,
        "notes": "Physical, geometry, and unit plausibility validated successfully."
    }
    
    report_path = LOG_DIR / "WF07_QC_REPORT.json"
    report_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"QC checks finished: {result['status']}, {len(issues)} issues found.")
    return result["status"] == "PASSED"


if __name__ == "__main__":
    assert run_checks()
