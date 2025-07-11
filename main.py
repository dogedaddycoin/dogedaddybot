import os
import telebot
from telebot import types

API_KEY = os.getenv("API_KEY")
bot = telebot.TeleBot(API_KEY)

# 🔹 COMMANDS
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👑 Welcome to DogeDaddyBot!\nUse /chart, /buy, /website or /tokenomics to learn more.")

@bot.message_handler(commands=['chart'])
def chart(message):
    bot.reply_to(message, "📊 Chart: https://dexscreener.com/solana/bnrpnul3p6zfsvwv6nfyat2xns2ozgrcqvcuk4hpkawk")

@bot.message_handler(commands=['buy'])
def buy(message):
    bot.reply_to(message, "🛒 How to buy $DADDY: https://dogedaddycoin.xyz/#howtobuy")

@bot.message_handler(commands=['website'])
def website(message):
    bot.reply_to(message, "🌐 Website: https://dogedaddycoin.xyz")

@bot.message_handler(commands=['twitter'])
def twitter(message):
    bot.reply_to(message, "🐦 Twitter: https://x.com/DogeDaddySol")

@bot.message_handler(commands=['telegram', 'community'])
def telegram(message):
    bot.reply_to(message, "💬 Telegram: https://t.me/dogedaddy_officiall")

@bot.message_handler(commands=['roadmap'])
def roadmap(message):
    bot.reply_to(message, "🗺️ Roadmap: Coming soon on the website!")

@bot.message_handler(commands=['tokenomics'])
def tokenomics(message):
    bot.reply_to(message, "📦 Tokenomics:\n80% LP Burned 🔥\n0% Tax ✅\nNo Team Wallet 💼")

@bot.message_handler(commands=['snipe'])
def snipe(message):
    bot.reply_to(message, "🚀 Sniper Mode: Coming soon with live buy tracker!")

@bot.message_handler(commands=['meme'])
def meme_drop(message):
    bot.reply_to(message, "😂 Here's your meme, degen:\nhttps://i.imgur.com/TxZ5KXG.jpeg")

# 🔹 Keyword Triggers
@bot.message_handler(func=lambda m: True)
def keyword_responses(message):
    msg = message.text.lower()

    if "how to buy" in msg:
        bot.reply_to(message, "🧾 Visit https://dogedaddycoin.xyz/#howtobuy for steps to buy $DADDY.")
    elif "chart" in msg:
        bot.reply_to(message, "📈 Live chart: https://dexscreener.com/solana/bnrpnul3p6zfsvwv6nfyat2xns2ozgrcqvcuk4hpkawk")
    elif "who is your daddy" in msg or "$daddy" in msg:
        bot.reply_to(message, "👑 $DADDY is your Solana meme king. Join us: https://t.me/DogeDaddy_Official")
    else:
        bot.reply_to(message, "👋 I'm DogeDaddyBot! Try /start or ask 'how to buy $DADDY'.")

bot.infinity_polling()
