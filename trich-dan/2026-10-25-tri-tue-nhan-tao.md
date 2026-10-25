# TRÍCH DẪN NGUYÊN VĂN — trí tuệ nhân tạo (app "bọc" AI: chatbot, chấm bài, tạo ảnh/giọng, gợi ý)

> Tham khảo, không phải tư vấn pháp lý — [MIEN-TRU-TRACH-NHIEM.md](../MIEN-TRU-TRACH-NHIEM.md).

Mốc đối chiếu: 25/10/2026. Dùng cho [mang/07-tri-tue-nhan-tao.md](../mang/07-tri-tue-nhan-tao.md).
Quy ước: khối `>` là nguyên văn chép từ bản chữ trích của tệp DOCX/PDF trên trang Công báo (chỉ bỏ ký tự rác của khung văn bản và dòng tiêu đề trang Công báo); `> …` là chỗ lược bớt. Dòng "Ghi chú" là diễn giải của người trích, không phải nguyên văn.

---

## Kết luận nhanh (đọc trước)

1. **Vai trò.** App đưa tính năng AI ra cho người dùng **dưới tên, thương hiệu của mình** thì khớp định nghĩa **nhà cung cấp** (Luật 134/2025 Điều 3 khoản 4: "không phụ thuộc hệ thống đó do họ tự phát triển hay được phát triển bởi bên thứ ba"), đồng thời là **bên triển khai** (Điều 3 khoản 5: dùng hệ thống trong phạm vi kiểm soát của mình để cung cấp dịch vụ). NĐ 142/2026 Điều 12 khoản 3 và Điều 16 khoản 6 nói thẳng trường hợp nhà cung cấp xây hệ thống "dựa trên nền tảng, mô hình hoặc dịch vụ trí tuệ nhân tạo của bên thứ ba". Bên bán API mô hình là bên cung cấp **mô hình**; việc phân loại rủi ro áp cho **hệ thống**, không áp cho mô hình (NĐ 142 Điều 6 khoản 2). Người dùng cuối là **người sử dụng** (Luật Điều 3 khoản 6). Ghi chú: đây là đọc theo chữ định nghĩa; văn bản không có ví dụ "app gọi API".
2. **Mức rủi ro.** Ba mức (Luật Điều 9). **Cao** = chỉ những hệ thống thuộc Danh mục do Thủ tướng ban hành (NĐ 142 Điều 6 khoản 3 điểm a) — nay là **QĐ 33/2026/QĐ-TTg** (46 hệ thống, hiệu lực 15/08/2026), trong đó **lĩnh vực giáo dục có 3 hệ thống** (nội dung tự học dùng dữ liệu không kiểm soát, quy mô lớn; chấm điểm tự động làm căn cứ chính thức trong hệ thống giáo dục quốc dân; giám sát hành vi người học bằng sinh trắc học hoặc cảnh báo tự động tần suất cao). **Trung bình** = không thuộc Danh mục **và** có khả năng gây nhầm lẫn, thao túng do người dùng không nhận biết đang tương tác với AI hoặc nội dung do AI tạo (NĐ 142 Điều 9 khoản 1), trừ 5 trường hợp loại trừ (Điều 9 khoản 3). **Thấp** = còn lại.
3. **Thủ tục.** Nhà cung cấp tự phân loại trước khi đưa vào dùng. Trung bình/cao: lập hồ sơ phân loại + **thông báo cho Bộ KH&CN qua Cổng thông tin điện tử một cửa về AI trước khi đưa vào sử dụng**, tự kê khai, được cấp mã định danh ngay (Luật Điều 10 khoản 1, 3; NĐ 142 Điều 12, 14). Thấp: không phải thông báo. Cao: thêm đánh giá sự phù hợp (Luật Điều 13; NĐ 142 Điều 13) — với 3 hệ thống giáo dục, cột đánh dấu là "điểm b khoản 2 Điều 13" (tự đánh giá hoặc thuê tổ chức).
4. **Minh bạch.** Nhà cung cấp: người dùng phải nhận biết đang tương tác với AI (Luật Điều 11 khoản 1); âm thanh, hình ảnh, video do hệ thống tạo phải **đánh dấu định dạng máy đọc** — văn bản thì **không bắt buộc** (NĐ 142 Điều 17 khoản 1). Bên triển khai: **thông báo rõ** khi đưa ra công cộng nội dung có khả năng gây nhầm lẫn về tính xác thực; **gắn nhãn dễ nhận biết** cho âm thanh/hình ảnh/video mô phỏng ngoại hình, giọng nói người thật hoặc tái hiện sự kiện thực tế (Luật Điều 11 khoản 3, 4; NĐ 142 Điều 18). Có danh sách miễn nhãn (NĐ 142 Điều 18 khoản 4).
5. **Cấm.** Luật 134/2025 Điều 7 (giả mạo/mô phỏng người thật để lừa dối, thao túng có chủ đích gây tổn hại nghiêm trọng; lợi dụng điểm yếu trẻ em…; tẩy xoá nhãn bắt buộc…) + Luật 116/2025 Điều 7 khoản 2 điểm g (dùng AI giả mạo video, hình ảnh, giọng nói người khác trái pháp luật).
6. **Chuyển tiếp.** Hệ thống đưa vào hoạt động **trước 01/03/2026**: 18 tháng (y tế, giáo dục, tài chính) / 12 tháng (còn lại) kể từ 01/03/2026 (Luật Điều 35). Hệ thống thuộc Danh mục rủi ro cao: trước 01/09/2027 (y tế, giáo dục, tài chính) / trước 01/03/2027 (còn lại) (QĐ 33 Điều 4).
7. **Mức phạt.** **Chưa thấy nghị định xử phạt riêng lĩnh vực AI** (tra cổng Chính phủ, Bộ KH&CN tới 25/10/2026). Luật Điều 29 khoản 5 giao Chính phủ quy định. Dự thảo nghị định xử phạt lĩnh vực khoa học, công nghệ, đổi mới sáng tạo (Bộ KH&CN lấy ý kiến 18–27/08/2026) — bản dự thảo đã tải **không có cụm "trí tuệ nhân tạo"**.

---

## A. Luật Trí tuệ nhân tạo 134/2025/QH15 (ban hành 10/12/2025, hiệu lực 01/03/2026)

Trang Công báo: https://congbao.chinhphu.vn/van-ban/luat-so-134-2025-qh15-468694.htm — chữ trích từ tệp DOCX trên trang (file_name `2026_40_134/2025/QH15.docx`); PDF ký số: https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/26/l134signed-176941401701024378539.pdf

### A1. Điều 3 — Giải thích từ ngữ
> Điều 3. Giải thích từ ngữ
> Trong Luật này, các từ ngữ dưới đây được hiểu như sau:
> 1. Trí tuệ nhân tạo là việc thực hiện bằng điện tử các năng lực trí tuệ của con người, bao gồm học tập, suy luận, nhận thức, phán đoán và hiểu ngôn ngữ tự nhiên.
> 2. Hệ thống trí tuệ nhân tạo là hệ thống dựa trên máy, được thiết kế để thực hiện các năng lực trí tuệ nhân tạo với các mức độ tự chủ khác nhau, có khả năng tự thích nghi sau khi được triển khai; căn cứ vào các mục tiêu được xác định rõ ràng hoặc được hình thành một cách ngầm định, hệ thống suy luận từ dữ liệu đầu vào để tạo ra các đầu ra như dự đoán, nội dung, khuyến nghị hoặc quyết định có thể gây ảnh hưởng tới môi trường vật lý hoặc môi trường số.
> 3. Nhà phát triển là tổ chức, cá nhân thực hiện việc thiết kế, xây dựng, huấn luyện, kiểm thử hoặc tinh chỉnh toàn bộ hoặc một phần mô hình, thuật toán hoặc hệ thống trí tuệ nhân tạo và có quyền kiểm soát trực tiếp đối với phương pháp kỹ thuật, dữ liệu huấn luyện hoặc tham số mô hình.
> 4. Nhà cung cấp là tổ chức, cá nhân đưa hệ thống trí tuệ nhân tạo ra thị trường hoặc đưa vào sử dụng dưới tên, thương hiệu hoặc nhãn hiệu của mình, không phụ thuộc hệ thống đó do họ tự phát triển hay được phát triển bởi bên thứ ba.
> 5. Bên triển khai là tổ chức, cá nhân sử dụng hệ thống trí tuệ nhân tạo thuộc phạm vi kiểm soát của mình trong hoạt động nghề nghiệp, thương mại hoặc cung cấp dịch vụ; không bao gồm trường hợp sử dụng cho mục đích cá nhân, phi thương mại.
> 6. Người sử dụng là tổ chức, cá nhân trực tiếp tương tác với hệ thống trí tuệ nhân tạo hoặc sử dụng kết quả đầu ra của hệ thống đó.
> 7. Người bị ảnh hưởng là tổ chức, cá nhân bị tác động trực tiếp hoặc gián tiếp đến quyền, lợi ích hợp pháp, tính mạng, sức khỏe, tài sản, uy tín hoặc cơ hội tiếp cận dịch vụ do việc triển khai hoặc do kết quả đầu ra của hệ thống trí tuệ nhân tạo.
> 8. Sự cố nghiêm trọng là sự kiện xảy ra trong hoạt động của hệ thống trí tuệ nhân tạo, gây ra hoặc có nguy cơ gây ra thiệt hại đáng kể đến tính mạng, sức khỏe, quyền con người, tài sản, an ninh mạng, trật tự công cộng, môi trường hoặc làm gián đoạn hoạt động của hệ thống thông tin quan trọng về an ninh quốc gia.

### A2. Điều 4 khoản 2 — Nguyên tắc (con người kiểm soát)
> 2. Trí tuệ nhân tạo phục vụ con người, không thay thế thẩm quyền và trách nhiệm của con người. Bảo đảm duy trì sự kiểm soát và khả năng can thiệp của con người đối với mọi quyết định và hành vi của hệ thống trí tuệ nhân tạo; an toàn hệ thống, an ninh dữ liệu và bảo mật thông tin; khả năng kiểm tra và giám sát quá trình phát triển và vận hành hệ thống trí tuệ nhân tạo.

### A3. Điều 6 khoản 2 — Lĩnh vực thiết yếu (giáo dục)
> 2. Đối với các lĩnh vực thiết yếu có tác động trực tiếp đến tính mạng, sức khỏe, quyền và lợi ích hợp pháp của con người hoặc trật tự, an toàn xã hội, việc ứng dụng trí tuệ nhân tạo phải được quản lý rủi ro ở mức độ chặt chẽ hơn, phù hợp với đặc thù của từng lĩnh vực, trong đó bao gồm một số lĩnh vực sau đây:
> …
> b) Lĩnh vực giáo dục: bảo đảm phù hợp với đặc điểm lứa tuổi và sự phát triển của người học; phòng ngừa rủi ro trong đánh giá, phân loại và tác động đến người học; bảo đảm an toàn dữ liệu và quyền riêng tư.

