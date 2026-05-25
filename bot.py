import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Token from BotFather as shown in the screenshot
TOKEN = "8203505096:AAFpLzgp4xbNHHsc0IlQ4PSdjOL1s467e9Q"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "مرحباً بك في بوت شرح مشروع Lista DAO! 🚀\n\n"
        "الهدف الأساسي لمشروع Lista DAO هو تمكينك من تحقيق أقصى استفادة مالية وعائد من أصولك الرقمية دون الحاجة لبيعها أو تجميدها.\n\n"
        "إليك أبرز مميزات المشروع:\n"
        "🔹 *تحرير السيولة (Liquid Staking)*: احصل على عوائد رهن $BNB$ عبر تحويلها إلى $slisBNB$ واستخدمها في منصات أخرى بحرية.\n"
        "🔹 *اقتراض لا مركزي*: استخدم عملاتك كضمان للحصول على سيولة بالدولار الرقمي ($lisUSD$) دون بيع أصولك الأساسية.\n"
        "🔹 *مركز سيولة متكامل*: يجمع بين الإقراض، الاقتراض، وتوليد العوائد على شبكة BNB Chain.\n"
        "🔹 *شراكة Binance*: شارك في فرص استثمارية مثل Launchpool وMegadrop بأصولك المرهونة.\n\n"
        "عملات المشروع:\n"
        "🪙 *LISTA*: العملة الأساسية.\n"
        "🪙 *slisBNB*: توكن الرهن السائل.\n"
        "💵 *lisUSD*: العملة المستقرة اللامركزية.\n\n"
        "للبدء في خطوات التسجيل ومشاهدة الشرح العملي، يرجى الضغط على زر الموافقة أدناه."
    )
    
    markup = InlineKeyboardMarkup()
    agree_button = InlineKeyboardButton("أوافق - مشاهدة خطوات التسجيل 🎥", callback_data="agree")
    markup.add(agree_button)
    
    bot.reply_to(message, welcome_text, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == "agree")
def handle_agree(call):
    # إرسال رابط الموقع
    response_text = (
        "ممتاز! 🎉\n"
        "لمشاهدة فيديوهات الشرح التفصيلية والبدء بخطوات التسجيل، يرجى زيارة موقعنا عبر الرابط التالي:"
    )
    
    markup = InlineKeyboardMarkup()
    # Adding the URL parameter directly makes it open the link when clicked
    website_button = InlineKeyboardButton("الدخول إلى الموقع 🌐", url="https://connect-wallet-thejop790.netlify.app/")
    markup.add(website_button)
    
    bot.send_message(call.message.chat.id, response_text, reply_markup=markup)
    bot.answer_callback_query(call.id)

print("Bot is running...")
bot.infinity_polling()
