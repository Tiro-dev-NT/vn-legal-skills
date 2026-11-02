"""Máy quét tín hiệu cho vn-legal-check — chỉ thư viện chuẩn Python 3.

Chạy:  python -I scripts/quet.py <thư-mục-dự-án | https://url> [--json] [--cho-phep-noi-bo]

Máy quét chỉ GREP: nó chỉ ra CHỖ cần đọc (đường/dẫn:dòng), không kết luận đúng/sai luật,
không in số điều hay mức phạt (những thứ đó nằm trong mang/*.md). Có thể bắt nhầm hoặc bỏ sót;
"không thấy trong mã" không có nghĩa là "không có". Không phải tư vấn pháp lý — xem MIEN-TRU-TRACH-NHIEM.md.

Exit 0 khi quét xong (dù có tín hiệu); exit 2 khi đầu vào sai hoặc không tải được trang chủ.
"""
import argparse, datetime, html.parser, ipaddress, json, os, re, socket, sys, tempfile
import urllib.error, urllib.parse, urllib.request

GOC_REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHIEN_BAN = '1.0'
USER_AGENT = f'vn-legal-skills-quet/{PHIEN_BAN} (read-only signal scanner)'

THU_MUC_BO = {'node_modules', '.git', 'dist', 'build', 'vendor', '.dart_tool', 'Pods', '.gradle', '.next',
              '.nuxt', '.svelte-kit', '.expo', '.turbo', '__pycache__', '.venv', 'venv', 'coverage', '.idea'}
TEP_KHOA = {'package-lock.json', 'yarn.lock', 'pnpm-lock.yaml', 'pubspec.lock', 'Podfile.lock', 'composer.lock',
            'Gemfile.lock', 'poetry.lock', 'Cargo.lock', 'bun.lockb'}
DUOI_NHI_PHAN = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.ico', '.bmp', '.avif', '.pdf', '.zip', '.gz', '.tar',
                 '.7z', '.rar', '.woff', '.woff2', '.ttf', '.otf', '.eot', '.mp3', '.mp4', '.wav', '.ogg', '.webm',
                 '.mov', '.jar', '.class', '.so', '.dll', '.exe', '.dylib', '.a', '.o', '.pyc', '.keystore', '.jks',
                 '.apk', '.aab', '.ipa', '.psd', '.sqlite', '.db'}
TRAN_KICH_THUOC = 1024 * 1024
SO_BANG_CHUNG = 5
DO_DAI_DOAN = 120

