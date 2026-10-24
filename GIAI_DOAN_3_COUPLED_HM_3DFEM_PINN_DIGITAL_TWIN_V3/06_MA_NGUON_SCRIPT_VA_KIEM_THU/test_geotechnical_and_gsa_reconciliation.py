"""Unit test độc lập kiểm thử module geotechnical_and_gsa_reconciliation.py."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.geotechnical_and_gsa_reconciliation import (
    build_verified_field_milestones,
    compute_eoed_and_mv_from_elastic,
    reconcile_stage3_mv_and_consolidation,
    run_saltelli_lhs_loganathan_poulos_gsa,
)


class TestGeotechnicalAndGsaReconciliation(unittest.TestCase):
    """Kiểm thử độc lập các hàm hiệu chỉnh mv, lấy mẫu Saltelli-LHS và mốc thực địa."""

    def test_bh12_layer3_eoed_and_mv_exact(self) -> None:
        """Kiểm tra tính toán E_oed và mv của lớp bùn sét L3 tại BH12 (E=7680 kPa, nu=0.35)."""
        eoed_kpa, mv_kpa_inv = compute_eoed_and_mv_from_elastic(7680.0, 0.35)
        self.assertAlmostEqual(eoed_kpa, 12325.9259, places=2)
        self.assertAlmostEqual(mv_kpa_inv, 8.113e-5, places=7)

    def test_reconcile_stage3_mv_and_consolidation(self) -> None:
        """Kiểm tra toàn bộ 6 lớp địa chất đều nằm trong dải mv hợp lý và 4 kịch bản đối sánh."""
        layers, scenarios = reconcile_stage3_mv_and_consolidation()
        self.assertEqual(len(layers), 6)
        for layer in layers:
            self.assertTrue(layer.is_geotechnically_plausible, f"Layer {layer.layer_id} failed plausibility")
        self.assertEqual(len(scenarios), 4)
        by_id = {s.scenario_id: s for s in scenarios}
        self.assertAlmostEqual(by_id["HM_SCEN_01_LEGACY_TYPO"].s_hydro_max_mm, 140.16, places=2)
        self.assertAlmostEqual(by_id["HM_SCEN_02_RELOADING_STIFF"].s_hydro_max_mm, 14.02, places=2)
        self.assertAlmostEqual(by_id["HM_SCEN_03_BH12_PARTIAL_DRAINAGE"].s_hydro_max_mm, 14.10, places=1)
        self.assertAlmostEqual(by_id["HM_SCEN_04_BH12_FULL_UNIFORM_UPPER_BOUND"].s_hydro_max_mm, 25.27, places=2)

    def test_saltelli_lhs_loganathan_poulos_gsa_properties(self) -> None:
        """Kiểm tra tính chất toán học của chỉ số Sobol từ lấy mẫu Saltelli-LHS thực tế."""
        records, stats, samples_matrix = run_saltelli_lhs_loganathan_poulos_gsa(
            n_base=1024, seed=202702, n_bootstrap=50
        )
        self.assertEqual(len(records), 5)
        self.assertEqual(samples_matrix.shape, (10000, 8))

        by_param = {r.parameter: r for r in records}
        # Trong Peck thuần túy, E và nu không tham gia nên S1 và ST phải bằng 0
        self.assertAlmostEqual(by_param["E"].peck_saltelli_s1, 0.0, places=3)
        self.assertAlmostEqual(by_param["nu"].peck_saltelli_s1, 0.0, places=3)

        # Trong Loganathan & Poulos Elasto-Gap thực tế, E và nu phải có độ nhạy > 0
        self.assertGreater(by_param["E"].lp_saltelli_s1, 0.02)
        self.assertGreater(by_param["nu"].lp_saltelli_s1, 0.01)
        self.assertGreater(by_param["V_L"].lp_saltelli_s1, 0.45)

        # Tổng các chỉ số bậc 1 phải xấp xỉ <= 1.05 (sai số mẫu hữu hạn)
        self.assertLessEqual(stats["sum_s1_lp_saltelli"], 1.05)
        self.assertGreaterEqual(stats["sum_s1_lp_saltelli"], 0.85)

    def test_verified_field_milestones_provenance(self) -> None:
        """Kiểm tra 9 mốc thực địa có đủ 5 trường provenance bắt buộc."""
        milestones = build_verified_field_milestones()
        self.assertGreaterEqual(len(milestones), 9)
        required_fields = {"source_id", "source_locator", "value_basis", "confidence", "qa_flag"}
        for m in milestones:
            self.assertTrue(required_fields.issubset(m.keys()))


if __name__ == "__main__":
    unittest.main()
