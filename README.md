
# تامر جابر للأقمشة — Frontend + Backend (Flask)

مشروع جاهز للرفع على GitHub.  
الفرونت إند (HTML/JS + Tailwind) + باك إند (Python Flask + SQLite).

## المتطلبات
- Python 3.13 أو أحدث
- pip
- اختياري: Postman للتجربة

## طريقة التشغيل (محليًا)
### 1) تشغيل الباك إند
```bash
cd backend
pip install -r requirements.txt
python app.py
```
سيفتح السيرفر على: `http://127.0.0.1:5000`

### 2) تشغيل الفرونت إند
افتح الملف:
```
frontend/index.html
```
(دبل كليك يفتح في المتصفح).

> لو المتصفح منع الطلبات المحلية، استخدم سيرفر بسيط:
```bash
cd frontend
python -m http.server 5500
```
ثم افتح: `http://127.0.0.1:5500/index.html`

## ملاحظات
- الصور تُحفظ Base64 داخل قاعدة بيانات SQLite (ملف `fabrics.db`).
- تقدر تغيّر رابط الباك إند من أعلى `index.html` في متغير `API_BASE`.
- لو هترفع الباك إند على استضافة/سيرفر، غيّر `API_BASE` لرابط السيرفر.
- ملفات `.gitignore` مضافة لتجنّب رفع البيئة الافتراضية وملف قاعدة البيانات.
