// Lỗi cố ý cho mẫu thử: khoá ký VNPay nằm ở mã chạy trên trình duyệt.
const vnp_TmnCode = "GIALAP01";
const vnp_HashSecret = "GIA_LAP_HASH_SECRET_000";
function taoUrlThanhToan(soTien) {
  const thamSo = { vnp_Amount: soTien * 100, vnp_TmnCode: vnp_TmnCode, vnp_Command: 'pay' };
  return 'https://sandbox.vnpayment.vn/paymentv2/vpcpay.html?' + new URLSearchParams(thamSo);
}
