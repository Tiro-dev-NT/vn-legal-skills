# Góp sức cho vn-legal-skills

Cảm ơn bạn! Mọi đóng góp đều tự động hiện trong mục **Contributors** của GitHub khi PR được merge (tính theo email commit của bạn).
Đóng góp = đồng ý phát hành phần mình viết theo [LICENSE](LICENSE) và chấp nhận [MIEN-TRU-TRACH-NHIEM.md](MIEN-TRU-TRACH-NHIEM.md).

## Ba cách góp, từ dễ đến khó

1. **Báo lỗi / báo luật mới** — mở *Issue*, chọn mẫu:
   - *Báo nội dung sai* — một mục, số điều, mức phạt bị sai hoặc lỗi thời.
   - *Luật mới / luật thay đổi* — có văn bản mới ban hành, sửa đổi, bãi bỏ.
   - *Đề xuất mục / mảng mới* — một nghĩa vụ chưa có trong checklist.
   Không biết Git cũng góp được, chỉ cần dán link văn bản.
2. **Sửa nhỏ** — bấm ✏️ trên GitHub, sửa, tạo PR.
3. **Sửa lớn / thêm mảng** — fork, làm theo "Luật nội dung" dưới đây, chạy cổng kiểm, tạo PR.

## Luật nội dung (bắt buộc)

1. **Nguồn chỉ từ cổng Nhà nước**: congbao.chinhphu.vn, vanban.chinhphu.vn, vbpl.vn, *.gov.vn. Không dùng trang tổng hợp tư nhân.
2. **Không bịa**: số điều, mức phạt chỉ ghi khi đã đọc **chính văn**; ghi rõ mức là của cá nhân hay tổ chức (mỗi nghị định một quy tắc).
   Nguồn chỉ là tin giải thích ⇒ ghi "theo tin …, chưa đối chiếu toàn văn".
3. **Nhãn** mỗi mục: `[luật]` (có trong văn bản) hoặc `[khuyến nghị]` (cách làm an toàn suy ra).
4. **Không ghi thông tin riêng** của dự án/công ty nào (tên app, khách hàng, cấu hình).
5. **Luật đổi ⇒ không xoá bản cũ**:
   - `NGUON.md`: giữ dòng văn bản cũ, ghi "đã bị thay/bãi bỏ bởi …".
   - Chép đoạn cũ trong `mang/` sang [`luu-tru/`](luu-tru/00-MUC-LUC.md) trước khi sửa.
   - Thêm một mục vào [LICH-SU-THAY-DOI.md](LICH-SU-THAY-DOI.md) (cũ → mới, ngày hiệu lực, chuyển tiếp, mục ảnh hưởng).
6. Trích nguyên văn đã dùng để kiểm (nếu dài) ⇒ thêm tệp vào `trich-dan/`.
7. Cập nhật ngày kiểm ở đầu `NGUON.md`.

## Rà luật định kỳ (người duy trì, mỗi tháng)

1. Trên congbao.chinhphu.vn / vanban.chinhphu.vn tìm văn bản mới từ ngày kiểm ở đầu `NGUON.md` với các từ khoá:
   *dữ liệu cá nhân · an ninh mạng · thương mại điện tử · bảo vệ quyền lợi người tiêu dùng · quảng cáo · khuyến mại ·
   quyền tác giả · trí tuệ nhân tạo · trò chơi điện tử · thông tin trên mạng · giao dịch điện tử · xử phạt vi phạm hành chính*.
2. Với mỗi văn bản dẫn trong `NGUON.md`: còn hiệu lực không, có văn bản sửa/thay chưa, dự thảo nào sắp ban hành.
3. Có thay đổi ⇒ làm theo Luật nội dung mục 5 (không xoá bản cũ, ghi LICH-SU-THAY-DOI.md), cập nhật `THU-TUC.md` nếu thủ tục đổi.
4. Cập nhật bảng "Đang siết" trong `LO-TRINH.md`: thêm văn bản mới, bỏ văn bản có hiệu lực quá 12 tháng, đổi ngày "Tính tại".
5. Không có thay đổi ⇒ vẫn đổi ngày kiểm ở đầu `NGUON.md` (skill cảnh báo khi bộ nguồn cũ quá 90 ngày).

## Cổng kiểm

```bash
python scripts/kiem-nhat-quan.py
```

Phải ra `OK`. GitHub Action chạy lại cổng này cho mỗi PR. Cổng kiểm: văn bản được dẫn có trong `NGUON.md`, mảng khớp với skill/README,
mã mục không trùng, tham chiếu chéo tồn tại, miễn trừ trách nhiệm có ở mọi tệp, liên kết không hỏng, nguồn chỉ từ cổng Nhà nước,
văn bản đã bị thay có mục trong lịch sử thay đổi.

## Người duyệt kiểm gì

Mở link nguồn, đọc đúng điều được trích, so con số. PR không có link nguồn chính thức sẽ không được merge.