### A4. Điều 7 — Các hành vi bị nghiêm cấm
> Điều 7. Các hành vi bị nghiêm cấm
> 1. Lợi dụng, chiếm đoạt hệ thống trí tuệ nhân tạo để thực hiện hành vi vi phạm pháp luật, xâm phạm quyền, lợi ích hợp pháp của tổ chức, cá nhân.
> 2. Phát triển, cung cấp, triển khai hoặc sử dụng các hệ thống trí tuệ nhân tạo nhằm mục đích sau đây:
> a) Thực hiện các hành vi bị nghiêm cấm theo quy định của luật;
> b) Sử dụng yếu tố giả mạo hoặc mô phỏng người, sự kiện thật để lừa dối hoặc thao túng nhận thức, hành vi của con người một cách có chủ đích và có hệ thống, gây tổn hại nghiêm trọng đến quyền, lợi ích hợp pháp của con người;
> c) Lợi dụng điểm yếu của nhóm người dễ bị tổn thương, bao gồm trẻ em, người cao tuổi, người khuyết tật, người dân tộc thiểu số hoặc người mất năng lực hành vi dân sự, người bị hạn chế năng lực hành vi dân sự, người có khó khăn trong nhận thức, làm chủ hành vi để gây tổn hại cho chính họ hoặc người khác;
> d) Tạo ra hoặc phổ biến nội dung giả mạo có khả năng gây nguy hại nghiêm trọng đến an ninh quốc gia, trật tự, an toàn xã hội.
> 3. Thu thập, xử lý hoặc sử dụng dữ liệu để phát triển, huấn luyện, kiểm thử hoặc vận hành hệ thống trí tuệ nhân tạo trái với quy định của pháp luật về dữ liệu, bảo vệ dữ liệu cá nhân, sở hữu trí tuệ và an ninh mạng.
> 4. Cản trở, vô hiệu hóa hoặc làm sai lệch cơ chế giám sát, can thiệp và kiểm soát của con người đối với hệ thống trí tuệ nhân tạo theo quy định của Luật này.
> 5. Che giấu thông tin bắt buộc phải công khai, minh bạch hoặc giải trình; tẩy xóa, làm sai lệch các thông tin, nhãn, cảnh báo bắt buộc trong hoạt động trí tuệ nhân tạo.
> 6. Lợi dụng hoạt động nghiên cứu, thử nghiệm, đánh giá hoặc kiểm định hệ thống trí tuệ nhân tạo để thực hiện hành vi trái quy định của luật.

### A5. Điều 8 khoản 1 — Cổng thông tin điện tử một cửa
> Điều 8. Cổng thông tin điện tử một cửa về trí tuệ nhân tạo và Cơ sở dữ liệu quốc gia về hệ thống trí tuệ nhân tạo
> 1. Cổng thông tin điện tử một cửa về trí tuệ nhân tạo là nền tảng số được thiết lập nhằm hỗ trợ việc tiếp nhận, đăng ký tham gia thử nghiệm có kiểm soát; tiếp nhận thông báo kết quả phân loại hệ thống trí tuệ nhân tạo, báo cáo sự cố nghiêm trọng và báo cáo định kỳ; công khai thông tin về hệ thống trí tuệ nhân tạo, kết quả đánh giá sự phù hợp, kết quả xử lý vi phạm theo quy định của pháp luật và kết nối các chương trình hỗ trợ, quỹ, hạ tầng, dữ liệu dùng chung.

### A6. Điều 9 — Phân loại mức độ rủi ro
> Điều 9. Phân loại mức độ rủi ro của hệ thống trí tuệ nhân tạo
> 1. Hệ thống trí tuệ nhân tạo được phân loại theo các mức độ rủi ro sau đây:
> a) Hệ thống trí tuệ nhân tạo có rủi ro cao là hệ thống có thể gây thiệt hại đáng kể đến tính mạng, sức khỏe, quyền và lợi ích hợp pháp của tổ chức, cá nhân, lợi ích quốc gia, lợi ích công cộng, an ninh quốc gia;
> b) Hệ thống trí tuệ nhân tạo có rủi ro trung bình là hệ thống có khả năng gây nhầm lẫn, tác động hoặc thao túng người sử dụng do không nhận biết được chủ thể tương tác là hệ thống trí tuệ nhân tạo hoặc nội dung do hệ thống tạo ra;
> c) Hệ thống trí tuệ nhân tạo có rủi ro thấp là hệ thống không thuộc trường hợp quy định tại điểm a và điểm b khoản này.
> 2. Việc phân loại rủi ro của hệ thống trí tuệ nhân tạo được xác định trên cơ sở các tiêu chí về mức độ tác động đến quyền con người, an toàn, an ninh; lĩnh vực sử dụng của hệ thống, đặc biệt là lĩnh vực thiết yếu hoặc liên quan trực tiếp đến lợi ích công cộng; phạm vi người sử dụng và quy mô ảnh hưởng của hệ thống.
> 3. Chính phủ quy định chi tiết Điều này.

### A7. Điều 10 — Phân loại và thông báo
> Điều 10. Phân loại và thông báo hệ thống trí tuệ nhân tạo
> 1. Nhà cung cấp tự phân loại hệ thống trí tuệ nhân tạo trước khi đưa vào sử dụng. Hệ thống được phân loại là rủi ro trung bình hoặc rủi ro cao phải có hồ sơ phân loại kèm theo.
> 2. Bên triển khai được kế thừa kết quả phân loại của nhà cung cấp và có trách nhiệm bảo đảm an toàn, nguyên vẹn của hệ thống trong quá trình sử dụng; trường hợp sửa đổi, tích hợp hoặc thay đổi chức năng làm phát sinh rủi ro mới hoặc rủi ro cao hơn thì phối hợp nhà cung cấp thực hiện phân loại lại.
> 3. Đối với hệ thống được phân loại là rủi ro trung bình hoặc rủi ro cao, nhà cung cấp phải thông báo kết quả phân loại cho Bộ Khoa học và Công nghệ thông qua Cổng thông tin điện tử một cửa về trí tuệ nhân tạo trước khi đưa vào sử dụng. Khuyến khích tổ chức, cá nhân phát triển hệ thống trí tuệ nhân tạo có rủi ro thấp công khai thông tin cơ bản của hệ thống nhằm tăng tính minh bạch.
> 4. Trường hợp chưa xác định được mức độ rủi ro, nhà cung cấp được đề nghị Bộ Khoa học và Công nghệ hướng dẫn về phân loại trên cơ sở hồ sơ kỹ thuật.
> 5. Việc kiểm tra, giám sát được thực hiện theo mức độ rủi ro của hệ thống:
> a) Hệ thống trí tuệ nhân tạo có rủi ro cao được kiểm tra định kỳ hoặc khi có dấu hiệu vi phạm;
> b) Hệ thống trí tuệ nhân tạo có rủi ro trung bình được giám sát thông qua báo cáo, kiểm tra chọn mẫu hoặc đánh giá của tổ chức độc lập;
> c) Hệ thống trí tuệ nhân tạo có rủi ro thấp được theo dõi, kiểm tra khi có sự cố, phản ánh hoặc khi cần bảo đảm an toàn, không làm phát sinh nghĩa vụ không cần thiết cho tổ chức, cá nhân.
> 6. Trên cơ sở kết quả kiểm tra, giám sát quy định tại khoản 5 Điều này, khi phát hiện sai lệch hoặc khai báo không trung thực, cơ quan có thẩm quyền yêu cầu tái phân loại, bổ sung hồ sơ hoặc tạm dừng việc sử dụng, đồng thời xử lý theo quy định của pháp luật.
> 7. Chính phủ quy định chi tiết về nội dung cần thông báo, trình tự, thủ tục thông báo và hướng dẫn kỹ thuật về phân loại rủi ro.

### A8. Điều 11 — Trách nhiệm minh bạch
> Điều 11. Trách nhiệm minh bạch
> 1. Nhà cung cấp bảo đảm hệ thống trí tuệ nhân tạo tương tác trực tiếp với con người được thiết kế và vận hành để người sử dụng nhận biết khi đang tương tác với hệ thống, trừ trường hợp pháp luật có quy định khác.
> 2. Nhà cung cấp bảo đảm các nội dung âm thanh, hình ảnh, video do hệ thống trí tuệ nhân tạo tạo ra được đánh dấu ở định dạng máy đọc theo quy định của Chính phủ.
> 3. Bên triển khai có trách nhiệm thông báo rõ ràng khi cung cấp ra công cộng văn bản, âm thanh, hình ảnh, video được tạo ra hoặc chỉnh sửa bằng hệ thống trí tuệ nhân tạo nếu nội dung đó có khả năng gây nhầm lẫn về tính xác thực của sự kiện, nhân vật, trừ trường hợp pháp luật có quy định khác.
> 4. Bên triển khai có trách nhiệm bảo đảm âm thanh, hình ảnh, video được tạo ra hoặc chỉnh sửa bằng hệ thống trí tuệ nhân tạo nhằm mô phỏng, giả lập ngoại hình, giọng nói của người thật hoặc tái hiện sự kiện thực tế phải được gắn nhãn dễ nhận biết để phân biệt với nội dung thật.
> Đối với sản phẩm là tác phẩm điện ảnh, nghệ thuật hoặc sáng tạo, việc gắn nhãn quy định tại khoản này được thực hiện theo phương thức phù hợp, bảo đảm không làm cản trở việc hiển thị, trình diễn hoặc thưởng thức tác phẩm.
> 5. Nhà cung cấp và bên triển khai có trách nhiệm duy trì thông tin minh bạch theo quy định tại Điều này trong suốt quá trình cung cấp hệ thống, sản phẩm hoặc nội dung cho người sử dụng.
> 6. Chính phủ quy định chi tiết hình thức thông báo, gắn nhãn.

### A9. Điều 12 — Sự cố
> Điều 12. Trách nhiệm quản lý và xử lý sự cố trí tuệ nhân tạo
> 1. Nhà phát triển, nhà cung cấp, bên triển khai và người sử dụng hệ thống trí tuệ nhân tạo có trách nhiệm bảo đảm an toàn, an ninh, độ tin cậy và kịp thời phát hiện, khắc phục sự cố có khả năng gây tổn hại đến con người, tài sản, dữ liệu hoặc trật tự xã hội.
> 2. Khi hệ thống trí tuệ nhân tạo xảy ra sự cố nghiêm trọng, nhà phát triển, nhà cung cấp, bên triển khai, người sử dụng hệ thống trí tuệ nhân tạo có trách nhiệm sau đây:
> a) Nhà phát triển, nhà cung cấp phải khẩn trương áp dụng biện pháp kỹ thuật để khắc phục, tạm dừng hoặc thu hồi hệ thống, đồng thời thông báo cho cơ quan có thẩm quyền;
> b) Bên triển khai và người sử dụng có nghĩa vụ ghi nhận, thông báo kịp thời sự cố và phối hợp trong quá trình khắc phục.
> 3. Cơ quan quản lý nhà nước có thẩm quyền tiếp nhận, xác minh và hướng dẫn xử lý sự cố; khi cần thiết, có quyền yêu cầu tạm dừng, thu hồi hoặc đánh giá lại hệ thống trí tuệ nhân tạo.
> 4. Báo cáo và xử lý sự cố được thực hiện qua Cổng thông tin điện tử một cửa về trí tuệ nhân tạo.
> 5. Chính phủ quy định việc báo cáo và trách nhiệm của các cơ quan, tổ chức, cá nhân có liên quan phù hợp với mức độ nghiêm trọng của sự cố và phạm vi ảnh hưởng của hệ thống trí tuệ nhân tạo.

### A10. Điều 13 khoản 1, 2, 4 — Đánh giá sự phù hợp (rủi ro cao)
> Điều 13. Đánh giá sự phù hợp đối với hệ thống trí tuệ nhân tạo có rủi ro cao
> 1. Hệ thống trí tuệ nhân tạo có rủi ro cao phải được đánh giá sự phù hợp theo quy định của Luật này trước khi đưa vào sử dụng hoặc khi có thay đổi đáng kể trong quá trình sử dụng. Trường hợp có tiêu chuẩn, quy chuẩn kỹ thuật về hệ thống trí tuệ nhân tạo thì còn phải thực hiện đánh giá sự phù hợp theo quy định của pháp luật về tiêu chuẩn, quy chuẩn kỹ thuật.
> 2. Đánh giá sự phù hợp là việc xác nhận hệ thống trí tuệ nhân tạo đáp ứng các yêu cầu tại Điều 14 của Luật này và được thực hiện như sau:
> a) Đối với hệ thống trí tuệ nhân tạo có rủi ro cao thuộc danh mục hệ thống trí tuệ nhân tạo phải chứng nhận sự phù hợp trước khi đưa vào sử dụng: việc đánh giá được thực hiện bởi tổ chức đánh giá sự phù hợp đã được đăng ký hoặc thừa nhận theo quy định của pháp luật;
> b) Đối với các hệ thống trí tuệ nhân tạo có rủi ro cao khác: nhà cung cấp tự đánh giá sự phù hợp hoặc thuê tổ chức đánh giá sự phù hợp đã được đăng ký hoặc thừa nhận theo quy định của pháp luật.
> …
> 4. Thủ tướng Chính phủ quy định Danh mục hệ thống trí tuệ nhân tạo có rủi ro cao, bao gồm danh mục hệ thống trí tuệ nhân tạo phải chứng nhận sự phù hợp trước khi đưa vào sử dụng.

