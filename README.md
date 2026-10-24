# vn-legal-skills

Bộ skill + checklist giúp AI (Claude Code, Codex, Cursor…) **rà một web/app nhỏ ở Việt Nam theo luật VN**:
dữ liệu cá nhân, người tiêu dùng, thương mại điện tử, quảng cáo, bản quyền, an ninh mạng, AI.

> ⚠️ **Không phải tư vấn pháp lý.** Đây là công cụ nhắc việc. Nó chỉ ra chỗ cần xem lại và dẫn văn bản
> gốc để bạn tự đọc; nó **không** chứng nhận app của bạn hợp pháp. Việc có rủi ro tiền/phạt ⇒ hỏi luật sư.
> Luật cập nhật tới: **2026-10-24** (xem [NGUON.md](NGUON.md)).

## Luật nguồn

- Mọi văn bản dẫn tới **cổng chính thức của Nhà nước** (Công báo, vanban.chinhphu.vn, vbpl.vn, *.gov.vn). Không dùng trang tổng hợp tư nhân.
- Checklist **chỉ trích số điều** khi văn bản đó đã được đối chiếu toàn văn (cột "Kiểm" trong [NGUON.md](NGUON.md)). Chưa đối chiếu ⇒ ghi tên văn bản, không bịa số điều.

## Cấu trúc — chia theo mảng

```
NGUON.md                         bảng văn bản: số hiệu · ngày · hiệu lực · link chính thức · đã kiểm tới đâu
skills/
  vn-legal-check/SKILL.md        skill điều phối: hỏi app làm gì → chọn mảng → rà → báo cáo
mang/                            mỗi mảng một tệp: áp khi nào · việc phải có · dấu hiệu lỗi trong mã · nguồn
  01-du-lieu-ca-nhan.md
  02-nguoi-tieu-dung.md
  03-thuong-mai-dien-tu.md
  04-quang-cao.md
  05-ban-quyen.md
  06-an-ninh-mang.md
  07-tri-tue-nhan-tao.md
mau/                             mẫu văn bản để trống [CHỖ ĐIỀN], tự viết, không chép của ai
  chinh-sach-quyen-rieng-tu.md
  dieu-khoan-su-dung.md
```

## Dùng

**Claude Code:** chép `skills/vn-legal-check/` vào `.claude/skills/` của dự án (hoặc `~/.claude/skills/`), rồi gõ
`/vn-legal-check`. Skill đọc tệp trong `mang/` theo đường tương đối với repo này — giữ nguyên cấu trúc, hoặc chép cả repo.

**AI khác:** đưa `skills/vn-legal-check/SKILL.md` + các tệp `mang/` cần thiết vào ngữ cảnh.

Skill **chỉ đọc mã và viết báo cáo**; không sửa mã, không gọi mạng ngoài việc mở link nguồn.

## Góp sức

- Sửa/ thêm văn bản: theo mục "Cách thêm" cuối [NGUON.md](NGUON.md). PR phải kèm link cổng chính thức.
- Thêm luật kiểm vào một mảng: ghi *vì sao* + văn bản gốc; luật suy diễn (chưa có điều cụ thể) ghi rõ là "khuyến nghị".

## Giấy phép

MIT — xem [LICENSE](LICENSE). Văn bản pháp luật trích dẫn không thuộc đối tượng bảo hộ quyền tác giả;
phần checklist và mẫu là nội dung tự viết của repo.
