"""Sensitivity analysis script for Gate 4 (WF-13).

Runs OAT (One-At-A-Time) scenarios for VL in [0.5%, 0.75%, 1.0%, 1.25%, 1.5%, 1.75%, 2.0%].
Generates publication plots and CSV summary tables.
"""

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import matplotlib.pyplot as plt
import numpy as np
from scripts.analytical_engine import PeckModel, LoganathanPoulosModel, twin_tunnel_settlement

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "research_outputs" / "2026-10-13_152753"
DATA_DIR = OUT_DIR / "03_processed_data"
FIG_DIR = OUT_DIR / "05_figures"
TABLE_DIR = OUT_DIR / "06_tables"
FIG_DIR.mkdir(parents=True, exist_ok=True)
TABLE_DIR.mkdir(parents=True, exist_ok=True)


def run_scenarios():
    vl_list = [0.005, 0.0075, 0.010, 0.0125, 0.015, 0.0175, 0.020]
    sections = [
        {"id": "S9_S10", "name": "Kim Mã - Cát Linh", "z0": 15.0, "K": 0.50, "nu": 0.35},
        {"id": "S10_S11", "name": "Cát Linh - Văn Miếu", "z0": 16.5, "K": 0.55, "nu": 0.36},
        {"id": "S11_S12", "name": "Văn Miếu - Ga Hà Nội", "z0": 18.0, "K": 0.60, "nu": 0.38}
    ]
    D = 6.30
    d_twin = 13.0
    x_grid = np.linspace(-40.0, 40.0, 401)
    
    summary_rows = []
    profile_rows = []
    
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    
    # 1. Plot comparison: Peck vs LP for each section at VL = 1.0%
    fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
    for idx, sec in enumerate(sections):
        peck = PeckModel(D, sec["z0"], sec["K"], 0.01)
        lp = LoganathanPoulosModel(D, sec["z0"], sec["nu"], 0.01)
        
        s_peck = np.array(peck.profile(x_grid)) * 1000.0  # mm
        s_lp = np.array(lp.profile(x_grid)) * 1000.0      # mm
        s_twin_peck = np.array([twin_tunnel_settlement(peck, peck, d_twin, x) for x in x_grid]) * 1000.0
        
        ax = axes[idx]
        ax.plot(x_grid, s_peck, 'b-', label='Peck (Single)', linewidth=2)
        ax.plot(x_grid, s_lp, 'r--', label='Loganathan-Poulos (Single)', linewidth=2)
        ax.plot(x_grid, s_twin_peck, 'g-.', label='Peck (Twin Tunnel)', linewidth=2)
        
        ax.set_title(f"{sec['name']}\n(z0={sec['z0']}m, K={sec['K']}, VL=1.0%)", fontsize=11, fontweight='bold')
        ax.set_xlabel("Offset from Tunnel Centerline x (m)")
        if idx == 0:
            ax.set_ylabel("Settlement S (mm)")
        ax.invert_yaxis()
        ax.legend(fontsize=9)
        ax.grid(True, linestyle='--', alpha=0.6)
        
    plt.tight_layout()
    comp_path = FIG_DIR / "peck_vs_lp_profiles.png"
    plt.savefig(comp_path, dpi=300)
    plt.close()
    print(f"Saved figure: {comp_path.name}")
    
    # 2. Multi-scenario evaluation and CSV export
    for sec in sections:
        for vl in vl_list:
            peck = PeckModel(D, sec["z0"], sec["K"], vl)
            lp = LoganathanPoulosModel(D, sec["z0"], sec["nu"], vl)
            
            smax_single_mm = peck.Smax * 1000.0
            smax_twin_mm = twin_tunnel_settlement(peck, peck, d_twin, 0.0) * 1000.0
            smax_lp_mm = lp.settlement(0.0) * 1000.0
            i_m = peck.i
            max_slope = abs(peck.slope(peck.i))  # mm/m (dimensionless)
            
            # Width to 5mm, 10mm thresholds (Peck single)
            # S(x) = Smax * exp(-x^2 / (2i^2)) >= S_thresh ==> |x| <= i * sqrt(2 * ln(Smax / S_thresh))
            w_5mm = 2.0 * i_m * np.sqrt(2.0 * np.log(max(1.0001, smax_single_mm / 5.0))) if smax_single_mm > 5.0 else 0.0
            w_10mm = 2.0 * i_m * np.sqrt(2.0 * np.log(max(1.0001, smax_single_mm / 10.0))) if smax_single_mm > 10.0 else 0.0
            
            summary_rows.append({
                "section_id": sec["id"],
                "section_name": sec["name"],
                "depth_z0_m": sec["z0"],
                "trough_K": sec["K"],
                "VL_pct": round(vl * 100.0, 2),
                "VL_ratio": vl,
                "trough_width_i_m": round(i_m, 2),
                "Smax_Peck_single_mm": round(smax_single_mm, 2),
                "Smax_Peck_twin_mm": round(smax_twin_mm, 2),
                "Smax_LP_single_mm": round(smax_lp_mm, 2),
                "max_slope_rad": round(max_slope, 6),
                "width_impact_5mm_m": round(w_5mm, 2),
                "width_impact_10mm_m": round(w_10mm, 2),
                "risk_level": "Severe" if smax_single_mm > 20 else ("Moderate" if smax_single_mm > 10 else "Slight")
            })

    # Save summary table
    summary_csv = TABLE_DIR / "settlement_scenarios_summary.csv"
    with summary_csv.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(summary_rows[0].keys()))
        writer.writeheader()
        writer.writerows(summary_rows)
    print(f"Saved table: {summary_csv.name} ({len(summary_rows)} scenario records)")

    # 3. Sensitivity Tornado / Curve plot: Smax vs VL for all sections
    plt.figure(figsize=(8, 5))
    for sec in sections:
        vl_vals = [r["VL_pct"] for r in summary_rows if r["section_id"] == sec["id"]]
        smax_vals = [r["Smax_Peck_single_mm"] for r in summary_rows if r["section_id"] == sec["id"]]
        plt.plot(vl_vals, smax_vals, marker='o', linewidth=2, label=f"{sec['name']} (z0={sec['z0']}m)")
    
    plt.axhline(y=10.0, color='orange', linestyle='--', label='Warning Threshold 10mm')
    plt.axhline(y=20.0, color='red', linestyle='--', label='Critical Threshold 20mm')
    plt.title("Sensitivity of Maximum Settlement Smax to Volume Loss VL (Peck Model)", fontsize=12, fontweight='bold')
    plt.xlabel("Volume Loss VL (%)", fontsize=11)
    plt.ylabel("Maximum Settlement Smax (mm)", fontsize=11)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    sens_path = FIG_DIR / "sensitivity_smax_vs_vl.png"
    plt.savefig(sens_path, dpi=300)
    plt.close()
    print(f"Saved figure: {sens_path.name}")


if __name__ == "__main__":
    run_scenarios()
