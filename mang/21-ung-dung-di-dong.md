# Mảng 21 — Ứng dụng di động (Android, iOS, Flutter, React Native)

> Tham khảo, không phải tư vấn pháp lý — [MIEN-TRU-TRACH-NHIEM.md](../MIEN-TRU-TRACH-NHIEM.md). Tóm tắt từ nguồn trong [NGUON.md](../NGUON.md); đối chiếu văn bản gốc trước khi dựa vào.

**Áp khi:** dự án có app cài trên điện thoại (kể cả bản bọc web như PWA/TWA/Capacitor đưa lên kho ứng dụng).
Mảng này **không thay** các mảng khác: app thu dữ liệu vẫn làm đủ mảng 1, app bán hàng vẫn làm mảng 2, 3, app có game vẫn làm mảng 8.
Ở đây chỉ gom những nghĩa vụ **riêng hoặc hay sót** khi làm app: quyền truy cập, vị trí, SDK, xoá tài khoản, quảng cáo trong app.

**Văn bản:** Luật 91/2025/QH15 (Điều 14, 28, 29, 31) · NĐ 356/2025/NĐ-CP (Điều 4, 5, 6) · NĐ 330/2026/NĐ-CP (Điều 46, 51, 65, 70) ·
NĐ 342/2025/NĐ-CP (Điều 17, quảng cáo trong giao diện) · NĐ 248/2026/NĐ-CP (Điều 52, 53, app bán hàng). Link: [NGUON.md](../NGUON.md).
**Đã đối chiếu toàn văn** các điều trên (bản trích: [trich-dan/2026-11-03-ung-dung-di-dong.md](../trich-dan/2026-11-03-ung-dung-di-dong.md); NĐ 342/2025 là ảnh quét, chép tay).
Yêu cầu riêng của kho ứng dụng (Apple, Google) **không phải luật Việt Nam** — mảng này chỉ nhắc khi trùng với nghĩa vụ luật, ghi nhãn [khuyến nghị].

## Phân loại trước

- **App mạng xã hội, dịch vụ truyền thông trực tuyến** (chat, gọi, cộng đồng, video): có thêm Luật 91/2025 Điều 29 (mục 21.7, 21.8). NĐ 330/2026 Điều 65 phạt cả "**nền tảng nội dung số**" — app học tập, đọc truyện, nghe nhạc có thuộc nhóm này không: văn bản không định nghĩa ⇒ **cần xác nhận**; an toàn thì làm như app mạng xã hội.
- **App bán hàng có chức năng đặt hàng** = nền tảng thương mại điện tử (NĐ 248/2026 Điều 53 ghi "nền tảng thương mại điện tử (website, ứng dụng)") ⇒ làm mảng 3, xem 21.10.
- **App game** ⇒ mảng 8. **App có tính năng AI** ⇒ mảng 7. **App cho trẻ em** ⇒ 1.6.
- **App có tài khoản** ⇒ xem thêm mảng 6 (xác thực tài khoản 6.8, lưu dữ liệu tại Việt Nam 6.10, dữ liệu phải giữ sau khi xoá 6.11).

## Việc phải có

