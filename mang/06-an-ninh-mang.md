# Mảng 6 — An ninh mạng, thông tin trên mạng

**Áp khi:** hệ thống có tài khoản, lưu dữ liệu người dùng, hoặc cho người dùng đăng nội dung.

**Văn bản:** Luật 116/2025/QH15 (An ninh mạng 2025, hiệu lực 01/07/2026) · NĐ 331/2026/NĐ-CP (bảo vệ ANM đối với hệ thống thông tin, hiệu lực 19/08/2026) ·
NĐ 330/2026/NĐ-CP (xử phạt ANM + DLCN) · NĐ 147/2024/NĐ-CP (dịch vụ internet và thông tin trên mạng — trang tin tổng hợp, mạng xã hội, trò chơi điện tử). Link: [NGUON.md](../NGUON.md). Số điều: **chưa trích**.

## Phân loại trước

- Có bình luận/diễn đàn/hồ sơ công khai **không tự động** là "mạng xã hội" theo NĐ 147/2024 — xem định nghĩa và ngưỡng trong bản gốc trước khi kết luận cần giấy phép/đăng ký.
- Cấp độ hệ thống thông tin và nghĩa vụ đi kèm theo NĐ 331/2026: **không mặc định mọi web nhỏ cùng nghĩa vụ** — đọc tiêu chí áp dụng.

## Việc phải có

| # | Việc | Nhãn | Dấu hiệu trong mã |
|---|---|---|---|
| 6.1 | **Gỡ nội dung vi phạm khi có yêu cầu** của lực lượng chuyên trách trong thời hạn luật định (tin Chính phủ: chậm nhất 24 giờ, khẩn cấp có thể 6 giờ) ⇒ có người + công cụ gỡ được | [luật] — điều kiện chính xác: **đọc bản gốc** | trang admin có ẩn/xoá nội dung |
| 6.2 | **Không dùng AI giả mạo trái pháp luật** hình ảnh, giọng nói, video người khác (xem 7.6) | [luật] | tính năng đổi giọng/ghép mặt |
| 6.3 | **Bảo mật cơ bản**: không lộ khoá bí mật trong mã client; phân quyền truy cập dữ liệu theo người dùng; HTTPS | [khuyến nghị] (biện pháp bảo vệ — liên quan mảng 1) | grep `sk_`, `secret`, `service_role`, khoá API trong JS gửi về trình duyệt; RLS/ACL |
| 6.4 | **Nhật ký sự cố** và quy trình báo cáo khi bị tấn công/lộ dữ liệu | [luật] (+ mảng 1.10) | tài liệu vận hành |
| 6.5 | **Nội dung cấm** trong nội dung người dùng ⇒ có cơ chế báo cáo + kiểm duyệt | [luật] | form báo cáo, bộ lọc |
| 6.6 | **Hệ thống thông tin** thuộc diện phải xác định cấp độ: thẩm định/phê duyệt cấp độ và đáp ứng yêu cầu bảo vệ; hệ thống có trước có thời hạn chuyển tiếp | [luật] NĐ 331/2026 — diện áp dụng và thời hạn: **đọc bản gốc** | — |
