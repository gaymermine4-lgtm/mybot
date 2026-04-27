import telebot
from telebot import types

TOKEN = "8708022715:AAG8pQw3JVcFHWRnSWzNkcKmYoF_eZIv6EA"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("🤖 Bot haqida"), types.KeyboardButton("📞 Aloqa"))
    bot.send_message(message.chat.id, "Bot ishga tushdi! Tugmani tanlang:", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def echo(message):
    if message.text == "🤖 Bot haqida":
        bot.reply_to(message, "Men Renderda 24/7 ishlayapman!")
    elif message.text == "📞 Aloqa":
        bot.reply_to(message, "Admin: @admin_username")
    else:
        bot.reply_to(message, "Iltimos, tugmalardan foydalaning.")

if __name__ == "__main__":
    bot.polling(none_stop=True)