| # | Việc | Nhãn | Dấu hiệu trong mã |
|---|---|---|---|
| 21.1 | **Chính sách quyền riêng tư mở được ngay trong app** (không chỉ link trên trang kho ứng dụng); nêu rõ dữ liệu thu **khi cài đặt và khi sử dụng**, kể cả dữ liệu do quyền truy cập và SDK thu | [luật] với app mạng xã hội / truyền thông trực tuyến / nền tảng nội dung số: Luật 91/2025 Điều 29 khoản 1, 6; NĐ 330/2026 Điều 65 khoản 1 điểm a, d, e · [luật] chung: mục 1.1 · [khuyến nghị] vị trí đặt link | màn Cài đặt/Hồ sơ có link chính sách; tệp chính sách liệt kê từng quyền và SDK |
| 21.2 | **Quyền truy cập (permission) xin đúng lúc, đúng mục đích**: chỉ xin quyền tính năng thật sự cần; xin khi người dùng bắt đầu dùng tính năng đó, kèm lý do nói thật (câu `NS…UsageDescription` của iOS, màn giải thích trước hộp thoại Android); từ chối một quyền thì phần còn lại của app vẫn chạy; không thu dữ liệu ngoài phạm vi đã thông báo | [luật] (đồng ý từng mục đích, không mặc định đồng ý, không chỉ dẫn gây hiểu lầm): Luật 91/2025 Điều 9; NĐ 356/2025 Điều 6 khoản 3; thu ngoài phạm vi đã thoả thuận khi cài — NĐ 330/2026 Điều 65 khoản 2 điểm c · [khuyến nghị] thời điểm xin, màn giải thích | `AndroidManifest.xml` `uses-permission`; `Info.plist` `NS*UsageDescription` (câu rỗng/chung chung); xin nhiều quyền ngay lúc mở app |
| 21.3 | **Vị trí**: dữ liệu vị trí xác định qua dịch vụ định vị là **dữ liệu nhạy cảm** ⇒ báo cho người dùng biết đó là dữ liệu nhạy cảm khi xin đồng ý. App thu vị trí phải: **thông báo** việc dùng dữ liệu vị trí; có biện pháp **ngăn bên thứ ba không liên quan** thu vị trí (kiểm SDK quảng cáo/analytics có đọc vị trí không); cho người dùng **tuỳ chọn theo dõi vị trí** (bật/tắt). Theo dõi định vị khi không có đồng ý bị cấm (trừ yêu cầu của cơ quan có thẩm quyền / luật khác) | [luật] Luật 91/2025 Điều 31 khoản 3; NĐ 356/2025 Điều 4 khoản 1 điểm h, Điều 6 khoản 4; phạt NĐ 330/2026 Điều 70 khoản 1 điểm a, b; khoản 2 điểm a | `ACCESS_FINE_LOCATION`, `ACCESS_BACKGROUND_LOCATION`, `NSLocationAlways…`; SDK có quyền vị trí; không có công tắc vị trí trong Cài đặt app |
| 21.4 | **Micro, camera, danh bạ, tin nhắn, tệp**: chỉ đọc khi có đồng ý và đúng tính năng; app mạng xã hội/OTT **không** nghe trộm, ghi âm cuộc gọi, đọc tin nhắn, **tự động trích danh bạ hay tệp phương tiện** khi chưa có đồng ý. Giọng nói/khuôn mặt dùng để **nhận dạng người** là dữ liệu sinh trắc học (nhạy cảm) ⇒ xem 1.5 | [luật] Luật 91/2025 Điều 29 khoản 5, Điều 31 khoản 4; NĐ 356/2025 Điều 4 khoản 1 điểm đ; phạt NĐ 330/2026 Điều 65 khoản 2 điểm b | `RECORD_AUDIO`, `CAMERA`, `READ_CONTACTS`, `READ_SMS`, `READ_MEDIA_*`; tải danh bạ lên máy chủ |
| 21.5 | **SDK theo dõi, quảng cáo, mã quảng cáo (IDFA/GAID)**: thu dữ liệu qua theo dõi ứng dụng để quảng cáo theo hành vi/cá nhân hoá **chỉ khi có đồng ý**; có cách **từ chối chia sẻ**; định thời gian lưu, xoá khi hết cần. Dữ liệu theo dõi hành vi sử dụng dịch vụ trên mạng là **dữ liệu nhạy cảm**. SDK phải **chưa chạy/chưa gửi dữ liệu** trước khi người dùng đồng ý (nhiều SDK mặc định tự bật khi khởi động); liệt kê tên SDK và bên nhận trong chính sách. Máy chủ SDK ở nước ngoài ⇒ thêm 1.7 | [luật] Luật 91/2025 Điều 28 khoản 8; NĐ 356/2025 Điều 4 khoản 1 điểm l · [khuyến nghị] cách tắt SDK trước đồng ý; App Tracking Transparency của iOS là luật của kho, không phải luật VN | Firebase Analytics, Facebook SDK, AppsFlyer, Adjust, AdMob…; `AD_ID`, `AdvertisingIdClient`, `ATTrackingManager`; cờ tự thu thập bật mặc định |
| 21.6 | **Xoá tài khoản và dữ liệu**: nhận yêu cầu xoá ⇒ **phản hồi trong 02 ngày làm việc**, thực hiện trong **20 ngày** (30 ngày nếu cần bên xử lý/bên thứ ba xoá; gia hạn tối đa 01 lần, không quá 20 ngày); yêu cầu **bên xử lý, bên thứ ba** (dịch vụ lưu trữ, analytics, email…) xoá theo; xoá bằng biện pháp an toàn, chống khôi phục trái phép; không xoá được vì lý do chính đáng ⇒ **thông báo lý do**. Được từ chối trong trường hợp Điều 19 Luật 91 (xử lý không cần đồng ý) và phải giữ phần luật buộc lưu (6.11). Nút xoá **trong app** không phải hình thức luật bắt buộc duy nhất (xem 1.4), nhưng kho ứng dụng thường đòi | [luật] Luật 91/2025 Điều 14 khoản 1 điểm a, khoản 2, 3, 5; NĐ 356/2025 Điều 5 khoản 4; phạt NĐ 330/2026 Điều 51 khoản 1 điểm a, b, khoản 2 điểm a, b · [khuyến nghị] nút xoá trong app | có đăng nhập nhưng không có màn/hàm xoá tài khoản; hàm xoá chỉ xoá bảng chính, bỏ sót dịch vụ bên thứ ba |
| 21.7 | **Không bắt chụp giấy tờ tuỳ thân để xác thực tài khoản** (ảnh/video có toàn bộ hoặc một phần CCCD, hộ chiếu…) với app mạng xã hội, truyền thông trực tuyến, khi luật chuyên ngành không đòi định danh. Ảnh thẻ căn cước là dữ liệu nhạy cảm. Xác thực bằng số điện thoại: xem 6.8 | [luật] Luật 91/2025 Điều 29 khoản 2; NĐ 356/2025 Điều 4 khoản 1 điểm i; phạt NĐ 330/2026 Điều 65 khoản 2 điểm a | màn đăng ký có bước chụp CCCD; tải ảnh giấy tờ lên kho lưu trữ |
| 21.8 | **App mạng xã hội / truyền thông trực tuyến**: lựa chọn **từ chối cookie/tệp dữ liệu theo dõi**; lựa chọn **"không theo dõi"** (hoặc chỉ theo dõi khi người dùng đồng ý); cơ chế cho người dùng **truy cập, sửa, xoá** dữ liệu, **tự đặt quyền riêng tư** cho tài khoản và **báo cáo vi phạm** về bảo mật, quyền riêng tư | [luật] Luật 91/2025 Điều 29 khoản 3, 4, 6; phạt NĐ 330/2026 Điều 65 khoản 1 điểm b, c, đ | màn Quyền riêng tư; công tắc theo dõi; nút báo cáo |
| 21.9 | **Quảng cáo trong app** (toàn màn hình, popup, chen giữa nội dung — "quảng cáo không ở vùng cố định"): tắt được **chỉ với một lần tương tác**; không có nút tắt giả hoặc khó nhận ra; ảnh tĩnh **tắt được ngay**; video/ảnh động chờ tối đa **05 giây**; có biểu tượng và hướng dẫn để **báo cáo** quảng cáo vi phạm và **từ chối/tắt** quảng cáo không phù hợp; báo cáo phải được xử lý và báo kết quả cho người dùng (xem 4.7) | [luật] NĐ 342/2025 Điều 17 khoản 1–4 | cấu hình interstitial/rewarded của SDK quảng cáo; thời gian trước khi hiện nút đóng; vùng bấm nút đóng |
| 21.10 | **App bán hàng có đặt hàng** là nền tảng TMĐT ⇒ thông báo/đăng ký theo mảng 3 (xem 3.1, 3.2); hồ sơ khai **tên ứng dụng, hệ điều hành, địa chỉ tải** (mẫu trong phụ lục NĐ 248/2026). NĐ 52/2013 và NĐ 85/2021 **hết hiệu lực từ 01/07/2026**. App đã được xác nhận thông báo/đăng ký **trước 01/07/2026** được hoạt động theo nội dung đã xác nhận **đến hết 30/06/2027**, trong thời gian đó phải sửa đổi, bổ sung hồ sơ theo NĐ 248/2026. Thông tư 59/2015/TT-BCT (TMĐT trên ứng dụng di động, hướng dẫn NĐ 52/2013): tình trạng hiệu lực **chưa kiểm được** — không dựa vào | [luật] NĐ 248/2026 Điều 52 khoản 3, Điều 53 | chức năng giỏ hàng/đặt hàng trong app; footer/màn Giới thiệu có thông tin người bán |
| 21.11 | **Bán qua kho ứng dụng** (mua trong app, gói gia hạn): doanh thu từ kho ứng dụng ghi nhận đủ (xem 9.3); tài khoản nhà phát triển và tài khoản nhận tiền đứng tên chủ thể đã đăng ký (xem 10.10); giá cho người dùng trong nước bằng đồng Việt Nam (xem 11.9). Trước khi mua, người dùng thấy rõ giá, chu kỳ trừ tiền, cách huỷ | [luật] theo các mục được trỏ · [khuyến nghị] hiển thị giá, chu kỳ, cách huỷ | `in_app_purchase`, `react-native-iap`, `BillingClient`, `StoreKit`; màn paywall |

