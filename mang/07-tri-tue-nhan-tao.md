# Mảng 7 — Trí tuệ nhân tạo

**Áp khi:** app có tính năng AI sinh nội dung (chữ, ảnh, giọng), chấm điểm, gợi ý, chatbot.

**Văn bản:** Luật 134/2025/QH15 (Trí tuệ nhân tạo, hiệu lực 01/03/2026) · NĐ 142/2026/NĐ-CP (chi tiết, hiệu lực 01/05/2026). Link: [NGUON.md](../NGUON.md). Số điều: **chưa trích**.
Luật quản lý theo **mức độ rủi ro** và phân biệt **nhà cung cấp** (làm ra hệ thống AI) với **bên triển khai** (đưa AI vào sản phẩm — đa số web nhỏ dùng API thuộc nhóm này).
Xác định mức rủi ro và vai trò ⇒ **đọc NĐ 142/2026 bản gốc**; chưa đọc thì ghi "cần xác nhận".

## Việc phải có

| # | Việc | Nhãn | Dấu hiệu trong mã |
|---|---|---|---|
| 7.1 | **Minh bạch**: cho người dùng biết họ đang tương tác với AI; nội dung do AI tạo được nhận biết/gắn nhãn theo điều kiện luật định (khác nhau theo chủ thể và loại nội dung) | [luật] — chi tiết từng loại nhãn: **đọc bản gốc** | nhãn "AI" cạnh kết quả; chatbot tự giới thiệu |
| 7.2 | **Con người là người quyết định cuối** với việc quan trọng (chấm thi, đánh giá ảnh hưởng người dùng); cho khiếu nại kết quả AI | [khuyến nghị] (Bộ KH&CN: AI là công cụ hỗ trợ) — có thể thành [luật] nếu hệ thống thuộc nhóm rủi ro cao | nút "báo sai", quy trình phúc khảo |
| 7.3 | Dữ liệu gửi nhà cung cấp AI **có thể nhận diện một người** (tên, email, giọng, ảnh mặt, bài viết kèm định danh) ⇒ là xử lý DLCN; nhà cung cấp ở nước ngoài ⇒ thêm mảng 1.7. Prompt chỉ có nội dung không định danh thì không mặc nhiên là DLCN | [luật] (qua Luật 91/2025) | gọi API AI kèm dữ liệu người dùng; vùng máy chủ của nhà cung cấp |
| 7.4 | **Không hiển thị con số AI không đo được** (vd điểm phát âm từ mô hình chỉ nhận dạng chữ) — dễ thành quảng cáo sai | [khuyến nghị] (+ mảng 4.2) | điểm % hiển thị từ đầu ra AI |
| 7.5 | **Lọc đầu ra** nội dung cấm/nhạy cảm trước khi hiện | [khuyến nghị] (+ mảng 6.5) | bước moderation |
| 7.6 | **Giả mạo** hình ảnh/giọng nói/video người khác **trái pháp luật**: cấm. Mô phỏng hợp pháp vẫn phải có đồng ý của người đó (quyền hình ảnh, DLCN) và gắn nhãn | [luật] (Luật 116/2025 — mảng 6.2; Luật 134/2025) | tính năng đổi giọng/ghép mặt |
