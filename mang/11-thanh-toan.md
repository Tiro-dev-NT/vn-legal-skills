# Mảng 11 — Thanh toán, ví điện tử, credit trong app, tài sản mã hoá

> Tham khảo, không phải tư vấn pháp lý — [MIEN-TRU-TRACH-NHIEM.md](../MIEN-TRU-TRACH-NHIEM.md). Tóm tắt từ nguồn trong [NGUON.md](../NGUON.md); đối chiếu văn bản gốc trước khi dựa vào.

**Áp khi:** web/app nhận tiền online (cổng thanh toán, chuyển khoản, QR, ví), bán gói credit/xu/điểm trả trước, có số dư trong tài khoản người dùng, chia tiền cho người bán/cộng tác viên, nhận tiền từ khách nước ngoài (PayPal, Stripe, giá USD), hoặc đụng tới crypto/token/NFT (nhận thanh toán, phát hành, sàn, quảng cáo).

**Văn bản (đã đối chiếu toàn văn Công báo cho các điều trích dưới đây, 25/10/2026 — bản trích: [trich-dan/2026-10-25-thanh-toan.md](../trich-dan/2026-10-25-thanh-toan.md)):**
NĐ 52/2024/NĐ-CP (thanh toán không dùng tiền mặt; hiệu lực 01/07/2024; thay NĐ 101/2012 và NĐ 80/2016; tìm kiếm không thấy văn bản sửa) ·
TT 40/2024/TT-NHNN (trung gian thanh toán; sửa bởi TT 41/2025, TT 22/2026 — không sửa Điều 6, 7) ·
Luật 32/2024/QH15 Luật Các tổ chức tín dụng (hiệu lực 01/07/2024; sửa bởi Luật 43/2024, Luật 96/2025 — đọc bản hợp nhất 158/VBHN-VPQH) ·
Pháp lệnh Ngoại hối 28/2005/PL-UBTVQH11 sửa bởi Pháp lệnh 06/2013/UBTVQH13 (bản hợp nhất 07/VBHN-VPQH) · TT 32/2013/TT-NHNN (hạn chế dùng ngoại hối; bản hợp nhất 14/VBHN-NHNN) ·
Luật 71/2025/QH15 Luật Công nghiệp công nghệ số (Chương V tài sản số; hiệu lực 01/01/2026) · NQ 05/2025/NQ-CP (thí điểm thị trường tài sản mã hoá; hiệu lực 09/09/2025, thí điểm 5 năm) ·
xử phạt: **NĐ 340/2025/NĐ-CP** (tiền tệ, ngân hàng; hiệu lực 09/02/2026; **thay NĐ 88/2019 và NĐ 143/2021**) · **NĐ 284/2026/NĐ-CP** (tài sản mã hoá; hiệu lực 01/09/2026 đến khi NQ 05/2025 hết hiệu lực). Link: [NGUON.md](../NGUON.md).
Tài liệu, điều khoản còn dẫn **NĐ 101/2012** (thanh toán) hay **NĐ 88/2019** (mức phạt) là đã cũ — xem [LICH-SU-THAY-DOI.md](../LICH-SU-THAY-DOI.md).

## Phân loại nhanh — cái gì người bán được tự làm

