"""Master reproducible execution pipeline for TBM Hanoi EIA (Gate 5 / WF-19).

Executes all pipeline components in sequence:
1. Data normalization
2. Quality control checks
3. Baseline freezing and hashing
4. Analytical settlement calculations and sensitivity analysis
5. Spatial GeoJSON and WebGIS Leaflet map generation
6. Surrogate AI model training and evaluation
7. Publication figure generation
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_step(desc: str, script_name: str):
    print(f"\n==========================================")
    print(f"[*] RUNNING: {desc} ({script_name})")
    print(f"==========================================")
    script_path = ROOT / "scripts" / script_name
    result = subprocess.run([sys.executable, str(script_path)], cwd=ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"[!] FAILED: {script_name}")
        print(result.stderr)
        raise RuntimeError(f"Step {script_name} failed with return code {result.returncode}")
    print(result.stdout.strip())
    print(f"[+] COMPLETED: {desc}")


def main():
    print("STARTING 100% REPRODUCIBLE PIPELINE EXECUTION...")
    run_step("Data Normalization", "normalize_data.py")
    run_step("Quality Control Checks", "qc_checks.py")
    run_step("Baseline Freezing", "freeze_baseline.py")
    run_step("Sensitivity Analysis & Scenarios", "sensitivity_analysis.py")
    run_step("Spatial Engine & WebGIS Leaflet", "spatial_engine.py")
    run_step("Surrogate AI Model", "surrogate_ai.py")
    run_step("Publication Figures", "make_publication_figures.py")
    print("\n[SUCCESS] ALL PIPELINE STEPS EXECUTED AND REPRODUCED 100% CLEANLY!")


if __name__ == "__main__":
    main()
