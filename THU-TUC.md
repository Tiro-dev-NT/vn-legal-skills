# Thủ tục pháp lý cần làm — theo tính năng của dự án

> Tham khảo, không phải tư vấn pháp lý — [MIEN-TRU-TRACH-NHIEM.md](MIEN-TRU-TRACH-NHIEM.md).
> Đây là những việc **ngoài mã nguồn** (hồ sơ, đăng ký, xin phép với cơ quan nhà nước) mà mã không thể tự chứng minh.
> Skill dùng bảng này để **nhắc** người dùng; thủ tục, cơ quan tiếp nhận, mẫu hồ sơ có thể đổi — **tra cổng dịch vụ công lúc làm**.

## Nền tảng (gần như mọi dự án có thu tiền)

| # | Khi nào | Thủ tục | Cơ quan / nơi làm | Căn cứ trong repo |
|---|---|---|---|---|
| T0 | Có thu tiền thường xuyên | Xác định chủ thể kinh doanh (hộ kinh doanh / doanh nghiệp) — đăng ký kinh doanh **chưa có trong bộ nguồn** (lộ trình mảng 10) | cơ quan đăng ký kinh doanh | hỏi luật sư/kế toán |
| T0a | Có thu tiền | **Đăng ký thuế** | Cơ quan thuế | mảng 9.1 |
| T0b | Hộ/cá nhân kinh doanh, doanh thu năm ≤ 01 tỷ | **Thông báo doanh thu thực tế** năm theo mẫu TT 18/2026 | Cơ quan thuế | mảng 9.2 |
| T0c | Hộ/cá nhân kinh doanh, doanh thu năm > 01 tỷ | **Khai thuế** theo quý/tháng; **dùng hoá đơn điện tử** có mã hoặc từ máy tính tiền | Cơ quan thuế | mảng 9.2, 9.4 |
| T0d | Có tài khoản ngân hàng / ví dùng cho kinh doanh | Thông báo theo mẫu TT 18/2026 | Cơ quan thuế | mảng 9.3 |

## Theo tính năng

