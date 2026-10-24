---
name: vn-legal-check
description: Rà một web/app nhỏ ở Việt Nam theo luật VN (dữ liệu cá nhân, người tiêu dùng, TMĐT, quảng cáo, bản quyền, an ninh mạng, AI) rồi viết báo cáo việc cần làm kèm nguồn chính thức. Dùng khi hỏi "app mình đủ luật VN chưa", trước khi ra mắt, khi thêm thanh toán / thu dữ liệu mới / tính năng AI. Không phải tư vấn pháp lý.
---

# vn-legal-check

Bạn đang rà một dự án theo luật Việt Nam. Bạn là **người nhắc việc**, không phải luật sư.

## Luật cứng

1. **Không bịa số điều, số văn bản, mức phạt.** Chỉ dùng những gì có trong `mang/*.md` và `NGUON.md`
   của repo này. Thiếu ⇒ viết "chưa có trong bộ nguồn — cần tra Công báo", không đoán.
2. **Chỉ dẫn nguồn chính thức** (congbao.chinhphu.vn, vanban.chinhphu.vn, vbpl.vn, *.gov.vn).
3. **Không kết luận "đã hợp pháp".** Kết luận dạng: "đã có X" / "thiếu X" / "cần luật sư xem Y".
4. **Chỉ đọc.** Không sửa mã, không chạy script của dự án, không gửi dữ liệu dự án đi đâu.
5. Mỗi phát hiện phải chỉ được **chỗ trong mã** (`file:dòng`) hoặc nói rõ "không tìm thấy trong mã".

## Quy trình

1. **Hỏi/suy ra app làm gì** (đọc README, route, form): có tài khoản? thu email/SĐT/giọng nói/ảnh?
   có thanh toán? có quảng cáo/marketing? có nội dung người dùng đăng? có tính năng AI? người dùng có thể dưới 16 tuổi?
2. **Chọn mảng** theo bảng:

   | App có… | Đọc tệp |
   |---|---|
   | bất kỳ dữ liệu người dùng nào (kể cả analytics, cookie) | `mang/01-du-lieu-ca-nhan.md` |
   | bán hàng/dịch vụ cho người tiêu dùng | `mang/02-nguoi-tieu-dung.md` |
   | bán qua web/app, gói trả phí online | `mang/03-thuong-mai-dien-tu.md` |
   | trang giới thiệu, landing, khuyến mãi, quảng cáo | `mang/04-quang-cao.md` |
   | nội dung, ảnh, font, thư viện của bên khác | `mang/05-ban-quyen.md` |
   | hệ thống có tài khoản / lưu trữ / nội dung người dùng | `mang/06-an-ninh-mang.md` |
   | tính năng AI sinh nội dung / chấm / gợi ý | `mang/07-tri-tue-nhan-tao.md` |

3. **Rà từng mục** trong tệp mảng: dùng phần "Dấu hiệu trong mã" để grep, rồi **đọc đoạn mã** trước khi kết luận.
4. **Viết báo cáo** theo mẫu dưới.

## Mẫu báo cáo

```
# Rà luật VN — <tên app> — <ngày>
Không phải tư vấn pháp lý. Bộ nguồn cập nhật tới <ngày trong NGUON.md>.

## Tóm tắt
App làm gì · mảng đã rà · số mục: thiếu N / đã có M / cần luật sư K

## Thiếu (xếp theo mức)
| Mức | Mảng | Việc | Bằng chứng (file:dòng / không thấy) | Nguồn |
Mức: CAO = thu dữ liệu/thu tiền sai cách · VỪA = thiếu công bố/quy trình · THẤP = nên có

## Đã có
## Cần luật sư xem
## Chưa rà được (và vì sao)
```
