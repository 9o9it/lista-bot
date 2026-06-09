# تعليمات النشر على منصات تدعم العمل 24/7

## الطريقة 1: استخدام Railway (مجاني - يعمل 24/7) ⭐

### الخطوة 1: إنشاء حساب
1. اذهب إلى https://railway.app
2. سجل حساب جديد باستخدام GitHub

### الخطوة 2: إنشاء مشروع جديد
1. اضغط "New Project"
2. اختر "Deploy from GitHub repo"
3. اختر مستودع: `9o9it/lista-bot`

### الخطوة 3: إضافة متغيرات البيئة
1. اذهب إلى "Variables"
2. أضف: `TOKEN=8203505096:AAFpLzgp4xbNHHsc0IlQ4PSdjOL1s467e9Q`

### الخطوة 4: النشر
1. Railway سيكتشف تلقائياً أنه مشروع Python
2. سيبدأ النشر تلقائياً
3. البوت سيعمل 24/7 بدون توقف

---

## الطريقة 2: استخدام Fly.io (مجاني - يعمل 24/7)

### الخطوة 1: تثبيت Fly CLI
```bash
curl -L https://fly.io/install.sh | sh
```

### الخطوة 2: تسجيل الدخول
```bash
fly auth login
```

### الخطوة 3: إنشاء التطبيق
```bash
fly launch
```

### الخطوة 4: إضافة متغيرات البيئة
```bash
fly secrets set TOKEN=8203505096:AAFpLzgp4xbNHHsc0IlQ4PSdjOL1s467e9Q
```

### الخطوة 5: النشر
```bash
fly deploy
```

---

## الطريقة 3: استخدام Oracle Cloud Free Tier (مجاني - يعمل 24/7)

### الخطوة 1: إنشاء حساب
1. اذهب إلى https://www.oracle.com/cloud/free/
2. سجل حساب مجاني (يتطلب بطاقة ائتمان للتحقق فقط)

### الخطوة 2: إنشاء Instance
1. اذهب إلى "Compute"
2. اضغط "Create Instance"
3. اختر: "Always Free" configuration
4. اختر Ubuntu 22.04

### الخطوة 3: الاتصال بالسيرفر
```bash
ssh ubuntu@your-instance-ip
```

### الخطوة 4: تثبيت Python والمكتبات
```bash
sudo apt update
sudo apt install python3-pip -y
pip3 install pyTelegramBotAPI==4.15.4
```

### الخطوة 5: رفع الملفات وتشغيل البوت
```bash
# رفع bot.py إلى السيرفر
export TOKEN=8203505096:AAFpLzgp4xbNHHsc0IlQ4PSdjOL1s467e9Q
python3 bot.py
```

### الخطوة 6: استخدام systemd للتشغيل الدائم
```bash
sudo nano /etc/systemd/system/telegram-bot.service
```

أضف المحتوى التالي:
```ini
[Unit]
Description=Telegram Bot
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu
Environment="TOKEN=8203505096:AAFpLzgp4xbNHHsc0IlQ4PSdjOL1s467e9Q"
ExecStart=/usr/bin/python3 /home/ubuntu/bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

شغله:
```bash
sudo systemctl enable telegram-bot
sudo systemctl start telegram-bot
```

---

## الطريقة 4: استخدام Render (مدفوع - يعمل 24/7)

### الخطوة 1: إنشاء حساب
1. اذهب إلى https://render.com
2. سجل حساب جديد

### الخطوة 2: إنشاء Web Service
1. اضغط "New +"
2. اختر "Web Service"
3. اختر مستودع: `9o9it/lista-bot`
4. املأ الإعدادات:
   - **Name**: lista-bot
   - **Environment**: Python 3
   - **Branch**: main
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot.py`
   - **Instance Type**: Starter ($7/month) - يعمل 24/7

### الخطوة 3: إضافة متغيرات البيئة
1. في قسم "Environment Variables"
2. أضف: `TOKEN=8203505096:AAFpLzgp4xbNHHsc0IlQ4PSdjOL1s467e9Q`

### الخطوة 4: النشر
1. اضغط "Create Web Service"
2. انتظر حتى ينتهي النشر

---

## مقارنة المنصات

| المنصة | السعر | العمل 24/7 | سهولة الاستخدام |
|--------|--------|-------------|------------------|
| **Railway** | مجاني ($5/month) | ✅ نعم | ⭐⭐⭐⭐⭐ |
| **Fly.io** | مجاني | ✅ نعم | ⭐⭐⭐⭐ |
| **Oracle Cloud** | مجاني | ✅ نعم | ⭐⭐⭐ |
| **Render** | $7/month | ✅ نعم | ⭐⭐⭐⭐⭐ |

---

## التوصية

**Railway هو الخيار الأفضل** لأن:
- مجاني (رصيد $5 شهرياً)
- يعمل 24/7 بدون توقف
- سهل الإعداد جداً
- واجهة مستخدم بسيطة

---

## ملاحظات هامة
- تأكد من إبقاء الـ Token سرياً
- يمكنك مراقبة البوت من لوحة تحكم المنصة
- Railway يوفر رصيد $5 شهرياً مجاناً (يكفي للبوت)
