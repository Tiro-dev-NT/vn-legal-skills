"""Cổng kiểm các tệp của repo khớp nhau. Chạy: python scripts/kiem-nhat-quan.py  (exit 1 nếu có lỗi)."""
import glob, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(GOC)
loi = []

def doc(p):
    return open(p, 'rb').read().decode('utf-8')

nguon = doc('NGUON.md')
skill = doc('skills/vn-legal-check/SKILL.md')
readme = doc('README.md')
mang = sorted(glob.glob('mang/*.md'))
mau = sorted(glob.glob('mau/*.md'))

# 1. Văn bản được dẫn ở đâu cũng phải có dòng trong NGUON.md
RE_VB = re.compile(r'(?:NĐ|Luật|QĐ|VBHN)\s+(\d{1,3}/\d{4})')
for p in mang + mau + ['skills/vn-legal-check/SKILL.md']:
    for so in set(RE_VB.findall(doc(p))):
        if so not in nguon:
            loi.append(f'{p}: dẫn văn bản {so} nhưng NGUON.md không có')

# 2. Mảng trong thư mục == mảng trong README == mảng trong bảng chọn của SKILL
ten = [os.path.basename(p) for p in mang]
for t in ten:
    if t not in readme: loi.append(f'README.md: thiếu {t} trong cây thư mục')
    if f'mang/{t}' not in skill: loi.append(f'SKILL.md: thiếu mang/{t} trong bảng chọn mảng')
for t in set(re.findall(r'mang/(\d\d-[\w-]+\.md)', skill + readme)):
    if t not in ten: loi.append(f'SKILL/README trỏ tới mang/{t} không tồn tại')

# 3. Mã mục trong từng mảng: đúng tiền tố, không trùng, tăng dần
ma_co = set()
for p in mang:
    n = int(os.path.basename(p)[:2])
    ids = re.findall(r'^\| (\d+)\.(\d+) \|', doc(p), re.M)
    so = [int(b) for a, b in ids]
    for a, b in ids:
        if int(a) != n: loi.append(f'{p}: mục {a}.{b} sai tiền tố (phải {n}.x)')
        ma_co.add(f'{a}.{b}')
    if so != sorted(so) or len(so) != len(set(so)):
        loi.append(f'{p}: mã mục không tăng dần/trùng: {so}')

# 4. Tham chiếu chéo "mảng 1.2", "mục 1.7", "(xem 7.6)", "+ mảng 4.2" phải tồn tại
for p in mang + ['skills/vn-legal-check/SKILL.md']:
    for ref in re.findall(r'(?:mảng|mục|xem)\s+(\d+\.\d+)', doc(p)):
        if ref not in ma_co: loi.append(f'{p}: tham chiếu {ref} không tồn tại')

# 5. Miễn trừ trách nhiệm phải có ở mọi điểm chạm
for p in mang + mau + ['README.md', 'AGENTS.md', 'skills/vn-legal-check/SKILL.md']:
    if 'MIEN-TRU-TRACH-NHIEM.md' not in doc(p): loi.append(f'{p}: thiếu liên kết MIEN-TRU-TRACH-NHIEM.md')
if 'Khi chia sẻ báo cáo, giữ nguyên khối này' not in skill:
    loi.append('SKILL.md: mẫu báo cáo thiếu khối cảnh báo bắt buộc')

# 6. Liên kết tương đối trỏ tới tệp có thật
for p in glob.glob('**/*.md', recursive=True):
    for l in re.findall(r'\]\(([^)#]+?\.md)(?:#[^)]*)?\)', doc(p)):
        if l.startswith('http'): continue
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(p), l))):
            loi.append(f'{p}: liên kết hỏng {l}')

# 7. Nguồn chỉ từ cổng Nhà nước
for l in re.findall(r'https?://([^/\s)]+)', nguon + ''.join(doc(p) for p in mang)):
    if not (l.endswith('.gov.vn') or l.endswith('chinhphu.vn') or l in ('vbpl.vn', 'online.gov.vn')):
        loi.append(f'nguồn ngoài cổng Nhà nước: {l}')

# 8. Văn bản đã bị thay/bãi bỏ trong NGUON.md phải có trong LICH-SU-THAY-DOI.md
lich_su = doc('LICH-SU-THAY-DOI.md')
for dong in nguon.splitlines():
    if dong.startswith('|') and 'đã bị' in dong:
        for so in re.findall(r'(\d{1,3}/\d{4})', dong.split('|')[1]):
            if so not in lich_su: loi.append(f'LICH-SU-THAY-DOI.md: thiếu văn bản đã bị thay {so}')
if not os.path.exists('luu-tru/00-MUC-LUC.md'): loi.append('thiếu luu-tru/00-MUC-LUC.md')

print('\n'.join(loi) if loi else f'OK — {len(mang)} mảng, {len(ma_co)} mục, {len(set(RE_VB.findall(nguon)))} văn bản trong NGUON.md')
sys.exit(1 if loi else 0)