| # | Khi dự án có… | Thủ tục | Cơ quan / nơi làm | Căn cứ trong repo |
|---|---|---|---|---|
| T1 | Website/app **bán hàng** của chính mình | Thông báo (hoặc thủ tục mới thay thế) website/app TMĐT bán hàng | Bộ Công Thương — online.gov.vn / dichvucong.moit.gov.vn | mảng 3.2; [mang/03](mang/03-thuong-mai-dien-tu.md) "Thủ tục với Bộ Công Thương" |
| T2 | **Nền tảng trung gian** (người khác bán trên nền tảng của bạn, livestream bán hàng) | Đăng ký nền tảng trước khi vận hành; xác thực người bán | Bộ Công Thương | mảng 3.1 |
| T3 | Xử lý **dữ liệu cá nhân** | Hồ sơ đánh giá tác động xử lý DLCN (Luật 91 Điều 21) + cập nhật (Điều 22); bộ phận/nhân sự bảo vệ DLCN (Điều 33 khoản 2) — **hộ KD, DN siêu nhỏ được miễn** trừ khi xử lý DL nhạy cảm, ≥100 nghìn chủ thể hoặc kinh doanh dịch vụ xử lý DL; DN nhỏ/khởi nghiệp được chọn trong 05 năm từ 01/01/2026 | Cơ quan chuyên trách bảo vệ DLCN (Bộ Công an) | mảng 1, "Miễn trừ cần đọc kỹ" |
| T4 | **Chuyển DLCN ra nước ngoài** (máy chủ, AI, email ở nước ngoài) | Hồ sơ đánh giá tác động chuyển DLCN xuyên biên giới, nộp trong 60 ngày (Luật 91 Điều 20; NĐ 356 Điều 18) — **không được miễn** cho hộ KD/DN siêu nhỏ | Cơ quan chuyên trách bảo vệ DLCN (Bộ Công an) | mảng 1.7 |
| T5 | Có **sự cố lộ dữ liệu** | Thông báo cơ quan chuyên trách trong 72 giờ; thông báo người bị ảnh hưởng | Cơ quan chuyên trách bảo vệ DLCN | mảng 1.10 |
| T6 | Dịch vụ thuộc **danh mục phải đăng ký hợp đồng theo mẫu** (QĐ 07/2024/QĐ-TTg) | Đăng ký hợp đồng theo mẫu / điều kiện giao dịch chung trước khi dùng | Bộ Công Thương hoặc Sở Công Thương (theo phạm vi áp dụng) | mảng 2.2 |
| T7 | Chạy **khuyến mại** (giảm giá, tặng quà, may rủi) | Thông báo / đăng ký khuyến mại với hình thức bắt buộc | Sở Công Thương / Bộ Công Thương theo hình thức, phạm vi (**chưa đối chiếu** — kiểm lại) | mảng 4.10 |
| T8 | **Game G1** (nhiều người chơi qua máy chủ) | Giấy phép cung cấp dịch vụ G1 + Quyết định phát hành từng game | Cơ quan quản lý game (Bộ VHTTDL theo tin Chính phủ 09/2026 — kiểm lại) | mảng 8.1 |
| T9 | **Game G2/G3/G4** | Giấy chứng nhận cung cấp dịch vụ + Giấy xác nhận thông báo phát hành từng game | như T8 | mảng 8.1 |
| T10 | **Mạng xã hội** / trang thông tin tổng hợp (theo định nghĩa NĐ 147/2024) | Giấy phép / thông báo theo loại và quy mô | Cơ quan quản lý thông tin trên mạng — đọc NĐ 147/2024 | mảng 6, "Phân loại trước" |
| T11 | **Hệ thống thông tin** thuộc diện xác định cấp độ | Hồ sơ đề xuất cấp độ, thẩm định, phê duyệt | theo NĐ 331/2026 | mảng 6.6 |
| T12 | Dùng **ảnh, nhạc, font, nội dung của người khác** | Xin phép / mua giấy phép; lưu bằng chứng | Chủ sở hữu quyền | mảng 5.1–5.3 |
| T12a | Dùng **dữ liệu/API của bên khác** cho sản phẩm thu tiền | Mua gói thương mại / ký hợp đồng cấp phép dữ liệu; lưu bản điều khoản | Bên cung cấp dữ liệu | mảng 5.8, 5.12 |
| T13 | **Email/SMS quảng cáo** | Thủ tục theo NĐ 91/2020 với từng kênh (nếu thuộc diện) | đọc NĐ 91/2020 | mảng 4.6 |
| T14 | **Tự cung ứng** ví điện tử / cổng thanh toán / hỗ trợ thu hộ, chi hộ (người dùng nạp – giữ – rút tiền, hoặc tiền người khác đi qua bạn) | Giấy phép hoạt động cung ứng dịch vụ trung gian thanh toán — chủ thể là tổ chức có đăng ký doanh nghiệp, vốn điều lệ tối thiểu 50 tỷ, đề án, an toàn hệ thống thông tin cấp độ 3; thẩm định 90 ngày làm việc; giấy phép 10 năm. **Web/app nhỏ: thường dùng đối tác có phép thay vì xin** | Ngân hàng Nhà nước — Bộ phận Một cửa / Cổng dịch vụ công NHNN / Cổng dịch vụ công quốc gia | mảng 11.1, 11.2, 11.3 |
| T15 | Muốn **giữ ngoại tệ** thu từ xuất khẩu dịch vụ **ở nước ngoài** (không chuyển về tài khoản ngoại tệ ở ngân hàng Việt Nam) · tổ chức mở tài khoản ngoại tệ ở nước ngoài | Xin NHNN cho phép (Pháp lệnh Ngoại hối Điều 7 khoản 2) · giấy phép mở tài khoản ngoại tệ ở nước ngoài (Điều 23 khoản 3) — có áp cho số dư PayPal/Stripe không: **chưa rõ, hỏi luật sư** | Ngân hàng Nhà nước | mảng 11.10 |
| T16 | Cung cấp dịch vụ **tài sản mã hoá** (sàn, tự doanh, lưu ký, nền tảng phát hành) | Giấy phép cung cấp dịch vụ tổ chức thị trường giao dịch tài sản mã hoá — doanh nghiệp Việt Nam, vốn điều lệ đã góp tối thiểu 10.000 tỷ | Bộ Tài chính (NQ 05/2025 Điều 8, 10) | mảng 11.13 |

## Cách skill dùng bảng này

1. Từ bước phân loại, chọn các dòng T áp dụng.
2. Thủ tục **không thể kiểm bằng mã** ⇒ đưa vào mục "Thủ tục phải làm" của báo cáo với trạng thái **"chưa xác nhận"** và hỏi người dùng đã làm chưa
   (đã có mã nhúng/biểu tượng Bộ Công Thương ở footer, số giấy phép game… thì ghi "có dấu hiệu đã làm" kèm `file:dòng`).
3. Không bao giờ ghi "đã đủ thủ tục".
