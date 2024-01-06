from transliterate import to_cyrillic, to_latin
import telebot
import logging
from config import token


bot = telebot.TeleBot(token, parse_mode=None)
logging.basicConfig(level=logging.INFO)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    javob = 'Assalomu alaykum, xush kelipsiz!'
    javob += '\nMatn kiriting:'
    bot.reply_to(message, javob)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text

    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)
    bot.reply_to(message, javob)


if __name__ == "__main__":
    bot.polling()
