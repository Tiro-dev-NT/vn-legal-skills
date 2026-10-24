# Mảng 2 — Bảo vệ quyền lợi người tiêu dùng

> Tham khảo, không phải tư vấn pháp lý — [MIEN-TRU-TRACH-NHIEM.md](../MIEN-TRU-TRACH-NHIEM.md). Tóm tắt từ nguồn trong [NGUON.md](../NGUON.md); đối chiếu văn bản gốc trước khi dựa vào.

**Áp khi:** bán hàng hoá/dịch vụ (kể cả gói thuê bao, vật phẩm số, credit) cho cá nhân.

**Văn bản:** Luật 19/2023/QH15 (BVQLNTD) · NĐ 55/2024/NĐ-CP (chi tiết). Link: [NGUON.md](../NGUON.md). Số điều: chỉ trích ở phần Mức phạt (đã đối chiếu toàn văn); luật nội dung **chưa trích**.

## Việc phải có

| # | Việc | Nhãn | Dấu hiệu trong mã |
|---|---|---|---|
| 2.1 | **Giá rõ trước khi trả tiền**: tổng tiền, đã gồm thuế/phí chưa, chu kỳ gia hạn | [luật] (thông tin trung thực, đầy đủ) | trang giá, nút mua; chuỗi "VAT", "đã bao gồm" |
| 2.2 | **Điều khoản dịch vụ bằng tiếng Việt**, rõ ràng, dễ hiểu; điều khoản là "hợp đồng theo mẫu / điều kiện giao dịch chung" ⇒ kiểm có thuộc **danh mục hàng hoá, dịch vụ thiết yếu phải đăng ký** không (QĐ 07/2024/QĐ-TTg — danh mục gồm nhóm thiết yếu như điện, nước sinh hoạt, truyền hình trả tiền, viễn thông, vận chuyển hành khách, mua bán căn hộ…; **đọc danh mục đủ**; không suy ra mọi dịch vụ online đều phải đăng ký) | [luật] NĐ 55/2024 | route `/terms`, `dieu-khoan` |
| 2.3 | **Chính sách hoàn tiền / huỷ** viết ra trước, khớp với hành vi thật của hệ thống | [luật] (minh bạch) · [khuyến nghị] nội dung | so điều khoản với mã xử lý thanh toán/huỷ |
| 2.4 | **Huỷ gia hạn dễ như lúc đăng ký**; không giấu nút huỷ | [khuyến nghị] | cài đặt tài khoản có nút huỷ không |
| 2.5 | **Không ô tick sẵn mua thêm**, không tự cộng dịch vụ kèm | [luật] (cấm ép buộc / lừa dối) | checkbox `checked` ở giỏ/thanh toán |
| 2.6 | **Kênh khiếu nại** công khai (email/form) và tiếp nhận được | [luật] | trang liên hệ, email hỗ trợ ở footer |
| 2.7 | **Không điều khoản miễn trừ trắng** trách nhiệm của bên bán (vd "không hoàn tiền trong mọi trường hợp") | [luật] (điều khoản vô hiệu) | đọc điều khoản |
| 2.8 | **Thông tin người bán**: tên chủ thể kinh doanh, mã số, địa chỉ liên hệ | [luật] | footer, trang giới thiệu |

## Mức phạt (NĐ 98/2020/NĐ-CP sửa bởi NĐ 24/2025/NĐ-CP — đã đối chiếu toàn văn Công báo)

**Mức Chương II là của CÁ NHÂN; tổ chức gấp 2** (Điều 4 khoản 4 điểm b; một số điều — gồm khoản 2, 3 Điều 53a — là mức tổ chức). Đọc từ NĐ 24/2025 và văn bản hợp nhất 03/VBHN-BCT (Công báo 02/06/2025).
Đến 24/10/2026 chưa thấy nghị định thay thế (Bộ Công Thương có kế hoạch sửa trong quý IV/2026) — **kiểm lại Công báo**.

| Hành vi | Mức | Căn cứ | Ứng với mục |
|---|---|---|---|
| Thu thập/dùng thông tin người tiêu dùng khi chưa đồng ý; dùng sai mục đích đã thông báo | 20–30 triệu (cá nhân) | Điều 46 khoản 1 | mảng 1 |
| Không có biện pháp bảo đảm an toàn thông tin; chuyển thông tin cho bên thứ ba khi chưa đồng ý | 30–40 triệu (cá nhân); gấp 2 nếu DL nhạy cảm, gấp 4 nếu nền tảng số lớn | Điều 46 khoản 2–4 | mảng 1, 6 |
| Nền tảng số: ẩn/hiển thị không trung thực đánh giá; quấy rối chào bán; không hoàn tiền/đổi khi sai cam kết; bắt mua thêm; không công khai tài trợ người có ảnh hưởng… | 50–70 triệu | Điều 53a khoản 1 | 2.3, 2.5, 4.5, 4.8 |
| Tổ chức vận hành nền tảng trung gian: không xác thực người bán… | 100–200 triệu (tổ chức) | Điều 53a khoản 2 | 3.1 |
| Vi phạm nặng hơn của nền tảng (xem bản gốc) | 300–400 triệu (tổ chức) | Điều 53a khoản 3 | 3.1 |
| Không có kênh tiếp nhận/giải quyết khiếu nại theo quy định | 20–40 triệu (theo bản trích) | Điều 61 | 2.6 |
| Vi phạm về website TMĐT (thông báo, công bố thông tin…) | 1–30 triệu tuỳ hành vi; có thể đình chỉ 6–12 tháng | Điều 62 (VBHN 03/VBHN-BCT) | 3.2, 3.3 |

Lưu ý: khi hành vi thuộc cả luật DLCN, NĐ 330/2026 (mảng 1) có thể là văn bản áp dụng — luật sư xác định.

## Cần luật sư khi

thuê bao tự gia hạn có giá cao · bán cho trẻ em · chính sách không hoàn tiền với vật phẩm số.
