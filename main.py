import telebot

# O'sha mashhur Tokenni shu yerga qo'ying
TOKEN = "7963212879:AAH8rY9rYvS1M6p7-mG9R_n9v0R8G9vR8G9" 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Men GitHub va Render orqali ishlayapman!")

bot.polling(none_stop=True)
