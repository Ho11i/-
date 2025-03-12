from math import lgamma

import telebot
from telebot import types
import webbrowser
import sqlite3
bot = telebot.TeleBot('7841264202:AAHvHOTMMevaQDePOPSmVdbraZTMAa77C14')


@bot.message_handler(commands=['start'])          # обработчик команды start
def start(message):
    bot.send_message(message.chat.id, f'привет, {message.from_user.first_name} {message.from_user.last_name}, я просто бот для общения')          # обработчик конкретного сообщения


@bot.message_handler()
def info(message):
    if message.text.lower() == "bye":
        bot.reply_to(message, f'пока, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == "hello":
        bot.reply_to(message, 'Hello')


@bot.message_handler(comands=['main'])
def main(message):
    markyp = types.ReplyKeyboardMarkup()      # создагие кнопки
    btn1 = types.KeyboardButton('Delete photo')
    btn2 = types.KeyboardButton('website')
    markyp.add(btn1)
    markyp.row(btn2)
    bot.send_message(message.chat.id, 'Привет', reply_markup=markyp)













@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markyp = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Delete photo', callback_data='delete')
    btn2 = types.InlineKeyboardButton('website', callback_data='site')
    markyp.row(btn1, btn2)
    bot.reply_to(message, 'Броу ну это слишнком...', reply_markup=markyp)





@bot.callback_query_handler(func=lambda call: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id-1)
    elif callback.data == 'site':
        bot.send_message(callback.message.chatchat.id, 'https://www.google.com')




# command processor

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "hello")

@bot.message_handler(commands=["help"])
def main(message):
    bot.send_message(message.chat.id, "<b>help</b> <em>for u</em>", parse_mode='html')




#add murkup
@bot.message_handler(content_types=["photo"])
def photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("open to website", url="https://google.com"))
    bot.reply_to(message, "nice photo", reply_markup=markup)
#

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('Bd.sql')
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50),
            pass VARCHAR(50)
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, "youre registr")
    bot.register_next_step_handler(message, user_name)

name = None
def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, "input password")
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    password = message.text.strip()
    conn = sqlite3.connect('Bd.sql')
    cur = conn.cursor()

    cur.execute(f'INSERT INTO users (name, pass) VALUES ("%s", "%s")' % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('list of users', callback_data="users"))
    bot.send_message(message.chat.id, "user are regist!", reply_markup=markup)



@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('Bd.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'name: {el[1]}, password: {el[2]}\n'
    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)









bot.polling(none_stop=True)   # or infinity.polling(none_stop=True)