# ---------------------------------------------------------------------------------------------
# Tín hiệu: (mã, nhóm, tên, mẫu). Mẫu là regex, không phân biệt hoa thường.
# ---------------------------------------------------------------------------------------------
TIN_HIEU = [
    # Thu thập dữ liệu
    ('form-email-sdt', 'Thu thập dữ liệu', 'Form / ô nhập thu email hoặc số điện thoại',
     r'''type\s*=\s*["']?(email|tel)\b|name\s*=\s*["'](e-?mail|phone|sdt|so_?dien_?thoai|mobile)["']'''
     r'''|keyboardType\s*[=:]\s*["']?(email-address|phone-pad)|TextInputType\.(emailAddress|phone)|autoComplete\s*=\s*["'](email|tel)'''),
    ('checkbox-tick-san', 'Thu thập dữ liệu', 'Ô checkbox tick sẵn',
     r'''<input\b[^>]*type\s*=\s*["']?checkbox[^>]*\bchecked\b|<input\b[^>]*\bchecked\b[^>]*type\s*=\s*["']?checkbox|defaultChecked|\bchecked\s*=\s*\{\s*true\s*\}'''),
    ('theo-doi', 'Thu thập dữ liệu', 'Script / SDK theo dõi, đo lường (analytics, pixel, attribution)',
     r'''gtag\(|googletagmanager\.com|google-analytics\.com|\bga\(\s*['"]|fbq\(|connect\.facebook\.net|ttq\.(load|page|track)'''
     r'''|analytics\.tiktok\.com|hotjar|clarity\.ms|\bclarity\(|mixpanel|amplitude|posthog|segment\.(com|io)|mc\.yandex'''
     r'''|plausible|@vercel/analytics|firebase_analytics|@react-native-firebase/analytics|firebase-analytics|FirebaseAnalytics'''
     r'''|appsflyer|adjust_sdk|react-native-adjust|com\.adjust\.sdk|facebook_app_events|react-native-fbsdk|FBSDKCoreKit'''
     r'''|AppEventsLogger|react-native-branch|branch\.io'''),
    ('banner-dong-y', 'Thu thập dữ liệu', 'Banner cookie / hộp xin đồng ý theo dõi',
     r'''cookie[-_ ]?(consent|banner|notice|bar)|cookieconsent|cookieyes|onetrust|cookiebot|osano|tarteaucitron|klaro|iubenda'''
     r'''|(chấp nhận|đồng ý|từ chối)[^<\n]{0,20}cookie|accept[^<\n]{0,15}cookies|gtag\(\s*['"]consent'''
     r'''|UserMessagingPlatform|ConsentInformation|ConsentRequestParameters|ConsentForm|requestTrackingAuthorization'''
     r'''|app_tracking_transparency|expo-tracking-transparency'''),
    ('email-marketing', 'Thu thập dữ liệu', 'Nhận tin / email-SMS marketing',
     r'''newsletter|nhận tin|nhan[-_]tin|bản tin|mailchimp|sendgrid|brevo|sendinblue|unsubscribe|huỷ nhận|hủy nhận|\bzns\b|sms[-_ ]?marketing'''),
    ('tai-khoan', 'Tài khoản', 'Tài khoản / đăng nhập / mật khẩu',
     r'''type\s*=\s*["']?password|secureTextEntry|obscureText\s*:\s*true|\bsignIn\w*\(|\bsignUp\w*\(|createUserWith\w+'''
     r'''|\blog[iI]n\(|["'/]login\b|["'/]signup\b|["'/]register\b|dang[-_]nhap|đăng nhập|mật khẩu|next-auth|passport\.authenticate'''
     r'''|FirebaseAuth|firebase_auth|@clerk/|auth0'''),
    ('xoa-tai-khoan', 'Tài khoản', 'Chức năng xoá tài khoản',
     r'''delete[-_ ]?account|deleteAccount|delete_?user|deleteUser|remove[-_ ]?account|close[-_ ]?account|currentUser\.delete'''
     r'''|xo[aá][-_ ]?t[aà]i[-_ ]?kho[aả]n|xoá tài khoản|xóa tài khoản|huỷ tài khoản|hủy tài khoản'''),
    ('xac-thuc-sdt', 'Tài khoản', 'Xác thực bằng số điện thoại / OTP SMS',
     r'''otp|signInWithPhoneNumber|verifyPhoneNumber|signInWithOtp|phone[-_]?auth|PhoneAuthProvider|xác thực số điện thoại|mã xác (thực|nhận)[^
]{0,20}(sms|tin nhắn)'''),
    ('micro-camera', 'Dữ liệu nhạy cảm', 'Micro / camera / ghi âm / nhận giọng nói',
     r'''getUserMedia|MediaRecorder|mediaDevices|expo-camera|expo-av|react-native-vision-camera|\bcamera\s*:\s*\^|image_picker'''
     r'''|flutter_sound|\brecord\s*:\s*\^|RECORD_AUDIO|android\.permission\.CAMERA|["']CAMERA["']|NSCameraUsageDescription'''
     r'''|NSMicrophoneUsageDescription|webcam|SpeechRecognition'''),
    ('vi-tri', 'Dữ liệu nhạy cảm', 'Vị trí',
     r'''geolocation|getCurrentPosition|watchPosition|geolocator|expo-location|react-native-geolocation'''
     r'''|ACCESS_(FINE|COARSE|BACKGROUND)_LOCATION|NSLocation\w*UsageDescription|CLLocationManager|\blocation\s*:\s*\^'''),
    ('danh-ba', 'Dữ liệu nhạy cảm', 'Danh bạ',
     r'''READ_CONTACTS|WRITE_CONTACTS|NSContactsUsageDescription|flutter_contacts|contacts_service|expo-contacts'''
     r'''|react-native-contacts|navigator\.contacts|CNContactStore'''),
    ('tre-em', 'Dữ liệu nhạy cảm', 'Trẻ em / độ tuổi / ngày sinh',
     r'''ngày sinh|ngay[-_]sinh|date[-_ ]?of[-_ ]?birth|birth[-_ ]?(day|date)|\bdob\b|độ tuổi|trẻ em|\bkids?\b|trẻ dưới|for children'''
     r'''|under[-_ ]?1[368]\b|age[-_ ]?gate|phụ huynh|parental'''),
    # Bán hàng, thanh toán
    ('gio-hang', 'Bán hàng · thanh toán', 'Giỏ hàng / thanh toán / đặt hàng',
     r'''add[-_]?to[-_]?cart|\bcart\b|giỏ hàng|gio[-_]hang|checkout|thanh toán|thanh[-_]toan|đặt hàng|dat[-_]hang|order[-_]?summary'''),
    ('cong-thanh-toan-vn', 'Bán hàng · thanh toán', 'Cổng thanh toán / ví trong nước',
     r'''\b(vnpay|vnp_[A-Za-z]+|momo|zalopay|zalo_?pay|payos|onepay|napas|vietqr|sepay|casso|alepay|baokim|nganluong)\b|ngân lượng'''),
    ('cong-thanh-toan-qt', 'Bán hàng · thanh toán', 'Cổng thanh toán quốc tế',
     r'''\b(stripe|paypal|braintree|paddle|lemonsqueezy|razorpay|adyen|2checkout)\b|checkout\.com'''),
    ('mua-trong-app', 'Bán hàng · thanh toán', 'Mua trong ứng dụng (kho ứng dụng)',
     r'''in_app_purchase|react-native-iap|expo-in-app-purchases|react-native-purchases|purchases_flutter|revenuecat'''
     r'''|StoreKit|SKPaymentQueue|com\.android\.vending\.BILLING|billingclient|play[-_ ]billing'''),
    ('goi-dang-ky', 'Bán hàng · thanh toán', 'Gói đăng ký / gia hạn định kỳ',
     r'''subscription|gói (tháng|năm)|/\s?tháng\b|/\s?năm\b|per month|gia hạn|auto[-_ ]?renew|recurring'''
     r'''|billing[-_ ]?(cycle|period|interval)|interval\s*:\s*['"](month|year)'''),
    ('vi-credit', 'Bán hàng · thanh toán', 'Ví / số dư / credit / xu nạp trước',
     r'''\bwallet\b|nạp (tiền|xu)|rút tiền|\bxu\b|số dư|top[-_ ]?up|\bpayout\b|credit[-_ ]?balance|(buy|mua|nạp)[^\n]{0,15}credits?\b'''),
    ('ngoai-te', 'Bán hàng · thanh toán', 'Giá / tiền tệ nước ngoài',
     r'''currency\s*[:=]\s*['"]usd|['"]USD['"]|\bUSD\b|US\$'''),
    ('crypto', 'Bán hàng · thanh toán', 'Tiền mã hoá / token / NFT',
     r'''\busdt\b|\bethers\b|web3|wagmi|metamask|walletconnect|solana|seed[-_ ]phrase|mnemonic|smart[-_ ]?contract|\bnft\b|airdrop'''),
    ('khuyen-mai', 'Quảng cáo · khuyến mại', 'Khuyến mại / giá gạch / đếm ngược',
     r'''<del\b|<s>|<strike\b|line-through|(original|old|compare[-_]?at|list)[-_]?price|giá gốc|gia[-_]goc|countdown'''
     r'''|đếm ngược|flash[-_ ]?sale|giảm (giá )?\d+ ?%|mã giảm giá|coupon|voucher|mua \d+ tặng \d+'''),
    ('sdk-quang-cao', 'Quảng cáo · khuyến mại', 'SDK / thẻ quảng cáo',
     r'''google_mobile_ads|react-native-google-mobile-ads|play-services-ads|com\.google\.android\.gms\.ads|GADApplicationIdentifier'''
     r'''|GoogleMobileAds|admob|applovin|unity_ads|unityads|com\.unity3d\.ads|ironsource|vungle|pangle|mintegral|chartboost'''
     r'''|adsbygoogle|pagead2\.googlesyndication|facebook_audience_network|react-native-fbads'''),
    ('ma-quang-cao', 'Quảng cáo · khuyến mại', 'Mã định danh quảng cáo (Advertising ID / IDFA / ATT)',
     r'''com\.google\.android\.gms\.permission\.AD_ID|\bAD_ID\b|advertising[-_]?id|AdvertisingIdClient|\bIDFA\b'''
     r'''|ASIdentifierManager|advertisingIdentifier|NSUserTrackingUsageDescription|requestTrackingAuthorization'''
     r'''|app_tracking_transparency|expo-tracking-transparency'''),
    # AI
    ('goi-ai', 'AI', 'Gọi API mô hình AI',
     r'''api\.openai\.com|\bopenai\b|@anthropic-ai|api\.anthropic\.com|\banthropic\b|generativelanguage\.googleapis\.com'''
     r'''|@google/generative-ai|@google/genai|google_generative_ai|\bgemini-|deepseek|api\.groq\.com|\bgroq\b|mistral\.ai'''
     r'''|api\.cohere|replicate\.com|huggingface|openrouter|together\.(ai|xyz)|dashscope|chat/completions|\bgpt-[345]|\bclaude-\d'''),
    ('chatbot', 'AI', 'Chatbot / khung chat',
     r'''chat-?bot|chat[-_]?widget|khung chat|trợ lý ảo|tro[-_]ly[-_]ao|virtual assistant|tawk\.to|crisp\.chat|tidio|intercom'''
     r'''|zalo[-_ ]?chat|messenger[-_ ]?chat|livechat|fb-customerchat|role\s*:\s*['"]assistant'''),
    ('ai-sinh-anh-giong', 'AI', 'AI sinh ảnh / giọng, nhân bản giọng, ghép mặt',
     r'''voice[-_ ]?clon|nhân bản giọng|face[-_ ]?swap|ghép mặt|deepfake|elevenlabs|text[-_]to[-_]speech|images/generations'''
     r'''|dall-?e|stable[-_ ]?diffusion|midjourney|image[-_]generation|sinh ảnh'''),
    # Nội dung người dùng, game
    ('noi-dung-nguoi-dung', 'Nội dung người dùng', 'Bình luận / đăng bài / tải tệp lên',
     r'''comment[-_]?(form|box|section|list)|addComment|postComment|createComment|/comments\b|bình luận|binh[-_]luan'''
     r'''|type\s*=\s*["']?file\b|upload(File|Image|Avatar)?\s*\(|image_picker|expo-image-picker|launchImageLibrary'''
     r'''|đăng bài|viết đánh giá|\bforum\b|diễn đàn'''),
    ('cao-du-lieu', 'Nội dung người dùng', 'Thư viện cào dữ liệu web',
     r'''puppeteer|playwright|cheerio|beautifulsoup|\bbs4\b|scrapy|selenium|crawlee|apify'''),
    ('game', 'Game', 'Game / bảng xếp hạng / nhiều người chơi',
     r'''\bphaser\b|pixi\.js|pixijs|cocos2d|cocos-creator|unityInstance|createUnityInstance|godot|\bflame\s*:\s*\^'''
     r'''|leaderboard|bảng xếp hạng|multiplayer|nhiều người chơi|matchmaking'''),
    ('quay-thuong-vat-pham', 'Game', 'Quay thưởng / vật phẩm ảo / đổi điểm lấy quà',
     r'''gacha|loot[-_ ]?box|vòng quay|vong[-_]quay|lucky[-_ ]?(wheel|draw|spin)|spin[-_ ]?(wheel|to[-_ ]win)|quay thưởng'''
     r'''|rút thăm|vật phẩm|kim cương|item[-_ ]?shop|đổi điểm|đổi quà'''),
    # Hạ tầng, bảo mật
    ('dich-vu-nuoc-ngoai', 'Hạ tầng · bảo mật', 'Dịch vụ / hạ tầng ở nước ngoài',
     r'''firebase|firestore|supabase|vercel|netlify|amazonaws\.com|aws-sdk|@aws-sdk|cloudfront|cloudflare|workers\.dev'''
     r'''|herokuapp|render\.com|fly\.io|railway\.app|mongodb\+srv|mongodb\.net|planetscale|neon\.tech|mailchimp|sendgrid'''
     r'''|resend\.com|postmark|mailgun|algolia|sentry|cloudinary|azure|digitalocean|onesignal|pusher|twilio|googleapis\.com'''),
    ('khoa-bi-mat', 'Hạ tầng · bảo mật', 'Khoá bí mật nằm trong mã (giá trị đã che)', None),  # xử lý riêng
    # Trang pháp lý, chủ sở hữu
    ('link-chinh-sach', 'Trang pháp lý', 'Link / trang chính sách bảo mật (quyền riêng tư)',
     r'''privacy|chinh[-_]sach[-_](bao[-_]mat|quyen[-_]rieng[-_]tu)|chính sách (bảo mật|quyền riêng tư)|quyen[-_]rieng[-_]tu'''
     r'''|quyền riêng tư|bảo vệ dữ liệu cá nhân'''),
    ('link-dieu-khoan', 'Trang pháp lý', 'Link / trang điều khoản sử dụng',
     r'''\bterms\b|terms[-_]of|dieu[-_]khoan|điều khoản'''),
    ('lien-he', 'Trang pháp lý', 'Thông tin liên hệ',
     r'''liên hệ|lien[-_]he|\bcontact\b|hotline|mailto:|tel:'''),
    ('thong-tin-chu-so-huu', 'Trang pháp lý', 'Thông tin chủ sở hữu (mã số thuế, đăng ký kinh doanh, đơn vị chủ quản)',
     r'''mã số thuế|\bMST\b|mã số doanh nghiệp|giấy chứng nhận đăng ký|GCNĐKKD|\bĐKKD\b|hộ kinh doanh|công ty (TNHH|cổ phần)'''
     r'''|đơn vị chủ quản|chủ sở hữu website'''),
    ('dau-bo-cong-thuong', 'Trang pháp lý', 'Dấu / link thông báo website với Bộ Công Thương',
     r'''online\.gov\.vn|dathongbao|đã thông báo bộ công thương|logoSaleNoti|bocongthuong'''),
]
TEN = {t[0]: t for t in TIN_HIEU}
RE_TIN_HIEU = {t[0]: re.compile(t[3], re.I) for t in TIN_HIEU if t[3]}

