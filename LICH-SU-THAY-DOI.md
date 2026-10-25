# Lịch sử thay đổi pháp luật & nội dung repo

> Mỗi lần luật đổi hoặc nội dung repo được sửa vì đọc sai, ghi **một mục** ở đây: mới nhất lên đầu.
> Mục đích: người dùng biết **luật cũ là gì, đổi thành gì, từ ngày nào, mục nào trong repo bị ảnh hưởng** — kể cả khi dự án của họ
> từng làm theo bản cũ (hành vi xảy ra trước ngày hiệu lực có thể vẫn xử theo văn bản cũ, xem điều khoản chuyển tiếp).
> Bản cũ của đoạn nội dung bị thay được lưu nguyên văn ở [`luu-tru/`](luu-tru/00-MUC-LUC.md). Lịch sử đầy đủ từng dòng: `git log -p`.

## Cách ghi một mục

```
### <ngày ghi YYYY-MM-DD> — <tiêu đề ngắn>
- Loại: LUẬT ĐỔI | SỬA ĐỌC SAI | BỔ SUNG
- Cũ: <văn bản cũ, ngày hết hiệu lực> — nội dung chính
- Mới: <văn bản mới, ngày ban hành, ngày hiệu lực> — nội dung chính; link nguồn chính thức
- Chuyển tiếp: <điều khoản chuyển tiếp nếu có / "chưa đọc">
- Mục repo bị ảnh hưởng: <mang/xx mục a.b, NGUON.md dòng …>
- Bản cũ lưu ở: <luu-tru/…> (nếu có thay nội dung)
```

---

### 2026-10-25 — Sở hữu công nghiệp: xử phạt sửa đổi 2026, phí, tên miền (khi thêm mảng 12)
- Loại: LUẬT ĐỔI (ghi lại lịch sử có sẵn) · BỔ SUNG
- **Xử phạt sở hữu công nghiệp** — NĐ 99/2013/NĐ-CP **không bị thay**, chỉ được sửa lần lượt bởi NĐ 126/2021/NĐ-CP (hiệu lực 01/01/2022), NĐ 46/2024/NĐ-CP (01/07/2024) và **NĐ 186/2026/NĐ-CP** (ban hành 26/05/2026, hiệu lực 15/07/2026). Điểm mới đáng chú ý của NĐ 186/2026 (đọc qua bản hợp nhất VBHN 25/2026/VBHN-NĐ-BKHCN, chú thích cuối trang): thêm biện pháp **ngăn chặn truy cập tên miền xâm phạm** (Điều 3 khoản 3 điểm a; Điều 14 khoản 18 điểm c), **tạm giữ tên miền** (Điều 3a), buộc đổi tên **hộ kinh doanh** ngoài tên doanh nghiệp (Điều 11 khoản 17 điểm d), phân định lại thẩm quyền (Điều 15 — chú thích 88 của bản hợp nhất; phần thẩm quyền chưa đọc). Chuyển tiếp: chưa đọc. Nguồn: https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-186-2026-nd-cp-469660.htm. Mục ảnh hưởng: mảng 12 (Mức phạt, 12.7, 12.9).
- **Luật SHTT sửa bởi Luật 131/2025/QH15** (hiệu lực 01/04/2026) — trong phạm vi mảng 12: Điều 205 khoản 1 điểm d (trần bồi thường khi không xác định được thiệt hại, nay **01 tỷ đồng**) và khoản 2 được sửa; Điều 119 khoản 2 sửa và thêm khoản 2a (**thẩm định nội dung nhanh** đơn nhãn hiệu, 3 tháng — điều kiện ở NĐ 65/2023 Điều 14a do NĐ 100/2026 bổ sung, hiệu lực 01/04/2026); Điều 198b đổi tên, thêm khoản 5a (trách nhiệm chủ quản nền tảng số). Mức trần cũ của Điều 205: chưa đọc bản cũ. Mục ảnh hưởng: mảng 12.14, 12.15, phần bồi thường.
- **Lệ phí sở hữu công nghiệp** — TT 263/2016/TT-BTC (hiệu lực 01/01/2017) vẫn là biểu gốc; TT 64/2025/TT-BTC giảm **50% lệ phí** (Mục A) từ 01/07/2025 đến hết **31/12/2026** ⇒ từ 01/01/2027 trở lại mức đầy đủ (trừ khi có văn bản mới). Mục ảnh hưởng: mảng 12 "Phí đăng ký".
- **Viễn thông, tên miền** — Luật Viễn thông 41/2009/QH12 (sửa bởi Luật 21/2017, Luật 23/2018) hết hiệu lực từ 01/07/2024, thay bởi Luật 24/2023/QH15 (Điều 72 khoản 2). NĐ 147/2024 ghi cơ quan quản lý tên miền là Bộ Thông tin và Truyền thông (Trung tâm Internet Việt Nam); văn bản năm 2026 (VBHN 25/2026, Điều 3a) ghi Bộ Khoa học và Công nghệ (Trung tâm Internet Việt Nam) — văn bản chuyển chức năng **chưa đọc**. Mục ảnh hưởng: mảng 12.9, 12.10.
- Bản cũ lưu ở: không có (mảng mới).

