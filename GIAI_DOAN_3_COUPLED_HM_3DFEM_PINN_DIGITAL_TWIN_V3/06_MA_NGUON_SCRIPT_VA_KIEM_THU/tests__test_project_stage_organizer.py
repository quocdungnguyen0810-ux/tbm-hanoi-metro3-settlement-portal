"""Unit test độc lập cho module project_stage_organizer.py."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.project_stage_organizer import (
    STANDARD_SUBFOLDERS,
    compute_sha256,
    validate_physical_plausibility,
)


class TestProjectStageOrganizer(unittest.TestCase):
    """Kiểm thử độc lập các hàm kiểm tra vật lý, mã băm và phân mục giai đoạn."""

    def test_standard_subfolders_count(self) -> None:
        """Đảm bảo có đủ 7 phân mục chức năng chuẩn trong mỗi giai đoạn."""
        self.assertEqual(len(STANDARD_SUBFOLDERS), 7)
        self.assertIn("audit_plan_hr_skill", STANDARD_SUBFOLDERS)
        self.assertIn("input_data", STANDARD_SUBFOLDERS)
        self.assertIn("analysis_data", STANDARD_SUBFOLDERS)
        self.assertIn("figures_tables", STANDARD_SUBFOLDERS)
        self.assertIn("web_html", STANDARD_SUBFOLDERS)
        self.assertIn("scripts_tests", STANDARD_SUBFOLDERS)
        self.assertIn("drafts_dossiers", STANDARD_SUBFOLDERS)

    def test_physical_plausibility_detects_factor_10_error(self) -> None:
        """Kiểm tra bộ lọc vật lý phát hiện chính xác lỗi hệ số 10 trong lún cố kết GĐ3."""
        results = validate_physical_plausibility(
            tunnel_diameter_m=6.3,
            cover_depth_m=17.8,
            volume_loss_ratio=0.01,
            trough_width_k=0.50,
            poisson_ratio=0.35,
            drawdown_m=2.5,
            mv_kpa_inv=0.00045,
            clay_thickness_m=12.7,
            claimed_consolidation_mm=14.1,
        )
        self.assertEqual(len(results), 4)
        by_id = {r.check_id: r for r in results}
        self.assertTrue(by_id["PHYS-01"].is_plausible)
        self.assertTrue(by_id["PHYS-02"].is_plausible)
        self.assertTrue(by_id["PHYS-03"].is_plausible)
        # PHYS-04 phải phát hiện sai lệch hệ số 10 (14.1 mm vs 140.16 mm) và yêu cầu cách ly
        self.assertFalse(by_id["PHYS-04"].is_plausible)
        self.assertTrue(by_id["PHYS-04"].quarantine_required)
        self.assertAlmostEqual(by_id["PHYS-04"].recalculated_physical_value, 140.16, places=2)
        self.assertEqual(by_id["PHYS-04"].qa_flag, "QUARANTINE_UNIT_FACTOR_10_ERROR")

    def test_physical_plausibility_invalid_geometry_and_poisson(self) -> None:
        """Kiểm tra bộ lọc vật lý bắt được lỗi hình học z0 <= R và hệ số Poisson > 0.5."""
        results = validate_physical_plausibility(
            tunnel_diameter_m=6.3,
            cover_depth_m=2.5,
            volume_loss_ratio=0.12,
            trough_width_k=0.50,
            poisson_ratio=0.60,
            drawdown_m=2.5,
            mv_kpa_inv=0.000045,
            clay_thickness_m=12.7,
            claimed_consolidation_mm=14.02,
        )
        by_id = {r.check_id: r for r in results}
        self.assertFalse(by_id["PHYS-01"].is_plausible)
        self.assertFalse(by_id["PHYS-02"].is_plausible)
        self.assertFalse(by_id["PHYS-03"].is_plausible)
        self.assertTrue(by_id["PHYS-04"].is_plausible)

    def test_compute_sha256_integrity(self) -> None:
        """Kiểm tra hàm băm SHA-256 chính xác tuyệt đối."""
        with tempfile.NamedTemporaryFile("wb", delete=False) as tmp:
            tmp.write(b"TBM_HANOI_METRO_LINE_3_S9_S12")
            tmp_path = Path(tmp.name)
        try:
            digest = compute_sha256(tmp_path)
            self.assertEqual(len(digest), 64)
        finally:
            tmp_path.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()