### A11. Điều 14 khoản 2, 3, 6 — Bên triển khai, người sử dụng, nhà cung cấp nước ngoài (rủi ro cao)
> Điều 14. Quản lý hệ thống trí tuệ nhân tạo có rủi ro cao
> …
> 2. Bên triển khai hệ thống trí tuệ nhân tạo có rủi ro cao có trách nhiệm sau đây:
> a) Vận hành và giám sát hệ thống đúng mục đích, phạm vi và mức độ rủi ro đã được phân loại, không làm phát sinh rủi ro mới hoặc rủi ro cao hơn;
> b) Bảo đảm an toàn, bảo mật dữ liệu và khả năng can thiệp của con người trong quá trình sử dụng;
> c) Duy trì việc tuân thủ tiêu chuẩn, quy chuẩn kỹ thuật về trí tuệ nhân tạo trong quá trình vận hành hệ thống;
> d) Thực hiện nghĩa vụ minh bạch và xử lý sự cố theo quy định tại Điều 11 và Điều 12 của Luật này;
> đ) Thực hiện trách nhiệm giải trình đối với cơ quan nhà nước có thẩm quyền về việc vận hành hệ thống, biện pháp kiểm soát rủi ro, xử lý sự cố và các nội dung cần thiết phục vụ công tác thanh tra, kiểm tra; cung cấp cho người sử dụng và người bị ảnh hưởng các thông tin công khai ở mức mô tả chức năng, cách thức vận hành và cảnh báo rủi ro nhằm bảo đảm an toàn trong sử dụng;
> e) Phối hợp với nhà cung cấp và cơ quan nhà nước có thẩm quyền trong kiểm tra, đánh giá, hậu kiểm và khắc phục sự cố.
> 3. Người sử dụng hệ thống trí tuệ nhân tạo có rủi ro cao có trách nhiệm tuân thủ quy trình vận hành, hướng dẫn kỹ thuật và các biện pháp bảo đảm an toàn; không can thiệp trái phép làm thay đổi tính năng của hệ thống; thông báo kịp thời các sự cố phát sinh cho bên triển khai.
> …
> 6. Nhà cung cấp nước ngoài có hệ thống trí tuệ nhân tạo có rủi ro cao được cung cấp tại Việt Nam phải có đầu mối liên hệ hợp pháp tại Việt Nam; trường hợp hệ thống thuộc diện bắt buộc chứng nhận sự phù hợp trước khi đưa vào sử dụng, phải có hiện diện thương mại hoặc đại diện được ủy quyền tại Việt Nam.

### A12. Điều 15 — Rủi ro trung bình và thấp
> Điều 15. Quản lý hệ thống trí tuệ nhân tạo có rủi ro trung bình và thấp
> 1. Hệ thống trí tuệ nhân tạo có rủi ro trung bình được quản lý như sau:
> a) Nhà cung cấp và bên triển khai phải bảo đảm minh bạch theo quy định tại Điều 11 của Luật này;
> b) Nhà cung cấp có trách nhiệm giải trình về mục đích sử dụng, nguyên lý hoạt động ở mức mô tả chức năng, dữ liệu đầu vào chủ yếu và biện pháp quản lý rủi ro, an toàn của hệ thống khi có yêu cầu của cơ quan nhà nước trong thanh tra, kiểm tra hoặc khi có dấu hiệu rủi ro hoặc sự cố; việc giải trình không yêu cầu tiết lộ mã nguồn, thuật toán chi tiết, bộ tham số hoặc bí mật kinh doanh, bí mật công nghệ;
> c) Bên triển khai có trách nhiệm giải trình về việc vận hành, kiểm soát rủi ro, xử lý sự cố và bảo vệ quyền, lợi ích hợp pháp của tổ chức, cá nhân khi có yêu cầu của cơ quan nhà nước có thẩm quyền trong quá trình thanh tra, kiểm tra hoặc xử lý sự cố;
> d) Người sử dụng có trách nhiệm tuân thủ quy định về thông báo, gắn nhãn hệ thống trí tuệ nhân tạo.
> 2. Hệ thống trí tuệ nhân tạo có rủi ro thấp được quản lý như sau:
> a) Nhà cung cấp có trách nhiệm giải trình khi có yêu cầu của cơ quan nhà nước có thẩm quyền trong trường hợp có dấu hiệu vi phạm pháp luật hoặc ảnh hưởng đến quyền, lợi ích hợp pháp của tổ chức, cá nhân;
> b) Bên triển khai có trách nhiệm giải trình khi có yêu cầu của cơ quan nhà nước có thẩm quyền trong trường hợp có dấu hiệu vi phạm pháp luật hoặc ảnh hưởng đến quyền, lợi ích hợp pháp của tổ chức, cá nhân;
> c) Người sử dụng có quyền khai thác, sử dụng hệ thống cho các mục đích hợp pháp và tự chịu trách nhiệm trước pháp luật về hoạt động sử dụng của mình.
> 3. Nhà nước khuyến khích tổ chức, cá nhân triển khai hệ thống trí tuệ nhân tạo có rủi ro trung bình và thấp áp dụng tiêu chuẩn kỹ thuật về trí tuệ nhân tạo.

### A13. Điều 29 — Xử lý vi phạm, bồi thường
> Điều 29. Xử lý vi phạm và trách nhiệm bồi thường thiệt hại
> 1. Tổ chức, cá nhân có hành vi vi phạm quy định của Luật này và quy định khác của pháp luật có liên quan đến trí tuệ nhân tạo, tùy theo tính chất, mức độ, hậu quả của hành vi vi phạm thì bị xử phạt vi phạm hành chính hoặc bị truy cứu trách nhiệm hình sự, nếu gây thiệt hại thì phải bồi thường theo quy định của pháp luật về dân sự.
> 2. Trường hợp hệ thống trí tuệ nhân tạo có rủi ro cao được quản lý, vận hành và sử dụng đúng quy định nhưng vẫn phát sinh thiệt hại thì bên triển khai phải chịu trách nhiệm bồi thường cho người bị thiệt hại. Sau khi bồi thường, bên triển khai yêu cầu nhà cung cấp, nhà phát triển hoặc các bên liên quan hoàn trả khoản tiền bồi thường nếu có thỏa thuận giữa các bên.
> 3. Trách nhiệm bồi thường thiệt hại quy định tại khoản 2 Điều này được miễn trừ trong các trường hợp sau đây:
> a) Thiệt hại xảy ra hoàn toàn do lỗi cố ý của người bị thiệt hại;
> b) Thiệt hại xảy ra trong trường hợp bất khả kháng hoặc tình thế cấp thiết, trừ trường hợp pháp luật có quy định khác.
> 4. Trường hợp hệ thống trí tuệ nhân tạo bị bên thứ ba xâm nhập, chiếm quyền điều khiển hoặc can thiệp trái pháp luật thì bên thứ ba phải chịu trách nhiệm bồi thường thiệt hại. Trường hợp bên triển khai, nhà cung cấp có lỗi trong việc để hệ thống bị xâm nhập, chiếm quyền điều khiển hoặc can thiệp trái pháp luật thì phải liên đới bồi thường thiệt hại theo quy định của pháp luật về dân sự.
> 5. Chính phủ quy định chi tiết về xử phạt vi phạm hành chính đối với hành vi vi phạm do hệ thống trí tuệ nhân tạo gây ra.

### A14. Điều 33, 34, 35 — Bãi bỏ, hiệu lực, chuyển tiếp
> Điều 33. Bãi bỏ một số chương, điều, khoản, điểm của Luật Công nghiệp công nghệ số số 71/2025/QH15
> Bãi bỏ khoản 9 Điều 3, khoản 7 Điều 4, khoản 6 Điều 12, điểm đ khoản 2 Điều 34 và Chương IV của Luật Công nghiệp công nghệ số.
> Điều 34. Hiệu lực thi hành
> Luật này có hiệu lực thi hành từ ngày 01 tháng 3 năm 2026, trừ các nội dung liên quan quy định tại Điều 35 của Luật này.
> Điều 35. Điều khoản chuyển tiếp
> 1. Đối với các hệ thống trí tuệ nhân tạo đã được đưa vào hoạt động trước ngày Luật này có hiệu lực thi hành, nhà cung cấp và bên triển khai có trách nhiệm thực hiện các nghĩa vụ tuân thủ theo quy định của Luật này trong thời hạn sau đây:
> a) 18 tháng kể từ ngày Luật này có hiệu lực thi hành đối với hệ thống trí tuệ nhân tạo trong lĩnh vực y tế, giáo dục và tài chính;
> b) 12 tháng kể từ ngày Luật này có hiệu lực thi hành đối với các hệ thống trí tuệ nhân tạo không thuộc trường hợp quy định tại điểm a khoản này.
> 2. Trong thời hạn quy định tại khoản 1 Điều này, hệ thống trí tuệ nhân tạo được tiếp tục hoạt động, trừ trường hợp cơ quan quản lý nhà nước về trí tuệ nhân tạo xác định hệ thống có nguy cơ gây thiệt hại nghiêm trọng thì có quyền yêu cầu tạm dừng hoặc chấm dứt hoạt động.

Ghi chú: Điều 33 bãi bỏ Chương IV (Trí tuệ nhân tạo) của Luật Công nghiệp công nghệ số 71/2025/QH15 — trong đó có Điều 44 "dấu hiệu nhận dạng đối với hệ thống trí tuệ nhân tạo" (đã đọc tiêu đề và nội dung Chương IV trong bản Công báo Luật 71/2025). Tài liệu nào còn dẫn Luật 71/2025 Điều 41–45 cho nghĩa vụ AI là đã cũ từ 01/03/2026.

---

## B. Nghị định 142/2026/NĐ-CP (ban hành 30/04/2026, hiệu lực 01/05/2026)

Trang Công báo: https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-142-2026-nd-cp-469480.htm (Công báo số 278) — chữ trích từ tệp DOCX trên trang (file_name `2026_278_142/2026/NĐ-CP.docx`); PDF ký số: https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/18/469480-1778814202_v1_1779067280_signed.pdf. Bản PDF trên vanban.chinhphu.vn (docid=218029) là **ảnh quét** (pdftotext ra 273 byte) nên không dùng.

### B1. Điều 3 khoản 2 — Mã định danh
> 2. Mã định danh hệ thống trí tuệ nhân tạo là mã điện tử phục vụ quản lý hồ sơ được tạo lập tự động trên Cổng thông tin điện tử một cửa về trí tuệ nhân tạo khi nhà cung cấp thực hiện thông báo kết quả phân loại rủi ro.

