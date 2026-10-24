# Mảng 1 — Dữ liệu cá nhân

> Tham khảo, không phải tư vấn pháp lý — [MIEN-TRU-TRACH-NHIEM.md](../MIEN-TRU-TRACH-NHIEM.md). Tóm tắt từ nguồn trong [NGUON.md](../NGUON.md); đối chiếu văn bản gốc trước khi dựa vào.

**Áp khi:** app thu bất kỳ dữ liệu nào gắn với một người: email, SĐT, tên, ảnh, giọng nói, IP, lịch sử dùng, cookie định danh.

**Văn bản:** Luật 91/2025/QH15 (Luật BVDLCN) · NĐ 356/2025/NĐ-CP (chi tiết) · NĐ 330/2026/NĐ-CP (xử phạt). Link: [NGUON.md](../NGUON.md).
Số điều: **chưa trích** (chưa đối chiếu toàn văn) — mở văn bản gốc khi cần dẫn điều.

> Nhãn mỗi mục: **[luật]** = nội dung có trong văn bản (đã nêu ở nguồn chính thức) · **[khuyến nghị]** = cách làm an toàn suy ra, không phải câu chữ của luật.

## Việc phải có

| # | Việc | Nhãn | Dấu hiệu trong mã (grep để TÌM, đọc rồi mới kết luận) |
|---|---|---|---|
| 1.1 | Có **chính sách quyền riêng tư** công khai: thu gì, để làm gì, giữ bao lâu, chia cho ai (kể cả nhà cung cấp hạ tầng/AI), người dùng liên hệ ở đâu | [luật] | tìm route `/privacy`, `privacy`, `chinh-sach`; link ở footer và trang đăng ký |
| 1.2 | **Đồng ý phải chủ động**: ô đồng ý **không tick sẵn**; im lặng/không bấm không phải đồng ý; mỗi mục đích tách riêng (vd: email marketing tách khỏi điều khoản) | [luật] — NĐ 330/2026 có hành vi phạt về thiết lập mặc định đồng ý không rõ ràng | `type="checkbox"` có `checked`; `defaultChecked`; form đăng ký gộp nhiều mục đích một ô |
| 1.3 | **Chứng minh được đã có đồng ý** (ghi nhận ai, đồng ý gì, lúc nào) và cho **rút đồng ý** — [luật]. Cách lưu (bảng, phiên bản chính sách) và rút dễ như lúc đồng ý — [khuyến nghị] | [luật] + [khuyến nghị] | bảng/khóa lưu consent; nút rút đồng ý trong cài đặt |
| 1.4 | Người dùng thực hiện được **quyền chủ thể dữ liệu** (xem, sửa, yêu cầu xoá, hạn chế, nhận bản sao…). Yêu cầu xoá có **ngoại lệ** (dữ liệu phải giữ theo luật khác, vd chứng từ thanh toán) ⇒ kiểm có căn cứ giữ lại + trả lời từ chối hợp lệ; vòng đời backup. Nút bấm là một cách làm, không phải hình thức bắt buộc duy nhất | [luật] (quyền chủ thể) · ngoại lệ: **đọc bản gốc** | nút "Xoá tài khoản", API xoá; bảng phụ/backup |
| 1.5 | Dữ liệu **nhạy cảm** (sức khoẻ, sinh trắc — giọng nói/khuôn mặt dùng để nhận dạng, vị trí, tài chính, trẻ em…) ⇒ phân loại theo **danh mục của NĐ 356/2025** (đừng tự suy), thông báo cho người dùng biết DL nhạy cảm đang được xử lý, đồng ý riêng theo mục đích; giữ ngắn nhất có thể | [luật] phân loại + thông báo · [khuyến nghị] thời hạn | `getUserMedia`, upload ảnh/ghi âm, geolocation |
| 1.6 | **Trẻ em**: xử lý DL của trẻ cần đồng ý của cha mẹ/người giám hộ; một số trường hợp còn cần **cả đồng ý của trẻ từ đủ 7 tuổi** (theo giải thích của Bộ Công an — đọc bản gốc) — [luật]. Cổng xác nhận tuổi là cách làm — [khuyến nghị] | [luật] + [khuyến nghị] | form đăng ký có hỏi tuổi không |
| 1.7 | **Chuyển dữ liệu ra nước ngoài** (máy chủ/AI/email ở nước ngoài — rất phổ biến: Supabase, Firebase, Vercel, OpenAI…) ⇒ công bố trong chính sách + làm hồ sơ theo NĐ 356/2025 | [luật] — chi tiết hồ sơ & miễn trừ cho hộ KD/DN siêu nhỏ: **đọc NĐ 356 + Luật 91 bản gốc** | biến môi trường, SDK bên thứ ba, vùng máy chủ |
| 1.8 | **Không bán/mua dữ liệu cá nhân**; không dùng dữ liệu cho mục đích ngoài điều đã công bố | [luật] | export danh sách email, chia sẻ cho đối tác quảng cáo |
| 1.9 | **Cookie/analytics**: dữ liệu theo dõi dùng cho quảng cáo theo hành vi/cá nhân hoá cần đồng ý — [luật]. Phân loại từng cookie theo dữ liệu + mục đích + căn cứ; "cần thiết" không tự là ngoại lệ, phải có căn cứ xử lý. Thiết kế banner — [khuyến nghị] | [luật] + [khuyến nghị] | `gtag`, `fbq`, `mixpanel`, pixel; banner cookie |
| 1.10 | **Sự cố lộ dữ liệu** ⇒ có quy trình thông báo cơ quan chức năng + người bị ảnh hưởng trong thời hạn luật định | [luật] — thời hạn: **đọc bản gốc** | tài liệu vận hành; nhật ký sự cố |
| 1.11 | **Không ghi dữ liệu cá nhân vào URL / log công khai** | [khuyến nghị] | `?email=`, `console.log(user` |

