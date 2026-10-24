# Mảng 6 — An ninh mạng & an toàn hệ thống

**Áp khi:** hệ thống có tài khoản, lưu dữ liệu người dùng, hoặc cho người dùng đăng nội dung.

**Văn bản:** Luật 116/2025/QH15 (An ninh mạng 2025, hiệu lực 01/07/2026) · NĐ 330/2026/NĐ-CP (xử phạt ANM + DLCN). Link: [NGUON.md](../NGUON.md). Số điều: **chưa trích**.
Nghị định hướng dẫn Luật 116/2025 (cấp độ hệ thống thông tin…): **chưa có trong bộ nguồn** — tra Công báo.

## Việc phải có

| # | Việc | Nhãn | Dấu hiệu trong mã |
|---|---|---|---|
| 6.1 | **Gỡ nội dung vi phạm khi có yêu cầu** của lực lượng chuyên trách trong thời hạn luật định (tin Chính phủ: chậm nhất 24 giờ, khẩn cấp có thể 6 giờ) ⇒ phải có người + công cụ gỡ được | [luật] — đọc bản gốc để lấy đúng điều kiện | trang admin có ẩn/xoá nội dung |
| 6.2 | **Không cho dùng AI giả mạo** hình ảnh, giọng nói, video người khác | [luật] | tính năng đổi giọng/ghép mặt |
| 6.3 | **Bảo mật cơ bản**: không lộ khoá bí mật trong mã client; phân quyền truy cập dữ liệu theo người dùng; HTTPS | [khuyến nghị] (biện pháp bảo vệ — liên quan mảng 1) | grep `sk_`, `secret`, `service_role`, khoá API trong JS gửi về trình duyệt; RLS/ACL |
| 6.4 | **Nhật ký sự cố** và quy trình báo cáo khi bị tấn công/lộ dữ liệu | [luật] (+ mảng 1.10) | tài liệu vận hành |
| 6.5 | **Nội dung cấm** (chống phá nhà nước, xúc phạm, lừa đảo…) trong nội dung người dùng ⇒ có cơ chế báo cáo + kiểm duyệt | [luật] | form báo cáo, bộ lọc |
| 6.6 | **Hệ thống thông tin đã chạy trước 01/07/2026** có thời hạn chuyển tiếp xác định cấp độ (tin Chính phủ/Bộ CA: 6 tháng thẩm định, 12 tháng đáp ứng) | [luật] — áp cho loại hệ thống nào: **đọc nghị định hướng dẫn** | — |