| Bạn làm | Tự làm được? | Căn cứ |
|---|---|---|
| Nhận tiền vào **tài khoản ngân hàng của chính mình** (chuyển khoản, QR) | được — ngân hàng là tổ chức cung ứng dịch vụ thanh toán | NĐ 52/2024 Điều 3 khoản 4; Điều 17 |
| Nhận tiền qua **cổng thanh toán / ví / dịch vụ hỗ trợ thu hộ** của bên thứ ba | được, nếu bên đó là **ngân hàng hoặc tổ chức trung gian thanh toán có Giấy phép của NHNN** | NĐ 52/2024 Điều 3 khoản 5; Điều 8 khoản 7; Điều 22 khoản 1 |
| **Tự lập ví**: người dùng nạp tiền, giữ số dư, rút ra, trả cho người khác | **không** — chỉ ngân hàng hoặc tổ chức trung gian thanh toán được cấp phép (doanh nghiệp, vốn điều lệ tối thiểu 50 tỷ, đề án, an toàn hệ thống thông tin cấp độ 3…) | NĐ 52/2024 Điều 3 khoản 12, 16; Điều 6; Điều 22 khoản 2 |
| **Thu hộ, chi hộ** cho người khác (tiền người mua vào tài khoản bạn rồi bạn trả người bán) | **không** tự làm — chuyển tiền, thu hộ, chi hộ là dịch vụ thanh toán của tổ chức cung ứng dịch vụ thanh toán; trường hợp "sàn nhận tiền rồi trả người bán" văn bản không định nghĩa riêng ⇒ cần luật sư | NĐ 52/2024 Điều 3 khoản 4, 17; Điều 18; Điều 8 khoản 7 |
| Bán **credit/xu/điểm** chỉ dùng cho dịch vụ của chính mình, không đổi ra tiền | **văn bản không quy định rõ — cần luật sư** (xem 11.7) | NĐ 52/2024 Điều 3 khoản 10–12, 16 |
| Nhận **crypto** làm tiền trả cho hàng hoá, dịch vụ | không có văn bản cho phép; rủi ro cao (xem 11.11) | NQ 05/2025 Điều 4 khoản 8; NĐ 52/2024 Điều 3 khoản 10, 11 |

## Việc phải có

