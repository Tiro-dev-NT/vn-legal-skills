# Mảng 8 — Trò chơi điện tử (game)

> Tham khảo, không phải tư vấn pháp lý — [MIEN-TRU-TRACH-NHIEM.md](../MIEN-TRU-TRACH-NHIEM.md). Tóm tắt từ nguồn trong [NGUON.md](../NGUON.md); đối chiếu văn bản gốc trước khi dựa vào.

**Áp khi:** web/app cung cấp game chơi qua mạng cho người ở Việt Nam — kể cả game nhỏ trên trình duyệt, game trong app học tập có xếp hạng/vật phẩm, mini-game.

**Văn bản:** NĐ 147/2024/NĐ-CP (mục Trò chơi điện tử trên mạng, Điều 37–57; hiệu lực 25/12/2024; bãi bỏ NĐ 72/2013 và NĐ 27/2018) ·
NĐ 174/2026/NĐ-CP (xử phạt, Điều 98–99; hiệu lực 01/07/2026) · trò chơi **có thưởng**/đặt cược: NĐ 391/2026/NĐ-CP. Link: [NGUON.md](../NGUON.md).
**Đã đối chiếu toàn văn Công báo** cho các điều trích dưới đây (24/10/2026). Có **dự thảo sửa NĐ 147/2024** — kiểm bản sửa đổi đã có hiệu lực chưa lúc rà.

## Phân loại (NĐ 147/2024 Điều 37 khoản 1)

| Nhóm | Định nghĩa (nguyên ý) | Được phát hành khi có (Điều 37 khoản 2, 3) |
|---|---|---|
| G1 | nhiều người chơi tương tác với nhau **đồng thời qua máy chủ** của doanh nghiệp | Giấy phép cung cấp dịch vụ G1 **+** Quyết định phát hành từng game |
| G2 | người chơi chỉ tương tác với máy chủ của doanh nghiệp | Giấy chứng nhận cung cấp dịch vụ G2–G4 **+** Giấy xác nhận thông báo phát hành từng game |
| G3 | nhiều người chơi tương tác với nhau nhưng **không** qua máy chủ doanh nghiệp | như G2 |
| G4 | tải về qua mạng, không tương tác giữa người chơi và không tương tác với máy chủ | như G2 |

- Chủ thể phát hành là **doanh nghiệp** (Điều 37 khoản 2, 3). Tổ chức/cá nhân **nước ngoài** cung cấp cho người dùng VN, kể cả xuyên biên giới, phải **thành lập doanh nghiệp tại VN** (Điều 37 khoản 4).
- Cá nhân/hộ kinh doanh tự phát hành game cho người chơi VN ⇒ **cần luật sư xem**.
- **Nhãn tuổi** (Điều 38): **18+ · 16+ · 12+ · 00+** (mọi lứa tuổi).

## Việc phải có