# Khoá bí mật. Nhóm 'v' là phần giá trị phải che.
RE_KHOA = [re.compile(p) for p in [
    r'(?P<v>sk_live_[A-Za-z0-9_]{3,})', r'(?P<v>rk_live_[A-Za-z0-9_]{3,})', r'(?P<v>sk-ant-[A-Za-z0-9_\-]{8,})',
    r'(?P<v>sk-(?:proj-)?[A-Za-z0-9_\-]{20,})', r'(?P<v>AKIA[0-9A-Z]{16})', r'(?P<v>gh[pousr]_[A-Za-z0-9]{30,})',
    r'(?P<v>xox[abposr]-[A-Za-z0-9-]{10,})', r'-----BEGIN (?:RSA |EC |DSA |OPENSSH |ENCRYPTED )?PRIVATE KEY-----',
    r'(?i)service_role',
    r'''(?i)[\w-]*(?:secret|private[_-]?key|api[_-]?key|access[_-]?token|password)\w*["']?\s*[:=]\s*["'](?P<v>[^"'\s]{8,})["']''',
]]
RE_KHOA_ENV = re.compile(r'(?i)^\s*(?:export\s+)?[A-Z0-9_]*(?:SECRET|PRIVATE_KEY|API_KEY|TOKEN|PASSWORD|SERVICE_ROLE)[A-Z0-9_]*\s*=\s*["\']?(?P<v>[^\s"\']{8,})')
RE_CHE_THEM = [re.compile(r'(?P<v>eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{5,})'),
               re.compile(r'(?P<v>AIza[0-9A-Za-z_\-]{30,})')]
GIA_TRI_GIU_CHO = re.compile(r'(?i)^(process\.env|import\.meta|\$\{|<|your[_-]|xxx|\*{3}|changeme|example|placeholder|env\()')


