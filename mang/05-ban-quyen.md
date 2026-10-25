# Mảng 5 — Bản quyền (sở hữu trí tuệ)

> Tham khảo, không phải tư vấn pháp lý — [MIEN-TRU-TRACH-NHIEM.md](../MIEN-TRU-TRACH-NHIEM.md). Tóm tắt từ nguồn trong [NGUON.md](../NGUON.md); đối chiếu văn bản gốc trước khi dựa vào.

**Áp khi:** dùng nội dung, ảnh, font, âm thanh, **dữ liệu hoặc API**, thư viện mã của người khác; cào dữ liệu từ web khác; hoặc cho người dùng đăng nội dung.

**Văn bản:** Luật SHTT — đọc bản hợp nhất VBHN 67/VBHN-VPQH (2026) · Luật 131/2025/QH15 (sửa đổi, hiệu lực 01/04/2026, có thêm trách nhiệm nền tảng số và vi phạm trên môi trường số). Link: [NGUON.md](../NGUON.md). Số điều: chỉ trích ở phần Mức phạt (đã đối chiếu toàn văn); luật nội dung **chưa trích**.

## Việc phải có

| # | Việc | Nhãn | Dấu hiệu trong mã |
|---|---|---|---|
| 5.1 | **Sổ nguồn gốc tài sản**: mỗi ảnh/âm thanh/font/bộ dữ liệu ghi nguồn + giấy phép | [khuyến nghị] | tệp `LICENSES`, `NOTICE`, `ATTRIBUTION`; thư mục `assets/` |
| 5.2 | **Giấy phép thư viện mã** được tôn trọng: giữ thông báo bản quyền (MIT/BSD/Apache), hiểu nghĩa vụ chia sẻ lại (GPL, CC BY-SA) | [luật] (quyền tác giả với phần mềm) | `package.json`, `vendor/`, thư viện tự host |
| 5.3 | **Không chép sách/giáo trình/đề thi** có bản quyền vào sản phẩm; trích dẫn ngắn có nguồn chỉ trong giới hạn luật cho phép | [luật] | dữ liệu nội dung; so với tài liệu gốc |
| 5.4 | **Sưu tập dữ liệu** của người khác — tập hợp có tính sáng tạo ở **sự tuyển chọn, sắp xếp** tư liệu — được bảo hộ quyền tác giả; bảo hộ không bao hàm chính các tư liệu đó (dữ kiện thô như một con số giá không tự thành tác phẩm, nhưng cách tuyển chọn, sắp xếp thì có thể) | [luật] Luật SHTT (VBHN 67/VBHN-VPQH) Điều 22 khoản 2 | — |
| 5.5 | **Nội dung người dùng đăng**: có điều khoản về quyền, có kênh nhận báo vi phạm và gỡ | [luật] (trách nhiệm nền tảng — Luật 131/2025) | form báo cáo vi phạm |
| 5.6 | **Ảnh/âm thanh do AI sinh**: ghi điều khoản dịch vụ của công cụ, tránh tạo theo tên nghệ sĩ/nhân vật có bản quyền | [khuyến nghị] (+ mảng 7) | prompt lưu kèm ảnh |
| 5.7 | **Văn bản pháp luật** không được bảo hộ quyền tác giả — được trích dẫn | [luật] | — |
| 5.8 | **Dữ liệu và API của bên khác** (giá chứng khoán, tỷ giá, giá vàng, bản đồ, thời tiết, tin tức, từ điển, dữ liệu sản phẩm…): đọc **điều khoản sử dụng / giấy phép** của bên cung cấp. Gói miễn phí thường chỉ cho dùng phi thương mại, giới hạn lưu trữ, cấm phân phối lại, bắt ghi nguồn; sản phẩm thu tiền ⇒ cần gói thương mại hoặc hợp đồng cấp phép. Điều khoản đã chấp nhận là **hợp đồng**: vi phạm phải chịu trách nhiệm dân sự và bồi thường thiệt hại, dù dữ liệu có hay không được bảo hộ quyền tác giả. Dùng API để thu thập, sao chép, trích xuất dữ liệu **trái phép** còn bị phạt hành chính (mục Mức phạt) | [luật] BLDS 91/2015 Điều 385, 351, 360, 419; NĐ 363/2026 Điều 13 khoản 3 điểm c · [khuyến nghị] lưu bản điều khoản + gói đã mua | khoá API, URL API bên ngoài trong mã; dữ liệu bên ngoài lưu vào DB của mình |
| 5.9 | **Cào dữ liệu (scraping)** từ web của người khác: dùng công cụ tự động, phần mềm truy xuất, công cụ khai thác, dò quét, can thiệp **trái phép** vào hệ thống để thu thập dữ liệu bị phạt hành chính; truy xuất **ngoài phạm vi được cấp quyền** cũng bị phạt. Cộng thêm điều khoản của web đó (thường cấm) và bảo hộ sưu tập dữ liệu (5.4). Cào **dữ liệu cá nhân** (mạng xã hội…) ⇒ thêm mảng 1.12. "Phi thương mại" **không** tự miễn trách nhiệm. NĐ chưa giải thích "trái phép" ⇒ trường hợp không rõ (web công khai không cấm) cần luật sư | [luật] NĐ 363/2026 Điều 12 khoản 3 điểm a, d (hiệu lực 11/11/2026; chép từ ảnh quét) · [khuyến nghị] ưu tiên API chính thức có giấy phép | bot/crawler, thư viện cào (puppeteer, playwright, cheerio, BeautifulSoup) chạy trên web của bên khác |
| 5.10 | **Dịch vụ nhúng và SDK** (video, bản đồ, đăng nhập, phông chữ, phân tích): tuân điều khoản hiển thị của bên đó (giữ logo/ghi nguồn, không che quảng cáo của họ, giới hạn lượt gọi); đồng thời là **bên nhận dữ liệu** ⇒ ghi vào chính sách bảo mật (mảng 1.7) | [khuyến nghị] · [luật] phần công bố bên nhận (mảng 1) | `<iframe`, thẻ script nhúng của bên ngoài, SDK |
| 5.11 | **Điều khoản của nhà cung cấp AI** về đầu ra: quyền dùng thương mại kết quả, cấm dùng đầu ra để huấn luyện mô hình cạnh tranh, cấm một số mục đích; dữ liệu người dùng gửi đi (mảng 7.3) | [khuyến nghị] — đọc điều khoản của từng nhà cung cấp | gọi API mô hình AI |
| 5.12 | **Dữ liệu thị trường tài chính** (giá chứng khoán theo thời gian thực, dữ liệu sàn) thường được bán theo giấy phép phân phối riêng; dùng để tư vấn, khuyến nghị đầu tư còn chạm điều kiện kinh doanh ngành tài chính (lộ trình mảng 18 — chưa làm) | [khuyến nghị] — văn bản ngành chứng khoán **chưa có trong bộ nguồn** | widget giá, bảng giá, tín hiệu mua/bán |
| 5.13 | **Dùng quyền truy cập của người khác hoặc cho người khác dùng quyền của mình**: dùng tài khoản, khoá truy cập của người khác để truy xuất dữ liệu; cho người khác dùng tài khoản, khoá API của mình; chia sẻ dữ liệu ngoài phạm vi hợp đồng cho phép — đều có hành vi bị phạt. API hay tài khoản cấp cho **một cá nhân** mà đem phục vụ người dùng của sản phẩm thường vi phạm điều khoản (5.8). **Lách chặn** (đổi IP, giả trình duyệt, vượt giới hạn lượt gọi): nếu biện pháp đó là biện pháp công nghệ bảo vệ quyền tác giả thì cố ý làm vô hiệu nó là **hành vi xâm phạm quyền tác giả**; với dữ liệu không được bảo hộ, vẫn là bằng chứng truy cập ngoài phạm vi được phép (5.9) | [luật] NĐ 363/2026 Điều 12 khoản 2 điểm b, c; Điều 13 khoản 1 điểm b (chép từ ảnh quét); Luật SHTT Điều 28 khoản 4, 5 | khoá API cá nhân trong mã server; proxy xoay IP; thay User-Agent; dữ liệu bên ngoài phát lại cho người dùng |
| 5.14 | **Dùng dữ liệu để huấn luyện AI**: được dùng văn bản và dữ liệu **đã công bố hợp pháp, công chúng được tiếp cận** cho nghiên cứu khoa học, thử nghiệm, **huấn luyện hệ thống AI**, nếu không ảnh hưởng bất hợp lý tới quyền của tác giả, chủ sở hữu; với tác phẩm được bảo hộ quyền tác giả còn phải theo quy định riêng của Chính phủ (**chưa kiểm đã có nghị định chưa**). Không phải giấy phép để phát lại nội dung gốc | [luật] Luật SHTT Điều 7 khoản 5 (bổ sung bởi Luật 131/2025, hiệu lực 01/04/2026) | pipeline huấn luyện/tinh chỉnh mô hình bằng dữ liệu bên ngoài |

