# Từ điển dữ liệu TBM–lún–GIS: tuyến Nhổn–Ga Hà Nội

## Quy tắc thiết kế

Schema này là bộ mẫu rỗng, không chứa số liệu suy đoán. CSV dùng UTF-8, dấu phẩy, số thập phân dấu chấm và thời gian ISO 8601. Một hàng biểu diễn một nguồn, đối tượng, khoảng địa tầng, số đọc hoặc tham số. Ô trống nghĩa là thiếu/không áp dụng; không dùng 0 hay -999 thay dữ liệu thiếu.

Đơn vị chuẩn là SI theo hậu tố tên cột. Khi chuyển đổi phải giữ `value_original`,`unit_original`. Độ sâu dương xuống từ mặt đất; cao độ dương lên theo `vertical_datum`. Mọi giá trị khoa học liên kết `source_id`, vị trí bằng `source_locator` (trang/bảng/hình/đoạn) và trích dẫn ngắn `evidence_excerpt`.

## Cấu trúc quan hệ

| Bảng | Một hàng | PK | FK chính |
|---|---|---|---|
| `sources.csv` | một tài liệu/phiên bản | `source_id` | — |
| `alignments.csv` | đoạn tuyến/ga/giếng/portal | `alignment_id` | `source_id` |
| `investigation_points.csv` | hố khoan/CPT/điểm khảo sát | `investigation_id` | `alignment_id`,`source_id` |
| `stratigraphy_intervals.csv` | khoảng vật liệu tại điểm khảo sát | `stratum_interval_id` | `investigation_id`,`source_id` |
| `groundwater_observations.csv` | một quan trắc nước ngầm | `groundwater_id` | điểm/tuyến, nguồn |
| `tbm_parameters.csv` | một tham số tại thời gian/khoảng tuyến | `tbm_record_id` | tuyến, nguồn |
| `settlement_monitoring.csv` | một số đọc tại điểm/thời điểm | `monitoring_record_id` | tuyến, nguồn |
| `nearby_buildings.csv` | một công trình | `building_id` | tuyến, nguồn |
| `analytical_parameters.csv` | một tham số/kịch bản | `analytical_parameter_id` | tuyến, nguồn |

## Trường chung và mã kiểm soát

- `extraction_method`: `manual_table|manual_text|ocr|pdf_table|figure_digitization|api|calculated|geocoded`.
- `value_basis`: `observed|reported|digitized|converted|derived|assumed`.
- `confidence`: `high|medium|low|unknown`.
- `qa_flag`: `ok|needs_review|unit_uncertain|location_uncertain|datum_uncertain|conflict|outlier|incomplete`; ghép nhiều cờ bằng `|`.
- `record_status`: `raw|reviewed|validated|superseded|excluded`.
- `geometry_wkt` là OGC WKT trong `crs_epsg`; `x`,`y` cùng CRS. `longitude`,`latitude` chỉ chứa WGS84/EPSG:4326 đã kiểm chứng. Không có EPSG thì để trống và mô tả `crs_original`. `spatial_method` ghi khảo sát/số hóa/geocode/chuyển hệ.
- `chainage_m` tăng theo `chainage_direction`; dấu offset theo `positive_offset_side` khai báo trong alignment.

## Nội dung từng bảng

### Sources

`source_type` nhận `EIA|feasibility_summary|journal_article|conference_paper|technical_report|monitoring_report|webpage|dataset|other`. Lưu tiêu đề, tác giả/cơ quan, ngày, phiên bản, domain phát hành, URL, ngày truy cập, DOI, ngôn ngữ, tên tệp, SHA-256, giấy phép và trích dẫn. URL + thời điểm truy cập + checksum nhận diện đúng phiên bản.

### Alignment và điểm khảo sát

Alignment lưu loại đối tượng, track, khoảng lý trình, quy ước hướng/dấu, cao độ mặt đất/trục hầm và cover. Investigation point lưu nhãn gốc, loại `borehole|CPT|CPTu|SPT|trial_pit|geophysics|other`, lý trình/offset, cao độ và độ sâu kết thúc. Mỗi bảng có WKT/x/y/lon/lat/CRS/datum và provenance/QA.

### Địa tầng

Mỗi hàng là `[top_depth_m,bottom_depth_m]` tại một `investigation_id`. Giữ mã/tên/mô tả nguyên văn; chuẩn hóa `soil_group` thành `fill|organic_soil|mud|clay|silt|sand|gravel|cobble|weathered_rock|rock|mixed|unknown`. Có USCS, geological unit, cao độ biên, độ chính xác đọc biên, sample/test ID, SPT N, dung trọng, w, e, n, c′, φ′, Su, E, môđun oedometer, ν, k và OCR. Nếu tính chất thuộc mẫu/độ sâu khác nhau thì tách hàng; không tự lấy trung bình.

### Nước ngầm

Một hàng là water strike, standing/piezometric/design level hoặc seasonal range. Lưu thời gian, tầng/screen, độ sâu dưới mặt đất, cao độ + datum, head/pressure, mùa, giá trị/đơn vị gốc và provenance/QA.

### TBM và quan trắc lún

TBM ở dạng dài (một `parameter_name`/hàng), có máy/drive/track, lý trình/ring/thời gian, giá trị/đơn vị, statistic và bối cảnh vận hành. Tên tham số có thể gồm đường kính, ring width, tail gap, face/chamber/grout pressure, grout volume, thrust, torque, penetration, advance rate, screw speed, FIR, volume loss.

Monitoring lưu point/type, vị trí, thời gian/baseline, measurement/value/unit, bắt buộc quy ước dấu, uncertainty/detection limit, vị trí TBM đồng bộ và distance to face, cùng trạng thái `baseline|valid|suspect|invalid|missing`.

### Công trình và tham số giải tích

Building lưu loại/công năng, quan hệ không gian tới hầm, vật liệu/móng, số tầng/hầm/năm xây, độ sâu móng/chiều cao, condition/sensitivity class và survey date. Polygon ưu tiên; Point chỉ dùng khi nêu phương pháp/độ bất định.

Analytical parameters ở dạng dài theo scenario/model/version và role `input|calibration|output|sensitivity_factor`; lưu giá trị/đơn vị, cận/phân phối, công thức/định nghĩa, phương pháp suy dẫn và `linked_record_ids`. Tên điển hình: `volume_loss_ratio`, `trough_width_parameter_K`, `trough_width_i_m`, `tunnel_axis_depth_m`, `excavation_radius_m`, `max_settlement_mm`, `influence_limit_mm`. Giá trị giả định phải có `value_basis=assumed` và lý do/nguồn.

## QA và nhập GIS

1. PK không trống/không trùng; FK tồn tại.
2. `bottom_depth_m > top_depth_m >= 0`; thickness xấp xỉ bottom−top trong sai số nêu.
3. Lon [-180,180], lat [-90,90]; WKT và tọa độ khớp sau chuyển hệ.
4. Mọi geometry có CRS; mọi cao độ có datum hoặc cờ `datum_uncertain`.
5. Đơn vị khớp tên cột; chuyển đổi giữ giá trị/đơn vị gốc.
6. Lún có baseline/quy ước dấu; rà trùng point–time–measurement.
7. Derived liệt kê input IDs/phương pháp; assumed không trình bày như đo đạc.
8. GIS đọc UTF-8, dựng geometry từ WKT theo EPSG và lưu GeoPackage. Chỉ dựng Point EPSG:4326 từ lon/lat đã kiểm chứng.