### B2. Điều 4 khoản 1, 2 — Cổng một cửa, CSDL quốc gia về hệ thống AI (Bộ KH&CN)
> Điều 4. Cổng thông tin điện tử một cửa về trí tuệ nhân tạo và Cơ sở dữ liệu quốc gia về hệ thống trí tuệ nhân tạo
> 1. Bộ Khoa học và Công nghệ có trách nhiệm quản lý, vận hành Cổng thông tin điện tử một cửa về trí tuệ nhân tạo để thực hiện các nhiệm vụ sau đây:
> a) Tiếp nhận thông báo kết quả phân loại mức độ rủi ro, kết quả đánh giá sự phù hợp; xác lập mã định danh hệ thống trí tuệ nhân tạo; tiếp nhận thông tin cập nhật hồ sơ phân loại rủi ro và các thông tin khác về hệ thống trí tuệ nhân tạo theo quy định của Nghị định này;
> b) Tiếp nhận báo cáo sự cố, báo cáo định kỳ và các thông tin phục vụ công tác quản lý, giám sát hệ thống trí tuệ nhân tạo theo quy định của Nghị định này;
> c) Hỗ trợ phân loại rủi ro tự động hệ thống trí tuệ nhân tạo;
> d) Công khai thông tin về hệ thống trí tuệ nhân tạo, kết quả đánh giá sự phù hợp, danh sách các cụm liên kết trí tuệ nhân tạo được công nhận, kết quả xử lý vi phạm, thông tin về năng lực hạ tầng trí tuệ nhân tạo dùng chung, điều kiện truy cập, quy định kỹ thuật, phương thức và quy trình khai thác dữ liệu, các chương trình, cơ chế hỗ trợ;
> đ) Tiếp nhận yêu cầu hướng dẫn; tiếp nhận, đăng tải để lấy ý kiến, công khai báo cáo đánh giá tác động và phục vụ việc theo dõi, giám sát việc sử dụng hệ thống trí tuệ nhân tạo trong cơ quan nhà nước theo quy định của Nghị định này;
> e) Tiếp nhận đăng ký nhu cầu và phát hành thông báo về quyền khai thác hạ tầng phục vụ nghiên cứu, phát triển và đổi mới sáng tạo trên môi trường điện tử.
> 2. Bộ Khoa học và Công nghệ là chủ quản dữ liệu đối với Cơ sở dữ liệu quốc gia về hệ thống trí tuệ nhân tạo nhằm phục vụ công tác quản lý nhà nước, giám sát và tổng hợp thông tin về hệ thống trí tuệ nhân tạo.

### B3. Điều 5 khoản 2, 3, 8 — Nguyên tắc phân loại
> 2. Nhà cung cấp phải thực hiện phân loại hệ thống trí tuệ nhân tạo trước khi đưa hệ thống vào sử dụng.
> 3. Bên triển khai phải phối hợp với nhà cung cấp để rà soát, phân loại lại hệ thống trí tuệ nhân tạo khi việc triển khai, sửa đổi, tích hợp hoặc thay đổi chức năng hoặc mục đích sử dụng làm phát sinh rủi ro mới hoặc rủi ro cao hơn của hệ thống đã được phân loại.
> …
> 8. Bộ Khoa học và Công nghệ cung cấp công cụ hỗ trợ điện tử phục vụ việc tự đánh giá, phân loại hệ thống trí tuệ nhân tạo trên cơ sở các tiêu chí quy định tại Điều 8 của Nghị định này. Việc sử dụng công cụ hỗ trợ điện tử có tính chất hỗ trợ, không bắt buộc và không làm phát sinh thủ tục phê duyệt hành chính hoặc nghĩa vụ khác ngoài quy định của Nghị định này.

### B4. Điều 6 — Phân loại
> Điều 6. Phân loại hệ thống trí tuệ nhân tạo
> 1. Nhà cung cấp có trách nhiệm tự thực hiện việc phân loại hệ thống trí tuệ nhân tạo theo quy định tại khoản 1 Điều 10 của Luật Trí tuệ nhân tạo trước khi đưa hệ thống vào sử dụng và chịu trách nhiệm trước pháp luật về tính chính xác, trung thực của kết quả phân loại.
> 2. Việc phân loại quy định tại Điều này chỉ áp dụng đối với hệ thống trí tuệ nhân tạo; không áp dụng đối với mô hình trí tuệ nhân tạo, trừ trường hợp mô hình được sử dụng như một thành phần của hệ thống trí tuệ nhân tạo cụ thể.
> 3. Mức độ rủi ro của hệ thống trí tuệ nhân tạo được xác định như sau:
> a) Hệ thống trí tuệ nhân tạo được phân loại rủi ro cao là các hệ thống thuộc Danh mục hệ thống trí tuệ nhân tạo có rủi ro cao do Thủ tướng Chính phủ ban hành theo quy định tại khoản 4 Điều 13 của Luật Trí tuệ nhân tạo;
> b) Hệ thống trí tuệ nhân tạo được phân loại có rủi ro trung bình là hệ thống không thuộc trường hợp quy định tại điểm a khoản này và thuộc các trường hợp quy định tại Điều 9 của Nghị định này;
> c) Hệ thống trí tuệ nhân tạo được phân loại có rủi ro thấp là hệ thống không thuộc trường hợp quy định tại điểm a và điểm b khoản này.
> 4. Trường hợp bên triển khai sửa đổi, tích hợp, thay đổi chức năng hoặc mục đích sử dụng của hệ thống so với công bố ban đầu của nhà cung cấp làm phát sinh rủi ro mới hoặc rủi ro cao hơn, bên triển khai có trách nhiệm phối hợp với nhà cung cấp để rà soát, phân loại lại mức độ rủi ro.

### B5. Điều 8 — Tiêu chí Danh mục rủi ro cao và trường hợp loại trừ
> Điều 8. Tiêu chí và nguyên tắc xây dựng Danh mục hệ thống trí tuệ nhân tạo có rủi ro cao
> 1. Hệ thống trí tuệ nhân tạo được xác định là có rủi ro cao khi đáp ứng một hoặc nhiều tiêu chí sau đây:
> a) Mức độ tác động: Mức độ có thể gây thiệt hại đối với tính mạng, sức khỏe, tài sản, quyền con người, lợi ích quốc gia, lợi ích công cộng hoặc an ninh quốc gia; mức độ tự động của hệ thống; mức độ hỗ trợ ra quyết định cuối cùng; khả năng giám sát và can thiệp của con người trong thực thi hành động;
> b) Lĩnh vực sử dụng: Triển khai trong lĩnh vực thiết yếu quy định tại khoản 2 Điều 6 của Luật Trí tuệ nhân tạo hoặc các lĩnh vực liên quan trực tiếp đến lợi ích công cộng;
> c) Phạm vi người sử dụng và quy mô ảnh hưởng: Phạm vi người sử dụng, quy mô đối tượng chịu tác động hoặc mức độ kết nối với hệ thống hạ tầng kỹ thuật quan trọng.
> 2. Hệ thống trí tuệ nhân tạo mặc dù thuộc tiêu chí quy định tại khoản 1 Điều này nhưng không được đề xuất đưa vào Danh mục hệ thống trí tuệ nhân tạo có rủi ro cao khi đáp ứng một trong các tiêu chí sau đây:
> a) Chỉ thực hiện các tác vụ thu thập, xử lý, chuẩn hóa, phân loại, dịch thuật hoặc cải thiện chất lượng dữ liệu; không trực tiếp tạo lập quyết định làm ảnh hưởng đến quyền và lợi ích hợp pháp của tổ chức, cá nhân;
> b) Có cơ chế kỹ thuật và quy trình vận hành bảo đảm sự giám sát thực chất của con người, theo đó người có thẩm quyền có khả năng xem xét độc lập, can thiệp, từ chối hoặc thay đổi quyết định của hệ thống trước khi quyết định đó có hiệu lực;
> c) Chỉ sử dụng phục vụ hoạt động quản trị, vận hành nội bộ của tổ chức, doanh nghiệp; không trực tiếp tác động đến quyền, nghĩa vụ pháp lý hoặc lợi ích hợp pháp của tổ chức, cá nhân bên ngoài tổ chức;
> d) Chỉ thực hiện chức năng phân tích, dự báo, đánh giá, khuyến nghị mang tính tham khảo; nhà cung cấp và bên triển khai không được sử dụng kết quả đầu ra làm căn cứ duy nhất để ra quyết định cuối cùng.

### B6. Điều 9 — Rủi ro trung bình
> Điều 9. Phân loại hệ thống trí tuệ nhân tạo có rủi ro trung bình
> 1. Nhà cung cấp có trách nhiệm phân loại hệ thống trí tuệ nhân tạo vào nhóm rủi ro trung bình khi hệ thống đó đáp ứng đồng thời các điều kiện sau đây:
> a) Không thuộc Danh mục hệ thống trí tuệ nhân tạo có rủi ro cao do Thủ tướng Chính phủ ban hành theo quy định tại khoản 4 Điều 13 của Luật Trí tuệ nhân tạo;
> b) Có khả năng gây nhầm lẫn, tác động hoặc thao túng người sử dụng do người sử dụng không nhận biết được chủ thể tương tác là hệ thống trí tuệ nhân tạo hoặc nội dung do hệ thống tạo ra theo quy định tại điểm b khoản 1 Điều 9 của Luật Trí tuệ nhân tạo.
> 2. Bên triển khai áp dụng quy định tại khoản 1 Điều này để thực hiện phân loại lại hệ thống trí tuệ nhân tạo đối với trường hợp quy định tại khoản 2 Điều 10 của Luật Trí tuệ nhân tạo.
> 3. Nhà cung cấp, bên triển khai không phân loại hệ thống trí tuệ nhân tạo là hệ thống có rủi ro trung bình khi thuộc một trong các trường hợp sau đây:
> a) Hệ thống chỉ hỗ trợ chỉnh sửa kỹ thuật nhằm cải thiện hình thức nội dung, không tạo nội dung mới và không thay đổi danh tính của chủ thể;
> b) Hệ thống hỗ trợ công việc văn phòng mà người sử dụng có thể nhận biết rõ ràng bản chất chức năng là công cụ trí tuệ nhân tạo thông qua bối cảnh sử dụng và không có chức năng mô phỏng, giả lập có khả năng gây nhầm lẫn về danh tính, tính xác thực của sự kiện;
> c) Hệ thống không tương tác, cung cấp trực tiếp dịch vụ hoặc nội dung ra công chúng bao gồm cả trường hợp không phát hành ra công chúng thông qua bên thứ ba, nền tảng trung gian;
> d) Hệ thống được sử dụng trong hoạt động nghệ thuật, điện ảnh, trò chơi điện tử hoặc hoạt động sáng tạo khác; bối cảnh công bố thể hiện rõ nội dung mang tính hư cấu;
> đ) Hệ thống trí tuệ nhân tạo chỉ thực hiện xử lý, phân tích dữ liệu hoặc tối ưu vận hành trong hệ thống kỹ thuật; không tương tác trực tiếp với người sử dụng, không tạo nội dung cung cấp ra công chúng và không trực tiếp tương tác với môi trường vật lý như chức năng điều khiển chính của hệ thống.

