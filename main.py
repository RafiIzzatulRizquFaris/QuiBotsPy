import telebot

bot = telebot.TeleBot("1114319677:AAF-hufSU3ApwicjNaJeahTe4LlC6GdjlC8")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    my_word = message.text.split("#")
    bot.reply_to(message, my_word[2])


bot.polling()