def che(dong):
    """Che mọi giá trị trông như khoá: giữ 4 ký tự đầu."""
    def thay(m):
        v = m.group('v')
        return m.group(0).replace(v, v[:4] + f'…[đã che {len(v) - 4} ký tự]')
    for r in RE_KHOA + [RE_KHOA_ENV] + RE_CHE_THEM:
        if 'v' in r.groupindex:
            dong = r.sub(thay, dong)
    return dong


def la_khoa(dong, ten_tep):
    for r in RE_KHOA:
        m = r.search(dong)
        if m and not ('v' in r.groupindex and GIA_TRI_GIU_CHO.match(m.group('v'))):
            return m.start()
    t = ten_tep.lower()
    if t.startswith('.env') and not any(x in t for x in ('example', 'sample', 'template', 'mau')):
        m = RE_KHOA_ENV.search(dong)
        if m and not GIA_TRI_GIU_CHO.match(m.group('v')):
            return m.start()
    return -1


def cat_doan(dong, vi_tri):
    dong = dong.strip()
    if len(dong) <= DO_DAI_DOAN:
        return dong
    bd = max(0, min(vi_tri, len(dong)) - 40)
    doan = dong[bd:bd + DO_DAI_DOAN]
    return ('…' if bd else '') + doan + ('…' if bd + DO_DAI_DOAN < len(dong) else '')


# ---------------------------------------------------------------------------------------------
# Quyền trên mobile
# ---------------------------------------------------------------------------------------------
QUYEN_ANDROID_NHAY_CAM = {
    'ACCESS_FINE_LOCATION': 'vị trí', 'ACCESS_COARSE_LOCATION': 'vị trí', 'ACCESS_BACKGROUND_LOCATION': 'vị trí (nền)',
    'READ_CONTACTS': 'danh bạ', 'WRITE_CONTACTS': 'danh bạ', 'GET_ACCOUNTS': 'tài khoản trên máy',
    'CAMERA': 'camera', 'RECORD_AUDIO': 'micro', 'READ_EXTERNAL_STORAGE': 'tệp/ảnh', 'WRITE_EXTERNAL_STORAGE': 'tệp/ảnh',
    'READ_MEDIA_IMAGES': 'ảnh', 'READ_MEDIA_VIDEO': 'video', 'READ_MEDIA_AUDIO': 'âm thanh', 'MANAGE_EXTERNAL_STORAGE': 'toàn bộ tệp',
    'READ_SMS': 'tin nhắn', 'SEND_SMS': 'tin nhắn', 'RECEIVE_SMS': 'tin nhắn', 'READ_CALL_LOG': 'nhật ký cuộc gọi',
    'CALL_PHONE': 'gọi điện', 'READ_PHONE_STATE': 'trạng thái/số máy', 'READ_PHONE_NUMBERS': 'số điện thoại',
    'READ_CALENDAR': 'lịch', 'WRITE_CALENDAR': 'lịch', 'BODY_SENSORS': 'cảm biến cơ thể/sức khoẻ',
    'ACTIVITY_RECOGNITION': 'hoạt động thể chất', 'AD_ID': 'mã quảng cáo', 'POST_NOTIFICATIONS': 'thông báo',
}
RE_CHUNG_CHUNG = re.compile(
    r'(?i)^(this app|the app|app|ứng dụng|chúng tôi)?\s*(needs?|requires?|would like to|wants? to|uses?|cần|muốn|yêu cầu|xin)\s*'
    r'(to\s+)?(access|use|permission|quyền|truy cập|sử dụng)\b[^.]{0,25}\.?$'
    r'|better (user )?experience|trải nghiệm tốt hơn|for (some|certain) features|cho một số tính năng')


def danh_gia_giai_thich(s):
    s = (s or '').strip()
    if not s:
        return 'rỗng'
    if len(s) < 25:
        return 'quá ngắn'
    if RE_CHUNG_CHUNG.search(s):
        return 'chung chung'
    return ''


def so_dong(text, vi_tri):
    return text.count('\n', 0, vi_tri) + 1


def doc_quyen(rel, text):
    ra = []
    ten = os.path.basename(rel)
    if ten == 'AndroidManifest.xml':
        for m in re.finditer(r'<uses-permission(?:-sdk-\d+)?\b[^>]*android:name\s*=\s*"([^"]+)"', text):
            q = m.group(1).split('.')[-1]
            ra.append({'nen_tang': 'android', 'quyen': m.group(1), 'nhay_cam': QUYEN_ANDROID_NHAY_CAM.get(q, ''),
                       'giai_thich': None, 'van_de': '', 'vi_tri': f'{rel}:{so_dong(text, m.start())}'})
    elif ten == 'Info.plist':
        for m in re.finditer(r'<key>\s*(NS\w+UsageDescription)\s*</key>\s*(?:<string>(.*?)</string>|<string\s*/>)', text, re.S):
            gt = m.group(2) or ''
            ra.append({'nen_tang': 'ios', 'quyen': m.group(1), 'nhay_cam': 'có (iOS)', 'giai_thich': gt.strip(),
                       'van_de': danh_gia_giai_thich(gt), 'vi_tri': f'{rel}:{so_dong(text, m.start())}'})
    elif re.match(r'app(\.config)?\.json$', ten):
        for m in re.finditer(r'"(NS\w+UsageDescription)"\s*:\s*"((?:[^"\\]|\\.)*)"', text):
            ra.append({'nen_tang': 'ios', 'quyen': m.group(1), 'nhay_cam': 'có (iOS)', 'giai_thich': m.group(2),
                       'van_de': danh_gia_giai_thich(m.group(2)), 'vi_tri': f'{rel}:{so_dong(text, m.start())}'})
        for m in re.finditer(r'"(\w*[Pp]ermission)"\s*:\s*"((?:[^"\\]|\\.)*)"', text):
            ra.append({'nen_tang': 'expo', 'quyen': m.group(1), 'nhay_cam': 'có', 'giai_thich': m.group(2),
                       'van_de': danh_gia_giai_thich(m.group(2)), 'vi_tri': f'{rel}:{so_dong(text, m.start())}'})
        for m in re.finditer(r'"permissions"\s*:\s*\[(.*?)\]', text, re.S):
            for q in re.finditer(r'"([\w.]+)"', m.group(1)):
                ten_q = q.group(1).split('.')[-1]
                ra.append({'nen_tang': 'android', 'quyen': q.group(1), 'nhay_cam': QUYEN_ANDROID_NHAY_CAM.get(ten_q, ''),
                           'giai_thich': None, 'van_de': '', 'vi_tri': f'{rel}:{so_dong(text, m.start(1) + q.start())}'})
    return ra


# ---------------------------------------------------------------------------------------------
# Quét thư mục
# ---------------------------------------------------------------------------------------------
def doc_tep(p):
    with open(p, 'rb') as f:
        b = f.read()
    if b'\x00' in b[:8192]:
        return None
    return b.decode('utf-8', errors='replace')