### 2026-10-25 — Sửa đọc sai: app dùng mô hình AI của bên khác là NHÀ CUNG CẤP, không chỉ bên triển khai
- Loại: SỬA ĐỌC SAI
- Cũ (mảng 7 trước commit này): "đa số web nhỏ dùng API thuộc nhóm bên triển khai".
- Mới: Luật 134/2025 Điều 3 khoản 4 — nhà cung cấp là người đưa hệ thống AI ra thị trường/đưa vào sử dụng **dưới tên, thương hiệu của mình, không phụ thuộc hệ thống đó do họ tự phát triển hay do bên thứ ba phát triển**; NĐ 142/2026 Điều 12 khoản 3, Điều 16 khoản 6. Hệ quả: nghĩa vụ phân loại rủi ro, thông báo (mức trung bình, cao), đánh dấu kỹ thuật âm thanh/ảnh/video (Điều 17) áp cho app.
- Mục ảnh hưởng: mảng 7 toàn bộ. Bản cũ: `git show 140e003:mang/07-tri-tue-nhan-tao.md`.


### 2026-10-25 — Trí tuệ nhân tạo: Luật 134/2025 thay Chương IV Luật 71/2025; Danh mục rủi ro cao; sửa vai trò "app gọi API"
- Loại: LUẬT ĐỔI + SỬA ĐỌC SAI + BỔ SUNG
- **Luật đổi** — Cũ: Luật 71/2025/QH15 (Công nghiệp công nghệ số) Chương IV "Trí tuệ nhân tạo" (Điều 41–45, gồm Điều 44 dấu hiệu nhận dạng hệ thống AI), khoản 9 Điều 3, khoản 7 Điều 4, khoản 6 Điều 12, điểm đ khoản 2 Điều 34 — hết hiệu lực 01/03/2026. Mới: Luật 134/2025/QH15 (ban hành 10/12/2025, hiệu lực 01/03/2026; bãi bỏ tại Điều 33) — https://congbao.chinhphu.vn/van-ban/luat-so-134-2025-qh15-468694.htm
- **Bổ sung** — QĐ 33/2026/QĐ-TTg Danh mục hệ thống AI có rủi ro cao (ban hành 30/06/2026, hiệu lực 15/08/2026) — https://congbao.chinhphu.vn/van-ban/quyet-dinh-so-33-2026-qd-ttg-469951/66726.htm
- **Sửa đọc sai** — bản cũ mảng 7 ghi "đa số web nhỏ dùng API thuộc nhóm bên triển khai". Theo Luật 134/2025 Điều 3 khoản 4 (nhà cung cấp gồm cả người đưa hệ thống do bên thứ ba phát triển ra dưới thương hiệu mình) và NĐ 142/2026 Điều 12 khoản 3, app mang tính năng AI dưới tên mình thường là **nhà cung cấp** (kiêm bên triển khai) ⇒ có nghĩa vụ tự phân loại và thông báo (nếu trung bình/cao).
- Chuyển tiếp: Luật 134/2025 Điều 35 (hệ thống hoạt động trước 01/03/2026: 18 tháng y tế/giáo dục/tài chính, 12 tháng còn lại); QĐ 33/2026 Điều 4 (hệ thống thuộc Danh mục: trước 01/09/2027 y tế/giáo dục/tài chính, trước 01/03/2027 còn lại; đưa vào hoạt động trong 6 tháng từ 15/08/2026: trước 01/03/2027).
- Mục repo bị ảnh hưởng: mang/07 (viết lại toàn bộ; giữ mã 7.1–7.6, thêm 7.7–7.17); NGUON.md dòng Luật 134/2025, NĐ 142/2026, QĐ 33/2026 (mới), Luật 116/2025, NĐ 356/2025, BLDS 91/2015, Luật 71/2025; THU-TUC.md (dòng AI mới).
- Bản cũ lưu ở: chưa chép sang luu-tru/ (người điều phối quyết — bản cũ còn trong git).

