import telebot
import asyncio
from googletrans import Translator

bot = telebot.TeleBot('7841264202:AAHvHOTMMevaQDePOPSmVdbraZTMAa77C14')

translator = Translator()

@bot.message_handler(func=lambda m: True)
def trans(message):
    asyncio.run(translate_message(message))

async def translate_message(message):
    result = await translator.translate(message.text, src='ru', dest='en')
    bot.send_message(message.chat.id, f"Translate: {result.text}")

bot.polling(non_stop=True)