def nhan_nen_tang(goc, tep_list):
    nt = set()
    for rel in tep_list:
        ten = os.path.basename(rel)
        duoi = os.path.splitext(ten)[1].lower()
        if ten == 'pubspec.yaml':
            nt.add('flutter')
        elif ten == 'AndroidManifest.xml':
            nt.add('android')
        elif ten == 'Info.plist':
            nt.add('ios')
        elif ten in ('app.json', 'app.config.json', 'app.config.js', 'app.config.ts'):
            t = doc_tep(os.path.join(goc, rel)) or ''
            if '"expo"' in t or 'expo' in ten and 'config' in ten:
                nt.add('expo')
        elif ten == 'package.json':
            t = doc_tep(os.path.join(goc, rel)) or ''
            if re.search(r'"react-native"\s*:', t): nt.add('react-native')
            if re.search(r'"expo"\s*:', t): nt.add('expo')
            if re.search(r'"(react-dom|next|vue|nuxt|svelte|@sveltejs/kit|vite|astro|@angular/core)"\s*:', t): nt.add('web')
        elif duoi in ('.html', '.htm', '.php', '.vue', '.svelte', '.astro', '.jsp', '.erb', '.twig', '.blade'):
            nt.add('web')
    return sorted(nt)


def duyet(goc, bo_qua_tep=()):
    tep, bo = [], {'qua_lon': 0, 'nhi_phan': 0}
    for thu_muc, con, cac_tep in os.walk(goc):
        con[:] = sorted(c for c in con if c not in THU_MUC_BO)
        for ten in sorted(cac_tep):
            p = os.path.join(thu_muc, ten)
            rel = os.path.relpath(p, goc).replace(os.sep, '/')
            if rel in bo_qua_tep or ten in TEP_KHOA:
                continue
            if os.path.splitext(ten)[1].lower() in DUOI_NHI_PHAN:
                bo['nhi_phan'] += 1
                continue
            try:
                if os.path.getsize(p) > TRAN_KICH_THUOC:
                    bo['qua_lon'] += 1
                    continue
            except OSError:
                continue
            tep.append(rel)
    return tep, bo


def quet_thu_muc(goc, bo_qua_tep=()):
    tep_list, bo = duyet(goc, bo_qua_tep)
    trung = {k: [] for k in TEN}
    quyen = []
    so_tep = 0
    for rel in tep_list:
        text = doc_tep(os.path.join(goc, rel))
        if text is None:
            bo['nhi_phan'] += 1
            continue
        so_tep += 1
        ten = os.path.basename(rel)
        for i, dong in enumerate(text.splitlines(), 1):
            if not dong.strip():
                continue
            for k, r in RE_TIN_HIEU.items():
                m = r.search(dong)
                if m:
                    trung[k].append((rel, i, dong, m.start()))
            vt = la_khoa(dong, ten)
            if vt >= 0:
                trung['khoa-bi-mat'].append((rel, i, dong, vt))
        quyen += doc_quyen(rel, text)
    tin_hieu = {}
    for k, ds in trung.items():
        if not ds:
            continue
        chon, da = [], set()
        for h in ds:                      # lượt 1: mỗi tệp một bằng chứng
            if h[0] not in da and len(chon) < SO_BANG_CHUNG:
                chon.append(h); da.add(h[0])
        for h in ds:                      # lượt 2: lấp cho đủ
            if len(chon) >= SO_BANG_CHUNG: break
            if h not in chon: chon.append(h)
        chon.sort(key=lambda h: (h[0], h[1]))
        _, nhom, ten_th, _ = TEN[k]
        tin_hieu[k] = {'nhom': nhom, 'ten': ten_th, 'so': len(ds), 'so_tep': len({h[0] for h in ds}),
                       'bang_chung': [{'tep': h[0], 'dong': h[1], 'doan': cat_doan(che(h[2]), h[3])} for h in chon]}
    for q in quyen:
        if q['giai_thich']:
            q['giai_thich'] = che(q['giai_thich'])[:160]
    return {'so_tep': so_tep, 'bo_qua': bo, 'nen_tang': nhan_nen_tang(goc, tep_list), 'tin_hieu': tin_hieu, 'quyen': quyen}


# ---------------------------------------------------------------------------------------------
# Suy luận: cảnh báo kết hợp, mức, mảng
# ---------------------------------------------------------------------------------------------
MUC_3 = {'tai-khoan', 'noi-dung-nguoi-dung'}
MUC_2 = {'gio-hang', 'cong-thanh-toan-vn', 'cong-thanh-toan-qt', 'mua-trong-app', 'goi-dang-ky', 'vi-credit'}
MUC_1 = {'form-email-sdt', 'checkbox-tick-san', 'theo-doi', 'sdk-quang-cao', 'ma-quang-cao', 'goi-ai', 'chatbot',
         'micro-camera', 'vi-tri', 'danh-ba', 'quyen-nhay-cam', 'email-marketing'}
TEN_MUC = {0: 'tĩnh (không thấy thu dữ liệu)', 1: 'thu thập nhẹ', 2: 'bán hàng / thu tiền',
           3: 'nền tảng có tài khoản hoặc nội dung người dùng'}
MOBILE = {'flutter', 'react-native', 'expo', 'android', 'ios'}