### 2026-10-25 — Đăng ký kinh doanh, danh mục ngành nghề có điều kiện, hệ thống ngành kinh tế
- Loại: LUẬT ĐỔI (ghi lại khi lập mảng 10)
- **Đăng ký doanh nghiệp, hộ kinh doanh** — Cũ: NĐ 01/2021/NĐ-CP (hết hiệu lực 01/07/2025). Mới: NĐ 168/2025/NĐ-CP (ban hành 30/06/2025, hiệu lực 01/07/2025; thay tại Điều 124 khoản 2), sửa bởi NĐ 296/2026/NĐ-CP (hiệu lực 23/07/2026: đăng ký hộ kinh doanh ở cấp xã, nộp qua Cổng dịch vụ công quốc gia / Ứng dụng định danh quốc gia). Nguồn: https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-168-2025-nd-cp-45354.htm · https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-296-2026-nd-cp-470177/67429.htm
- **Luật Đầu tư** — Cũ: Luật 61/2020/QH14 (hết hiệu lực 01/03/2026; Điều 7 và Phụ lục IV cũ hết 01/07/2026). Mới: Luật 143/2025/QH15 (ban hành 11/12/2025, hiệu lực 01/03/2026; Điều 7 + Phụ lục IV — 198 ngành — từ 01/07/2026; Điều 51 khoản 4). Nguồn: https://congbao.chinhphu.vn/van-ban/luat-so-143-2025-qh15-468703.htm
- **Danh mục ngành nghề có điều kiện (ba lớp)** — (1) 01/07/2026 – 28/02/2027: **NQ 66.17/2026/NQ-CP** (ban hành 15/05/2026) — Danh mục **142** ngành, ưu tiên áp dụng (Điều 6 khoản 3). (2) Từ **01/03/2027**: **Luật 24/2026/QH16** (ban hành 24/08/2026) thay Phụ lục IV bằng Danh mục **137** ngành. Ra khỏi danh mục từ 01/07/2026: nội dung thông tin trên mạng, trò chơi điện tử (dòng 172 gốc), tên miền, dịch vụ kế toán…; "mạng xã hội" và "trò chơi trên mạng viễn thông, mạng Internet" vẫn còn. Nguồn: https://congbao.chinhphu.vn/van-ban/nghi-quyet-so-6617-2026-nq-cp-469565.htm · https://congbao.chinhphu.vn/van-ban/luat-so-24-2026-qh16-470458.htm
- Chuyển tiếp: NQ 66.17/2026 Điều 5 (giấy phép đã cấp cho ngành bị cắt được dùng đến hết hạn); Luật 24/2026 Điều 3 khoản 3 (ngành bị bãi bỏ: được kinh doanh không cần đáp ứng điều kiện; giấy tờ đã cấp dùng đến hết hạn; hồ sơ đang xử lý bị trả lại); Điều 2 khoản 3 (bộ quy định phương án quản lý thay thế trước 01/03/2027).
- **Hệ thống ngành kinh tế (mã ngành)** — Cũ: QĐ 27/2018/QĐ-TTg (hết hiệu lực 15/11/2025). Mới: QĐ 36/2025/QĐ-TTg (ban hành 29/09/2025, hiệu lực 15/11/2025; Điều 4 khoản 2). Mã 6201, 6312 không có trong Danh mục QĐ 36/2025 (đã tìm, 0 kết quả; nội dung QĐ 27/2018 chưa đọc); lập trình nay là 6219, xuất bản phần mềm 5829, hạ tầng/xử lý dữ liệu 6310. Nguồn: https://congbao.chinhphu.vn/van-ban/quyet-dinh-so-36-2025-qd-ttg-46315/59210.htm
- **Xử phạt đăng ký doanh nghiệp** — NĐ 122/2021/NĐ-CP sửa bởi NĐ 288/2026/NĐ-CP (hiệu lực 21/07/2026): tăng mức Điều 43 (kê khai không trung thực: 30–70 triệu), Điều 44 (không thông báo thay đổi: 30–70 triệu; trễ hạn theo bậc), Điều 48. Điều 46 khoản 4 và Điều 62 (hộ kinh doanh) không đổi. Nguồn: https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-288-2026-nd-cp-470148.htm
- Mục repo bị ảnh hưởng: mang/10 (mới); THU-TUC.md dòng T0; NGUON.md dòng NĐ 168/2025 (chuyển mục, thêm ngày/link).
- Bản cũ lưu ở: không có (mảng mới, chưa thay nội dung cũ).

