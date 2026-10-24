# Mảng 1 — Dữ liệu cá nhân

> Tham khảo, không phải tư vấn pháp lý — [MIEN-TRU-TRACH-NHIEM.md](../MIEN-TRU-TRACH-NHIEM.md). Tóm tắt từ nguồn trong [NGUON.md](../NGUON.md); đối chiếu văn bản gốc trước khi dựa vào.

**Áp khi:** app thu bất kỳ dữ liệu nào gắn với một người: email, SĐT, tên, ảnh, giọng nói, IP, lịch sử dùng, cookie định danh.

**Văn bản:** Luật 91/2025/QH15 (Luật BVDLCN) · NĐ 356/2025/NĐ-CP (chi tiết) · NĐ 330/2026/NĐ-CP (xử phạt). Link: [NGUON.md](../NGUON.md).
**Đã đối chiếu toàn văn** Luật 91/2025, NĐ 356/2025, NĐ 330/2026 (bản trích: [trich-dan/2026-10-24-luat91-nd356-nd363.md](../trich-dan/2026-10-24-luat91-nd356-nd363.md)). NĐ 363/2026 (xử phạt lĩnh vực **dữ liệu** nói chung, hiệu lực 11/11/2026) loại trừ hành vi thuộc nghị định về DLCN (Điều 1 khoản 2) — PDF ảnh quét, mới đọc một phần.

> Nhãn mỗi mục: **[luật]** = nội dung có trong văn bản (đã nêu ở nguồn chính thức) · **[khuyến nghị]** = cách làm an toàn suy ra, không phải câu chữ của luật.

## Việc phải có

| # | Việc | Nhãn | Dấu hiệu trong mã (grep để TÌM, đọc rồi mới kết luận) |
|---|---|---|---|
| 1.1 | Có **chính sách quyền riêng tư** công khai: thu gì, để làm gì, giữ bao lâu, chia cho ai (kể cả nhà cung cấp hạ tầng/AI), người dùng liên hệ ở đâu | [luật] | tìm route `/privacy`, `privacy`, `chinh-sach`; link ở footer và trang đăng ký |
| 1.2 | **Đồng ý phải chủ động**: ô đồng ý **không tick sẵn**; **im lặng/không phản hồi không phải đồng ý**; mỗi mục đích tách riêng (vd: email marketing tách khỏi điều khoản); phương thức thể hiện đồng ý theo NĐ 356/2025 Điều 6 | [luật] Luật 91/2025 Điều 9 (khoản 4 về im lặng); phạt NĐ 330/2026 Điều 43 | `type="checkbox"` có `checked`; `defaultChecked`; form đăng ký gộp nhiều mục đích một ô |
| 1.3 | **Chứng minh được đã có đồng ý** (ghi nhận ai, đồng ý gì, lúc nào) và cho **rút đồng ý** — [luật]. Cách lưu (bảng, phiên bản chính sách) và rút dễ như lúc đồng ý — [khuyến nghị] | [luật] + [khuyến nghị] | bảng/khóa lưu consent; nút rút đồng ý trong cài đặt |
| 1.4 | Người dùng thực hiện được **quyền chủ thể dữ liệu** (xem, sửa, yêu cầu xoá, hạn chế, nhận bản sao…); có **quy trình, biểu mẫu** tiếp nhận; **phản hồi trong 02 ngày làm việc** rồi thực hiện trong thời hạn theo từng loại yêu cầu (NĐ 356/2025 Điều 5). Yêu cầu xoá có **ngoại lệ** (dữ liệu phải giữ theo luật khác, vd chứng từ thanh toán) ⇒ kiểm có căn cứ giữ lại + trả lời từ chối hợp lệ; vòng đời backup. Nút bấm là một cách làm, không phải hình thức bắt buộc duy nhất | [luật] (quyền chủ thể) · ngoại lệ: **đọc bản gốc** | nút "Xoá tài khoản", API xoá; bảng phụ/backup |
| 1.5 | Dữ liệu **nhạy cảm** (sức khoẻ, sinh trắc — giọng nói/khuôn mặt dùng để nhận dạng, vị trí, tài chính, trẻ em…) ⇒ phân loại theo **danh mục của NĐ 356/2025** (đừng tự suy), thông báo cho người dùng biết DL nhạy cảm đang được xử lý, đồng ý riêng theo mục đích; giữ ngắn nhất có thể | [luật] phân loại + thông báo · [khuyến nghị] thời hạn | `getUserMedia`, upload ảnh/ghi âm, geolocation |
| 1.6 | **Trẻ em**: xử lý DL của trẻ cần đồng ý của cha mẹ/người giám hộ; trẻ **từ đủ 7 tuổi** cần **đồng thời** đồng ý của trẻ và người đại diện; phải **xác minh tuổi** trước khi xử lý (NĐ 330 Điều 60 khoản 1 — xử phạt) — [luật]. Cổng xác nhận tuổi là cách làm — [khuyến nghị] | [luật] + [khuyến nghị] | form đăng ký có hỏi tuổi không |
| 1.7 | **Chuyển dữ liệu ra nước ngoài** (máy chủ/AI/email ở nước ngoài — rất phổ biến: Supabase, Firebase, Vercel, OpenAI…) ⇒ công bố trong chính sách + **hồ sơ đánh giá tác động chuyển DLCN xuyên biên giới**, nộp cơ quan chuyên trách trong **60 ngày** kể từ khi chuyển; có trường hợp không phải đánh giá (Luật Điều 20 khoản 6; NĐ 356 Điều 17). **Không thuộc diện miễn của hộ KD/DN siêu nhỏ** (miễn trừ Điều 38 không gồm Điều 20). Phạt tối đa **5% doanh thu năm trước** với tổ chức (Luật Điều 8 khoản 4) | [luật] Luật 91/2025 Điều 20; NĐ 356/2025 Điều 17, 18 | biến môi trường, SDK bên thứ ba, vùng máy chủ |
| 1.8 | **Không bán/mua dữ liệu cá nhân**; không dùng dữ liệu cho mục đích ngoài điều đã công bố | [luật] | export danh sách email, chia sẻ cho đối tác quảng cáo |
| 1.9 | **Cookie/analytics**: dữ liệu theo dõi dùng cho quảng cáo theo hành vi/cá nhân hoá cần đồng ý — [luật]. Phân loại từng cookie theo dữ liệu + mục đích + căn cứ; "cần thiết" không tự là ngoại lệ, phải có căn cứ xử lý. Thiết kế banner — [khuyến nghị] | [luật] + [khuyến nghị] | `gtag`, `fbq`, `mixpanel`, pixel; banner cookie |
| 1.10 | **Vi phạm/sự cố DLCN** có thể gây tổn hại (an ninh, trật tự, tính mạng, sức khoẻ, danh dự, tài sản của chủ thể) ⇒ **thông báo cơ quan chuyên trách chậm nhất 72 giờ**; nội dung thông báo theo NĐ 356 Điều 28 | [luật] Luật 91/2025 Điều 23; NĐ 356/2025 Điều 28 | tài liệu vận hành; nhật ký sự cố |
| 1.11 | **Không ghi dữ liệu cá nhân vào URL / log công khai** | [khuyến nghị] | `?email=`, `console.log(user` |

