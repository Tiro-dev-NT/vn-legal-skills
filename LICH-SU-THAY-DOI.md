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