| # | Việc | Nhãn | Dấu hiệu trong mã |
|---|---|---|---|
| 11.1 | Nhận tiền online **chỉ qua ngân hàng hoặc tổ chức trung gian thanh toán có Giấy phép NHNN** (cổng thanh toán điện tử, ví điện tử, hỗ trợ thu hộ chi hộ là ba loại dịch vụ trung gian cần giấy phép). Lưu tên pháp nhân và số giấy phép của đối tác | [luật] NĐ 52/2024 Điều 3 khoản 5, 16–18; Điều 8 khoản 7; Điều 22 khoản 1 · [khuyến nghị] lưu bằng chứng giấy phép đối tác (liên quan mảng 3.6) | SDK cổng thanh toán, URL webhook, khoá API nhà cung cấp thanh toán |
| 11.2 | **Không tự lập ví điện tử**: không cho người dùng nạp tiền thật vào số dư rồi rút ra, chuyển cho người khác hay trả cho bên khác. "Tiền điện tử" là giá trị đồng Việt Nam trả trước cho ngân hàng / tổ chức trung gian thanh toán; ví điện tử, thẻ trả trước chỉ ngân hàng hoặc tổ chức được cấp phép phát hành | [luật] NĐ 52/2024 Điều 3 khoản 12, 16; Điều 6 khoản 1–3; Điều 22 khoản 2; phạt NĐ 340/2025 Điều 31 khoản 6 | bảng `balance`/`wallet`, nút "nạp tiền", "rút tiền", chuyển số dư giữa người dùng |
| 11.3 | **Không thu hộ, chi hộ** cho người khác bằng tài khoản của mình (marketplace, chia tiền cho giáo viên/người bán/cộng tác viên, gom tiền nhóm). Dùng chức năng chia tiền của ngân hàng hoặc tổ chức trung gian có phép; trường hợp sàn nhận tiền rồi trả người bán: **văn bản không định nghĩa riêng — cần luật sư**. Nghĩa vụ thuế khi là nền tảng: mảng 9.7 | [luật] NĐ 52/2024 Điều 3 khoản 4, 17; Điều 17, 18; Điều 8 khoản 7; phạt NĐ 340/2025 Điều 30 khoản 8 điểm b | `payout`, bảng số dư người bán, lệnh chuyển tiền đi từ tài khoản của bạn |
| 11.4 | Tài khoản/ví nhận tiền **đứng tên chính chủ thể kinh doanh**; không mượn, thuê, mua tài khoản thanh toán hay ví của người khác, không cho mượn. Thông báo tài khoản dùng cho kinh doanh với cơ quan thuế: mảng 9.3 | [luật] NĐ 52/2024 Điều 8 khoản 5; phạt NĐ 340/2025 Điều 30 khoản 4 điểm c, khoản 5 điểm a; Điều 31 khoản 3 điểm b | số tài khoản, QR tĩnh viết cứng trong mã đứng tên người khác |
| 11.5 | **Dịch vụ đối soát chuyển khoản tự động** (xác nhận đơn từ giao dịch vào tài khoản): ưu tiên kết nối chính thức của ngân hàng hoặc tổ chức trung gian có phép; bên nào **nhận/giữ tiền thay bạn** thì đó là thu hộ — phải có phép. Không giao mật khẩu/đăng nhập ngân hàng cho bên thứ ba. Loại dịch vụ **chỉ đọc dữ liệu giao dịch, không giữ tiền**: văn bản đã đọc không quy định riêng — cần xác nhận | [luật] NĐ 52/2024 Điều 3 khoản 17; Điều 8 khoản 4, 7 · [khuyến nghị] phần còn lại | webhook dịch vụ đối soát, mã nội dung chuyển khoản, khoá truy cập tài khoản ngân hàng |
| 11.6 | Không dùng tài khoản, ví, cổng thanh toán cho **đánh bạc, lừa đảo, kinh doanh trái pháp luật**; dịch vụ trung gian thanh toán chỉ dùng cho hàng hoá, dịch vụ hợp pháp (game có thưởng: mảng 8.10) | [luật] NĐ 52/2024 Điều 8 khoản 8; TT 40/2024 Điều 6; phạt NĐ 340/2025 Điều 30 khoản 7 điểm c | cược, vòng quay trả tiền, hàng cấm |
| 11.7 | **Credit / xu / điểm trả trước** chỉ dùng cho dịch vụ của chính mình, không đổi ngược ra tiền: NĐ 52/2024 **không nói** loại này có phải "phương tiện thanh toán", "tiền điện tử" hay "ví điện tử" — **văn bản không quy định rõ — cần luật sư**. Nếu bị coi là phương tiện thanh toán ngoài danh sách thì là "phương tiện thanh toán không hợp pháp" (bị cấm). Cách làm an toàn hơn: credit **không rút, không đổi ra tiền, không chuyển giữa người dùng, không dùng mua hàng của bên thứ ba**; không gọi là "ví", "tiền", "số dư tiền"; giá gói bán bằng đồng Việt Nam; chính sách hạn dùng/hoàn tiền viết rõ (mảng 2.3); lập hoá đơn khi thu tiền (mảng 9.5); trong game xem mảng 8.7 | [luật] NĐ 52/2024 Điều 3 khoản 10, 11, 12, 16; Điều 6; Điều 8 khoản 6 (định nghĩa, cấm) · phân loại credit: **cần luật sư** · [khuyến nghị] thiết kế | bảng số dư credit, nút "nạp xu", gói xu/credit, chức năng tặng/chuyển credit, đổi credit lấy tiền/voucher |
| 11.8 | **Không dùng từ "ngân hàng", "tổ chức tín dụng", "công ty tài chính", "tổ chức tài chính vi mô", "quỹ tín dụng nhân dân"** (hoặc từ khác) trong tên, giấy tờ giao dịch, quảng cáo nếu có thể gây nhầm là tổ chức tín dụng. Không làm **hoạt động ngân hàng** (nhận tiền gửi; cấp tín dụng — cho vay, chiết khấu, bao thanh toán, bảo lãnh…; cung ứng dịch vụ thanh toán qua tài khoản) khi không phải tổ chức tín dụng | [luật] Luật 32/2024 Điều 4 khoản 4, 17; Điều 5; Điều 15 khoản 2; phạt NĐ 340/2025 Điều 7 khoản 7 điểm a, b | tên thương hiệu chứa "bank"/"ngân hàng"; tính năng "gửi tiết kiệm", "lãi suất", "cho vay", "mua trước trả sau" tự vận hành |
| 11.9 | **Giá trong nước bằng đồng Việt Nam.** Trên lãnh thổ Việt Nam, giao dịch, niêm yết, quảng cáo, báo giá bằng ngoại tệ bị cấm trừ trường hợp NHNN cho phép; người cư trú **được báo giá bằng ngoại tệ và nhận ngoại tệ chuyển khoản khi cung cấp hàng hoá, dịch vụ cho người không cư trú**. Giao dịch qua trung gian thanh toán trong nước bằng đồng Việt Nam. Hiển thị giá USD cho khách trong nước: rủi ro | [luật] Pháp lệnh Ngoại hối Điều 22; TT 32/2013 Điều 3, Điều 4 khoản 16 điểm b; TT 40/2024 Điều 7; phạt NĐ 340/2025 Điều 27 khoản 4 điểm n · [khuyến nghị] chỉ hiện giá ngoại tệ cho người mua ở nước ngoài, lưu quốc gia thanh toán | giá USD, `currency: 'USD'`, bộ chọn tiền tệ, chọn giá theo IP |
| 11.10 | **Khách nước ngoài trả bằng ngoại tệ** (PayPal, Stripe…): giao dịch vãng lai giữa người cư trú và người không cư trú được tự do; thanh toán, chuyển tiền xuất khẩu dịch vụ phải qua tổ chức tín dụng được phép; **người cư trú (kể cả cá nhân là công dân cư trú tại Việt Nam) phải chuyển toàn bộ ngoại tệ thu từ xuất khẩu hàng hoá, dịch vụ vào tài khoản ngoại tệ tại tổ chức tín dụng được phép ở Việt Nam**; muốn giữ ở nước ngoài phải được NHNN cho phép. Văn bản **không nhắc** PayPal/Stripe: để số dư lâu trên ví nước ngoài có bị coi là "giữ ngoại tệ ở nước ngoài" không — **cần luật sư**. Thuế với khách nước ngoài: mảng 9.12 | [luật] Pháp lệnh Ngoại hối Điều 4 khoản 2 điểm e, khoản 5; Điều 6; Điều 7 khoản 2, 3 · [khuyến nghị] rút định kỳ về tài khoản ngoại tệ ở ngân hàng Việt Nam, lưu sao kê | SDK PayPal/Stripe, cấu hình rút tiền (payout), tài khoản nhận ở nước ngoài |
| 11.11 | **Nhận thanh toán bằng crypto** (BTC, USDT…) cho hàng hoá, dịch vụ: không văn bản nào đã đọc cho phép. Tài sản mã hoá được dùng "cho mục đích trao đổi hoặc đầu tư" theo NQ 05/2025; không nằm trong danh sách phương tiện thanh toán; giao dịch tài sản mã hoá phải qua tổ chức được Bộ Tài chính cấp phép, và **sau 6 tháng kể từ khi tổ chức đầu tiên được cấp phép**, nhà đầu tư trong nước giao dịch ngoài tổ chức đó bị xử phạt. Có bị xử như "phương tiện thanh toán không hợp pháp" không: văn bản không nói thẳng — **cần luật sư**; khuyến nghị không nhận | [luật] NĐ 52/2024 Điều 3 khoản 10, 11; Luật 71/2025 Điều 47 khoản 2; NQ 05/2025 Điều 4 khoản 7, 8; Điều 7 khoản 2, 3; phạt NĐ 284/2026 Điều 9 khoản 1 · [khuyến nghị] không nhận | địa chỉ ví crypto, SDK thanh toán crypto, "pay with USDT", QR ví |
| 11.12 | **Phát hành, bán token/coin/NFT** có tính chất tài sản mã hoá: chỉ **doanh nghiệp Việt Nam (công ty TNHH hoặc cổ phần)**, tài sản mã hoá phải dựa trên **tài sản thực** (không phải chứng khoán, tiền pháp định), **chỉ chào bán cho nhà đầu tư nước ngoài**, qua tổ chức được Bộ Tài chính cấp phép, công bố bản cáo bạch tối thiểu 15 ngày trước. Cá nhân, hộ kinh doanh không thuộc diện được phát hành. Điểm/vật phẩm trong app đặt trên blockchain có là "tài sản mã hoá" không — **cần luật sư** | [luật] Luật 71/2025 Điều 46, 47; NQ 05/2025 Điều 3 khoản 2, Điều 5, Điều 6; phạt NĐ 284/2026 Điều 6 khoản 3 | smart contract, `mint`, bán token, airdrop, NFT |
| 11.13 | **Sàn / dịch vụ tài sản mã hoá** (tổ chức thị trường giao dịch, tự doanh, lưu ký, nền tảng phát hành): chỉ doanh nghiệp Việt Nam có Giấy phép Bộ Tài chính, vốn điều lệ đã góp tối thiểu **10.000 tỷ đồng** và các điều kiện cổ đông khác | [luật] NQ 05/2025 Điều 3 khoản 3; Điều 7 khoản 3; Điều 8 khoản 1–3; phạt NĐ 284/2026 Điều 7 khoản 4 điểm a | sổ lệnh, lưu ký ví hộ người dùng, swap, nạp/rút crypto |
| 11.14 | **Quảng cáo, tiếp thị liên quan đến tài sản mã hoá**: chỉ tổ chức có Giấy phép mới được làm; NĐ 284/2026 phạt hành vi quảng cáo, tiếp thị liên quan đến tài sản mã hoá khi chưa có giấy phép. Web/app nhỏ đặt banner, link giới thiệu (affiliate) sàn crypto có thuộc hành vi này không: văn bản không nói rõ chủ thể — **cần luật sư**; khuyến nghị không đặt | [luật] NQ 05/2025 Điều 4 khoản 4; phạt NĐ 284/2026 Điều 7 khoản 4 điểm b · [khuyến nghị] không đặt | banner/link giới thiệu sàn crypto, bài "kèo coin", mã mời đăng ký sàn |
| 11.15 | Không **thu thập, tàng trữ, trao đổi, mua bán, công khai trái phép dữ liệu, thông tin tài khoản tài sản mã hoá** của người khác | [luật] NĐ 284/2026 Điều 11 khoản 1 (dữ liệu cá nhân: mảng 1) | lưu khoá ví, cụm từ khôi phục (seed phrase), khoá API sàn của người dùng |