## Mức phạt (NĐ 330/2026/NĐ-CP)

Nguồn: [Báo Chính phủ 22/08/2026](https://baochinhphu.vn/muc-xu-phat-vi-pham-hanh-chinh-doi-voi-hanh-vi-vi-pham-ve-bao-ve-du-lieu-ca-nhan-102260822154959691.htm). Bài nêu khoản, chưa nêu số điều;
chưa tách mức cá nhân/tổ chức — **mở toàn văn NĐ 330 trên Công báo trước khi trích cho người dùng**.
Hộ kinh doanh bị phạt như cá nhân (theo bài trên). **Đối tượng của từng mức chưa xác minh ⇒ không tự nhân đôi cho tổ chức.**

| Hành vi | Mức phạt | Ứng với mục |
|---|---|---|
| Xử lý DL sai phạm vi/mục đích đã xác định, vượt mức cần thiết, không có đồng ý (nhóm vi phạm **nguyên tắc** xử lý); giữ quá thời gian cần thiết; không sửa DL sai | 20–40 triệu | 1.1, 1.8 |
| Xử lý DL **sau khi thu thập mà chưa có đồng ý** (nhóm vi phạm về **sự đồng ý**; có ngoại lệ theo luật) | 30–50 triệu | 1.2 |
| Dùng DL cá nhân người khác để làm việc trái luật; cản trở hoạt động bảo vệ DL | 40–60 triệu | 1.8 |
| Đặt sẵn mặc định đồng ý / chỉ dẫn gây nhầm giữa đồng ý và không | 30–50 triệu | 1.2 |
| Không cho đồng ý riêng theo từng mục đích; ép đồng ý mục đích không liên quan, hoặc từ chối dịch vụ nếu không đồng ý | 30–50 triệu | 1.2 |
| Không lưu nhật ký đồng ý / không chứng minh được đã có đồng ý | 30–50 triệu | 1.3 |
| Không cung cấp thông tin minh bạch (loại DL, mục đích, quyền) khi xin đồng ý | 30–50 triệu | 1.1 |
| Không thông báo cho người dùng biết DL nhạy cảm của họ đang được xử lý | 30–50 triệu | 1.5 |
| Coi im lặng/không phản hồi là đồng ý; tiếp tục xử lý sau khi người dùng yêu cầu ngừng | 50–70 triệu | 1.2, 1.3 |

Biện pháp kèm theo có thể gồm: buộc xoá dữ liệu thu không hợp lệ, buộc nộp lại khoản thu bất hợp pháp, buộc xin lỗi công khai.
Mức phạt cho chính sách, quyền chủ thể, chuyển DL ra nước ngoài, thông báo sự cố: **chưa có trong bộ nguồn**.

## Miễn trừ cần đọc kỹ

Theo tin của Chính phủ/Bộ Công an, **hộ kinh doanh và doanh nghiệp siêu nhỏ** được miễn một số nghĩa vụ
(hồ sơ đánh giá tác động, chỉ định bộ phận bảo vệ dữ liệu); DN nhỏ/khởi nghiệp có thời gian chuyển tiếp.
**Điều kiện miễn và trường hợp không được miễn (vd xử lý DL nhạy cảm, kinh doanh dịch vụ xử lý DL) phải đọc trong bản gốc** — đừng tự kết luận được miễn.

## Cần luật sư khi

xử lý dữ liệu nhạy cảm số lượng lớn · nhắm người dùng trẻ em · chuyển dữ liệu ra nước ngoài là cốt lõi sản phẩm · đã xảy ra lộ dữ liệu.
