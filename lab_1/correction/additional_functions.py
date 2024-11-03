import json
import time
import schedule
from datetime import datetime
from typing import Tuple

from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

from config import TOKEN
from constants import LISTMESSAGETEXT


bot = TeleBot(TOKEN)


def json_loader(filename: str) -> dict:
    with open(filename, "r") as texts_json:
        return json.load(texts_json)


flag_pay = False
s_buttons_d = []
list_classes = []


def send_message(message, message_text) -> None:
    bot.send_message(message.chat.id, message_text)


def send_message_wth_markup(message, message_text: str, markup: InlineKeyboardMarkup | ReplyKeyboardMarkup) -> None:
    bot.send_message(message.chat.id, message_text, reply_markup=markup)


def counter(s: list) -> int:
    count = 1
    tmp1 = s[0]
    for i in range(1, len(s)):
        if s[i] == tmp1: count += 1
    return count


def make_day(trainer_list: list, days_list: list, time_list: list) -> str:
    return_message = '\n'
    trainers_flag = False
    data = json_loader('texts.json')
    days = data['days']
    times = data['times']
    trainer = data['trainers']
    if len(trainer_list) > 1:
        trainers_flag = True
    if len(trainer_list) == 1:
        return_message += f'Тренер: {trainer[f"trainer{trainer_list[0]}"]}\n'
    if not trainers_flag:
        for i in range(len(days_list)):
            return_message += f'{days[f"day{days_list[i] + 1}"]} {times[f"time{time_list[i] + 1}"]} '  # trainer[trainer_list[i]]
            if i != len(days_list) - 1: return_message += f',\n'
    else:
        count = counter(trainer_list)
        return_message += f'Тренер: {trainer[f"trainer{trainer_list[0] + 1}"]}\n'
        for i in range(count):
            return_message += f'{days[f"day{days_list[i] + 1}"]} {times[f"time{time_list[i] + 1}"]} '  # trainer[trainer_list[i]]
            if i != len(days_list) - 1: return_message += f',\n'
        return_message += f'Тренер: {trainer[f"trainer{trainer_list[count - 1]}"]}\n'
        for i in range(count, len(trainer_list)):
            return_message += f'{days[f"day{days_list[i] + 1}"]} {times[f"time{time_list[i] + 1}"]} '  # trainer[trainer_list[i]]
            if i != len(days_list) - 1: return_message += f',\n'
    return return_message


def make_day_buttons(days_list: list, time_list: list, type_class: int) -> Tuple:
    global s_buttons_d
    data = json_loader('texts.json')
    days = data['days']
    times = data['times']
    types_classes = data['types_classes']
    stmp = []
    keyboard_button_day = InlineKeyboardMarkup()
    for i in range(len(days_list)):
        stmp.append(f'{days[f"day{days_list[i] + 1}"]} {times[f"time{days_list[i] + 1}"]} ')
        keyboard_button_day.add(InlineKeyboardButton(text=f'{days[f"day{days_list[i] + 1}"]} {times[f"time{time_list[i] + 1}"]} ',
                                                     callback_data=f'day_button_{str(i)}'))
    s_buttons_d = stmp
    return_message = f'{types_classes[f"types_classes{type_class + 1}"]}\n ' # {week[days_list[i]]} {time[time_list[i]]}
    return return_message, keyboard_button_day


tmps = make_day_buttons([0], [0], 0) # переменная записывающая в себя временную категорию


def app_mdb(index: int) -> str:
    return s_buttons_d[index]


def adm_link() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup().add(InlineKeyboardButton("Администратор ", "t.me/ch_chrissy"))


def pay_markup(list_classes: list) -> Tuple:
    return_message = 'Ваша запись на: \n'
    murk = InlineKeyboardMarkup()
    butn = InlineKeyboardButton(text="Оплатить", callback_data="pay")
    murk.add(butn)
    for i in range(len(list_classes)):
        return_message += str(list_classes[i])
    return return_message, murk



LISTMESSAGETIME = [0, 0]
LISTID = []


def dotime() -> None:
    time_now = str(str(datetime.now()).split(' ')[1][:5])
    if time_now == LISTMESSAGETIME[0]:
        for i in range(len(LISTID)):
            bot.send_message(LISTID[i], LISTMESSAGETEXT[0])


def schedule_handler() -> None:
    schedule.every(60).seconds.do(dotime)
    while True:
        schedule.run_pending()
        time.sleep(1)