### B7. Điều 11 khoản 1–4 — Rà soát, phân loại lại
> Điều 11. Rà soát và cập nhật mức độ rủi ro
> 1. Nhà cung cấp phải thực hiện rà soát và phân loại lại mức độ rủi ro của hệ thống trí tuệ nhân tạo khi phát sinh một trong các sự kiện pháp lý sau đây:
> a) Hệ thống có sự thay đổi đáng kể về chức năng, mục đích sử dụng hoặc ngữ cảnh triển khai làm ảnh hưởng đến tiêu chí phân loại rủi ro ban đầu của hệ thống;
> b) Hệ thống xảy ra sự cố nghiêm trọng chứng minh mức độ rủi ro thực tế cao hơn mức đã được phân loại;
> c) Có quyết định của Thủ tướng Chính phủ về việc sửa đổi, bổ sung Danh mục hệ thống trí tuệ nhân tạo có rủi ro cao làm thay đổi mức độ rủi ro của hệ thống;
> d) Có yêu cầu bằng văn bản của cơ quan quản lý nhà nước có thẩm quyền theo quy định tại khoản 6 Điều 10 của Luật Trí tuệ nhân tạo.
> 2. Bên triển khai phải phối hợp với nhà cung cấp thực hiện phân loại lại hệ thống trí tuệ nhân tạo trong trường hợp bên triển khai thực hiện sửa đổi, tích hợp hoặc thay đổi chức năng làm phát sinh rủi ro mới hoặc rủi ro cao hơn so với kết quả phân loại ban đầu của nhà cung cấp.
> 3. Việc thực hiện thông báo kết quả sau khi rà soát, phân loại lại được quy định như sau:
> a) Trường hợp kết quả phân loại lại xác định mức độ rủi ro của hệ thống cao hơn mức đã phân loại, nhà cung cấp, bên triển khai phải thực hiện thông báo kết quả phân loại lại cho cơ quan nhà nước có thẩm quyền trong thời hạn 15 ngày làm việc kể từ ngày hoàn thành việc rà soát và phải áp dụng ngay các biện pháp quản lý rủi ro tương ứng với mức độ rủi ro mới;
> b) Trường hợp kết quả phân loại lại xác định mức độ rủi ro của hệ thống thấp hơn mức đã phân loại, nhà cung cấp, bên triển khai có quyền thực hiện thông báo kết quả phân loại lại cho cơ quan nhà nước có thẩm quyền để được áp dụng chế độ quản lý tương ứng với mức độ rủi ro mới.
> 4. Nhà cung cấp, bên triển khai không phải thực hiện rà soát và thông báo phân loại lại khi tiến hành các hoạt động nâng cấp, tối ưu hóa hiệu suất, sửa lỗi kỹ thuật thông thường hoặc cập nhật dữ liệu định kỳ mà không làm thay đổi bản chất rủi ro của hệ thống.

### B8. Điều 12 — Hồ sơ phân loại rủi ro
> Điều 12. Hồ sơ phân loại rủi ro của hệ thống trí tuệ nhân tạo
> 1. Nhà cung cấp phải lập hồ sơ phân loại rủi ro đối với hệ thống trí tuệ nhân tạo có rủi ro cao và hệ thống trí tuệ nhân tạo có rủi ro trung bình trước khi đưa hệ thống vào sử dụng theo quy định tại khoản 1 Điều 10 của Luật Trí tuệ nhân tạo.
> 2. Đối với hệ thống trí tuệ nhân tạo có rủi ro cao và rủi ro trung bình, nhà cung cấp phải bảo đảm hồ sơ phân loại rủi ro bao gồm các tài liệu sau đây:
> a) Thông tin nhận diện hệ thống, bao gồm: tên hệ thống; phiên bản; mã định danh nội bộ hoặc mã định danh do cơ quan nhà nước có thẩm quyền cấp; tên, địa chỉ và thông tin liên hệ của nhà cung cấp;
> b) Mô tả hệ thống và bối cảnh sử dụng: mục đích sử dụng; chức năng chính; kiến trúc hệ thống ở mức chức năng, nghiệp vụ; phạm vi triển khai; nhóm người sử dụng và người bị ảnh hưởng;
> c) Thông tin về dữ liệu: Mô tả khái quát loại dữ liệu đầu vào chủ yếu được sử dụng để vận hành hệ thống;
> d) Nội dung quản lý rủi ro: Tóm tắt các biện pháp quản lý rủi ro, bảo đảm an toàn và tính minh bạch của hệ thống.
> 3. Trường hợp nhà cung cấp phát triển hệ thống trí tuệ nhân tạo dựa trên nền tảng, mô hình hoặc dịch vụ trí tuệ nhân tạo của bên thứ ba, nhà cung cấp chỉ phải cung cấp thông tin kỹ thuật và thông tin về dữ liệu trong phạm vi quyền tiếp cận và kiểm soát hợp pháp của mình.
> 4. Việc lập, cung cấp và quản lý hồ sơ phân loại rủi ro không bắt buộc nhà cung cấp phải tiết lộ mã nguồn, bộ tham số mô hình, thuật toán chi tiết, dữ liệu huấn luyện thô hoặc các thông tin thuộc danh mục bí mật nhà nước, bí mật kinh doanh, bí mật công nghệ theo quy định tại điểm e khoản 1 Điều 14 của Luật Trí tuệ nhân tạo, trừ trường hợp pháp luật có quy định khác.
> 5. Nhà cung cấp có quyền sử dụng tài liệu mô tả kỹ thuật mô hình hoặc tài liệu kỹ thuật tương đương được lập theo tiêu chuẩn quốc tế để đáp ứng các thành phần hồ sơ quy định tại khoản 2 và khoản 3 Điều này, với điều kiện các tài liệu đó đáp ứng đầy đủ các nội dung thông tin theo yêu cầu của Nghị định này.
> 6. Nhà cung cấp, bên triển khai có trách nhiệm lưu trữ hồ sơ phân loại trong suốt thời gian hệ thống hoạt động.
> 7. Trường hợp hệ thống trí tuệ nhân tạo có sử dụng dữ liệu cá nhân, nhà cung cấp được sử dụng Hồ sơ đánh giá tác động xử lý dữ liệu cá nhân theo quy định của pháp luật về bảo vệ dữ liệu cá nhân để thay thế hoặc tích hợp làm thành phần của Hồ sơ phân loại rủi ro, nhằm giảm thiểu chi phí tuân thủ hành chính.

### B9. Điều 13 khoản 2 — Phương thức đánh giá sự phù hợp
> 2. Nhà cung cấp phải thực hiện đánh giá sự phù hợp với yêu cầu của Điều 14 của Luật Trí tuệ nhân tạo theo các phương thức sau đây:
> a) Đối với hệ thống trí tuệ nhân tạo có rủi ro cao thuộc Danh mục hệ thống trí tuệ nhân tạo phải chứng nhận sự phù hợp trước khi đưa vào sử dụng, nhà cung cấp phải thực hiện đánh giá sự phù hợp thông qua tổ chức đánh giá sự phù hợp quy định tại khoản 4 Điều này;
> b) Đối với hệ thống trí tuệ nhân tạo có rủi ro cao không thuộc trường hợp quy định tại điểm a khoản này, nhà cung cấp có quyền tự thực hiện đánh giá sự phù hợp hoặc sử dụng dịch vụ của tổ chức đánh giá sự phù hợp quy định tại khoản 4 Điều này. Trường hợp tự thực hiện đánh giá sự phù hợp, nhà cung cấp phải lập hồ sơ kỹ thuật và chịu trách nhiệm trước pháp luật về kết quả đánh giá.

### B10. Điều 14 — Thông báo kết quả phân loại
> Điều 14. Thông báo kết quả phân loại rủi ro đối với hệ thống trí tuệ nhân tạo
> 1. Nhà cung cấp hệ thống trí tuệ nhân tạo có rủi ro trung bình và hệ thống trí tuệ nhân tạo có rủi ro cao phải thông báo kết quả phân loại rủi ro cho Bộ Khoa học và Công nghệ thông qua Cổng thông tin điện tử một cửa về trí tuệ nhân tạo trước khi đưa hệ thống vào sử dụng. Nhà cung cấp tự kê khai, tự chịu trách nhiệm trước pháp luật về nội dung thông báo.
> 2. Nhà cung cấp phải bảo đảm nội dung thông báo kết quả phân loại rủi ro tuân thủ theo quy định tại Điều 12 của Nghị định này.
> 3. Nhà cung cấp thực hiện thông báo bằng phương thức điện tử trên Cổng thông tin điện tử một cửa về trí tuệ nhân tạo theo một trong các hình thức sau đây:
> a) Kê khai trực tiếp theo biểu mẫu điện tử trên Cổng thông tin điện tử một cửa về trí tuệ nhân tạo;
> b) Gửi thông tin tự động thông qua giao diện lập trình ứng dụng hoặc phương thức điện tử phù hợp khác theo quy định của pháp luật.
> 4. Bộ Khoa học và Công nghệ thông qua Cổng thông tin điện tử một cửa về trí tuệ nhân tạo tự động ghi nhận thông tin, cấp mã định danh hệ thống trí tuệ nhân tạo và gửi xác nhận điện tử cho nhà cung cấp ngay sau khi nhà cung cấp hoàn tất việc gửi thông báo. Trong quá trình tiếp nhận thông báo, cơ quan nhà nước có thẩm quyền không được yêu cầu nhà cung cấp nộp thêm tài liệu hoặc bổ sung thành phần thông tin ngoài nội dung quy định tại khoản 2 Điều này. Cơ quan nhà nước có thẩm quyền thực hiện thanh tra, kiểm tra và hậu kiểm theo quy định của pháp luật.

### B11. Điều 15 khoản 4–6 — Bên triển khai hệ thống rủi ro cao
> 4. Bên triển khai hệ thống trí tuệ nhân tạo có rủi ro cao phải tổ chức quản lý rủi ro trong quá trình triển khai và vận hành hệ thống phù hợp với mục đích sử dụng, phạm vi triển khai, mức độ rủi ro của hệ thống và hướng dẫn kỹ thuật của nhà cung cấp.
> 5. Trong quá trình triển khai và vận hành, bên triển khai thực hiện các biện pháp quản lý rủi ro sau đây:
> a) Vận hành hệ thống đúng mục đích sử dụng, điều kiện sử dụng và giới hạn sử dụng do nhà cung cấp xác định;
> b) Tổ chức giám sát hoạt động của hệ thống nhằm phát hiện sai lệch, rủi ro hoặc sự cố có thể phát sinh;
> c) Thiết lập và duy trì cơ chế giám sát và can thiệp của con người trong quá trình sử dụng hệ thống theo quy định của pháp luật;
> d) Áp dụng biện pháp hạn chế hoặc kiểm soát rủi ro trong phạm vi quyền kiểm soát của mình khi phát hiện hệ thống hoạt động không đúng mục đích sử dụng hoặc phát sinh rủi ro mới;
> đ) Phối hợp với nhà cung cấp trong việc rà soát, cập nhật biện pháp quản lý rủi ro khi hệ thống có thay đổi đáng kể hoặc khi phát sinh sự cố.
> 6. Trường hợp phát hiện hệ thống có nguy cơ gây thiệt hại nghiêm trọng đến tính mạng, sức khỏe con người, quyền con người, tài sản, an ninh mạng, trật tự, an toàn xã hội hoặc lợi ích công cộng, bên triển khai phải kịp thời áp dụng biện pháp hạn chế rủi ro trong phạm vi quyền kiểm soát của mình và thông báo cho nhà cung cấp và cơ quan nhà nước có thẩm quyền theo quy định của pháp luật.

### B12. Điều 16 — Nguyên tắc minh bạch và giải trình
> Điều 16. Nguyên tắc minh bạch và giải trình
> 1. Nhà cung cấp và bên triển khai hệ thống trí tuệ nhân tạo phải thực hiện trách nhiệm minh bạch, thông báo, đánh dấu kỹ thuật và gắn nhãn hiển thị đối với hệ thống trí tuệ nhân tạo và nội dung do hệ thống tạo ra theo quy định tại Điều 11 của Luật Trí tuệ nhân tạo. Việc thực hiện trách nhiệm minh bạch phải phù hợp với mục đích sử dụng, bối cảnh triển khai và mức độ rủi ro của hệ thống.
> 2. Nhà cung cấp và bên triển khai phải thực hiện các nghĩa vụ sau đây:
> a) Thông báo, đánh dấu kỹ thuật và gắn nhãn hiển thị đối với hệ thống trí tuệ nhân tạo và nội dung do hệ thống tạo ra theo quy định của pháp luật;
> b) Cung cấp thông tin về mục đích sử dụng, phạm vi áp dụng, điều kiện sử dụng và các hạn chế của hệ thống trí tuệ nhân tạo;
> c) Lưu trữ thông tin, tài liệu phục vụ việc kiểm tra, giám sát theo quy định của pháp luật.
> 3. Nhà cung cấp và bên triển khai phải giải trình khi có yêu cầu bằng văn bản của cơ quan nhà nước có thẩm quyền theo quy định tại Điều 14 và Điều 15 của Luật Trí tuệ nhân tạo. Phạm vi, nội dung và thời hạn giải trình phải phù hợp với địa vị pháp lý của từng chủ thể và mức độ rủi ro của hệ thống.
> 4. Khi thực hiện trách nhiệm giải trình và cung cấp thông tin theo quy định của pháp luật, nhà cung cấp và bên triển khai không bắt buộc phải tiết lộ mã nguồn, thuật toán chi tiết, dữ liệu huấn luyện, bộ tham số hoặc thông tin thuộc phạm vi bí mật kinh doanh, bí mật công nghệ, trừ trường hợp pháp luật có quy định khác.
> 5. Việc cung cấp thông tin trong quá trình minh bạch, giải trình phải tuân thủ pháp luật về bảo vệ dữ liệu cá nhân và pháp luật về dữ liệu.
> 6. Trường hợp hệ thống trí tuệ nhân tạo tích hợp mô hình trí tuệ nhân tạo của tổ chức, cá nhân khác, nhà cung cấp phải thỏa thuận với tổ chức, cá nhân cung cấp mô hình để bảo đảm việc phối hợp cung cấp thông tin kỹ thuật cần thiết phục vụ việc thực hiện trách nhiệm minh bạch và giải trình theo quy định của pháp luật.

