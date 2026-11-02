// Lỗi cố ý cho mẫu thử: khoá API nằm trong mã gửi về trình duyệt.
const OPENAI_API_KEY = "sk-GIALAPKHOA0000000000000000000000";
async function gui() {
  const cauHoi = document.getElementById('cau-hoi').value;
  const res = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + OPENAI_API_KEY },
    body: JSON.stringify({ model: 'mo-hinh-mau', messages: [{ role: 'user', content: cauHoi }] })
  });
  const data = await res.json();
  document.getElementById('khung-tin').textContent = data.choices[0].message.content;
}