### 2026-10-25 — Thanh toán, xử phạt tiền tệ ngân hàng: văn bản đã bị thay trước ngày lập mảng 11
- Loại: LUẬT ĐỔI (ghi lại lịch sử có sẵn)

| Cũ | Mới | Ngày hiệu lực | Căn cứ thay | Chuyển tiếp | Mục ảnh hưởng |
|---|---|---|---|---|---|
| NĐ 88/2019/NĐ-CP (xử phạt VPHC tiền tệ, ngân hàng) + NĐ 143/2021/NĐ-CP (sửa NĐ 88) | NĐ 340/2025/NĐ-CP | 09/02/2026 | NĐ 340/2025 Điều 72 khoản 2 | Quyết định xử phạt ban hành trước 09/02/2026 còn khiếu nại ⇒ áp quy định tại thời điểm ra quyết định (Điều 73) | mảng 11 — Mức phạt |
| NĐ 23/2023/NĐ-CP — Điều 2, Điều 3 (sửa NĐ 88/2019) | bãi bỏ | 09/02/2026 | NĐ 340/2025 Điều 72 khoản 3 | — | mảng 11 — Mức phạt |
| NĐ 101/2012/NĐ-CP (thanh toán không dùng tiền mặt) + NĐ 80/2016/NĐ-CP (sửa NĐ 101) | NĐ 52/2024/NĐ-CP | 01/07/2024 | NĐ 52/2024 Điều 37 khoản 2 (cũng bãi bỏ Điều 3 NĐ 16/2019) | Giấy phép trung gian thanh toán cấp trước 01/07/2024 dùng tới hết hạn (Điều 36 khoản 5) | mảng 11.1–11.3 |

Ghi chú: tài liệu, điều khoản sử dụng còn dẫn "NĐ 101/2012" (thanh toán) hay "NĐ 88/2019" (mức phạt) là đã cũ.


### 2026-10-24 — Khởi tạo bộ nguồn: ghi nhận các văn bản đã bị thay trước ngày lập repo
- Loại: LUẬT ĐỔI (ghi lại lịch sử có sẵn)
- **Dữ liệu cá nhân** — Cũ: NĐ 13/2023/NĐ-CP. Mới: Luật 91/2025/QH15 (hiệu lực 01/01/2026) + NĐ 356/2025/NĐ-CP (hiệu lực 01/01/2026); xử phạt riêng NĐ 330/2026/NĐ-CP (hiệu lực 19/08/2026). Tài liệu nào còn dẫn NĐ 13/2023 là đã cũ. Mục ảnh hưởng: mảng 1.
- **Quảng cáo (xử phạt)** — Cũ: NĐ 38/2021/NĐ-CP, NĐ 128/2022/NĐ-CP, Điều 4 NĐ 129/2021/NĐ-CP. Mới: NĐ 87/2026/NĐ-CP (ban hành 27/03/2026, hiệu lực 15/05/2026), bãi bỏ tại Điều 93; chuyển tiếp Điều 94. Luật Quảng cáo sửa bởi Luật 75/2025/QH15 (hiệu lực 01/01/2026). Mục ảnh hưởng: mảng 4.
- **Quyền tác giả (xử phạt)** — Cũ: NĐ 131/2013/NĐ-CP, NĐ 28/2017/NĐ-CP. Mới: NĐ 341/2025/NĐ-CP (hiệu lực 15/02/2026), bãi bỏ tại Điều 63. Luật SHTT sửa bởi Luật 131/2025/QH15 (hiệu lực 01/04/2026). Mục ảnh hưởng: mảng 5.
- **Internet, game** — Cũ: NĐ 72/2013/NĐ-CP, NĐ 27/2018/NĐ-CP (game: chỉ giới hạn 180 phút/ngày cho G1). Mới: NĐ 147/2024/NĐ-CP (hiệu lực 25/12/2024), bãi bỏ tại Điều 83; thêm giới hạn 60 phút/một game, áp cho G1–G4, nhãn 16+. Xử phạt game: NĐ 174/2026/NĐ-CP (hiệu lực 01/07/2026). Mục ảnh hưởng: mảng 6, 8.
- **Thương mại điện tử** — Mới: Luật 122/2025/QH15 + NĐ 248/2026/NĐ-CP (cùng hiệu lực 01/07/2026); thủ tục thông báo website cũ trên cổng Bộ Công Thương đang chuyển sang khung mới. Chuyển tiếp: chưa đọc chính văn. Mục ảnh hưởng: mảng 3.
- **An ninh mạng** — Mới: Luật 116/2025/QH15 (hiệu lực 01/07/2026), NĐ 331/2026/NĐ-CP (hiệu lực 19/08/2026). Quan hệ với Luật An ninh mạng 2018 và Luật An toàn thông tin mạng 2015: **chưa đọc điều bãi bỏ**. Mục ảnh hưởng: mảng 6.
- **Khuyến mại** — NĐ 81/2018/NĐ-CP sửa bởi NĐ 128/2024/NĐ-CP (hiệu lực 01/12/2024) và NĐ 239/2026/NĐ-CP (26/06/2026). Mục ảnh hưởng: 4.10.

