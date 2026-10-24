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

## Mức phạt (NĐ 98/2020/NĐ-CP, sửa bởi NĐ 24/2025/NĐ-CP)

Nguồn: [Báo Chính phủ 24/02/2025](https://baochinhphu.vn/tang-muc-phat-vi-pham-hanh-chinh-ve-bao-ve-quyen-loi-nguoi-tieu-dung-102250224185539081.htm) · [tóm tắt NĐ 24/2025](https://xaydungchinhsach.chinhphu.vn/nghi-dinh-24-2025-nd-cp-sua-doi-bo-sung-quy-dinh-xu-phat-vi-pham-hanh-chinh-bao-ve-quyen-loi-nguoi-tieu-dung-119250225072906906.htm).
Đến 24/10/2026 chưa thấy nghị định thay thế (Bộ Công Thương có kế hoạch sửa trong quý IV/2026) — **kiểm lại Công báo**. Bài không tách cá nhân/tổ chức.

| Hành vi | Mức phạt | Ứng với mục |
|---|---|---|
| Thu thập/dùng thông tin người tiêu dùng khi chưa đồng ý; dùng sai mục đích đã thông báo | 20–30 triệu | mảng 1 |
| Không có biện pháp bảo đảm an toàn thông tin; chuyển thông tin cho bên thứ ba khi chưa đồng ý | 30–40 triệu | mảng 1, 6 |
| ↳ liên quan DL cá nhân nhạy cảm | gấp 2 | |
| Không đền bù/hoàn tiền/đổi khi sản phẩm không đúng cam kết, quảng cáo | 50–70 triệu | 2.3, 2.7 |
| Bắt mua thêm sản phẩm/dịch vụ như điều kiện giao kết hợp đồng | 50–70 triệu | 2.5 |
| Ẩn hoặc hiển thị không trung thực đánh giá của người tiêu dùng | 50–70 triệu (chủ nền tảng số) | 4.5 |
| Không công khai việc tài trợ người có ảnh hưởng để quảng bá | 50–70 triệu | 4.8 |
| Quấy rối người tiêu dùng để chào bán trái ý muốn | 50–70 triệu | 4.6 |
| Nền tảng trung gian không xác thực danh tính người bán | 100–200 triệu (tổ chức) | 3.1 |

Lưu ý: khi hành vi thuộc cả luật DLCN, NĐ 330/2026 (mảng 1) có thể là văn bản áp dụng — luật sư xác định.

## Cần luật sư khi

thuê bao tự gia hạn có giá cao · bán cho trẻ em · chính sách không hoàn tiền với vật phẩm số.
