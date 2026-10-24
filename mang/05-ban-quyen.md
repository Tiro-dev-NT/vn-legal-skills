# Mảng 5 — Bản quyền (sở hữu trí tuệ)

> Tham khảo, không phải tư vấn pháp lý — [MIEN-TRU-TRACH-NHIEM.md](../MIEN-TRU-TRACH-NHIEM.md). Tóm tắt từ nguồn trong [NGUON.md](../NGUON.md); đối chiếu văn bản gốc trước khi dựa vào.

**Áp khi:** dùng nội dung, ảnh, font, âm thanh, dữ liệu, thư viện mã của người khác; hoặc cho người dùng đăng nội dung.

**Văn bản:** Luật SHTT — đọc bản hợp nhất VBHN 67/VBHN-VPQH (2026) · Luật 131/2025/QH15 (sửa đổi, hiệu lực 01/04/2026, có thêm trách nhiệm nền tảng số và vi phạm trên môi trường số). Link: [NGUON.md](../NGUON.md). Số điều: **chưa trích**.

## Việc phải có

| # | Việc | Nhãn | Dấu hiệu trong mã |
|---|---|---|---|
| 5.1 | **Sổ nguồn gốc tài sản**: mỗi ảnh/âm thanh/font/bộ dữ liệu ghi nguồn + giấy phép | [khuyến nghị] | tệp `LICENSES`, `NOTICE`, `ATTRIBUTION`; thư mục `assets/` |
| 5.2 | **Giấy phép thư viện mã** được tôn trọng: giữ thông báo bản quyền (MIT/BSD/Apache), hiểu nghĩa vụ chia sẻ lại (GPL, CC BY-SA) | [luật] (quyền tác giả với phần mềm) | `package.json`, `vendor/`, thư viện tự host |
| 5.3 | **Không chép sách/giáo trình/đề thi** có bản quyền vào sản phẩm; trích dẫn ngắn có nguồn chỉ trong giới hạn luật cho phép | [luật] | dữ liệu nội dung; so với tài liệu gốc |
| 5.4 | **Sưu tập/tuyển chọn** của người khác (bộ câu, cách sắp xếp) cũng có thể được bảo hộ — không chép nguyên cấu trúc | [luật] | — |
| 5.5 | **Nội dung người dùng đăng**: có điều khoản về quyền, có kênh nhận báo vi phạm và gỡ | [luật] (trách nhiệm nền tảng — Luật 131/2025) | form báo cáo vi phạm |
| 5.6 | **Ảnh/âm thanh do AI sinh**: ghi điều khoản dịch vụ của công cụ, tránh tạo theo tên nghệ sĩ/nhân vật có bản quyền | [khuyến nghị] (+ mảng 7) | prompt lưu kèm ảnh |
| 5.7 | **Văn bản pháp luật** không được bảo hộ quyền tác giả — được trích dẫn | [luật] | — |

## Mức phạt (NĐ 341/2025/NĐ-CP — hiệu lực 15/02/2026)

Nguồn: [Cổng Bản quyền tác giả — Cục Bản quyền](https://cov.gov.vn/tin-tuc/gioi-thieu-nghi-dinh-so-3412025ndcp-quy-dinh-xu-phat-vi-pham-hanh-chinh-ve-quyen-tac-gia-quyen-lien-quan-168844.html) · [Bộ VHTTDL](https://bvhttdl.gov.vn/nhung-hanh-vi-bi-xu-phat-hanh-chinh-ve-quyen-tac-gia-quyen-lien-quan-20260102213551722.htm) · [Báo Chính phủ](https://baochinhphu.vn/nhung-hanh-vi-nao-bi-xu-phat-hanh-chinh-ve-quyen-tac-gia-quyen-lien-quan-102260102151640525.htm).

- Mức tối đa: **250 triệu (cá nhân) · 500 triệu (tổ chức)**; cùng hành vi tổ chức gấp 2; hộ kinh doanh phạt như cá nhân.
- **Sao chép tác phẩm không được phép** (5.3, 5.4): các nguồn chính thức **ghi lệch nhau** (5–50 triệu vs 5–100 triệu tuỳ hành vi) — đọc toàn văn trước khi trích.
- **Truyền đạt tác phẩm đến công chúng** khi chưa được phép (đăng lên web/app cho người dùng xem): 30–50 triệu.
- Biện pháp kèm: tịch thu tang vật/phương tiện; buộc gỡ bỏ bản sao vi phạm (theo tóm tắt).
- Vi phạm nghiêm trọng có thể bị xử lý **hình sự** ([tóm tắt Chính phủ](https://xaydungchinhsach.chinhphu.vn/quy-dinh-muc-phat-toi-xam-pham-quyen-tac-gia-quyen-lien-quan-119260508154839332.htm)).
