import os
import telebot

TOKEN = os.getenv("TOKEN")  # سيأخذ التوكن من Render
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "البوت شغال 24 ساعة على Render ✔")

bot.polling()