### B13. Điều 17 — Đánh dấu kỹ thuật (định dạng máy đọc)
> Điều 17. Đánh dấu kỹ thuật đối với nội dung do hệ thống trí tuệ nhân tạo tạo ra
> 1. Nhà cung cấp hệ thống trí tuệ nhân tạo phải áp dụng giải pháp kỹ thuật để nội dung đầu ra là âm thanh, hình ảnh hoặc video được đánh dấu ở định dạng máy đọc theo quy định tại khoản 2 Điều 11 của Luật Trí tuệ nhân tạo. Nhà cung cấp không bắt buộc phải thực hiện đánh dấu kỹ thuật ở định dạng máy đọc đối với nội dung đầu ra là văn bản, trừ trường hợp pháp luật có quy định khác.
> 2. Việc đánh dấu kỹ thuật quy định tại khoản 1 Điều này phải bảo đảm khả năng nhận diện bằng máy đọc và có thể được thực hiện bằng một trong các biện pháp sau đây:
> a) Tích hợp dấu hiệu nhận biết vào cấu trúc tệp tin hoặc dữ liệu nội dung;
> b) Tích hợp dấu hiệu nhận biết vào siêu dữ liệu của tệp tin;
> c) Sử dụng chữ ký số, chữ ký điện tử hoặc phương thức xác thực kỹ thuật tương đương;
> d) Áp dụng giải pháp kỹ thuật khác bảo đảm khả năng nhận diện nội dung được tạo ra hoặc chỉnh sửa bằng hệ thống trí tuệ nhân tạo.
> 3. Dấu hiệu nhận biết ở định dạng máy đọc phải thể hiện thông tin xác nhận nội dung được tạo ra hoặc chỉnh sửa bằng hệ thống trí tuệ nhân tạo. Nhà cung cấp có thể tích hợp thêm thông tin về nhà cung cấp, hệ thống trí tuệ nhân tạo hoặc thời điểm tạo, chỉnh sửa nội dung nếu giải pháp kỹ thuật cho phép, nhằm phục vụ việc xác thực nguồn gốc và truy vết nội dung.
> 4. Nhà cung cấp phải bảo đảm chức năng đánh dấu kỹ thuật được duy trì trong quá trình tạo, xuất và cung cấp nội dung trong phạm vi các chức năng do hệ thống kiểm soát.
> 5. Trường hợp hệ thống trí tuệ nhân tạo được cung cấp dưới dạng mã nguồn mở hoặc cung cấp miễn phí, nhà cung cấp được coi là đã thực hiện nghĩa vụ quy định tại khoản 1 Điều này khi:
> a) Tích hợp sẵn chức năng đánh dấu kỹ thuật; hoặc
> b) Công bố công khai công cụ, cấu hình tiêu chuẩn, giao diện lập trình ứng dụng hoặc tài liệu kỹ thuật cho phép bên triển khai cấu hình và vận hành chức năng đánh dấu.
> Bên triển khai khi sử dụng hệ thống này để cung cấp nội dung ra công cộng phải áp dụng giải pháp kỹ thuật để thực hiện việc đánh dấu nội dung đầu ra.
> 6. Bộ Khoa học và Công nghệ công bố và cập nhật danh mục tiêu chuẩn, quy chuẩn kỹ thuật hoặc hướng dẫn kỹ thuật tham chiếu phục vụ việc thực hiện đánh dấu kỹ thuật quy định tại Điều này. Việc công bố quy định tại khoản này không làm phát sinh thủ tục hành chính, điều kiện đầu tư kinh doanh hoặc nghĩa vụ ngoài quy định của Nghị định này.

### B14. Điều 18 — Thông báo và gắn nhãn hiển thị
> Điều 18. Thông báo và gắn nhãn hiển thị đối với nội dung do hệ thống trí tuệ nhân tạo tạo ra
> 1. Bên triển khai phải thông báo rõ ràng khi cung cấp ra công cộng nội dung do hệ thống trí tuệ nhân tạo tạo ra hoặc chỉnh sửa có khả năng gây nhầm lẫn về tính xác thực của sự kiện, nhân vật hoặc nguồn gốc nội dung theo quy định tại khoản 3 Điều 11 của Luật Trí tuệ nhân tạo.
> 2. Bên triển khai phải gắn nhãn dễ nhận biết đối với âm thanh, hình ảnh hoặc video được tạo ra hoặc chỉnh sửa bằng hệ thống trí tuệ nhân tạo trong các trường hợp sau đây:
> a) Mô phỏng hoặc giả lập ngoại hình, giọng nói của người thật;
> b) Tái hiện sự kiện thực tế để phân biệt với nội dung thật, trừ trường hợp pháp luật có quy định khác.
> 3. Việc thông báo và gắn nhãn hiển thị phải bảo đảm các yêu cầu sau đây:
> a) Rõ ràng, dễ hiểu và dễ nhận biết đối với người tiếp nhận;
> b) Được thực hiện trước hoặc tại thời điểm người tiếp nhận tiếp cận nội dung;
> c) Không được thiết kế theo cách che giấu hoặc làm giảm khả năng nhận biết bản chất của nội dung;
> d) Phù hợp với loại hình nội dung và phương thức cung cấp nội dung;
> đ) Không gây cản trở đáng kể việc hiển thị, trình diễn hoặc sử dụng nội dung.
> 4. Bên triển khai không phải thực hiện nghĩa vụ gắn nhãn hiển thị trong các trường hợp sau đây:
> a) Nội dung được chỉnh sửa kỹ thuật nhằm cải thiện chất lượng âm thanh, hình ảnh hoặc video mà không làm thay đổi bản chất hoặc ngữ cảnh chính của nội dung;
> b) Văn bản được xử lý bằng công cụ hỗ trợ sửa lỗi chính tả, ngữ pháp, tóm tắt, diễn giải hoặc dịch thuật mà không làm sai lệch nội dung cơ bản của văn bản gốc;
> c) Nội dung được sử dụng trong phạm vi nội bộ của cơ quan, tổ chức, doanh nghiệp và không được cung cấp ra công cộng;
> d) Nội dung được tạo ra trong quá trình nghiên cứu, phát triển hoặc thử nghiệm trong môi trường kiểm soát và không được cung cấp ra công cộng.
> 5. Bên triển khai có quyền lựa chọn hình thức thể hiện thông báo và nhãn hiển thị phù hợp với loại hình nội dung và phương thức cung cấp, bao gồm:
> a) Hiển thị trực tiếp trên nội dung;
> b) Hiển thị tại tiêu đề, phần mô tả hoặc chú thích kèm theo nội dung;
> c) Hiển thị trên giao diện của nền tảng cung cấp nội dung;
> d) Phát thông báo bằng âm thanh hoặc hình thức phù hợp khác.
> 6. Đối với tác phẩm điện ảnh, chương trình nghệ thuật hoặc nội dung sáng tạo, việc thông báo và gắn nhãn hiển thị do bên triển khai trực tiếp đưa nội dung ra công cộng thực hiện và có thể được thực hiện tại phần mở đầu, phần kết thúc, phần danh đề, phần mô tả hoặc tài liệu kèm theo tác phẩm, phù hợp với đặc thù của từng loại hình. Việc thông báo và gắn nhãn phải bảo đảm người tiếp nhận có thể nhận biết rõ ràng nội dung được tạo ra hoặc được chỉnh sửa bằng hệ thống trí tuệ nhân tạo, không gây nhầm lẫn về nguồn gốc của nội dung.
> Trường hợp nội dung do hệ thống trí tuệ nhân tạo tạo ra hoặc chỉnh sửa trong quá trình sản xuất, bên thực hiện việc tạo ra hoặc chỉnh sửa nội dung có trách nhiệm cung cấp thông tin cần thiết để thực hiện nghĩa vụ quy định tại khoản này; bên trực tiếp đưa nội dung ra công cộng thực hiện nghĩa vụ trên cơ sở thông tin được cung cấp.
> 7. Bộ Khoa học và Công nghệ công bố và cập nhật hướng dẫn kỹ thuật tham chiếu về hình thức thông báo và gắn nhãn hiển thị quy định tại Điều này. Việc công bố quy định tại khoản này không làm phát sinh thủ tục hành chính, điều kiện đầu tư kinh doanh hoặc nghĩa vụ ngoài quy định của Nghị định này.