| # | Việc | Nhãn | Dấu hiệu trong mã |
|---|---|---|---|
| 8.1 | Xác định **nhóm G1–G4** từng game; có đủ giấy phép/giấy chứng nhận + quyết định/xác nhận phát hành tương ứng | [luật] NĐ 147 Điều 37 | chế độ nhiều người chơi, websocket/realtime, máy chủ game, bảng xếp hạng trực tuyến |
| 8.2 | Tài khoản người chơi có **họ tên, ngày sinh, số điện thoại di động tại VN**; **xác thực** bằng số điện thoại; lưu thông tin trong thời gian dùng + 06 tháng sau | [luật] NĐ 147 Điều 39 (G1), Điều 48 (G2–G4) — thời hạn lưu theo tin Chính phủ | form đăng ký game; OTP |
| 8.3 | **Dưới 16 tuổi**: cha/mẹ/người giám hộ đăng ký tài khoản bằng thông tin của mình và giám sát thời gian, nội dung chơi | [luật] NĐ 147 Điều 39, 48 | luồng tài khoản trẻ em |
| 8.4 | **Dưới 18 tuổi**: hệ thống bảo đảm **≤ 60 phút/một game** và **≤ 180 phút/ngày** cho tất cả game của doanh nghiệp (ngày tính 00h00–24h00) | [luật] NĐ 147 Điều 39 khoản 1 điểm e (G1) và quy định tương ứng ở Điều 48 | bộ đếm thời gian theo tài khoản |
| 8.5 | **Hiển thị liên tục nhãn tuổi** khi giới thiệu, quảng cáo, phát hành; khuyến cáo *"Chơi quá 180 phút một ngày sẽ ảnh hưởng xấu đến sức khỏe"* trên màn hình **30 phút/lần** khi chơi và ở diễn đàn game | [luật] NĐ 147 Điều 39 khoản 1 điểm g (G1) và quy định tương ứng ở Điều 48 | nhãn tuổi trên trang game; thông báo định kỳ |
| 8.6 | **Không** nội dung mô phỏng casino / dùng hình ảnh lá bài (điều kiện không được phê duyệt) | [luật] NĐ 147 Điều 43, 52; phạt NĐ 174 Điều 99 khoản 4 | chủ đề game |
| 8.7 | **Vật phẩm ảo, đơn vị ảo, điểm thưởng**: chỉ khởi tạo đúng hồ sơ đã báo cáo; chỉ dùng trong game; **không quy đổi** ra tiền, thẻ cào, thẻ ngân hàng, thẻ mua hàng, thẻ game, thẻ quà tặng, hiện vật; **không mua bán giữa người chơi**; **không gắn khuyến mại có thưởng** bằng tiền/hiện vật thật vào giao diện game | [luật] NĐ 147 Điều 57 | cửa hàng vật phẩm; đổi điểm lấy quà/voucher; chợ giao dịch giữa người chơi |
| 8.8 | **Quảng cáo game** chỉ sau khi có quyết định phát hành (G1) / giấy xác nhận thông báo (G2–G4) | [luật] (phạt NĐ 174 Điều 99 khoản 2, 3 điểm d) | landing game, chiến dịch quảng cáo |
| 8.9 | Có trang thông tin giới thiệu dịch vụ game đủ thông tin; gắn **đoạn mã** được cấp vào mô tả trên kho ứng dụng/trang game; quản lý nội dung trò chuyện, diễn đàn trong game; giải quyết tranh chấp với người chơi | [luật] (phạt NĐ 174 Điều 99 khoản 1, 2) | trang giới thiệu game; chat trong game |
| 8.10 | **Có thưởng / may rủi** (quay thưởng, hộp quà ngẫu nhiên mua bằng tiền, cược): vùng của pháp luật trò chơi có thưởng — rủi ro rất cao | [luật] NĐ 391/2026 (xử phạt) — chưa đối chiếu toàn văn | gacha, loot box trả tiền, vòng quay |
| 8.11 | **Game trong app học tập** (đố vui, đấu từ vựng có xếp hạng): đấu với người khác qua máy chủ ⇒ có thể là **G1**; chỉ chơi với máy chủ ⇒ **G2**. **Không tự kết luận "không phải game"** | [khuyến nghị] — cần luật sư khi không rõ | — |

## Mức phạt (NĐ 174/2026/NĐ-CP — đã đối chiếu toàn văn)

**Mức dưới đây là của TỔ CHỨC; cá nhân vi phạm như tổ chức chịu 1/2** (Điều 4 khoản 3). Văn bản không nói rõ hộ kinh doanh tính theo mức nào ⇒ ghi "cần xác nhận".

| Hành vi | Mức (tổ chức) | Căn cứ |
|---|---|---|
| Cung cấp **G1 không có Giấy phép** | 150–170 triệu + tịch thu phương tiện, buộc nộp lợi bất hợp pháp, thu hồi tên miền/ứng dụng | Điều 98 khoản 5–7 |
| G1 không có Quyết định phát hành · G2–G4 không có Giấy chứng nhận | 70–100 triệu (+ biện pháp như trên) | Điều 98 khoản 4 |
| G2–G4 không có Giấy xác nhận thông báo phát hành | 50–70 triệu | Điều 98 khoản 3 điểm a |
| Không phân loại/hiển thị nhãn tuổi, không khuyến cáo; không xác thực số điện thoại; không hạn chế giờ chơi người dưới 18; quảng cáo khi chưa phép; gắn khuyến mại có thưởng vào game; không lưu thông tin người chơi | **G2–G4: 20–40 triệu · G1: 40–60 triệu** | Điều 99 khoản 2 (điểm a, d, đ, e, g, k, p…) và khoản 3 |
| Nội dung mô phỏng casino/lá bài, bạo lực, khiêu dâm, đánh bạc…; **cho mua bán vật phẩm ảo giữa người chơi** | 60–80 triệu | Điều 99 khoản 4 |
| **Quy đổi vật phẩm ảo/điểm thưởng ra tiền, thẻ, hiện vật** | 170–200 triệu | Điều 99 khoản 5 điểm a |

Trò chơi có thưởng/đặt cược (NĐ 391/2026, theo tin Chính phủ — chưa đối chiếu toàn văn): tối đa 100 triệu (cá nhân) · 200 triệu (tổ chức).

## Cần luật sư khi

phát hành game G1 · có vật phẩm trả tiền ngẫu nhiên · có quy đổi điểm/vật phẩm ra quà · người phát hành là cá nhân/hộ kinh doanh · doanh nghiệp nước ngoài.