## Mức phạt (NĐ 340/2025/NĐ-CP — đã đối chiếu toàn văn)

**Mức dưới đây là của CÁ NHÂN; tổ chức có cùng hành vi chịu gấp 2** (Điều 5 khoản 3 điểm a). NĐ 340/2025 **không** nói hộ kinh doanh tính theo mức nào ⇒ "cần xác nhận".

| Hành vi | Mức (cá nhân) | Căn cứ |
|---|---|---|
| Cung ứng dịch vụ thanh toán mà không phải tổ chức cung ứng dịch vụ thanh toán (vd tự thu hộ, chi hộ) | 250–300 triệu + buộc nộp lợi bất hợp pháp | Điều 30 khoản 8 điểm b; khoản 10 điểm a |
| Cung ứng dịch vụ trung gian thanh toán (ví, cổng, hỗ trợ thu hộ chi hộ) **không có giấy phép** | 150–250 triệu + buộc nộp lợi bất hợp pháp | Điều 31 khoản 6; khoản 8 điểm a |
| Phát hành, cung ứng, sử dụng **phương tiện thanh toán không hợp pháp** | 150–200 triệu + tịch thu tang vật, phương tiện | Điều 30 khoản 6 điểm d; khoản 9 |
| Sử dụng, lợi dụng hoặc tạo điều kiện dùng tài khoản/phương tiện/dịch vụ thanh toán để đánh bạc, lừa đảo, kinh doanh trái pháp luật | 200–250 triệu | Điều 30 khoản 7 điểm c |
| Mua, bán, thuê, cho thuê, mượn, cho mượn tài khoản thanh toán: từ 01 đến dưới 10 tài khoản · từ 10 tài khoản | 100–150 triệu · 150–200 triệu | Điều 30 khoản 5 điểm a; khoản 6 điểm b |
| Mở, sử dụng, ủy quyền sử dụng tài khoản thanh toán không đúng quy định | 50–100 triệu | Điều 30 khoản 4 điểm c |
| Mua, bán, thuê, mượn ví điện tử; ví nặc danh, mạo danh: từ 01 đến dưới 10 ví · từ 10 ví | 50–100 triệu · 100–120 triệu | Điều 31 khoản 3 điểm b; khoản 4 điểm đ |
| Vi phạm quy định về sử dụng dịch vụ ví điện tử | 30–50 triệu | Điều 31 khoản 2 điểm a |
| **Báo giá, định giá, niêm yết, quảng cáo giá** hàng hoá, dịch vụ **bằng ngoại tệ** không đúng quy định | 30–50 triệu | Điều 27 khoản 4 điểm n |
| **Thanh toán tiền hàng hoá, dịch vụ bằng ngoại tệ** không đúng quy định: dưới 1.000 USD · 1.000 đến dưới 10.000 USD · 10.000 đến dưới 100.000 USD · từ 100.000 USD | cảnh cáo · 10–20 triệu · 20–30 triệu · 80–100 triệu (hành vi ở khoản 2, khoản 3 điểm k, khoản 5 điểm h: tịch thu số ngoại tệ) | Điều 27 khoản 1 điểm c, khoản 2 điểm c, khoản 3 điểm k, khoản 5 điểm h; khoản 10 điểm a |
| Mở, đóng, sử dụng **tài khoản ngoại tệ ở nước ngoài** không đúng quy định (có áp cho ví PayPal/Stripe không: chưa rõ) | 80–100 triệu | Điều 27 khoản 5 điểm a |
| Dùng từ ngữ liên quan đến hoạt động ngân hàng trái Luật Các tổ chức tín dụng · thực hiện hoạt động ngân hàng không có giấy phép | 400–500 triệu | Điều 7 khoản 7 điểm b, điểm a |

