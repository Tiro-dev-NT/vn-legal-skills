# Mảng 7 — Trí tuệ nhân tạo

**Áp khi:** app có tính năng AI sinh nội dung (chữ, ảnh, giọng), chấm điểm, gợi ý, chatbot.

**Văn bản:** Luật 134/2025/QH15 (Trí tuệ nhân tạo, hiệu lực 01/03/2026; 8 chương 35 điều). Link: [NGUON.md](../NGUON.md). Số điều: **chưa trích**.
Nghị định hướng dẫn: theo Bộ KH&CN đang dự thảo — **chưa có trong bộ nguồn**.

## Việc phải có

| # | Việc | Nhãn | Dấu hiệu trong mã |
|---|---|---|---|
| 7.1 | **Cho người dùng biết họ đang tương tác với AI** / nội dung do AI tạo | [khuyến nghị] — đối chiếu nghĩa vụ minh bạch trong Luật 134/2025 bản gốc | nhãn "AI" cạnh kết quả; chatbot tự giới thiệu |
| 7.2 | **Con người là người quyết định cuối** với việc quan trọng (chấm thi, đánh giá ảnh hưởng người dùng); cho khiếu nại kết quả AI | [khuyến nghị] (Bộ KH&CN: "AI là công cụ hỗ trợ, quyết định cuối cùng vẫn là con người") | nút "báo sai", quy trình phúc khảo |
| 7.3 | **Dữ liệu gửi cho nhà cung cấp AI** là chuyển/chia sẻ dữ liệu cá nhân ⇒ công bố + mảng 1.7 | [luật] (qua Luật 91/2025) | gọi API AI kèm nội dung người dùng |
| 7.4 | **Không sinh con số AI không đo được** (vd điểm phát âm từ mô hình chỉ nhận dạng chữ) — dễ thành quảng cáo sai | [khuyến nghị] (+ mảng 4.2) | điểm % hiển thị từ đầu ra AI |
| 7.5 | **Lọc đầu ra** nội dung cấm/nhạy cảm trước khi hiện | [khuyến nghị] (+ mảng 6.5) | bước moderation |
| 7.6 | **Deepfake** giọng/mặt người thật: cấm | [luật] (Luật 116/2025 — mảng 6.2) | — |
