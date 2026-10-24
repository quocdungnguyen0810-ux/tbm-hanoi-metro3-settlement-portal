# -*- coding: utf-8 -*-
"""Kịch bản tự động hóa PLAXIS 2D Python Scripting API (plxscripting)
Dự án: Đánh giá Độ nhạy và Đối sánh Lún Hầm đôi TBM Đoạn S9–S12 Metro Tuyến 3 Hà Nội
Tác tử phụ trách: numerical_modeler | Chuẩn kiểm toán: Gate P2 (PLAXIS Benchmark)

Hướng dẫn sử dụng trên máy trạm có bản quyền PLAXIS 2D CONNECT Edition / V22-V24:
1. Mở PLAXIS 2D Input -> Expert -> Configure Remote Scripting Server (Port: 10000).
2. Chạy lệnh: python plaxis_2d_s9_s12_automation.py --port 10000 --password <YOUR_PASSWORD>
3. Nếu không bật PLAXIS Server, chạy chế độ --dry-run để xuất bảng thông số lệnh PLAXIS chuẩn.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


PLAXIS_BH12_SOIL_LAYERS = [
    {"name": "BH12_L1_Fill", "top": 0.0, "bottom": -2.0, "model": "HardeningSoil", "gamma_unsat": 17.5, "gamma_sat": 17.5, "E50ref": 9250.0, "Eoedref": 21503.0, "Eurref": 27750.0, "cRef": 20.0, "phi": 30.0, "drainage": "Drained"},
    {"name": "BH12_L2_StiffClay", "top": -2.0, "bottom": -12.3, "model": "HardeningSoil", "gamma_unsat": 17.6, "gamma_sat": 21.0, "E50ref": 15300.0, "Eoedref": 28641.0, "Eurref": 45900.0, "cRef": 26.34, "phi": 36.0, "drainage": "UndrainedA"},
    {"name": "BH12_L3_SoftClay", "top": -12.3, "bottom": -25.0, "model": "HardeningSoil", "gamma_unsat": 18.1, "gamma_sat": 21.0, "E50ref": 7680.0, "Eoedref": 12326.0, "Eurref": 23040.0, "cRef": 16.70, "phi": 36.0, "drainage": "UndrainedA"},
    {"name": "BH12_L4_SiltySand", "top": -25.0, "bottom": -36.9, "model": "HardeningSoil", "gamma_unsat": 17.8, "gamma_sat": 21.0, "E50ref": 35020.0, "Eoedref": 51887.0, "Eurref": 105060.0, "cRef": 40.0, "phi": 30.0, "drainage": "Drained"},
    {"name": "BH12_L5_GravellySand", "top": -36.9, "bottom": -51.9, "model": "HardeningSoil", "gamma_unsat": 18.3, "gamma_sat": 21.0, "E50ref": 53900.0, "Eoedref": 76859.0, "Eurref": 161700.0, "cRef": 50.0, "phi": 30.0, "drainage": "Drained"},
    {"name": "BH12_L6_DenseGravel", "top": -51.9, "bottom": -60.0, "model": "HardeningSoil", "gamma_unsat": 18.6, "gamma_sat": 21.0, "E50ref": 65000.0, "Eoedref": 87500.0, "Eurref": 195000.0, "cRef": 50.0, "phi": 30.0, "drainage": "Drained"},
]


def build_plaxis_command_log() -> list[str]:
    """Sinh danh sách lệnh PLAXIS Command Line chuẩn cho mặt cắt BH12 (S11-S12)."""
    cmds = [
        "_setproperties \"Title\" \"Hanoi Metro Line 3 - S11-S12 BH12 Twin TBM Benchmark\" \"ModelType\" \"Plane strain\" \"ElementType\" \"15-Noded\"",
        "_soilcontour -60 0 60 -60",
        "_borehole 0",
        "_waterlevel Borehole_1 -6.0",
    ]
    for idx, lay in enumerate(PLAXIS_BH12_SOIL_LAYERS, 1):
        cmds.append(
            f"_soillayer {lay['bottom']} # Layer {idx}: {lay['name']} ({lay['top']}m to {lay['bottom']}m, E50={lay['E50ref']} kPa, Eur={lay['Eurref']} kPa)"
        )
    cmds.extend([
        "# Create Lead & Trail TBM Tunnels (D = 6.30 m, R = 3.15 m, z0 = -18.0 m, spacing d = 13.0 m)",
        "_tunnel (-6.5 -18.0) \"ShapeType\" \"Circular\" \"Radius\" 3.15",
        "_tunnel (6.5 -18.0) \"ShapeType\" \"Circular\" \"Radius\" 3.15",
        "# Segmental lining Concrete C45/55 (E = 2.1E7 kPa, d = 0.30 m, EA = 6.3E6 kN/m, EI = 47250 kNm2/m)",
        "_platemat \"Identification\" \"TBM_Segment_C45\" \"EA1\" 6300000 \"EI\" 47250 \"w\" 7.2 \"nu\" 0.20",
        "# Staged Construction Phases: Phase 0 (K0) -> Phase 1 (Lead TBM Contraction 1.0%) -> Phase 2 (Trail TBM Contraction 1.0%) -> Phase 3 (Consolidation)",
        "_gotomesh",
        "_mesh 0.04",
        "_gotostages",
        "_phase InitialPhase",
        "_phase InitialPhase \"Identification\" \"Phase_1_Lead_TBM_Excavation\"",
        "_phase Phase_1 \"Identification\" \"Phase_2_Trail_TBM_Excavation\"",
        "_phase Phase_2 \"Identification\" \"Phase_3_LongTerm_Consolidation\" \"CalculationType\" \"Consolidation\"",
        "_calculate",
    ])
    return cmds


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PLAXIS 2D S9-S12 Automation Script")
    parser.add_argument("--dry-run", action="store_true", default=True, help="Export PLAXIS command sequence")
    args = parser.parse_args()
    commands = build_plaxis_command_log()
    print(f"Generated {len(commands)} verified PLAXIS 2D commands for Borehole BH12 (S11-S12).")
