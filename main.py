import os
import telebot

API_KEY = os.getenv("API_KEY")
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "🐶 Welcome to DogeDaddyBot! Use /snipers or /chart to get started!")

@bot.message_handler(commands=['snipers'])
def snipers(message):
    bot.reply_to(message, "🔫 Snipers will be displayed here. (Coming soon...)")

@bot.message_handler(commands=['chart'])
def chart(message):
    bot.reply_to(message, "📊 Chart Link: https://dexscreener.com/solana/bnrpnul3p6zfsvwv6nfyat2xns2ozgrcqvcuk4hpkawk")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "👋 I'm DogeDaddyBot. Use /help to see what I can do!")

bot.infinity_polling()