## Mức phạt (NĐ 284/2026/NĐ-CP — tài sản mã hoá, đã đối chiếu toàn văn)

**Mức dưới đây là của TỔ CHỨC; cá nhân vi phạm như tổ chức chịu 1/2** (Điều 4 khoản 2). Tối đa 200 triệu (tổ chức) / 100 triệu (cá nhân) (Điều 4 khoản 1). Không nói hộ kinh doanh. Hiệu lực 01/09/2026 đến khi NQ 05/2025 hết hiệu lực (Điều 21).

| Hành vi | Mức (tổ chức) | Căn cứ |
|---|---|---|
| Cung cấp dịch vụ liên quan đến tài sản mã hoá khi chưa có giấy phép | 180–200 triệu + tịch thu; buộc gỡ trang web, phần mềm, hệ thống giao dịch; nộp lợi bất hợp pháp | Điều 7 khoản 4 điểm a; khoản 5 điểm b; khoản 6 |
| Quảng cáo, tiếp thị liên quan đến tài sản mã hoá khi chưa có giấy phép | 180–200 triệu + buộc huỷ bỏ, cải chính thông tin | Điều 7 khoản 4 điểm b; khoản 6 điểm d |
| Chào bán, phát hành tài sản mã hoá cho đối tượng không đúng quy định / khi không đủ điều kiện Điều 5 NQ 05/2025 | 150–200 triệu + đình chỉ 06–12 tháng; buộc huỷ đợt phát hành, trả lại toàn bộ tiền thu được | Điều 6 khoản 3 điểm a, b; khoản 4 điểm b; khoản 5 điểm b |
| Nhà đầu tư trong nước giao dịch tài sản mã hoá **không qua tổ chức được Bộ Tài chính cấp phép** (áp sau mốc 6 tháng của NQ 05/2025 Điều 7 khoản 2) | 30–50 triệu | Điều 9 khoản 1 |
| Nhà đầu tư trong nước giao dịch tài sản mã hoá chỉ được chào bán cho nhà đầu tư nước ngoài | 70–100 triệu | Điều 9 khoản 2 |
| Thu thập, tàng trữ, trao đổi, mua bán, tặng cho, công khai hoá trái phép dữ liệu, thông tin tài khoản tài sản mã hoá | 150–200 triệu + đình chỉ giao dịch 01–03 tháng | Điều 11 khoản 1, 2 |

