# Mảng 8 — Trò chơi điện tử (game)

> Tham khảo, không phải tư vấn pháp lý — [MIEN-TRU-TRACH-NHIEM.md](../MIEN-TRU-TRACH-NHIEM.md). Tóm tắt từ nguồn trong [NGUON.md](../NGUON.md); đối chiếu văn bản gốc trước khi dựa vào.

**Áp khi:** web/app cung cấp game chơi qua mạng cho người ở Việt Nam — kể cả game nhỏ chạy trên trình duyệt, game trong app học tập có xếp hạng/vật phẩm,
mini-game có thưởng. Game chơi offline hoàn toàn không qua mạng: đọc định nghĩa trong NĐ 147/2024 trước khi kết luận không áp dụng.

**Văn bản:** NĐ 147/2024/NĐ-CP (dịch vụ internet và thông tin trên mạng — mục trò chơi điện tử trên mạng; hiệu lực 25/12/2024) ·
NĐ 174/2026/NĐ-CP (xử phạt bưu chính, viễn thông, giao dịch điện tử, CNTT; hiệu lực 01/07/2026) ·
trò chơi **có thưởng**/đặt cược: NĐ 391/2026/NĐ-CP (xử phạt, ký 20/10/2026, hiệu lực 05/12/2026 theo tin Chính phủ). Link: [NGUON.md](../NGUON.md).
Cơ quan trả lời về game hiện nay: **Bộ Văn hoá, Thể thao và Du lịch** (theo Báo Chính phủ 28/09/2026). Có **dự thảo sửa NĐ 147/2024** — kiểm bản sửa đổi đã có hiệu lực chưa lúc rà.

## Phân loại trước (NĐ 147/2024 Điều 37 — theo Báo Chính phủ)

| Nhóm | Thủ tục |
|---|---|
| G1 | **Giấy phép** cung cấp dịch vụ G1 + **Quyết định** phát hành từng game |
| G2, G3, G4 | **Giấy chứng nhận** cung cấp dịch vụ + **Giấy xác nhận thông báo** phát hành từng game |

Đặc điểm từng nhóm (G1 thường là game nhiều người chơi tương tác qua máy chủ doanh nghiệp): **chưa trích — đang đối chiếu toàn văn**.

Ranh giới chính xác G1–G4: **đọc định nghĩa trong NĐ 147/2024 bản gốc**. Chủ thể cung cấp phải là **doanh nghiệp** (theo tin chính thức) ⇒ cá nhân/hộ kinh doanh tự phát hành game cho người chơi VN: **cần luật sư xem**.

## Việc phải có

| # | Việc | Nhãn | Dấu hiệu trong mã |
|---|---|---|---|
| 8.1 | **Xác định nhóm G1–G4** cho từng game và có giấy phép / giấy chứng nhận / quyết định hoặc xác nhận phát hành tương ứng | [luật] NĐ 147/2024 Điều 37 | chế độ nhiều người chơi, websocket/realtime, máy chủ game, bảng xếp hạng trực tuyến |
| 8.2 | **Đăng ký tài khoản người chơi** có họ tên, ngày sinh, **số điện thoại di động Việt Nam**; doanh nghiệp **xác thực** và lưu thông tin trong thời gian dùng + **06 tháng** sau | [luật] NĐ 147/2024 Điều 56 (theo Báo Chính phủ) | form đăng ký game; xác thực OTP |
| 8.3 | **Người dưới 16 tuổi**: cha/mẹ/người giám hộ đăng ký tài khoản và giám sát thời gian, nội dung chơi | [luật] Điều 56 (theo Báo Chính phủ) | luồng tài khoản trẻ em |
| 8.4 | **Người dưới 18 tuổi**: tối đa **60 phút/một game** và **180 phút/ngày** tổng — doanh nghiệp phải có hệ thống kỹ thuật quản lý | [luật] (theo Cục PTTH&TTĐT — mic.gov.vn; điều chính xác: chờ đối chiếu toàn văn) | bộ đếm thời gian chơi theo tài khoản |
| 8.5 | **Khuyến cáo sức khoẻ** "chơi quá 180 phút/ngày ảnh hưởng xấu đến sức khoẻ" hiển thị **30 phút/lần** trong khi chơi | [luật] (theo mst.gov.vn) | thông báo định kỳ trong game |
| 8.6 | **Phân loại độ tuổi** của game hiển thị cho người chơi (NĐ 147/2024 có thêm mốc **16+**) | [luật] — các mốc và nơi hiển thị: **đọc bản gốc** | nhãn độ tuổi ở trang game, quảng cáo game |
| 8.7 | **Không làm game mô phỏng casino / dùng hình ảnh lá bài** (không được cấp phép) | [luật] (theo mst.gov.vn) | chủ đề game |
| 8.8 | **Vật phẩm ảo, điểm thưởng**: không cho quy đổi ra tiền/hiện vật ngoài quy định; vật phẩm mua bằng tiền thật ⇒ thêm mảng 2 (hoàn tiền, giá rõ) | [luật] — quy định chính xác: **đọc bản gốc + dự thảo sửa đổi** | cửa hàng vật phẩm, đổi điểm lấy quà, chuyển nhượng giữa người chơi |
| 8.9 | **Có thưởng / may rủi** (quay thưởng, hộp quà ngẫu nhiên mua bằng tiền, cược): vùng của pháp luật trò chơi có thưởng — rủi ro rất cao | [luật] NĐ 391/2026 (xử phạt) | gacha, loot box trả tiền, vòng quay |
| 8.10 | **Quảng cáo game** chỉ cho game đã được phép phát hành; quảng cáo phải có nhãn độ tuổi | [khuyến nghị] — đối chiếu NĐ 147/2024 + mảng 4 | landing game |
| 8.11 | **Game trong app học tập** (đố vui, đấu từ vựng có xếp hạng): nếu có chơi cùng người khác qua máy chủ ⇒ có thể rơi vào G1; nếu chỉ chơi một mình ⇒ xem G2–G4. **Không tự kết luận "không phải game"** | [khuyến nghị] — cần luật sư khi không rõ | — |

## Mức phạt

- NĐ 174/2026: có chương xử phạt về trò chơi điện tử trên mạng — **mức cụ thể chưa có trong bộ nguồn** (đang đối chiếu toàn văn).
- Trò chơi có thưởng/đặt cược (NĐ 391/2026, theo tin Chính phủ): tối đa **100 triệu (cá nhân) · 200 triệu (tổ chức)**; có thể đình chỉ hoạt động, tịch thu tang vật.
- Tin cũ "phạt tới 200 triệu vì game G1 không phép" thuộc **dự thảo cũ** — không dùng.

## Cần luật sư khi

phát hành game G1 · có vật phẩm trả tiền ngẫu nhiên · có quy đổi điểm/vật phẩm ra tiền hoặc quà · người phát hành là cá nhân/hộ kinh doanh · máy chủ game ở nước ngoài cho người chơi VN.
