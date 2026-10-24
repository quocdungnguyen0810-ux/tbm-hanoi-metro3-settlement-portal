# -*- coding: utf-8 -*-
"""Unit test độc lập kiểm thử bộ giải Phần tử hữu hạn 2D (PLAXIS MC vs. HS-DCM),
đối sánh giải tích Peck/Loganathan-Poulos và đường cong Fragility Curves Giai đoạn 5.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.stage5_publication_and_plaxis_orchestrator import (
    build_verified_plaxis_soil_layers,
    compute_peck_and_lp_profiles,
    compute_probabilistic_fragility_curves,
    run_comprehensive_plaxis_benchmark,
    solve_2d_continuum_fem_tunnel,
)


class TestStage5PublicationAndPlaxis(unittest.TestCase):
    """Kiểm thử tính đúng đắn cơ học của bộ giải 2D FEM, bảng thông số PLAXIS và Fragility Curves."""

    def test_verified_plaxis_soil_layers_provenance_and_bounds(self) -> None:
        """Kiểm tra 11 lớp đất tại S9-S10 và BH12 có E_ur = 3 * E_50 và đủ 5 trường provenance."""
        layers = build_verified_plaxis_soil_layers()
        self.assertEqual(len(layers), 11)
        for lay in layers:
            self.assertGreater(lay.e50_ref_kpa, 0.0)
            self.assertAlmostEqual(lay.eur_ref_kpa, 3.0 * lay.e50_ref_kpa, places=1)
            self.assertTrue(0.15 <= lay.nu_isotrop < 0.49)
            self.assertTrue(lay.source_id.startswith("SRC_"))
            self.assertIn(lay.value_basis, {"direct_table", "derived"})

    def test_2d_continuum_fem_mc_vs_hs_mechanics(self) -> None:
        """Kiểm tra tính chất vật lý cốt lõi: Mô hình MC cho phễu lún rộng hơn (i_x lớn hơn)
        và S_max nhỏ hơn so với mô hình Hardening Soil (HS_DCM) tại cùng mất mát thể tích VL=1.0%.
        """
        x_grid = np.linspace(-50.0, 50.0, 201)
        z_grid = np.linspace(0.0, 42.0, 85)
        res_mc = solve_2d_continuum_fem_tunnel(
            x_grid, z_grid, z0_m=18.0, radius_m=3.15, vl_ratio=0.010,
            constitutive_mode="MC", section_id="SEC_S11_S12_BH12",
        )
        res_hs = solve_2d_continuum_fem_tunnel(
            x_grid, z_grid, z0_m=18.0, radius_m=3.15, vl_ratio=0.010,
            constitutive_mode="HS_DCM", section_id="SEC_S11_S12_BH12",
        )
        # Độ lún cực đại tại tim (x=0) phải dương và nằm trong dải vật lý hợp lý (8 - 18 mm cho hầm đơn VL=1%)
        self.assertGreater(float(res_hs["s_max_mm"]), float(res_mc["s_max_mm"]))
        self.assertGreater(float(res_hs["s_max_mm"]), 9.0)
        self.assertLess(float(res_hs["s_max_mm"]), 18.0)
        # Phễu lún MC rộng hơn phễu lún HS_DCM (i_x_MC > i_x_HS)
        self.assertGreater(float(res_mc["inflection_ix_m"]), float(res_hs["inflection_ix_m"]))

    def test_comprehensive_plaxis_benchmark_metrics(self) -> None:
        """Kiểm tra ma trận đối sánh gồm 33 bản ghi (2 mặt cắt x 4 mức VL x 4 phương pháp + 1 mốc 3D FEM Midas)."""
        metrics, curves = run_comprehensive_plaxis_benchmark()
        self.assertEqual(len(metrics), 33)
        self.assertIn("SEC_S9_S10_KIMMA", curves["sections"])
        self.assertIn("SEC_S11_S12_BH12", curves["sections"])
        # Kiểm tra sự hội tụ cao giữa LP_1998 và PLAXIS_HS_DCM (R^2 > 0.90)
        lp_bh12_vl1 = [
            m for m in metrics
            if m.section_id == "SEC_S11_S12_BH12" and m.method_id == "LP_1998" and abs(m.vl_percent - 1.0) < 1e-6
        ][0]
        self.assertGreater(lp_bh12_vl1.r2_vs_hs, 0.90)

    def test_probabilistic_fragility_curves_monotonicity(self) -> None:
        """Kiểm tra xác suất vượt ngưỡng hư hại tăng đơn điệu khi VL tăng từ 0.25% lên 2.50%."""
        records = compute_probabilistic_fragility_curves(seed=202705)
        self.assertEqual(len(records), 10)
        for i in range(len(records) - 1):
            self.assertLessEqual(records[i].mean_smax_twin_mm, records[i + 1].mean_smax_twin_mm)
            self.assertLessEqual(records[i].prob_cat2_moderate_pct, records[i + 1].prob_cat2_moderate_pct)
            # Tại cùng một mức VL, P(Cat >= 1) >= P(Cat >= 2) >= P(Cat >= 3) >= P(Cat >= 4)
            self.assertGreaterEqual(records[i].prob_cat1_slight_pct, records[i].prob_cat2_moderate_pct)
            self.assertGreaterEqual(records[i].prob_cat2_moderate_pct, records[i].prob_cat3_severe_pct)
            self.assertGreaterEqual(records[i].prob_cat3_severe_pct, records[i].prob_cat4_very_severe_pct)


if __name__ == "__main__":
    unittest.main()

