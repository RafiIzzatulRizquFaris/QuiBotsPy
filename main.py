import mysql.connector
import telebot

bot = telebot.TeleBot("1114319677:AAF-hufSU3ApwicjNaJeahTe4LlC6GdjlC8")
connector = mysql.connector.connect(host='localhost', user='root', password='', database='indohoteldb')
cursor = connector.cursor()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi! \n To look the entire room that we have type /room \n")


@bot.message_handler(commands=['room'])
def send_welcome(message):
    data_result = ''
    cursor.execute("SELECT * FROM `kamar` ")
    data = cursor.fetchall()
    row = cursor.rowcount
    print(data)
    if row > 0:
        numbering = 0
        for x in data:
            numbering += 1
            data_result = data_result + str(numbering) + ". " + str(x) + '\n'
        bot.reply_to(message, str(data_result))


bot.polling()