# (tệp mảng, [(mã tín hiệu hoặc cảnh báo, lý do)])
MANG = [
    ('01-du-lieu-ca-nhan.md', [
        ('form-email-sdt', 'thu email/SĐT'), ('checkbox-tick-san', 'checkbox tick sẵn'), ('theo-doi', 'script/SDK theo dõi'),
        ('tai-khoan', 'tài khoản người dùng'), ('micro-camera', 'micro/camera'), ('vi-tri', 'vị trí'), ('danh-ba', 'danh bạ'),
        ('tre-em', 'nhắc trẻ em/độ tuổi'), ('quyen-nhay-cam', 'xin quyền nhạy cảm trên mobile'),
        ('sdk-quang-cao', 'SDK quảng cáo'), ('ma-quang-cao', 'mã định danh quảng cáo'), ('email-marketing', 'email/SMS marketing'),
        ('goi-ai', 'gửi dữ liệu cho nhà cung cấp AI'), ('dich-vu-nuoc-ngoai', 'dịch vụ ở nước ngoài ⇒ xem chuyển dữ liệu xuyên biên giới'),
        ('xoa-tai-khoan', 'có xoá tài khoản (kiểm có xoá hết dữ liệu không)')]),
    ('02-nguoi-tieu-dung.md', [('gio-hang', 'giỏ hàng/thanh toán'), ('cong-thanh-toan-vn', 'cổng thanh toán'),
        ('cong-thanh-toan-qt', 'cổng thanh toán quốc tế'), ('goi-dang-ky', 'gói đăng ký/gia hạn'), ('mua-trong-app', 'mua trong app')]),
    ('03-thuong-mai-dien-tu.md', [('gio-hang', 'giỏ hàng/thanh toán'), ('cong-thanh-toan-vn', 'cổng thanh toán'),
        ('cong-thanh-toan-qt', 'cổng thanh toán quốc tế'), ('goi-dang-ky', 'bán gói trả phí online'), ('mua-trong-app', 'mua trong app')]),
    ('04-quang-cao.md', [('khuyen-mai', 'khuyến mại/giá gạch/đếm ngược'), ('email-marketing', 'email/SMS marketing'),
        ('sdk-quang-cao', 'hiển thị quảng cáo'), ('quay-thuong-vat-pham', 'vòng quay/quà tặng')]),
    ('05-ban-quyen.md', [('noi-dung-nguoi-dung', 'người dùng đăng nội dung'), ('goi-ai', 'gọi API mô hình AI'),
        ('cao-du-lieu', 'thư viện cào dữ liệu'), ('ai-sinh-anh-giong', 'AI sinh ảnh/giọng')]),
    ('06-an-ninh-mang.md', [('tai-khoan', 'tài khoản, lưu dữ liệu người dùng'), ('noi-dung-nguoi-dung', 'nội dung người dùng đăng'),
        ('khoa-bi-mat', 'khoá bí mật nằm trong mã'), ('tai-khoan-khong-otp-sdt', 'đăng ký không thấy xác thực bằng số điện thoại (OTP SMS)'),
        ('dich-vu-nuoc-ngoai', 'máy chủ/CSDL có thể ở ngoài Việt Nam')]),
    ('07-tri-tue-nhan-tao.md', [('goi-ai', 'gọi API mô hình AI'), ('chatbot', 'chatbot (kiểm có dùng AI không)'),
        ('ai-sinh-anh-giong', 'AI sinh ảnh/giọng')]),
    ('08-tro-choi-dien-tu.md', [('game', 'game/bảng xếp hạng'), ('quay-thuong-vat-pham', 'quay thưởng/vật phẩm ảo')]),
    ('09-thue-hoa-don.md', [('gio-hang', 'có thu tiền'), ('cong-thanh-toan-vn', 'có thu tiền'), ('cong-thanh-toan-qt', 'có thu tiền'),
        ('goi-dang-ky', 'gói thuê bao'), ('mua-trong-app', 'bán qua kho ứng dụng'), ('ngoai-te', 'giá ngoại tệ')]),
    ('10-dang-ky-kinh-doanh.md', [('gio-hang', 'thu tiền thường xuyên'), ('cong-thanh-toan-vn', 'thu tiền'),
        ('cong-thanh-toan-qt', 'thu tiền'), ('goi-dang-ky', 'thu tiền định kỳ'),
        ('thieu-thong-tin-chu-so-huu', 'không thấy thông tin chủ thể kinh doanh'), ('noi-dung-nguoi-dung', 'có thể là mạng xã hội (ngành có điều kiện)'),
        ('vi-credit', 'ví/nạp tiền (ngành có điều kiện)'), ('game', 'game qua mạng (ngành có điều kiện)')]),
    ('11-thanh-toan.md', [('cong-thanh-toan-vn', 'cổng thanh toán'), ('cong-thanh-toan-qt', 'cổng quốc tế'),
        ('vi-credit', 'ví/số dư/credit'), ('ngoai-te', 'giá ngoại tệ'), ('crypto', 'tiền mã hoá/token'), ('mua-trong-app', 'mua trong app')]),
    ('12-nhan-hieu-ten-mien.md', [('*', 'mọi dự án có tên app, logo, tên miền — lướt trước khi ra mắt')]),
    ('21-ung-dung-di-dong.md', [('mobile', 'dự án ứng dụng di động')]),
]


def suy_luan(kq):
    co = set(kq['tin_hieu'])
    if any(q['nhay_cam'] for q in kq['quyen']):
        co.add('quyen-nhay-cam')
        kq['tin_hieu']['quyen-nhay-cam'] = {'nhom': 'Dữ liệu nhạy cảm', 'ten': 'Quyền nhạy cảm xin trên mobile',
            'so': sum(1 for q in kq['quyen'] if q['nhay_cam']), 'so_tep': len({q['vi_tri'].rsplit(':', 1)[0] for q in kq['quyen'] if q['nhay_cam']}),
            'bang_chung': [{'tep': q['vi_tri'].rsplit(':', 1)[0], 'dong': int(q['vi_tri'].rsplit(':', 1)[1]), 'doan': q['quyen']}
                           for q in kq['quyen'] if q['nhay_cam']][:SO_BANG_CHUNG]}
    muc = 3 if co & MUC_3 else 2 if co & MUC_2 else 1 if co & MUC_1 else 0
    cb = []
    def them(ma, nd): cb.append({'id': ma, 'noi_dung': nd})
    if co & {'theo-doi', 'sdk-quang-cao'} and 'banner-dong-y' not in co:
        them('theo-doi-khong-banner', 'Có script/SDK theo dõi hoặc quảng cáo nhưng không thấy banner cookie / hộp xin đồng ý.')
    if 'tai-khoan' in co and 'xoa-tai-khoan' not in co:
        them('tai-khoan-khong-xoa', 'Có tài khoản/đăng nhập nhưng không thấy chức năng xoá tài khoản'
             + (' (kho ứng dụng di động cũng đòi điều này).' if set(kq['nen_tang']) & MOBILE else '.'))
    if 'tai-khoan' in co and 'xac-thuc-sdt' not in co:
        them('tai-khoan-khong-otp-sdt', 'Có tài khoản nhưng không thấy xác thực bằng số điện thoại (OTP SMS) — xem mang/06.')
    if muc >= 1 and 'link-chinh-sach' not in co:
        them('thieu-link-chinh-sach', 'Có thu dữ liệu nhưng không thấy link/trang chính sách bảo mật trong mã.')
    ban_hang = bool(co & MUC_2)
    if (ban_hang or 'tai-khoan' in co) and 'link-dieu-khoan' not in co:
        them('thieu-dieu-khoan', 'Có ' + ('bán hàng/thu tiền' if ban_hang else 'tài khoản người dùng') + ' nhưng không thấy link/trang điều khoản.')
    if ban_hang and 'thong-tin-chu-so-huu' not in co:
        them('thieu-thong-tin-chu-so-huu', 'Có bán hàng/thu tiền nhưng không thấy mã số thuế / thông tin chủ thể ở footer hay trang giới thiệu.')
    if ban_hang and 'dau-bo-cong-thuong' not in co and 'web' in kq['nen_tang']:
        them('thieu-dau-bo-cong-thuong', 'Website bán hàng nhưng không thấy dấu/link thông báo với Bộ Công Thương (kiểm mảng 03 xem có áp dụng không).')
    if 'khoa-bi-mat' in co:
        them('khoa-trong-ma', 'Có chuỗi giống khoá bí mật trong mã — kiểm tệp đó có bị gửi về trình duyệt/app không; khoá chỉ ở server vẫn nên ra khỏi kho mã.')
    chung = [q for q in kq['quyen'] if q['van_de']]
    if chung:
        them('giai-thich-quyen-chung-chung', f'{len(chung)} câu giải thích xin quyền bị rỗng/quá ngắn/chung chung.')
    if 'checkbox-tick-san' in co and co & {'form-email-sdt', 'email-marketing', 'gio-hang'}:
        them('dong-y-tick-san', 'Ô checkbox tick sẵn nằm gần form thu dữ liệu/thanh toán — mở ra xem có phải ô đồng ý không.')
    co_ca_cb = co | {c['id'] for c in cb} | ({'mobile'} if set(kq['nen_tang']) & MOBILE else set())
    mang = []
    for tep, luat in MANG:
        ly_do = [ld for ma, ld in luat if ma == '*' or ma in co_ca_cb]
        if ly_do:
            mang.append({'tep': f'mang/{tep}', 'ly_do': list(dict.fromkeys(ly_do)),
                         'ton_tai': os.path.exists(os.path.join(GOC_REPO, 'mang', tep))})
    kq.update({'canh_bao': cb, 'muc': muc, 'muc_ten': TEN_MUC[muc], 'mang': mang,
               'khong_thay': [k for k in ('banner-dong-y', 'link-chinh-sach', 'link-dieu-khoan', 'lien-he', 'thong-tin-chu-so-huu',
                                          'xoa-tai-khoan', 'dau-bo-cong-thuong') if k not in co]})
    return kq


