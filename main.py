import mysql.connector
import telebot

bot = telebot.TeleBot("1114319677:AAF-hufSU3ApwicjNaJeahTe4LlC6GdjlC8")
connector = mysql.connector.connect(host='localhost', user='root', password='', database='indohoteldb')
cursor = connector.cursor()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi! \n To look the entire room that we have type /room \n")


@bot.message_handler(commands=['reservation'], func=lambda message: True)
def echo_all(message):
    order = message.text.split('#')
    room_number = order[1]
    name = order[2]
    telephone = order[3]
    id_number = order[4]
    cursor.execute(
        "INSERT INTO `pelanggan` (`id_pelanggan`, `nama_pelanggan`, `nomor_telepon`, `nomor_identitas`) VALUES (NULL, '" + name + "', '" + telephone + "', '" + id_number + "');")
    connector.commit()
    cursor.execute("SELECT pelanggan.id_pelanggan FROM `pelanggan` WHERE `nama_pelanggan` LIKE '%" + name + "%' ")
    data_customer = cursor.fetchone()
    data_customer_str = str(data_customer)
    data_customer_str = data_customer_str.replace('(', '')
    data_customer_str = data_customer_str.replace(')', '')
    data_customer_str = data_customer_str.replace(',', '')
    cursor.execute(
        "INSERT INTO `reservasi` (`id_reservasi`, `id_pelanggan`, `id_kamar`, `tgl_checkin`) VALUES (NULL, '" + data_customer_str.strip() + "', '" + idKamar + "', CURRENT_DATE());")
    connector.commit()
    bot.reply_to(message, data_customer_str.strip())


@bot.message_handler(commands=['room'])
def send_room(message):
    data_result = ''
    cursor.execute(
        "SELECT kamar.nomor_kamar, jeniskamar.nama_jenis_kamar, jeniskamar.harga_jenis_kamar, jeniskamar.keterangan FROM jeniskamar, kamar LEFT JOIN reservasi ON reservasi.id_kamar = kamar.id_kamar WHERE reservasi.id_reservasi IS null AND kamar.id_jenis_kamar = jeniskamar.id_jenis_kamar "
    )
    data = cursor.fetchall()
    row = cursor.rowcount
    if row > 0:
        numbering = 0
        for x in data:
            numbering += 1
            data_result = data_result + str(numbering) + ". " + str(x) + '\n'
            data_result = data_result.replace('(', '')
            data_result = data_result.replace(')', '')
            data_result = data_result.replace("'", '')
            data_result = data_result.replace(",", '')
        bot.reply_to(message, str(data_result))


bot.polling()
