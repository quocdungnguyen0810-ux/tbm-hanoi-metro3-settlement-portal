"""Module quản trị, đánh giá, kiểm toán độc lập và phân kỳ giai đoạn toàn dự án TBM Hà Nội.

Tuân thủ nghiêm ngặt:
- PEP 8, Type Hints đầy đủ, Logging tiếng Việt chuẩn kỹ thuật.
- Không ghi đè, đổi tên hoặc xóa dữ liệu gốc trong `research/`.
- Kiểm tra ràng buộc hợp lý vật lý (Physical Plausibility) và cách ly dị biệt (Quarantine).
- Phân tách rõ 7 phân khu chức năng trong từng giai đoạn (Giai đoạn 0 đến Giai đoạn 4).
"""

from __future__ import annotations

import csv
import hashlib
import json
import logging
import shutil
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
)
logger = logging.getLogger("TBM_Project_Organizer")


@dataclass(frozen=True)
class PhysicalPlausibilityResult:
    """Kết quả kiểm tra ràng buộc vật lý và truy xuất nguồn gốc."""

    check_id: str
    parameter_name: str
    observed_or_claimed_value: float
    recalculated_physical_value: float
    unit: str
    is_plausible: bool
    quarantine_required: bool
    reason: str
    source_id: str
    source_locator: str
    value_basis: str
    confidence: str
    qa_flag: str


@dataclass
class StageDefinition:
    """Định nghĩa cấu trúc chuẩn của một giai đoạn thực hiện dự án."""

    stage_id: str
    stage_code: str
    folder_name: str
    title_vn: str
    period: str
    lead_human: list[str]
    supporting_humans: list[str]
    lead_agents: list[str]
    supporting_agents: list[str]
    skills_and_mcp: list[str]
    gates: list[str]
    gate_verdicts: dict[str, str]
    objectives: list[str]
    key_outputs: list[str]
    audit_findings: list[str]
    input_files: list[str] = field(default_factory=list)
    analysis_files: list[str] = field(default_factory=list)
    figure_table_files: list[str] = field(default_factory=list)
    web_html_files: list[str] = field(default_factory=list)
    script_test_files: list[str] = field(default_factory=list)
    draft_dossier_files: list[str] = field(default_factory=list)


STANDARD_SUBFOLDERS: dict[str, str] = {
    "audit_plan_hr_skill": "01_AUDIT_KE_HOACH_NHAN_SU_SKILL_CONG_CU",
    "input_data": "02_DU_LIEU_DAU_VAO",
    "analysis_data": "03_DU_LIEU_PHAN_TICH",
    "figures_tables": "04_KET_QUA_BANG_BIEU_HINH_VE_CHAT_LUONG_CAO",
    "web_html": "05_FILE_HIEN_HANH_HTML_WEB",
    "scripts_tests": "06_MA_NGUON_SCRIPT_VA_KIEM_THU",
    "drafts_dossiers": "07_FILE_DU_THAO_BAO_CAO_VA_NGHIEM_THU",
}