## Mức phạt (NĐ 341/2025/NĐ-CP — đã đối chiếu toàn văn Công báo)

**Mức Chương II là của CÁ NHÂN; tổ chức gấp 2; hộ kinh doanh như cá nhân** (Điều 5 khoản 1, 2 — một số khoản, gồm phần lớn Điều 41, là mức tổ chức). Trần: 250 triệu (cá nhân) · 500 triệu (tổ chức).
Hiệu lực 15/02/2026; bãi bỏ NĐ 131/2013 và NĐ 28/2017 (Điều 63).

| Hành vi | Mức | Căn cứ | Ứng với mục |
|---|---|---|---|
| **Sao chép tác phẩm** không được phép | 5–50 triệu (cá nhân) theo bậc giá trị; tổ chức 10–100 triệu — xem bậc trong bản gốc | Điều 16 | 5.3, 5.4 |
| **Truyền đạt tác phẩm đến công chúng** (đăng lên web/app) không được phép | 30–50 triệu (theo bản trích) | Điều 15 | 5.3 |
| Không ghi/ghi sai tên tác giả | 1–5 triệu (theo bản trích) | Điều 7 | 5.1 |
| Doanh nghiệp **trung gian** (cho người dùng đăng nội dung): không cảnh báo người dùng, không công bố quy trình gỡ bỏ… | 10–20 triệu (tổ chức) | Điều 41 khoản 1 | 5.5 |
| Doanh nghiệp trung gian **không gỡ bỏ/ngăn chặn** nội dung xâm phạm trong **24 giờ** kể từ khi nhận yêu cầu bằng văn bản | 100–150 triệu (tổ chức) | Điều 41 khoản 7 | 5.5 |