## Mức phạt (NĐ 330/2026/NĐ-CP, Mục 6 Chương II — đã đối chiếu toàn văn Công báo)

> **Mức dưới đây là của TỔ CHỨC; cá nhân một nửa** (Điều 7 khoản 1) — như mảng 1, ngược với mảng 6.

| Hành vi | Mức (tổ chức) | Căn cứ | Mục |
|---|---|---|---|
| Không thông báo lý do khi không xoá được; xoá không bằng biện pháp an toàn; không chống khôi phục trái phép | 10–30 triệu | Điều 51 khoản 1 | 21.6 |
| Từ chối cho người dùng xem, chỉnh sửa dữ liệu của mình | 20–30 triệu | Điều 46 khoản 1 điểm a | 21.6, 21.8 |
| Không xoá dữ liệu trong các trường hợp luật định; không yêu cầu bên xử lý/bên thứ ba xoá | 30–50 triệu | Điều 51 khoản 2 điểm a, b | 21.6 |
| (Mạng xã hội, truyền thông trực tuyến, nền tảng nội dung số) không thông báo dữ liệu thu khi cài và dùng; không cho từ chối cookie; không có lựa chọn "không theo dõi"; chính sách không rõ; không có cơ chế truy cập, sửa, xoá, đặt quyền riêng tư, báo cáo vi phạm | 50–70 triệu | Điều 65 khoản 1 | 21.1, 21.8 |
| Bắt cung cấp ảnh/video giấy tờ tuỳ thân để xác thực tài khoản thông thường; OTT/mạng xã hội dùng tính năng không công khai để nghe trộm, ghi âm, đọc tin nhắn, tự trích danh bạ/tệp khi chưa đồng ý; thu dữ liệu vượt phạm vi đã thoả thuận khi cài | 70–150 triệu | Điều 65 khoản 2 | 21.2, 21.4, 21.7 |
| App thu vị trí nhưng không thông báo việc dùng; không chặn bên thứ ba không liên quan thu vị trí; không có tuỳ chọn theo dõi vị trí | 50–70 triệu | Điều 70 khoản 1 điểm a, b | 21.3 |
| Theo dõi định vị khi không có đồng ý (trừ yêu cầu của cơ quan có thẩm quyền / luật khác) | 70–150 triệu | Điều 70 khoản 2 điểm a | 21.3 |

