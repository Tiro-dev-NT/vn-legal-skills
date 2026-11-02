"""Chạy máy quét trên bộ mẫu thử và so với kỳ vọng. Chạy: python -I scripts/chay-mau-thu.py  (exit 1 nếu có mẫu sai).

Mỗi mẫu là kiem-thu/mau-du-an/<tên>/ gồm du-an/ (dự án giả để quét) và MONG-DOI.json:
  muc                 mức phân loại phải ra (0–3)
  phai_co             mã tín hiệu / cảnh báo kết hợp / nền tảng phải có
  khong_duoc_co       mã không được có
  khong_duoc_in       chuỗi không được xuất hiện trong đầu ra (kiểm việc che khoá)
  mang_phai_co, mang_khong_duoc_co   tệp mảng phải / không được nằm trong bảng "Mảng nên mở"
"""
import glob, json, os, subprocess, sys

sys.stdout.reconfigure(encoding='utf-8')
GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUET = os.path.join(GOC, 'scripts', 'quet.py')


def doc(p):
    with open(p, 'rb') as f:
        return f.read().decode('utf-8')


def chay(du_an, *co):
    r = subprocess.run([sys.executable, '-I', QUET, du_an, *co], capture_output=True)
    return r.returncode, r.stdout.decode('utf-8', errors='replace'), r.stderr.decode('utf-8', errors='replace')


def kiem_mau(thu_muc):
    loi = []
    md = json.loads(doc(os.path.join(thu_muc, 'MONG-DOI.json')))
    du_an = os.path.join(thu_muc, 'du-an')
    ma, ra_json, err = chay(du_an, '--json')
    if ma != 0:
        return [f'quet.py --json exit {ma}: {err.strip()[:300]}']
    _, ra_chu, err2 = chay(du_an)
    kq = json.loads(ra_json)
    co = set(kq['tin_hieu']) | {c['id'] for c in kq['canh_bao']} | set(kq['nen_tang'])
    mang = {m['tep'] for m in kq['mang']}
    if kq['muc'] != md['muc']:
        loi.append(f"mức {kq['muc']} ≠ mong đợi {md['muc']}")
    loi += [f'thiếu {x}' for x in md.get('phai_co', []) if x not in co]
    loi += [f'không được có {x}' for x in md.get('khong_duoc_co', []) if x in co]
    loi += [f'thiếu mảng {x}' for x in md.get('mang_phai_co', []) if x not in mang]
    loi += [f'không được mở mảng {x}' for x in md.get('mang_khong_duoc_co', []) if x in mang]
    for s in md.get('khong_duoc_in', []):
        if s in ra_json or s in ra_chu:
            loi.append(f'đầu ra lộ chuỗi phải che: {s}')
    if err2.strip():
        loi.append(f'chế độ chữ in ra stderr: {err2.strip()[:200]}')
    return loi


def main():
    mau = sorted(os.path.dirname(p) for p in glob.glob(os.path.join(GOC, 'kiem-thu', 'mau-du-an', '*', 'MONG-DOI.json')))
    if not mau:
        print('FAIL — không tìm thấy mẫu nào trong kiem-thu/mau-du-an/')
        return 1
    sai = 0
    for m in mau:
        loi = kiem_mau(m)
        ten = os.path.basename(m)
        if loi:
            sai += 1
            print(f'FAIL {ten}: ' + '; '.join(loi))
        else:
            print(f'OK   {ten}')
    # Đầu vào sai phải ra exit 2
    ma, _, _ = chay(os.path.join(GOC, 'kiem-thu', 'mau-du-an', 'khong-ton-tai'))
    if ma != 2:
        sai += 1
        print(f'FAIL đầu vào sai: exit {ma} ≠ 2')
    ma, _, _ = chay('http://127.0.0.1/')
    if ma != 2:
        sai += 1
        print(f'FAIL URL nội bộ không bị từ chối: exit {ma} ≠ 2')
    print(f"{'OK' if not sai else 'FAIL'} — {len(mau)} mẫu, {sai} sai")
    return 1 if sai else 0


if __name__ == '__main__':
    sys.exit(main())
