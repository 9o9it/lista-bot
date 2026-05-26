# تعليمات النشر على منصة مجانية (Render)

## الطريقة 1: استخدام Render (مجاني)

### الخطوة 1: إنشاء حساب على Render
1. اذهب إلى https://render.com
2. سجل حساب جديد باستخدام GitHub أو البريد الإلكتروني

### الخطوة 2: ربط المشروع بـ GitHub
1. ارفع الكود إلى GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/USERNAME/REPO-NAME.git
   git push -u origin main
   ```

### الخطوة 3: إنشاء Web Service على Render
1. في لوحة تحكم Render، اضغط "New +"
2. اختر "Web Service"
3. اختر المستودع من GitHub
4. املأ الإعدادات:
   - **Name**: lista-bot (أو أي اسم تريده)
   - **Environment**: Python 3
   - **Branch**: main
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot.py`
   - **Instance Type**: Free

### الخطوة 4: إضافة متغيرات البيئة
1. في قسم "Environment Variables"
2. أضف متغير جديد:
   - **Key**: `TOKEN`
   - **Value`: `8203505096:AAFpLzgp4xbNHHsc0IlQ4PSdjOL1s467e9Q`

### الخطوة 5: النشر
1. اضغط "Create Web Service"
2. انتظر حتى ينتهي النشر (سيستغرق بضع دقائق)
3. البوت سيعمل تلقائياً

---

## الطريقة 2: استخدام Railway (مجاني)

### الخطوة 1: إنشاء حساب
1. اذهب إلى https://railway.app
2. سجل حساب جديد

### الخطوة 2: إنشاء مشروع جديد
1. اضغط "New Project"
2. اختر "Deploy from GitHub repo"
3. اختر مستودعك

### الخطوة 3: إضافة متغيرات البيئة
1. اذهب إلى "Variables"
2. أضف: `TOKEN=8203505096:AAFpLzgp4xbNHHsc0IlQ4PSdjOL1s467e9Q`

### الخطوة 4: النشر
1. Railway سيكتشف تلقائياً أنه مشروع Python
2. سيبدأ النشر تلقائياً

---

## الطريقة 3: استخدام PythonAnywhere (مجاني للبوتات)

### الخطوة 1: إنشاء حساب
1. اذهب إلى https://www.pythonanywhere.com
2. سجل حساب مجاني (Beginner account)

### الخطوة 2: رفع الملفات
1. اذهب إلى "Files"
2. ارفع: bot.py, requirements.txt

### الخطوة 3: تثبيت المكتبات
1. اذهب إلى "Consoles"
2. أنشئ console جديد (Bash)
3. شغل: `pip install pyTelegramBotAPI==4.15.4`

### الخطوة 4: إنشاء Task
1. اذهب إلى "Tasks"
2. أضف task جديد:
   - **Description**: Telegram Bot
   - **Command**: `python3 /home/USERNAME/bot.py`
   - **Interval**: 5 minutes

---

## ملاحظات هامة
- البوت يعمل 24/7 على Render وRailway
- PythonAnywhere المجاني يعمل فقط لفترات محدودة
- تأكد من إبقاء الـ Token سرياً
- يمكنك مراقبة البوت من لوحة تحكم المنصة