Hình thức bổ sung đáng chú ý: **đình chỉ cung cấp dịch vụ của ứng dụng tại Việt Nam** 01–03 tháng với vi phạm Điều 65 khoản 1, 03–06 tháng với vi phạm khoản 2 (Điều 65 khoản 3); buộc cung cấp tuỳ chọn bật/tắt thu thập vị trí (Điều 70 khoản 4 điểm b).
Mức phạt cho quảng cáo trong app (21.9): xem mảng 4.

## Chưa có / chưa chắc

- App học tập, đọc, nghe có phải "**nền tảng nội dung số**" (NĐ 330/2026 Điều 65) không: văn bản không định nghĩa.
- **Thông tư 59/2015/TT-BCT** (TMĐT trên ứng dụng di động) còn hiệu lực sau khi NĐ 52/2013 hết hiệu lực không: chưa đọc văn bản bãi bỏ; cổng vbpl.vn không truy cập được lúc rà (03/11/2026).
- Mua trong app, gói tự gia hạn: chưa thấy quy định riêng trong các văn bản đã đọc; áp chung mảng 2 (người tiêu dùng) và mảng 3.
- Quảng cáo có thưởng (xem quảng cáo để nhận vật phẩm): NĐ 342/2025 Điều 17 không nhắc riêng; nếu vật phẩm dùng trong game ⇒ mảng 8.

## Cần luật sư khi

- App thu vị trí chạy nền, dữ liệu sinh trắc học (nhận dạng khuôn mặt/giọng nói), hoặc dữ liệu sức khoẻ.
- App có cộng đồng/chat và người dùng dưới 16 tuổi.
- App bán hàng đã thông báo theo khung cũ, cần chuyển hồ sơ sang NĐ 248/2026 trước 30/06/2027.
