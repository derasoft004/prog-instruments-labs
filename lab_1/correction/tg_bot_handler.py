from telebot import TeleBot

from config import TOKEN

bot = TeleBot(TOKEN)


def send_message(message, message_text):
    bot.send_message(message.chat.id, message_text)


def send_message_wth_markup(message, message_text, markup):
    bot.send_message(message.chat.id, message_text, reply_markup=markup)