### B15. Điều 19 — Báo cáo, xử lý sự cố nghiêm trọng
> Điều 19. Báo cáo và xử lý sự cố nghiêm trọng
> 1. Sự cố nghiêm trọng của hệ thống trí tuệ nhân tạo theo quy định tại khoản 8 Điều 3 của Luật Trí tuệ nhân tạo là sự kiện xảy ra trong hoạt động của hệ thống trí tuệ nhân tạo gây ra một trong các hậu quả sau đây:
> a) Thiệt hại về tính mạng hoặc tổn hại nghiêm trọng đến sức khỏe của con người;
> b) Thiệt hại đáng kể về tài sản hoặc ảnh hưởng nghiêm trọng đến hoạt động của tổ chức;
> c) Xâm phạm nghiêm trọng quyền con người, quyền và lợi ích hợp pháp của cơ quan, tổ chức, cá nhân;
> d) Gây gián đoạn nghiêm trọng việc cung cấp dịch vụ công, dịch vụ thiết yếu theo quy định của pháp luật hoặc ảnh hưởng đến an ninh quốc gia, trật tự, an toàn xã hội.
> 2. Khi xảy ra sự cố nghiêm trọng của hệ thống trí tuệ nhân tạo, các chủ thể có trách nhiệm sau đây:
> a) Bên triển khai và người sử dụng phải kịp thời ghi nhận sự cố, thực hiện các biện pháp cần thiết để hạn chế hậu quả và thông báo cho nhà cung cấp để phối hợp khắc phục;
> b) Nhà cung cấp phải áp dụng các biện pháp kỹ thuật cần thiết để ngăn chặn, hạn chế và khắc phục hậu quả của sự cố;
> c) Nhà cung cấp và bên triển khai có trách nhiệm phối hợp cung cấp thông tin và thực hiện các biện pháp cần thiết để xử lý sự cố theo quy định của pháp luật.
> 3. Nhà cung cấp hoặc bên triển khai phải báo cáo sơ bộ sự cố nghiêm trọng cho cơ quan nhà nước có thẩm quyền theo Mẫu AI01a đối với tổ chức hoặc Mẫu AI01b đối với cá nhân tại Phụ lục ban hành kèm theo Nghị định này thông qua Cổng thông tin điện tử một cửa về trí tuệ nhân tạo trong thời hạn như sau:
> a) Đối với các sự cố nghiêm trọng có tính khẩn cấp quy định tại điểm a, điểm d khoản 1 Điều này và trường hợp không thể kiểm soát đối với quy định tại điểm c khoản 1 Điều này: thực hiện báo cáo sơ bộ trong thời hạn 72 giờ kể từ thời điểm xác nhận sự cố;
> b) Đối với các sự cố nghiêm trọng còn lại: thực hiện báo cáo sơ bộ trong thời hạn 05 ngày làm việc kể từ thời điểm xác nhận sự cố;
> c) Thời điểm xác nhận sự cố quy định tại khoản này được tính từ khi tổ chức, cá nhân có đủ cơ sở thông tin ban đầu để xác định sự cố đã thực sự xảy ra và có khả năng cao bắt nguồn từ lỗi của hệ thống trí tuệ nhân tạo, không đợi đến khi hoàn thành điều tra toàn diện nguyên nhân kỹ thuật. Việc nộp báo cáo sơ bộ trong thời hạn quy định không bị coi là sự thừa nhận lỗi kỹ thuật hoặc trách nhiệm pháp lý của tổ chức, cá nhân báo cáo.
> Trường hợp bên triển khai không thể liên lạc với nhà cung cấp, bên triển khai có trách nhiệm thực hiện việc báo cáo theo quy định tại khoản này.
> 4. Nhà cung cấp và bên triển khai phải duy trì, lưu giữ nhật ký hệ thống, dữ liệu và thông tin liên quan đến sự cố để phục vụ việc xác minh, đánh giá và khắc phục sự cố; đồng thời gửi báo cáo chính thức về kết quả khắc phục sự cố cho cơ quan nhà nước có thẩm quyền trong thời hạn 15 ngày kể từ ngày nộp báo cáo sơ bộ.
> 5. Trường hợp sự cố nghiêm trọng đồng thời thuộc trường hợp phải báo cáo theo quy định của pháp luật về an ninh mạng, bảo vệ dữ liệu cá nhân hoặc pháp luật chuyên ngành khác, việc báo cáo được thực hiện theo quy định của pháp luật đó.
> Cơ quan nhà nước có thẩm quyền có trách nhiệm phối hợp, chia sẻ thông tin và không yêu cầu cung cấp lại thông tin, tài liệu đã có trong hệ thống thông tin hoặc cơ sở dữ liệu được kết nối, chia sẻ theo quy định của pháp luật, các hệ thống trí tuệ nhân tạo, cơ sở dữ liệu quy định tại điểm d khoản 3 Điều 4 Nghị định này.
> 6. Cơ quan nhà nước có thẩm quyền tiếp nhận báo cáo, tổ chức xác minh và hướng dẫn xử lý sự cố nghiêm trọng; khi cần thiết, có quyền yêu cầu tạm dừng hoạt động, thu hồi hoặc đánh giá lại hệ thống trí tuệ nhân tạo theo quy định tại khoản 2 Điều 12 của Luật Trí tuệ nhân tạo.
> 7. Trường hợp sự cố có dấu hiệu ảnh hưởng đến an ninh quốc gia, trật tự, an toàn xã hội hoặc có dấu hiệu vi phạm pháp luật hình sự, Bộ Khoa học và Công nghệ phối hợp với Bộ Công an và các cơ quan có liên quan để thực hiện việc xác minh và xử lý theo quy định của pháp luật.
> 8. Việc báo cáo và tiếp nhận báo cáo sự cố nghiêm trọng được thực hiện thông qua Cổng thông tin điện tử một cửa về trí tuệ nhân tạo.

### B16. Điều 32 khoản 2 — CSDL quốc gia về trí tuệ nhân tạo (Bộ Công an)
> 2. Bộ Công an là cơ quan chủ quản Cơ sở dữ liệu quốc gia về trí tuệ nhân tạo, có trách nhiệm sau đây:
> a) Chịu trách nhiệm xây dựng, quản lý, vận hành Cơ sở dữ liệu quốc gia về trí tuệ nhân tạo tại Trung tâm dữ liệu quốc gia;

Ghi chú: có HAI cơ sở dữ liệu tên gần giống nhau — "Cơ sở dữ liệu quốc gia về **hệ thống** trí tuệ nhân tạo" (Bộ KH&CN chủ quản, nơi ghi nhận hệ thống đã thông báo — Điều 4 khoản 2) và "Cơ sở dữ liệu quốc gia về trí tuệ nhân tạo" (Bộ Công an chủ quản, dữ liệu phục vụ huấn luyện — Điều 32 khoản 2). App chỉ "đăng ký" với cái thứ nhất, qua thủ tục thông báo ở B10.

### B17. Điều 45, 46 — Hiệu lực, chuyển tiếp
> Điều 45. Hiệu lực thi hành
> Nghị định này có hiệu lực thi hành từ ngày 01 tháng 5 năm 2026.
> Điều 46. Điều khoản chuyển tiếp
> 1. Trường hợp Cổng thông tin điện tử một cửa về trí tuệ nhân tạo chưa được Bộ Khoa học và Công nghệ công bố vận hành chính thức, việc thực hiện các thủ tục thông báo, báo cáo theo quy định của Nghị định này được thực hiện thông qua hệ thống thông tin điện tử, dịch vụ công trực tuyến hoặc phương thức tiếp nhận do Bộ Khoa học và Công nghệ công bố, bảo đảm thống nhất trên phạm vi toàn quốc.
> Việc thực hiện thông báo, báo cáo theo phương thức quy định tại khoản này có giá trị pháp lý tương đương với việc thực hiện thông qua Cổng thông tin điện tử một cửa về trí tuệ nhân tạo.
> 2. Trong thời gian quy định tại khoản 1 Điều này, việc công khai thông tin theo quy định của Nghị định này được thực hiện trên cổng thông tin điện tử hoặc trang thông tin điện tử chính thức của cơ quan, tổ chức, đơn vị có trách nhiệm công khai theo quy định của Nghị định này, trừ trường hợp pháp luật có quy định khác.
> 3. Hồ sơ, thông tin đã được tiếp nhận trước thời điểm quy định tại khoản 3 Điều này tiếp tục được xử lý theo quy định tại thời điểm tiếp nhận./.

Ghi chú: Điều 46 khoản 3 viết "trước thời điểm quy định tại khoản 3 Điều này" (tự dẫn chính nó) — nhiều khả năng ý là thời điểm Cổng một cửa vận hành chính thức ở khoản 1; nguyên văn như trên.

Mẫu biểu (Phụ lục, chỉ chép tên): AI01a/AI01b báo cáo sự cố nghiêm trọng (tổ chức/cá nhân); AI02 đánh giá tác động trong cơ quan nhà nước; AI03a–d đơn tham gia/gia hạn thử nghiệm có kiểm soát; AI04 giấy xác nhận hoàn thành thử nghiệm; AI05a/b báo cáo định kỳ thử nghiệm; AI06a/b sự cố trong thử nghiệm; AI07a/b vượt giới hạn thử nghiệm; AI08a/b tổng kết thử nghiệm; AI09a/b giấy xác nhận tham gia thử nghiệm. **Không có mẫu riêng cho thông báo phân loại rủi ro** — thông báo theo biểu mẫu điện tử trên Cổng (Điều 14 khoản 3).

Phần đã đọc lướt, không trích: Chương IV (thử nghiệm có kiểm soát, Điều 21–27 — tự nguyện), Chương V–VI (hạ tầng, dữ liệu, hệ sinh thái, phiếu hỗ trợ, Điều 28–40), Điều 20 (chỉ cho cơ quan nhà nước), Chương VII (trách nhiệm cơ quan nhà nước). Đã grep các chương này với "bên triển khai", "nhãn", "giáo dục", "trẻ em", "xử phạt": không thấy nghĩa vụ mới cho app tư nhân ngoài thử nghiệm tự nguyện.

---

## C. Quyết định 33/2026/QĐ-TTg — Danh mục hệ thống AI có rủi ro cao (ban hành 30/06/2026, hiệu lực 15/08/2026)

Trang Công báo: https://congbao.chinhphu.vn/van-ban/quyet-dinh-so-33-2026-qd-ttg-469951/66726.htm (Công báo số 395) — chữ trích từ DOCX trên trang; PDF: https://congbaocdn.chinhphu.vn/180507251028987904/2026/7/14/469951-1784024086_v1_1784024564_signed.pdf

### C1. Điều 1–4
> Điều 1. Phạm vi điều chỉnh
> 1. Ban hành kèm theo Quyết định này “Danh mục hệ thống trí tuệ nhân tạo có rủi ro cao” (Phụ lục kèm theo Quyết định này).
> 2. Hệ thống trí tuệ nhân tạo phải đáp ứng các nguyên tắc hoạt động cơ bản theo quy định của pháp luật về trí tuệ nhân tạo; việc sử dụng hệ thống trí tuệ nhân tạo không làm thay đổi, chuyển giao hoặc loại trừ thẩm quyền, trách nhiệm của cơ quan, tổ chức, cá nhân có thẩm quyền theo quy định của pháp luật; bảo đảm sự giám sát, kiểm soát và khả năng can thiệp của con người trong quá trình vận hành hệ thống; không thực hiện các hành vi bị nghiêm cấm theo quy định của pháp luật.
> Điều 2. Tiêu chí xác định hệ thống trí tuệ nhân tạo rủi ro cao
> Các hệ thống trí tuệ nhân tạo được xác định là có rủi ro cao căn cứ trên các tiêu chí sau đây:
> 1. Hệ thống có thể gây thiệt hại đáng kể đến tính mạng, sức khỏe, quyền và lợi ích hợp pháp của tổ chức, cá nhân, lợi ích quốc gia, lợi ích công cộng, an ninh quốc gia theo quy định tại Điều 9 Luật Trí tuệ nhân tạo; khoản 1 Điều 8 của Nghị định số 142/2026/NĐ-CP quy định chi tiết một số điều và biện pháp thi hành Luật Trí tuệ nhân tạo.
> 2. Hệ thống không được loại trừ theo quy định tại khoản 2 Điều 8 của Nghị định số 142/2026/NĐ-CP quy định chi tiết một số điều và biện pháp thi hành Luật Trí tuệ nhân tạo.
> Điều 3. Hiệu lực và trách nhiệm thi hành
> 1. Quyết định này có hiệu lực thi hành từ ngày 15 tháng 8 năm 2026.
> 2. Các Bộ trưởng, Thủ trưởng cơ quan ngang bộ, Chủ tịch Ủy ban nhân dân các tỉnh, thành phố trực thuộc trung ương và Thủ trưởng các cơ quan, tổ chức, cá nhân có liên quan chịu trách nhiệm thi hành Quyết định này.
> Điều 4. Điều khoản chuyển tiếp
> 1. Đối với các hệ thống trí tuệ nhân tạo thuộc Danh mục ban hành kèm theo Quyết định này đã được đưa vào hoạt động trước ngày Quyết định này có hiệu lực, nhà cung cấp và bên triển khai có trách nhiệm hoàn thành các nghĩa vụ tuân thủ theo quy định của pháp luật về trí tuệ nhân tạo theo lộ trình sau:
> a) Trước ngày 01 tháng 9 năm 2027 đối với các hệ thống trí tuệ nhân tạo trong lĩnh vực y tế, giáo dục và tài chính;
> b) Trước ngày 01 tháng 3 năm 2027 đối với các hệ thống trí tuệ nhân tạo thuộc các lĩnh vực còn lại trong Danh mục.
> 2. Trong thời hạn chuyển tiếp quy định tại khoản 1 Điều này, các hệ thống trí tuệ nhân tạo nêu trên được phép tiếp tục hoạt động, trừ trường hợp cơ quan nhà nước có thẩm quyền xác định hệ thống có nguy cơ gây thiệt hại nghiêm trọng và yêu cầu tạm dừng hoặc chấm dứt hoạt động theo quy định tại khoản 2 Điều 35 Luật Trí tuệ nhân tạo.
> 3. Đối với các hệ thống trí tuệ nhân tạo được đưa vào hoạt động trong thời gian 06 tháng kể từ ngày Quyết định này có hiệu lực, nhà cung cấp và bên triển khai có trách nhiệm hoàn thành các nghĩa vụ tuân thủ theo quy định của pháp luật về trí tuệ nhân tạo trước ngày 01 tháng 3 năm 2027.

