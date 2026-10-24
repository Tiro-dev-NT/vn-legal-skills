# Mảng 2 — Bảo vệ quyền lợi người tiêu dùng

**Áp khi:** bán hàng hoá/dịch vụ (kể cả gói thuê bao, vật phẩm số, credit) cho cá nhân.

**Văn bản:** Luật 19/2023/QH15 (BVQLNTD) · NĐ 55/2024/NĐ-CP (chi tiết). Link: [NGUON.md](../NGUON.md). Số điều: **chưa trích**.

## Việc phải có

| # | Việc | Nhãn | Dấu hiệu trong mã |
|---|---|---|---|
| 2.1 | **Giá rõ trước khi trả tiền**: tổng tiền, đã gồm thuế/phí chưa, chu kỳ gia hạn | [luật] (thông tin trung thực, đầy đủ) | trang giá, nút mua; chuỗi "VAT", "đã bao gồm" |
| 2.2 | **Điều khoản dịch vụ bằng tiếng Việt**, rõ ràng, dễ hiểu; điều khoản là "hợp đồng theo mẫu / điều kiện giao dịch chung" ⇒ kiểm có thuộc danh mục phải đăng ký không | [luật] NĐ 55/2024 | route `/terms`, `dieu-khoan` |
| 2.3 | **Chính sách hoàn tiền / huỷ** viết ra trước, khớp với hành vi thật của hệ thống | [luật] (minh bạch) · [khuyến nghị] nội dung | so điều khoản với mã xử lý thanh toán/huỷ |
| 2.4 | **Huỷ gia hạn dễ như lúc đăng ký**; không giấu nút huỷ | [khuyến nghị] | cài đặt tài khoản có nút huỷ không |
| 2.5 | **Không ô tick sẵn mua thêm**, không tự cộng dịch vụ kèm | [luật] (cấm ép buộc / lừa dối) | checkbox `checked` ở giỏ/thanh toán |
| 2.6 | **Kênh khiếu nại** công khai (email/form) và tiếp nhận được | [luật] | trang liên hệ, email hỗ trợ ở footer |
| 2.7 | **Không điều khoản miễn trừ trắng** trách nhiệm của bên bán (vd "không hoàn tiền trong mọi trường hợp") | [luật] (điều khoản vô hiệu) | đọc điều khoản |
| 2.8 | **Thông tin người bán**: tên chủ thể kinh doanh, mã số, địa chỉ liên hệ | [luật] | footer, trang giới thiệu |

## Cần luật sư khi

thuê bao tự gia hạn có giá cao · bán cho trẻ em · chính sách không hoàn tiền với vật phẩm số.
