# TBM Ha Noi EIA — Operating Rules

## Scope

This workspace studies surface-settlement sensitivity for the underground S9–S12 section of Ha Noi Metro Line 3 using transparent analytical methods and GIS. The baseline methods are Peck (1969) and, only after the original equations are verified, Loganathan & Poulos (1998).

## Non-negotiable rules

1. Treat `research/` and future `data/raw/` as source material. Never overwrite, rename, move, or delete source files.
2. Put generated artifacts under a timestamped `research_outputs/YYYY-MM-DD_HHMMSS/` run directory or another explicitly versioned generated-data directory.
3. Every scientific value must have `source_id`, `source_locator`, `value_basis`, `confidence`, and `qa_flag`. Never turn an assumption, regional value, or derived value into a field observation.
4. Keep evidence classes separate: `direct_text`, `direct_table`, `observed`, `derived`, `regional_crosscheck`, `model_assumption`, and `scenario_assumption`.
5. Do not advance past an Audit Gate with unresolved critical findings. Automation may recommend a verdict, but only evidence-backed checks may set it to `PASSED`.
6. `data/raw/` is immutable. Invalid or doubtful records go to `data/quarantine/` with a reason; they are not silently deleted.
7. Freeze a clean baseline only after Gate 1–3 checks and create SHA-256 checksums and a manifest.
8. Use SI units internally. Preserve original values and units whenever conversion occurs.
9. Use a declared settlement sign convention. Do not mix groundwater-consolidation settlement with tunnelling-induced settlement.
10. Do not implement remembered versions of published equations. Verify the original source, equation/page, definitions, validity range, and units first.

## AUTO mode

- Default mode: `auto_guarded`.
- Default model policy: `inherit` (use the host default model unless a task explicitly requires another capability).
- The General Contractor reads `AGENT_STATE.json`, dispatches the next dependency-ready task according to `.agents/agents.json`, writes a handoff package, and updates the handoff log.
- Agent switches:
  - mechanics derivation/dispute -> `mechanics_reviewer`;
  - long/scanned PDF or difficult tables -> `source_harvester`;
  - local syntax, test, or schema issue -> `pipeline_engineer`;
  - citation/provenance conflict -> `evidence_auditor`;
  - spatial/CRS problem -> `gis_analyst`;
  - numerical FEM/3D simulation -> `numerical_modeler`.
- Retry transient/tool errors at most twice. Scientific/QC failures are not retried blindly: quarantine the item and route it to the auditor.
- Never expose secrets in configs, logs, or handoff packages.

## Five mandatory Audit Gates

1. Source acquisition and extraction integrity.
2. Physical, geotechnical, unit, and spatial plausibility.
3. Clean baseline freeze, manifest, and SHA-256 checksums.
4. Analytical verification, sensitivity analysis, and GIS validation.
5. Scientific reporting, traceability, and reproducibility.

## Scientific baseline

- Peck Gaussian trough must pass numerical-integration and limiting-case tests.
- Volume-loss scenarios are `0.005, 0.010, 0.015, 0.020` as ratios (0.5%–2.0%).
- Treat trough width, tunnel geometry/depth, stratigraphy, and groundwater as uncertain unless directly sourced at the analyzed chainage.
- Loganathan & Poulos is a separate benchmark branch, not an unchecked drop-in replacement.
- Machine learning and OpenSeesPy are outside the minimum viable scope. Add them only after Gate 4 identifies a justified need and sufficient data exist.
