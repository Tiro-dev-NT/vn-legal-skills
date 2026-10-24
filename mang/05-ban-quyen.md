# Mảng 5 — Bản quyền (sở hữu trí tuệ)

> Tham khảo, không phải tư vấn pháp lý — [MIEN-TRU-TRACH-NHIEM.md](../MIEN-TRU-TRACH-NHIEM.md). Tóm tắt từ nguồn trong [NGUON.md](../NGUON.md); đối chiếu văn bản gốc trước khi dựa vào.

**Áp khi:** dùng nội dung, ảnh, font, âm thanh, dữ liệu, thư viện mã của người khác; hoặc cho người dùng đăng nội dung.

**Văn bản:** Luật SHTT — đọc bản hợp nhất VBHN 67/VBHN-VPQH (2026) · Luật 131/2025/QH15 (sửa đổi, hiệu lực 01/04/2026, có thêm trách nhiệm nền tảng số và vi phạm trên môi trường số). Link: [NGUON.md](../NGUON.md). Số điều: chỉ trích ở phần Mức phạt (đã đối chiếu toàn văn); luật nội dung **chưa trích**.

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

## Mức phạt (NĐ 341/2025/NĐ-CP — đã đối chiếu toàn văn Công báo)

**Mức Chương II là của CÁ NHÂN; tổ chức gấp 2; hộ kinh doanh như cá nhân** (Điều 5 khoản 1, 2 — một số khoản, gồm phần lớn Điều 41, là mức tổ chức). Trần: 250 triệu (cá nhân) · 500 triệu (tổ chức).
Hiệu lực 15/02/2026; bãi bỏ NĐ 131/2013 và NĐ 28/2017 (Điều 63).

| Hành vi | Mức | Căn cứ | Ứng với mục |
|---|---|---|---|
| **Sao chép tác phẩm** không được phép | 5–50 triệu (cá nhân) theo bậc giá trị; tổ chức 10–100 triệu — xem bậc trong bản gốc | Điều 16 | 5.3, 5.4 |
| **Truyền đạt tác phẩm đến công chúng** (đăng lên web/app) không được phép | 30–50 triệu (theo bản trích) | Điều 15 | 5.3 |
| Không ghi/ghi sai tên tác giả | 1–5 triệu (theo bản trích) | Điều 7 | 5.1 |
| Doanh nghiệp **trung gian** (cho người dùng đăng nội dung): không cảnh báo người dùng, không công bố quy trình gỡ bỏ… | 10–20 triệu (tổ chức) | Điều 41 khoản 1 | 5.5 |
| Doanh nghiệp trung gian **không gỡ bỏ/ngăn chặn** nội dung xâm phạm trong **24 giờ** kể từ khi nhận yêu cầu bằng văn bản | 100–150 triệu (tổ chức) | Điều 41 khoản 7 | 5.5 |

Phần mềm/chương trình máy tính dùng không phép: NĐ 341 **không có điều riêng** — áp các điều chung (sao chép, phân phối) theo bản gốc; **cần luật sư** khi gặp.
Vi phạm nghiêm trọng có thể bị xử lý **hình sự** ([tóm tắt Chính phủ](https://xaydungchinhsach.chinhphu.vn/quy-dinh-muc-phat-toi-xam-pham-quyen-tac-gia-quyen-lien-quan-119260508154839332.htm)).

