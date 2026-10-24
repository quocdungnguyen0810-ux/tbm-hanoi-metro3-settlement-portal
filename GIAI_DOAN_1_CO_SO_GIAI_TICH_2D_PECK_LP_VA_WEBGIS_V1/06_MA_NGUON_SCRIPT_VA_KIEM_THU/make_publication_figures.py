"""Publication figure generator for Gate 5 (WF-17)."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import matplotlib.pyplot as plt
import numpy as np
from scripts.analytical_engine import PeckModel, twin_tunnel_settlement

OUT_DIR = ROOT / "research_outputs" / "2026-10-13_152753"
FIG_DIR = OUT_DIR / "05_figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def plot_envelope():
    D = 6.30
    z0 = 18.0
    K = 0.60
    d_twin = 13.0
    x = np.linspace(-50, 50, 501)

    plt.figure(figsize=(10, 6))
    
    # Plot twin tunnel at VL = 0.5%, 1.0%, 1.5%, 2.0%
    colors = ['#2ca02c', '#1f77b4', '#ff7f0e', '#d62728']
    vl_list = [0.005, 0.010, 0.015, 0.020]
    
    for vl, col in zip(vl_list, colors):
        model = PeckModel(D, z0, K, vl)
        s_twin = [twin_tunnel_settlement(model, model, d_twin, xi) * 1000.0 for xi in x]
        plt.plot(x, s_twin, label=f'Twin Tunnel VL = {vl*100:.1f}%', color=col, linewidth=2.2)

    # Risk zones shading
    plt.axhspan(20, 50, color='red', alpha=0.12, label='Severe Damage Risk (>20 mm)')
    plt.axhspan(10, 20, color='orange', alpha=0.12, label='Moderate Damage Risk (10–20 mm)')
    plt.axhspan(5, 10, color='yellow', alpha=0.12, label='Slight Damage Risk (5–10 mm)')
    plt.axhspan(0, 5, color='green', alpha=0.08, label='Negligible Risk (<5 mm)')

    # Tunnel locations indicator
    plt.axvline(x=-d_twin/2, color='gray', linestyle=':', label='Left Tunnel Axis (-6.5 m)')
    plt.axvline(x=d_twin/2, color='gray', linestyle=':', label='Right Tunnel Axis (+6.5 m)')

    plt.title("Twin Tunnel Settlement Trough Envelope & Building Damage Risk Zones (S11–S12, z₀=18m, K=0.60)", fontsize=11, fontweight='bold')
    plt.xlabel("Transverse Distance from Route Centerline x (m)", fontsize=10)
    plt.ylabel("Ground Settlement S(x) (mm)", fontsize=10)
    plt.gca().invert_yaxis()
    plt.legend(loc='lower left', fontsize=9, framealpha=0.9)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()

    out_file = FIG_DIR / "spatial_settlement_envelope.png"
    plt.savefig(out_file, dpi=350)
    plt.close()
    print(f"Saved: {out_file.name}")


if __name__ == "__main__":
    plot_envelope()
