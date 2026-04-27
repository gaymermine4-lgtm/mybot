import telebot
from telebot import types

# Sizning tokeningiz
TOKEN = "8708022715:AAG8pQw3JVcFHWRnSWzNkcKmYoF_eZIv6EA"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    # Asosiy menyu tugmalari
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("👤 Profilim")
    btn2 = types.KeyboardButton("⚙️ Sozlamalar")
    btn3 = types.KeyboardButton("📚 Kurslar")
    btn4 = types.KeyboardButton("📞 Aloqa")
    
    markup.add(btn1, btn2, btn3, btn4)
    
    welcome_text = f"Salom {message.from_user.first_name}! Botingizga xush kelibsiz.\nQuyidagi menyudan foydalaning:"
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    if message.text == "👤 Profilim":
        user_info = (f"Sizning profilingiz:\n\n"
                     f"Ism: {message.from_user.first_name}\n"
                     f"ID: {message.from_user.id}")
        bot.send_message(message.chat.id, user_info)
        
    elif message.text == "⚙️ Sozlamalar":
        bot.send_message(message.chat.id, "Hozircha sozlamalar bo'limi bo'sh.")
        
    elif message.text == "📚 Kurslar":
        bot.send_message(message.chat.id, "Tez kunda yangi kurslar qo'shiladi!")
        
    elif message.text == "📞 Aloqa":
        bot.send_message(message.chat.id, "Admin bilan bog'lanish: @admin_username")
        
    else:
        bot.send_message(message.chat.id, "Iltimos, pastdagi tugmalardan foydalaning.")

if __name__ == "__main__":
    bot.polling(none_stop=True)