Truy cứu trách nhiệm hình sự (một số hành vi tại NĐ 340/2025 Điều 5 khoản 6 phải chuyển hồ sơ khi có dấu hiệu tội phạm): Bộ luật Hình sự chưa có trong bộ nguồn.

## Thủ tục với cơ quan nhà nước

Web/app nhỏ **chỉ dùng ngân hàng và tổ chức trung gian thanh toán có phép** thì không thấy thủ tục nào phải làm với NHNN trong các văn bản đã đọc. Thủ tục chỉ phát sinh khi:
- **Tự cung ứng ví điện tử / cổng thanh toán / hỗ trợ thu hộ chi hộ** ⇒ Giấy phép hoạt động cung ứng dịch vụ trung gian thanh toán (NĐ 52/2024 Điều 22–24): chủ thể là tổ chức có giấy chứng nhận đăng ký doanh nghiệp, vốn điều lệ tối thiểu 50 tỷ, đề án, thuyết minh kỹ thuật an toàn hệ thống thông tin cấp độ 3; nộp Bộ phận Một cửa NHNN, qua bưu chính hoặc Cổng dịch vụ công; thẩm định 90 ngày làm việc kể từ khi đủ hồ sơ; giấy phép 10 năm.
- **Giữ ngoại tệ thu từ xuất khẩu dịch vụ ở nước ngoài** ⇒ phải được NHNN cho phép (Pháp lệnh Ngoại hối Điều 7 khoản 2); tổ chức mở tài khoản ngoại tệ ở nước ngoài ⇒ giấy phép NHNN (Điều 23 khoản 3).
- **Sàn / dịch vụ tài sản mã hoá** ⇒ Giấy phép cung cấp dịch vụ tổ chức thị trường giao dịch tài sản mã hoá của **Bộ Tài chính** (NQ 05/2025 Điều 8, 10).