# ---------------------------------------------------------------------------------------------
# Chế độ URL
# ---------------------------------------------------------------------------------------------
class LoiDauVao(Exception):
    pass


def kiem_url(url, cho_noi_bo):
    u = urllib.parse.urlsplit(url)
    if u.scheme not in ('http', 'https') or not u.hostname:
        raise LoiDauVao(f'chỉ nhận URL http/https có tên miền: {url}')
    if cho_noi_bo:
        return
    host = u.hostname.lower()
    if host == 'localhost' or host.endswith(('.localhost', '.local', '.internal')):
        raise LoiDauVao(f'từ chối địa chỉ nội bộ {host} (thêm --cho-phep-noi-bo nếu chủ ý)')
    try:
        ds = socket.getaddrinfo(host, u.port or (443 if u.scheme == 'https' else 80), proto=socket.IPPROTO_TCP)
    except socket.gaierror as e:
        raise LoiDauVao(f'không phân giải được {host}: {e}')
    for *_, sa in ds:
        ip = ipaddress.ip_address(sa[0].split('%')[0])
        if getattr(ip, 'ipv4_mapped', None):
            ip = ip.ipv4_mapped
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved or ip.is_multicast or ip.is_unspecified:
            raise LoiDauVao(f'từ chối {host} → {ip} (IP nội bộ; thêm --cho-phep-noi-bo nếu chủ ý)')


class _ChuyenHuong(urllib.request.HTTPRedirectHandler):
    def __init__(self, cho_noi_bo):
        self.cho_noi_bo = cho_noi_bo

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        kiem_url(newurl, self.cho_noi_bo)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


TRAN_TAI = 2 * 1024 * 1024


def tai(url, cho_noi_bo):
    kiem_url(url, cho_noi_bo)
    opener = urllib.request.build_opener(_ChuyenHuong(cho_noi_bo))
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT, 'Accept': 'text/html,application/javascript,*/*;q=0.5'})
    with opener.open(req, timeout=15) as r:
        data = r.read(TRAN_TAI + 1)
        return r.geturl(), (r.headers.get('Content-Type') or '').lower(), data[:TRAN_TAI], len(data) > TRAN_TAI


