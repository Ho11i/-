import telebot
from telebot import types


bot = telebot.TeleBot('7903847896:AAH3vRhLsrhcBdruoH_f-_kh5vaxU57ZMpQ')

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("понедельник")
    btn2 = types.KeyboardButton("вторник")
    btn3 = types.KeyboardButton("среда")
    btn4 = types.KeyboardButton("четверг")
    btn5 = types.KeyboardButton("пятница")
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    markup.add(btn5)
    bot.send_message(message.chat.id, "привет, {0.first_name} я бот расписание".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=["text"])
def func(message):
    if message.text == "понедельник":
        bot.send_message(message.chat.id, "8:30 - 10:00 Введение в професию\n10:10 - 11:40 Введение в "
                                          "профессию\n13:00 - 14:30 Метрология")
    elif message.text == "вторник":
        bot.send_message(message.chat.id, "8:30 - 10:00 Основы Российского Государства\n10:10 - 11:40 Физика("
                                          "Практика)\n12:20 - 13:50 физическая культура\n14:00 - 15:30 Математический "
                                          "анализ(практика)\n 15:40 - 17:10 Математический анализ")
    elif message.text == "среда":
        bot.send_message(message.chat.id, "8:30 - 10:00 Общественный проект\n10:10 - 11:40 философия\n12:20 - 13:50 "
                                          "Математический анализ")
    elif message.text == "четверг":
        bot.send_message(message.chat.id, "10:10 - 11:40 физика\n12:20 - 13:50 "
                                          "философия\n14:00 - 15:30 Иностранный язык")
    elif message.text == "пятница":
        bot.send_message(message.chat.id, "8:30 - 10:00 Общественный проект\n10:10 - 11:40  Математический "
                                          "анализ\n12:20 - 13:50 Основы информатики")















bot.polling(none_stop=True)