Phần mềm/chương trình máy tính dùng không phép: NĐ 341 **không có điều riêng** — áp các điều chung (sao chép, phân phối) theo bản gốc; **cần luật sư** khi gặp.
Vi phạm nghiêm trọng có thể bị xử lý **hình sự** ([tóm tắt Chính phủ](https://xaydungchinhsach.chinhphu.vn/quy-dinh-muc-phat-toi-xam-pham-quyen-tac-gia-quyen-lien-quan-119260508154839332.htm)).


**Dữ liệu (NĐ 363/2026/NĐ-CP, hiệu lực 11/11/2026 — chép từ ảnh quét, đối chiếu lại bản Công báo khi có):** mức Chương II là của **cá nhân**, tổ chức gấp 2, hộ kinh doanh như cá nhân (Điều 6, Điều 2 khoản 3).

| Hành vi | Mức (cá nhân) | Căn cứ |
|---|---|---|
| Dùng tài khoản, khoá truy cập của người khác; cho người khác dùng tài khoản, khoá của mình để truy xuất dữ liệu | 20–40 triệu | Điều 12 khoản 2 điểm b, c |
| Chia sẻ, cung cấp dữ liệu ngoài phạm vi hợp đồng cho phép | 20–40 triệu | Điều 13 khoản 1 điểm b |
| Truy xuất ngoài phạm vi được cấp quyền; **dùng công cụ tự động, dò quét trái phép để thu thập dữ liệu** | 40–60 triệu + tịch thu phương tiện, buộc gỡ công cụ, nộp lại lợi bất hợp pháp | Điều 12 khoản 3 điểm a, d; khoản 4, 5 |
| **Dùng API, nền tảng chia sẻ dữ liệu để thu thập, sao chép, trích xuất dữ liệu trái phép** | 80–100 triệu + đình chỉ 1–6 tháng, buộc xoá dữ liệu | Điều 13 khoản 3 điểm c; khoản 4, 5 |