### C2. Phụ lục — mục I. Lĩnh vực giáo dục (nguyên văn 3 dòng)
> I
> Lĩnh vực giáo dục
> 1
> Hệ thống trí tuệ nhân tạo cung cấp nội dung tự học theo chương trình giáo dục, có sử dụng các nguồn dữ liệu không kiểm soát
> Chỉ áp dụng khi hệ thống trí tuệ nhân tạo:
> - Cung cấp nội dung tự động phục vụ hoạt động tự học của người học theo chương trình giáo dục;
> - Dữ liệu nội dung học tập được đưa vào không có kiểm soát;
> - Được triển khai trên quy mô lớn có khả năng tạo ra rủi ro mang tính hệ thống hoặc tác động trên diện rộng tới người học.
> …
> 2
> Hệ thống có sử dụng AI tự động kiểm tra, đánh giá kết quả, xếp hạng người học
> Chỉ áp dụng khi hệ thống trí tuệ nhân tạo:
> - Được sử dụng để thực hiện việc kiểm tra, đánh giá người học một cách tự động;
> - Kết quả do hệ thống tạo ra được sử dụng làm căn cứ chính thức để đánh giá kết quả học tập, đánh giá năng lực hoặc xếp hạng người học;
> - Việc đánh giá được thực hiện trong hệ thống giáo dục quốc dân.
> …
> 3
> Hệ thống có sử dụng AI để giám sát, phân tích hành vi người học
> Chỉ áp dụng khi hệ thống AI giám sát, phân tích hành vi người học:
> Sử dụng dữ liệu sinh trắc học (nhận diện khuôn mặt, ánh mắt, hành vi, cảm xúc cá nhân) hoặc thiết lập các cơ chế phản hồi, cảnh báo tự động tần suất cao về trạng thái chú ý, biểu cảm cá nhân, kết quả học tập, đánh giá người học gây căng thẳng tâm lý hoặc xâm phạm quyền riêng tư của người học trong quá trình học tập.

Ghi chú: bảng có 2 cột "Đánh giá sự phù hợp": "Theo quy định tại điểm b, khoản 2 Điều 13, Luật Trí tuệ nhân tạo" (tự đánh giá hoặc thuê tổ chức) và "… điểm a …" (phải chứng nhận qua tổ chức đánh giá). Đọc cấu trúc bảng trong DOCX: cả 3 hệ thống giáo dục đánh dấu ở cột **điểm b**. Đếm toàn phụ lục: giáo dục 3 · dân tộc và tôn giáo 7 · y tế 2 · ngân hàng 2 · tố tụng 1 · giao thông vận tải 31 = 46 dòng. Không có dòng nào cho chatbot chung, tạo ảnh/giọng, gợi ý nội dung thương mại.

---

## D. Luật An ninh mạng 116/2025/QH15 (ban hành 10/12/2025, hiệu lực 01/07/2026)

Trang Công báo: https://congbao.chinhphu.vn/van-ban/luat-so-116-2025-qh15-468678.htm — chữ trích từ DOCX trên trang.

### D1. Điều 7 khoản 2 điểm g
> Điều 7. Các hành vi bị nghiêm cấm về an ninh mạng
> …
> 2. Thực hiện hành vi sau trên không gian mạng:
> …
> g) Sử dụng trí tuệ nhân tạo hoặc công nghệ mới để giả mạo video, hình ảnh, giọng nói của người khác trái quy định của pháp luật; tạo lập, đăng tải, phát tán thông tin quy định tại khoản 1 Điều này;

### D2. Điều 13 khoản 3 điểm h
> Điều 13. Các thông tin và hành vi sử dụng công nghệ thông tin, phương tiện điện tử xâm phạm an ninh quốc gia, trật tự, an toàn xã hội trên không gian mạng
> …
> 3. Thông tin có nội dung xâm phạm quyền, lợi ích hợp pháp của tổ chức, cá nhân bao gồm:
> …
> h) Mạo danh, giả mạo thông tin, hình ảnh, giọng nói của cá nhân, gây ảnh hưởng đến uy tín, danh dự, nhân phẩm của cá nhân.

---

## E. Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 — Điều 30 (liên hệ mảng 1)

Trang Công báo: https://congbao.chinhphu.vn/van-ban/luat-so-91-2025-qh15-45578.htm (bản chữ đã trích ở đợt đối chiếu mảng 1).

> Điều 30. Bảo vệ dữ liệu cá nhân trong xử lý dữ liệu lớn, trí tuệ nhân tạo, chuỗi khối, vũ trụ ảo, điện toán đám mây
> 1. Dữ liệu cá nhân trong môi trường dữ liệu lớn, trí tuệ nhân tạo, chuỗi khối, vũ trụ ảo và điện toán đám mây phải được xử lý đúng mục đích và giới hạn trong phạm vi cần thiết, bảo đảm quyền, lợi ích hợp pháp của chủ thể dữ liệu cá nhân.
> 2. Việc xử lý dữ liệu cá nhân trong môi trường dữ liệu lớn, trí tuệ nhân tạo, chuỗi khối, vũ trụ ảo và điện toán đám mây phải tuân thủ quy định của Luật này và quy định khác của pháp luật có liên quan; phù hợp với chuẩn mực đạo đức, thuần phong mỹ tục của Việt Nam.
> 3. Hệ thống và dịch vụ sử dụng dữ liệu lớn, trí tuệ nhân tạo, chuỗi khối, vũ trụ ảo và điện toán đám mây phải được tích hợp các biện pháp bảo mật dữ liệu cá nhân phù hợp; phải sử dụng phương thức xác thực, định danh phù hợp và phân quyền truy cập để xử lý dữ liệu cá nhân.
> 4. Việc xử lý dữ liệu cá nhân bằng trí tuệ nhân tạo phải thực hiện phân loại theo mức độ rủi ro để có biện pháp bảo vệ dữ liệu cá nhân phù hợp.
> 5. Không sử dụng, phát triển hệ thống xử lý dữ liệu lớn, trí tuệ nhân tạo, chuỗi khối, vũ trụ ảo, điện toán đám mây có sử dụng dữ liệu cá nhân để gây tổn hại đến quốc phòng, an ninh quốc gia, trật tự, an toàn xã hội hoặc xâm phạm đến tính mạng, sức khỏe, danh dự, nhân phẩm, tài sản của người khác.

## F. Nghị định 356/2025/NĐ-CP — Điều 10 khoản 1–3, 5 (liên hệ mảng 1)

Trang Công báo: https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-356-2025-nd-cp-468371.htm (bản chữ đã trích ở đợt đối chiếu mảng 1).

> Điều 10. Bảo vệ dữ liệu cá nhân trong hệ thống trí tuệ nhân tạo, vũ trụ ảo
> 1. Các tổ chức, cá nhân được quyền sử dụng dữ liệu cá nhân để nghiên cứu, phát triển các thuật toán tự học, hệ thống trí tuệ nhân tạo và các hệ thống tự động khác nhưng cần bảo đảm tuân thủ các quy định về bảo vệ dữ liệu cá nhân.
> 2. Dữ liệu từ kết quả suy luận của trí tuệ nhân tạo nếu có thể được sử dụng để xác định hoặc giúp xác định một con người cụ thể thì phải được áp dụng các biện pháp bảo vệ dữ liệu cá nhân theo quy định của pháp luật.
> 3. Bên kiểm soát dữ liệu cá nhân, bên kiểm soát và xử lý dữ liệu cá nhân có trách nhiệm thông báo cho chủ thể dữ liệu về việc xử lý dữ liệu cá nhân tự động, giải thích nguyên tắc hoạt động của thuật toán và ảnh hưởng đối với quyền và lợi ích hợp pháp của chủ thể dữ liệu; đưa ra các lựa chọn để chủ thể dữ liệu có quyền không tham gia.
> …
> 5. Các tổ chức, cá nhân áp dụng các biện pháp bảo vệ dữ liệu cá nhân trong hệ thống trí tuệ nhân tạo, vũ trụ ảo, gồm:
> a) Nghiên cứu, xây dựng và triển khai hệ thống đáp ứng các tiêu chuẩn an ninh mạng, tiêu chuẩn bảo vệ dữ liệu toàn diện cho các hệ thống trí tuệ nhân tạo, đặc biệt chú trọng các yếu tố: bảo mật thông tin, độ tin cậy của thuật toán, tính ổn định hệ thống và khả năng phòng chống tấn công mạng;
> b) Thiết lập cơ chế giám sát hoạt động của hệ thống trí tuệ nhân tạo trên hai phương diện: giám sát của cơ quan nhà nước có thẩm quyền; trách nhiệm giải trình đối với chủ thể dữ liệu cá nhân của bên kiểm soát dữ liệu cá nhân, bên kiểm soát và xử lý dữ liệu cá nhân.
> c) Xây dựng cơ chế bảo vệ dữ liệu cá nhân theo tiêu chuẩn phù hợp, phát triển hệ thống giám sát và cảnh báo sớm các nguy cơ an ninh mạng;
> d) Thiết lập cơ chế kiểm soát, ngăn chặn việc lợi dụng trí tuệ nhân tạo, vũ trụ ảo vào các hoạt động xâm phạm an ninh quốc gia, trật tự an toàn xã hội;

## G. Bộ luật Dân sự 91/2015/QH13 — Điều 32 khoản 1 (quyền đối với hình ảnh)

Trang Công báo: https://congbao.chinhphu.vn/van-ban/luat-so-91-2015-qh13-18397.htm (Công báo số 1243+1244 ngày 28-12-2015, bản chữ đã trích ở đợt đối chiếu trước).

> Điều 32. Quyền của cá nhân đối với hình ảnh
> 1. Cá nhân có quyền đối với hình ảnh của mình.
> Việc sử dụng hình ảnh của cá nhân phải được người đó đồng ý.
> Việc sử dụng hình ảnh của người khác vì mục đích thương mại thì phải trả thù
> lao cho người có hình ảnh, trừ trường hợp các bên có thỏa thuận khác.

Ghi chú: chỉ đọc khoản 1; chưa kiểm Điều 32 có bị sửa bởi luật sau không.

---

## H. Nghị định xử phạt lĩnh vực AI — KHÔNG THẤY

- Tra ngày 25/10/2026 trên congbao.chinhphu.vn, vanban.chinhphu.vn, baochinhphu.vn, mst.gov.vn với các cụm "xử phạt vi phạm hành chính" + "trí tuệ nhân tạo": không thấy nghị định đã ban hành.
- Luật 134/2025 Điều 29 khoản 5 (trích A13): "Chính phủ quy định chi tiết về xử phạt vi phạm hành chính đối với hành vi vi phạm do hệ thống trí tuệ nhân tạo gây ra."
- Trang dự thảo của Bộ KH&CN: https://mst.gov.vn/van-ban-phap-luat/du-thao/2549.htm — "Dự thảo Nghị định quy định xử phạt vi phạm hành chính trong lĩnh vực khoa học, công nghệ, đổi mới sáng tạo và chuyển giao công nghệ", lấy ý kiến 18/08/2026–27/08/2026. Đã tải tệp "02-Dự thảo Nghị định.docx" từ trang này và tìm cụm "nhân tạo": **0 lần**. Kết luận: bản dự thảo đó không nhắm hành vi vi phạm Luật 134/2025.
- Các nghị định xử phạt khác trong bộ nguồn (NĐ 174/2026, NĐ 363/2026): bản chữ đã trích không có cụm "trí tuệ nhân tạo". Vi phạm về DLCN khi dùng AI ⇒ phạt theo khung DLCN (Luật 91/2025 Điều 8; NĐ 330/2026 — mảng 1).