### 2026-10-24 — Thuế, hoá đơn: các văn bản đã bị thay trước ngày lập repo
- Loại: LUẬT ĐỔI (ghi lại lịch sử có sẵn)
- **Thuế khoán** hộ kinh doanh — Cũ: Điều 51 Luật 38/2019/QH14. Hết từ 01/01/2026 (Luật 108/2025/QH15 Điều 52 khoản 3); thay bằng tự khai/thông báo doanh thu theo NĐ 68/2026/NĐ-CP (hiệu lực 05/03/2026). Mục ảnh hưởng: mảng 9.2.
- **Luật Quản lý thuế** — Cũ: Luật 38/2019/QH14. Mới: Luật 108/2025/QH15 (ban hành 10/12/2025, hiệu lực 01/07/2026).
- **Ngưỡng doanh thu** hộ/cá nhân kinh doanh không chịu GTGT, không nộp TNCN — Luật 149/2025 và NĐ 68/2026: 500 triệu (mức trước đó: chưa đối chiếu). Hiện: **01 tỷ** (Luật 09/2026/QH16 giao Chính phủ; NĐ 141/2026/NĐ-CP, áp từ 01/01/2026). Mục ảnh hưởng: mảng 9 "Số liệu chính".
- **Hoá đơn điện tử** — Cũ: NĐ 123/2020/NĐ-CP, NĐ 70/2025/NĐ-CP, TT 32/2025/TT-BTC. Mới: NĐ 254/2026/NĐ-CP (Điều 43 khoản 2) + TT 91/2026/TT-BTC, hiệu lực 01/07/2026. Mục ảnh hưởng: 9.4, 9.5.
- **Hồ sơ thuế hộ kinh doanh** — Cũ: TT 40/2021, TT 100/2021. Mới: TT 18/2026/TT-BTC (sửa bởi TT 50/2026).
- **Thuế TNCN** — Cũ: Luật 04/2007/QH12. Mới: Luật 109/2025/QH15 (hiệu lực 01/07/2026; thu nhập kinh doanh từ kỳ tính thuế 2026).

### 2026-10-24 — Sửa đọc sai: mức phạt NĐ 330/2026 là mức TỔ CHỨC
- Loại: SỬA ĐỌC SAI
- Cũ (bản repo trước commit 21e84c6): bảng phạt mảng 1 lấy từ tin Báo Chính phủ, ghi "chưa tách cá nhân/tổ chức — không tự nhân đôi cho tổ chức".
- Mới: đối chiếu toàn văn — Mục 6 Chương II (bảo vệ DLCN) ghi **mức tổ chức**, cá nhân **1/2** (Điều 7 khoản 1); hộ kinh doanh như cá nhân (Điều 2 khoản 3). Ngược với mảng 4, 5 (mức cá nhân, tổ chức gấp 2) — đọc đúng quy tắc của từng nghị định.
- Mục repo bị ảnh hưởng: mảng 1 phần Mức phạt. Bản cũ: `git show 7984ad6:mang/01-du-lieu-ca-nhan.md`.