def compute_sha256(file_path: Path) -> str:
    """Tính mã băm SHA-256 bảo toàn toàn vẹn nhị phân của tệp tin."""
    digest = hashlib.sha256()
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_physical_plausibility(
    tunnel_diameter_m: float,
    cover_depth_m: float,
    volume_loss_ratio: float,
    trough_width_k: float,
    poisson_ratio: float,
    drawdown_m: float,
    mv_kpa_inv: float,
    clay_thickness_m: float,
    claimed_consolidation_mm: float,
) -> list[PhysicalPlausibilityResult]:
    """Kiểm tra các ràng buộc logic vật lý địa kỹ thuật và phát hiện dị biệt cần cách ly."""
    results: list[PhysicalPlausibilityResult] = []

    # 1. Kiểm tra đường kính và chiều sâu chôn hầm (z0 > R)
    radius_m = tunnel_diameter_m / 2.0
    geom_ok = tunnel_diameter_m > 0.0 and cover_depth_m > radius_m
    results.append(
        PhysicalPlausibilityResult(
            check_id="PHYS-01",
            parameter_name="tunnel_geometry_z0_vs_R",
            observed_or_claimed_value=cover_depth_m,
            recalculated_physical_value=radius_m,
            unit="m",
            is_plausible=geom_ok,
            quarantine_required=not geom_ok,
            reason=(
                f"Hợp lý vật lý: z0={cover_depth_m:.2f}m > R={radius_m:.2f}m (tỷ số C/D={(cover_depth_m - radius_m)/tunnel_diameter_m:.2f})."
                if geom_ok
                else f"Vi phạm hình học không gian ngầm: z0={cover_depth_m:.2f}m <= R={radius_m:.2f}m."
            ),
            source_id="SRC_ETASR_2024_AND_MRB_2024",
            source_locator="normalized_parameters.csv:2-3; MOC_2025_TBM1_Depth_17.8m",
            value_basis="direct_table",
            confidence="high",
            qa_flag="PASS" if geom_ok else "QUARANTINE_GEOMETRY_ERROR",
        )
    )

    # 2. Kiểm tra tỷ lệ tổn thất thể tích VL trong dải [0.001, 0.05] cho khiên EPB-TBM
    vl_ok = 0.001 <= volume_loss_ratio <= 0.05
    results.append(
        PhysicalPlausibilityResult(
            check_id="PHYS-02",
            parameter_name="volume_loss_ratio_VL",
            observed_or_claimed_value=volume_loss_ratio,
            recalculated_physical_value=0.010,
            unit="ratio",
            is_plausible=vl_ok,
            quarantine_required=not vl_ok,
            reason=(
                f"Hợp lý vật lý: VL={volume_loss_ratio*100:.2f}% nằm trong dải vận hành EPB-TBM đất yếu [0.1%, 5.0%]."
                if vl_ok
                else f"Dị biệt vật lý: VL={volume_loss_ratio*100:.2f}% vượt ngưỡng EPB-TBM tiêu chuẩn."
            ),
            source_id="SRC_PECK_1969_SCENARIO",
            source_locator="configs/project_config.json:volume_loss_scenarios",
            value_basis="scenario_assumption",
            confidence="high",
            qa_flag="PASS" if vl_ok else "QUARANTINE_VL_OUTLIER",
        )
    )

    # 3. Kiểm tra hệ số Poisson đất bão hòa không thoát nước (0 < nu <= 0.5)
    nu_ok = 0.0 < poisson_ratio <= 0.5
    results.append(
        PhysicalPlausibilityResult(
            check_id="PHYS-03",
            parameter_name="poisson_ratio_nu",
            observed_or_claimed_value=poisson_ratio,
            recalculated_physical_value=0.35,
            unit="dimensionless",
            is_plausible=nu_ok,
            quarantine_required=not nu_ok,
            reason=(
                f"Hợp lý nhiệt động lực học đàn hồi: nu={poisson_ratio:.2f} thuộc (0, 0.5]."
                if nu_ok
                else f"Vi phạm cơ học môi trường liên tục: nu={poisson_ratio:.2f} nằm ngoài (0, 0.5]."
            ),
            source_id="SRC_TCXD_2024_STRATIGRAPHY",
            source_locator="normalized_parameters.csv:5",
            value_basis="regional_crosscheck",
            confidence="medium",
            qa_flag="PASS" if nu_ok else "QUARANTINE_POISSON_INVALID",
        )
    )

    # 4. Kiểm tra phương trình lún cố kết Terzaghi 1D: Sc = gamma_w * dh * mv * H * 1000 (mm)
    gamma_w = 9.81  # kN/m3
    recalc_sc_mm = drawdown_m * gamma_w * mv_kpa_inv * clay_thickness_m * 1000.0
    rel_err = abs(claimed_consolidation_mm - recalc_sc_mm) / max(recalc_sc_mm, 1e-9)
    sc_ok = rel_err < 0.05
    results.append(
        PhysicalPlausibilityResult(
            check_id="PHYS-04",
            parameter_name="terzaghi_1d_consolidation_settlement",
            observed_or_claimed_value=claimed_consolidation_mm,
            recalculated_physical_value=round(recalc_sc_mm, 2),
            unit="mm",
            is_plausible=sc_ok,
            quarantine_required=not sc_ok,
            reason=(
                f"Khớp phương trình Terzaghi 1D: {claimed_consolidation_mm:.2f} mm vs {recalc_sc_mm:.2f} mm."
                if sc_ok
                else (
                    f"PHÁT HIỆN LỖI HỆ SỐ 10 (C-07): Giá trị báo cáo GĐ3 ({claimed_consolidation_mm:.2f} mm) "
                    f"sai lệch 10 lần so với tích số vật lý Δu·mv·H = {drawdown_m}×9.81×{mv_kpa_inv}×{clay_thickness_m}×1000 = {recalc_sc_mm:.2f} mm "
                    f"(hoặc mv phải là 0.000045 m2/kN thay vì 0.00045 m2/kN). Đưa vào vùng cách ly (Quarantine)!"
                )
            ),
            source_id="AUDIT_20261015_FEM_01",
            source_locator="scripts/generate_stage_3_models_and_excel.py:155-165",
            value_basis="derived",
            confidence="high",
            qa_flag="PASS" if sc_ok else "QUARANTINE_UNIT_FACTOR_10_ERROR",
        )
    )

    return results