## Chưa có / chưa chắc

- Credit/xu/điểm trả trước dùng nội bộ: **không văn bản nào đã đọc phân loại** (11.7). Luật 71/2025 giao Chính phủ quy định "tài sản số khác" (Điều 48 khoản 2) — chưa thấy nghị định.
- Chưa đọc: NĐ 70/2014/NĐ-CP (hướng dẫn Pháp lệnh Ngoại hối) và các thông tư NHNN về tài khoản ngoại tệ của cá nhân; TT 15/2024/TT-NHNN (cung ứng dịch vụ thanh toán, trách nhiệm với đơn vị chấp nhận thanh toán); quy định NHNN về kết nối Open API ngân hàng (liên quan 11.5).
- Pháp lệnh Ngoại hối: chưa kiểm văn bản sửa sau 2013. TT 32/2013: chưa kiểm văn bản sửa sau 2019.
- Ngày tổ chức cung cấp dịch vụ tài sản mã hoá **đầu tiên** được cấp phép (mốc 6 tháng của NQ 05/2025 Điều 7 khoản 2): chưa xác minh. Theo tin baochinhphu.vn 06/10/2026 (hỏi–đáp, chưa đối chiếu văn bản), lúc đó chưa có tổ chức nào được cấp phép.
- Thuế với giao dịch tài sản mã hoá: NQ 05/2025 Điều 4 khoản 9 cho áp như thuế chứng khoán cho tới khi có chính sách riêng — chi tiết chưa đọc.
- Mức phạt hộ kinh doanh theo NĐ 340/2025 và NĐ 284/2026: hai nghị định không nêu.

## Cần luật sư khi

credit/xu có rút, đổi ra tiền, chuyển giữa người dùng hoặc dùng mua hàng của bên thứ ba · làm sàn/marketplace nhận tiền rồi trả người bán · để số dư ngoại tệ lâu trên PayPal/Stripe hay ví nước ngoài · nhận crypto · phát hành token/NFT, điểm trên blockchain · đặt quảng cáo hoặc link giới thiệu sàn crypto · tự vận hành "mua trước trả sau", cho vay, trả góp · dùng dịch vụ đối soát đọc tài khoản ngân hàng của bên chưa rõ giấy phép.