## Mức phạt (NĐ 330/2026/NĐ-CP — đã đối chiếu toàn văn Công báo)

**Mức dưới đây là của TỔ CHỨC. Cá nhân vi phạm cùng hành vi chịu 1/2** (Điều 7 khoản 1, đoạn về Mục 6 — bảo vệ DLCN).
**Hộ kinh doanh** bị áp mức như **cá nhân** (Điều 2 khoản 3). Hiệu lực 19/08/2026.
Phạt theo % doanh thu chỉ áp cho **chuyển DLCN xuyên biên giới** (Điều 56) và mua bán DLCN — đọc bản gốc khi gặp.

| Hành vi | Mức (tổ chức) | Căn cứ | Ứng với mục |
|---|---|---|---|
| Xử lý DL sai phạm vi/mục đích hoặc vượt mức cần thiết; không bảo đảm chính xác/không sửa kịp; lưu quá thời gian cần thiết | 20–40 triệu | Điều 39 khoản 1 | 1.1, 1.8 |
| Cản trở hoạt động bảo vệ DLCN; dùng DLCN người khác làm việc trái luật | 40–60 triệu | Điều 39 khoản 2 | 1.8 |
| Xử lý DL sau khi thu thập mà **chưa có đồng ý** (trừ trường hợp luật khác) | 30–50 triệu | Điều 43 khoản 1 điểm a | 1.2 |
| **Ép đồng ý** mục đích không liên quan / từ chối dịch vụ nếu không đồng ý | 30–50 triệu | Điều 43 khoản 1 điểm b | 1.2 |
| **Mặc định đồng ý**, chỉ dẫn gây hiểu lầm giữa đồng ý và không | 30–50 triệu | Điều 43 khoản 1 điểm c | 1.2 |
| Xin đồng ý không rõ ràng, không kiểm chứng được ai/lúc nào/nội dung gì | 30–50 triệu | Điều 43 khoản 1 điểm d | 1.3 |
| Không cung cấp thông tin minh bạch (loại DL, mục đích, quyền) | 30–50 triệu | Điều 43 khoản 1 điểm đ | 1.1 |
| Không cho đồng ý **riêng từng mục đích** | 30–50 triệu | Điều 43 khoản 1 điểm e | 1.2 |
| Không lưu **nhật ký đồng ý** / không chứng minh được đã có đồng ý | 30–50 triệu | Điều 43 khoản 1 điểm g | 1.3 |
| Không thông báo người dùng biết **DL nhạy cảm** đang được xử lý | 30–50 triệu | Điều 43 khoản 1 điểm h | 1.5 |
| Cố ý tiếp tục xử lý sau yêu cầu **ngừng/hạn chế** | 50–70 triệu | Điều 43 khoản 2 điểm a | 1.3, 1.4 |
| Coi **im lặng** là đồng ý | 50–70 triệu | Điều 43 khoản 2 điểm b | 1.2 |
| Không thông báo cơ quan chuyên trách khi phát hiện vi phạm / xử lý sai mục đích / không bảo đảm quyền chủ thể | 20–40 triệu | Điều 54 khoản 2 | 1.10 |
| Thông báo sự cố cho cơ quan chuyên trách **chậm quá 72 giờ** | xem Điều 54 khoản 3 (bản gốc) | Điều 54 khoản 3 | 1.10 |
| **Trẻ em**: không xác minh tuổi trước khi xử lý; xử lý DL trẻ **dưới 7 tuổi** không có đồng ý của người đại diện; trẻ **từ đủ 7 tuổi** không có **đồng thời** đồng ý của trẻ và người đại diện | 30–50 triệu | Điều 60 khoản 1 | 1.6 |
| Trẻ em: công bố/tiết lộ đời tư trẻ từ đủ 7 tuổi không có đồng thời hai đồng ý; không ngừng xử lý khi người đại diện rút đồng ý | 50–100 triệu | Điều 60 khoản 2 | 1.6 |
| **Mạng xã hội / dịch vụ truyền thông trực tuyến / nền tảng nội dung số**: không cho từ chối cookies; không có lựa chọn "không theo dõi"; không công khai chính sách bảo mật minh bạch; không có cơ chế truy cập/sửa/xoá DL; không báo rõ DL thu khi cài ứng dụng | 50–70 triệu | Điều 65 khoản 1 | 1.1, 1.4, 1.9 |