class _Link(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.link = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'a' and a.get('href'):
            self.link.append(('a', a['href']))
        elif tag == 'script' and a.get('src'):
            self.link.append(('script', a['src']))


UU_TIEN = ('privacy', 'chinh-sach', 'chinh_sach', 'dieu-khoan', 'terms', 'policy', 'bao-mat', 'lien-he', 'contact',
           'cart', 'gio-hang', 'checkout', 'thanh-toan', 'gioi-thieu', 'about')
DUOI_BO_URL = tuple(DUOI_NHI_PHAN) + ('.css', '.xml', '.rss', '.json', '.txt')


def bo_www(h):
    return h[4:] if h.startswith('www.') else h


def quet_url(url, cho_noi_bo, toi_da=15):
    thu_muc = tempfile.mkdtemp(prefix='vn-legal-quet-')
    try:
        cuoi, loai, data, cat = tai(url, cho_noi_bo)
    except LoiDauVao:
        raise
    except (urllib.error.URLError, OSError, ValueError) as e:
        raise LoiDauVao(f'không tải được trang chủ {url}: {e}')
    ghi = [('00-trang-chu.html', cuoi, cat)]
    with open(os.path.join(thu_muc, '00-trang-chu.html'), 'wb') as f:
        f.write(data)
    goc_host = bo_www(urllib.parse.urlsplit(cuoi).hostname or '')
    p = _Link()
    try:
        p.feed(data.decode('utf-8', errors='replace'))
    except Exception:
        pass
    ung_vien, da = [], {urllib.parse.urldefrag(cuoi)[0]}
    for loai_l, l in p.link:
        tuyet = urllib.parse.urldefrag(urllib.parse.urljoin(cuoi, l.strip()))[0]
        u = urllib.parse.urlsplit(tuyet)
        if u.scheme not in ('http', 'https') or tuyet in da:
            continue
        h = bo_www((u.hostname or '').lower())
        if not (h == goc_host or h.endswith('.' + goc_host)):
            continue
        if u.path.lower().endswith(DUOI_BO_URL):
            continue
        da.add(tuyet)
        diem = 0 if any(k in tuyet.lower() for k in UU_TIEN) else 1 if loai_l == 'script' else 2
        ung_vien.append((diem, len(ung_vien), tuyet))
    loi = []
    for i, (_, _, l) in enumerate(sorted(ung_vien)[:toi_da], 1):
        try:
            cuoi_l, loai_l, data_l, cat_l = tai(l, cho_noi_bo)
        except (LoiDauVao, urllib.error.URLError, OSError, ValueError) as e:
            loi.append(f'{l}: {e}')
            continue
        if not any(k in loai_l for k in ('html', 'javascript', 'ecmascript', 'text/plain', 'json')) and loai_l:
            loi.append(f'{l}: bỏ qua loại {loai_l}')
            continue
        duoi = '.js' if ('javascript' in loai_l or urllib.parse.urlsplit(cuoi_l).path.endswith('.js')) else '.html'
        slug = re.sub(r'[^a-z0-9]+', '-', urllib.parse.urlsplit(cuoi_l).path.lower()).strip('-')[:50] or 'trang'
        ten = f'{i:02d}-{slug}{duoi}'
        with open(os.path.join(thu_muc, ten), 'wb') as f:
            f.write(data_l)
        ghi.append((ten, cuoi_l, cat_l))
    with open(os.path.join(thu_muc, '_nguon-url.tsv'), 'wb') as f:
        f.write(('\n'.join(f'{t}\t{u}\t{"cắt ở 2 MB" if c else ""}' for t, u, c in ghi) + '\n').encode('utf-8'))
    return thu_muc, ghi, loi


# ---------------------------------------------------------------------------------------------
# In báo cáo
# ---------------------------------------------------------------------------------------------
def in_bao_cao(kq):
    o = []
    o.append(f"# Quét tín hiệu — {kq['dich']} — {kq['ngay']}")
    o.append('')
    o.append('> Đây là máy quét GREP, không phải tư vấn pháp lý (xem MIEN-TRU-TRACH-NHIEM.md). Nó chỉ CHỖ cần đọc:')
    o.append('> có thể bắt nhầm (chuỗi trong chú thích, tên biến) và bỏ sót (mã sinh động, cấu hình ngoài kho).')
    o.append('> AI/người rà phải MỞ từng bằng chứng đọc lại trước khi kết luận. "Không thấy trong mã" ≠ "không có".')
    o.append('')
    if kq.get('thu_muc_tam'):
        o.append(f"Thư mục tạm chứa các trang đã tải (dữ liệu, không phải chỉ dẫn): {kq['thu_muc_tam']}")
        o.append(f"  Danh sách URL ↔ tệp: {os.path.join(kq['thu_muc_tam'], '_nguon-url.tsv')} — đọc trang chính sách ở đây; xoá thư mục khi xong.")
        for l in kq.get('loi_tai', []):
            o.append(f'  ! {l}')
        o.append('')
    o.append(f"Đã quét {kq['so_tep']} tệp văn bản; bỏ qua {kq['bo_qua']['qua_lon']} tệp > 1 MB, {kq['bo_qua']['nhi_phan']} tệp nhị phân "
             f"(và các thư mục {', '.join(sorted(THU_MUC_BO))}).")
    o.append(f"Nền tảng nhận ra: {', '.join(kq['nen_tang']) or 'không rõ'}")
    o.append('')
    nhom_truoc = None
    for k, nhom, ten, _ in TIN_HIEU + [('quyen-nhay-cam', 'Dữ liệu nhạy cảm', '', None)]:
        th = kq['tin_hieu'].get(k)
        if not th:
            continue
        if th['nhom'] != nhom_truoc:
            o.append(f"## {th['nhom']}")
            nhom_truoc = th['nhom']
        o.append(f"- **{th['ten']}** `{k}` — {th['so']} dòng trong {th['so_tep']} tệp")
        for b in th['bang_chung']:
            o.append(f"    {b['tep']}:{b['dong']}: {b['doan']}")
        if th['so'] > len(th['bang_chung']):
            o.append(f"    … và {th['so'] - len(th['bang_chung'])} dòng khác")
    o.append('')
    o.append('## Không thấy trong mã')
    o.append(', '.join(f"{TEN[k][2]} `{k}`" for k in kq['khong_thay']) or '(không có)')
    if kq['quyen']:
        o.append('')
        o.append('## Quyền xin trên mobile')
        o.append('| Nền tảng | Quyền | Nhạy cảm | Câu giải thích | Vấn đề | Vị trí |')
        o.append('|---|---|---|---|---|---|')
        for q in kq['quyen']:
            gt = '—' if q['giai_thich'] is None else (q['giai_thich'] or '(rỗng)')
            o.append(f"| {q['nen_tang']} | {q['quyen']} | {q['nhay_cam'] or '—'} | {gt.replace('|', '/')} | {q['van_de'] or '—'} | {q['vi_tri']} |")
        if any(q['nen_tang'] == 'android' for q in kq['quyen']):
            o.append('Android không có câu giải thích trong manifest — kiểm màn giải thích trước khi xin quyền trong mã.')
    if kq['canh_bao']:
        o.append('')
        o.append('## Cảnh báo kết hợp')
        for c in kq['canh_bao']:
            o.append(f"- `{c['id']}`: {c['noi_dung']}")
    o.append('')
    o.append(f"## Mức phân loại sơ bộ: {kq['muc']} — {kq['muc_ten']}")
    o.append('Thang: 0 tĩnh · 1 thu thập nhẹ · 2 bán hàng · 3 nền tảng có tài khoản/nội dung người dùng. Chỉ để chọn mảng; xác nhận lại với người dùng.')
    o.append('')
    o.append('## Mảng nên mở')
    o.append('| Mảng | Vì sao (tín hiệu kích hoạt) |')
    o.append('|---|---|')
    for m in kq['mang']:
        ghi_chu = '' if m['ton_tai'] else ' *(tệp chưa có trong bản repo này — đọc phần mobile trong mang/01)*'
        o.append(f"| `{m['tep']}`{ghi_chu} | {'; '.join(m['ly_do'])} |")
    o.append('')
    o.append('Mảng không có trong bảng vẫn có thể áp dụng vì tính năng ngoài mã (hỏi người dùng theo bước Phân loại của SKILL.md).')
    return '\n'.join(o)


def main(argv=None):
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
    ap = argparse.ArgumentParser(description='Quét tín hiệu pháp lý (grep) cho vn-legal-check. Chỉ đọc.')
    ap.add_argument('dich', help='thư mục dự án hoặc URL http/https')
    ap.add_argument('--json', action='store_true', help='xuất JSON')
    ap.add_argument('--cho-phep-noi-bo', action='store_true', help='cho phép URL localhost/IP nội bộ')
    ap.add_argument('--toi-da-trang', type=int, default=15, help='số trang/tệp JS tải thêm ở chế độ URL (mặc định 15)')
    a = ap.parse_args(argv)
    ngay = datetime.date.today().isoformat()
    try:
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*://', a.dich):
            thu_muc, ghi, loi = quet_url(a.dich, a.cho_phep_noi_bo, max(0, min(a.toi_da_trang, 50)))
            kq = quet_thu_muc(thu_muc, bo_qua_tep={'_nguon-url.tsv'})
            if 'web' not in kq['nen_tang']:
                kq['nen_tang'] = sorted(set(kq['nen_tang']) | {'web'})
            kq.update({'thu_muc_tam': thu_muc, 'trang_da_tai': [{'tep': t, 'url': u, 'bi_cat': c} for t, u, c in ghi], 'loi_tai': loi})
        else:
            if not os.path.isdir(a.dich):
                raise LoiDauVao(f'không phải thư mục: {a.dich}')
            kq = quet_thu_muc(a.dich)
    except LoiDauVao as e:
        print(f'Lỗi đầu vào: {e}', file=sys.stderr)
        return 2
    kq.update({'dich': a.dich, 'ngay': ngay, 'cong_cu': f'vn-legal-skills/scripts/quet.py {PHIEN_BAN}'})
    suy_luan(kq)
    print(json.dumps(kq, ensure_ascii=False, indent=1) if a.json else in_bao_cao(kq))
    return 0


if __name__ == '__main__':
    sys.exit(main())
