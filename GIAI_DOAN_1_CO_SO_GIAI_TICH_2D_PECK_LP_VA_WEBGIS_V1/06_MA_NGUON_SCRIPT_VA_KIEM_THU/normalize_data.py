"""Data normalization script for Gate 2 (WF-06).

Normalizes raw research tables into structured, SI-unit tables in 03_processed_data/.
"""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "research_outputs" / "2026-10-13_152753" / "03_processed_data"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def build_normalized_sources():
    sources = [
        {
            "source_id": "SRC_ADB_2013",
            "title": "Updated Environmental Impact Assessment Ha Noi Metro Line 3",
            "authors": "Hanoi People's Committee for ADB",
            "year": "2013",
            "type": "official_report",
            "license": "Public Listing",
            "status": "pilot_reference"
        },
        {
            "source_id": "SRC_ETASR_2024",
            "title": "The Effect of Seismic Load on TBM Structures for Metro Line 3 in Hanoi",
            "authors": "Nguyen, Bui & Nguyen",
            "year": "2024",
            "type": "journal_article",
            "doi": "10.48084/etasr.6748",
            "status": "verified_open_access"
        },
        {
            "source_id": "SRC_TCXD_2024",
            "title": "Design of urban tunnels in soft soil using TBM for UMRT Line 3 in Hanoi",
            "authors": "Nguyen, Kohata & Nguyen",
            "year": "2024",
            "type": "journal_article",
            "doi": "vjol.info.vn/index.php/tcxd/article/view/98280",
            "status": "verified_local_pdf"
        },
        {
            "source_id": "SRC_GIAO_2020",
            "title": "Geotechnical Characterization and Land Subsidence Analysis for UMRT Line 3",
            "authors": "Giao, Nguyen & Hoang",
            "year": "2020",
            "type": "conference_proceedings",
            "doi": "10.1007/978-981-15-2184-3_36",
            "status": "verified_regional_crosscheck"
        },
        {
            "source_id": "SRC_PECK_1969",
            "title": "Deep excavations and tunneling in soft ground",
            "authors": "Peck, R.B.",
            "year": "1969",
            "type": "state_of_art_paper",
            "doi": "ICSMFE_1969",
            "status": "canonical_baseline"
        },
        {
            "source_id": "SRC_LP_1998",
            "title": "Analytical solutions for tunnel-induced ground movement in clays",
            "authors": "Loganathan, N. & Poulos, H.G.",
            "year": "1998",
            "type": "journal_article",
            "doi": "10.1061/(ASCE)1090-0241(1998)124:9(846)",
            "status": "secondary_source_benchmark"
        }
    ]
    fields = ["source_id", "title", "authors", "year", "type", "doi", "license", "status"]
    for s in sources:
        s.setdefault("doi", "")
        s.setdefault("license", "")
    path = OUTPUT_DIR / "normalized_sources.csv"
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(sources)
    print(f"Wrote {len(sources)} sources to {path.name}")


def build_normalized_parameters():
    params = [
        # S9-S10 Section
        {"section_id": "SEC_S9_S10", "name": "Kim Mã - Cát Linh", "D_m": 6.30, "z0_m": 15.0, "K": 0.50, "nu": 0.35, "gwl_m": 11.0, "evidence_class": "direct_text_and_table", "qa_flag": "verified"},
        # S10-S11 Section (Extrapolated)
        {"section_id": "SEC_S10_S11", "name": "Cát Linh - Văn Miếu", "D_m": 6.30, "z0_m": 16.5, "K": 0.55, "nu": 0.36, "gwl_m": 9.0, "evidence_class": "scenario_assumption", "qa_flag": "pilot_synthetic_scenario"},
        # S11-S12 Section (BH12)
        {"section_id": "SEC_S11_S12", "name": "Văn Miếu - Ga Hà Nội", "D_m": 6.30, "z0_m": 18.0, "K": 0.60, "nu": 0.38, "gwl_m": 6.0, "evidence_class": "direct_table_plus_derived_depth", "qa_flag": "verified_with_soft_clay_flag"}
    ]
    path = OUTPUT_DIR / "normalized_parameters.csv"
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(params[0].keys()))
        writer.writeheader()
        writer.writerows(params)
    print(f"Wrote {len(params)} sections to {path.name}")


if __name__ == "__main__":
    build_normalized_sources()
    build_normalized_parameters()