Biện pháp kèm theo (Điều 39, 43): có thể tịch thu tang vật, phương tiện; **buộc huỷ/xoá tới mức không khôi phục** DL thu không có đồng ý hợp lệ.
Chưa trích: Điều 46–47, 50–51, 57–59, 61–64, 66–71 và phần sàn/trần theo doanh thu của Điều 56 — đọc bản gốc khi dự án có các hoạt động đó.

## Miễn trừ cho hộ kinh doanh, doanh nghiệp nhỏ (đã đối chiếu toàn văn)

- **Hộ kinh doanh, doanh nghiệp siêu nhỏ** *không phải* thực hiện **Điều 21** (đánh giá tác động xử lý DLCN), **Điều 22** (cập nhật hồ sơ) và **khoản 2 Điều 33** (bộ phận/nhân sự bảo vệ DLCN) — Luật 91/2025 Điều 38 khoản 3; NĐ 356/2025 Điều 41 khoản 2.
- **Trừ khi**: kinh doanh dịch vụ xử lý DLCN · **trực tiếp xử lý DL nhạy cảm** · xử lý DLCN của **từ 100 nghìn chủ thể trở lên** (tính tích luỹ, kể từ khi đạt quy mô) — NĐ 356/2025 Điều 41 khoản 2.
- **Doanh nghiệp nhỏ, khởi nghiệp** được **chọn** thực hiện hay không ba nghĩa vụ trên trong **05 năm** kể từ 01/01/2026 (NĐ 356/2025 Điều 41 khoản 1; Luật Điều 38 khoản 2) — kèm các ngoại lệ tương tự, đọc bản gốc.
- Mọi nghĩa vụ **khác** vẫn áp dụng: đồng ý, quyền chủ thể, chính sách, thông báo vi phạm 72 giờ, **hồ sơ chuyển DL xuyên biên giới (Điều 20)**.
- Mức phạt tối đa (Luật Điều 8): **03 tỷ** (vi phạm thông thường) · **5% doanh thu năm trước** (chuyển xuyên biên giới, tổ chức) · **10 lần khoản thu** (mua bán DLCN); cá nhân bằng một nửa tổ chức.
- **Trẻ em** (Luật Điều 24): xử lý DL trẻ em cần đồng ý của người đại diện; **công bố, tiết lộ đời sống riêng tư** của trẻ **từ đủ 07 tuổi** cần đồng ý của **cả trẻ và người đại diện**. NĐ 330/2026 Điều 60 khoản 1 còn phạt việc không xác minh tuổi và xử lý DL trẻ từ đủ 7 tuổi thiếu đồng thời hai đồng ý — hai văn bản đọc cùng nhau.
## Cần luật sư khi

xử lý dữ liệu nhạy cảm số lượng lớn · nhắm người dùng trẻ em · chuyển dữ liệu ra nước ngoài là cốt lõi sản phẩm · đã xảy ra lộ dữ liệu.
