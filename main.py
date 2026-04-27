iimpot telebot
from telebot import types

# Sizning yangi tokeningiz
TOKEN = "8708022715:AAG8pQw3JVcFHWRnSWzNkcKmYoF_eZIv6EA"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    # Tugmalarni yaratamiz
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🤖 Bot haqida")
    btn2 = types.KeyboardButton("📞 Aloqa")
    markup.add(btn1, btn2)
    
    bot.send_message(message.chat.id, f"Salom {message.from_user.first_name}! Tugmalardan birini tanlang:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "🤖 Bot haqida":
        bot.send_message(message.chat.id, "Men Render-da 24/7 ishlaydigan aqlli botman!")
    elif message.text == "📞 Aloqa":
        bot.send_message(message.chat.id, "Admin bilan bog'lanish uchun: @admin_username")
    else:
        bot.send_message(message.chat.id, "Iltimos, tugmalardan birini tanlang.")

bot.polling(none_stop=True)
