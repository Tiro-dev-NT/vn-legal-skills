# Kiểm thử skill

> Tham khảo, không phải tư vấn pháp lý — [MIEN-TRU-TRACH-NHIEM.md](../MIEN-TRU-TRACH-NHIEM.md).

`cau-hoi.json` là bộ câu hỏi để đo skill có làm AI trả lời **đúng hơn** không (ý tưởng lấy từ cách các bộ skill pháp lý khác chạy "có skill / không có skill" rồi chấm).

## Cách chạy (thủ công)

1. Mở một phiên AI **không** cắm skill, hỏi từng câu trong `cau_hoi`, lưu câu trả lời.
2. Mở phiên mới **có** skill (`skills/vn-legal-check/SKILL.md`), hỏi lại đúng câu đó.
3. Với mỗi câu trả lời, đánh dấu từng ý trong `phai_co` (có/không) và từng ý trong `khong_duoc` (có mắc/không).
4. Ghi kết quả vào `ket-qua/<ngày>-<model>.md` nếu muốn góp kết quả (PR).

## Mẫu thử cho máy quét

`mau-du-an/<tên>/du-an/` là dự án giả nhỏ, tự viết (không tên app/công ty thật, khoá đều là chuỗi giả `GIA_LAP`);
`mau-du-an/<tên>/MONG-DOI.json` ghi mức phân loại phải ra, tín hiệu phải có / không được có, mảng phải mở và chuỗi không được in
(kiểm việc che khoá). Chạy `python -I scripts/chay-mau-thu.py`; cổng `scripts/kiem-nhat-quan.py` cũng gọi lệnh này.
Sửa regex trong `scripts/quet.py` ⇒ thêm hoặc sửa mẫu tương ứng để chặn bắt nhầm/bỏ sót quay lại.

## Luật khi thêm câu hỏi

- Mỗi ý trong `phai_co` phải lấy từ phần **đã đối chiếu toàn văn** trong `mang/` và có `can_cu`.
- Câu nào phụ thuộc văn bản mới ⇒ cập nhật cùng lúc khi luật đổi (xem [LICH-SU-THAY-DOI.md](../LICH-SU-THAY-DOI.md)).
- Không đưa thông tin riêng của dự án/công ty nào vào câu hỏi.
