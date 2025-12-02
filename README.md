# SRT to DOCX Web

Chuyển file **SRT** sang **DOCX** trực tuyến bằng **Python Flask**.

**Demo trực tuyến:** [https://srt-to-docx-web.onrender.com/](https://srt-to-docx-web.onrender.com/)

---

## 📁 Cấu trúc dự án
```
SRT_TO_DOCX_WEB/
│── app.py # Flask backend
│── requirements.txt # Thư viện Python cần cài
│── Procfile # Cho Render/Heroku biết cách chạy app
│── templates/
│ └── index.html # Giao diện web
```

---

## ⚡ Tính năng

- Upload file `.srt` → nhận file `.docx` tương ứng
- Giữ nguyên nội dung, loại bỏ số thứ tự và timestamp
- Web đơn giản, dễ sử dụng

---

## 🛠 Cài đặt và chạy local

1. Clone repo:

```bash
git clone https://github.com/CaoHoangKhai/SRT_TO_DOCX_WEB.git
cd SRT_TO_DOCX_WEB
```

2. Cài thư viện Python:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

3. Chạy ứng dụng:

```bash
python app.py
```

4. Mở trình duyệt:

```cpp
http://127.0.0.1:5000
```

5. Upload file `.srt` → download `.docx`

##  🚀 Deploy trên Render

Render tự động đọc requirements.txt và Procfile

Ứng dụng chạy trên port do Render cung cấp

Demo trực tiếp: https://srt-to-docx-web.onrender.com/
