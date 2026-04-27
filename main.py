import telebot

# O'sha mashhur Tokenni shu yerga qo'ying
TOKEN = "8708022715:AAG8pQw3JVcFHWRnSWzNkcKmYoF_eZIv6EA" 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Men GitHub va Render orqali ishlayapman!")

bot.polling(none_stop=True)
