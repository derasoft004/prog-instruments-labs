from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
import json


def json_loader(filename: str) -> dict:
    with open(filename, "r") as texts_json:
        return json.load(texts_json)

listmessagetext = ["_", ';']
listmessagetime = [0, 0]

flag_pay = False


def counter(s):
    count = 1
    tmp1 = s[0]
    for i in range(1, len(s)):
        if s[i] == tmp1: count += 1
    return count


def make_day(trainer_list, days_list, time_list):
    return_message = ''
    return_message += '\n'
    trainers = False
    if len(trainer_list) > 1: trainers = True
    if len(trainer_list) == 1: return_message += f'Тренер: {trainer[trainer_list[0]]}\n'
    if not trainers:
        for i in range(len(days_list)):
            return_message += f'{week[days_list[i]]} {time_s[time_list[i]]} '  # trainer[trainer_list[i]]
            if i != len(days_list) - 1: return_message += f',\n'
    else:
        count = counter(trainer_list)
        return_message += f'Тренер: {trainer[trainer_list[0]]}\n'
        for i in range(count):
            return_message += f'{week[days_list[i]]} {time_s[time_list[i]]} '  # trainer[trainer_list[i]]
            if i != len(days_list) - 1: return_message += f',\n'
        return_message += f'Тренер: {trainer[trainer_list[count]]}\n'
        for i in range(count, len(trainer_list)):
            return_message += f'{week[days_list[i]]} {time_s[time_list[i]]} '  # trainer[trainer_list[i]]
            if i != len(days_list) - 1: return_message += f',\n'
    return return_message


def make_day_buttons(days_list, time_list, type_class):
    global s_buttons_d
    stmp = []
    keyboard_button_day = InlineKeyboardMarkup()
    for i in range(len(days_list)):
        stmp.append(f'{week[days_list[i]]} {time_s[time_list[i]]} ')
        keyboard_button_day.add(InlineKeyboardButton(text=f'{week[days_list[i]]} {time_s[time_list[i]]} ',
                                                     callback_data=f'day_button_{str(i)}'))
    s_buttons_d = stmp
    return_message = f'{types_classes[type_class]}\n ' # {week[days_list[i]]} {time[time_list[i]]}
    return return_message, keyboard_button_day

tmps = make_day_buttons([0], [0], 0) # переменная записывающая в себя тмпшную категорию


def app_mdb(index):
    global s_buttons_d
    return s_buttons_d[index]


def adm_link():
    return InlineKeyboardMarkup().add(InlineKeyboardButton("Администратор ",
                                      "t.me/ch_chrissy"))

def pay_markup(list_classes):
    return_message = 'Ваша запись на: \n'
    murk = InlineKeyboardMarkup()
    butn = InlineKeyboardButton(text="Оплатить", callback_data="pay")
    murk.add(butn)
    for i in range(len(list_classes)):
        return_message += str(list_classes[i])
    return return_message, murk


def dotime():
    time_now = str(str(datetime.now()).split(' ')[1][:5])
    if time_now == listmessagetime[0]:
        for i in range(len(listid)):
            bot.send_message(listid[i], listmessagetext[0])


def sh():
    schedule.every(60).seconds.do(dotime)
    while True:
        schedule.run_pending()
        time.sleep(1)

def run():
    @bot.message_handler(commands=['start', 'command'])
    def start_message(message):
        global listid
        if message.chat.id not in listid: listid.append(message.chat.id)
        print(listid, 'commands')
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)  # one_time_keyboard=True
        markup.add(s_buttons_main[0], s_buttons_main[1])
        markup.add(s_buttons_main[2], s_buttons_main[3])
        markup.add(s_buttons_main[4])
        send_message_wth_markup(message, texts.hello, markup)


    @bot.callback_query_handler(func=lambda call: True)
    def main_messages_callback(call):
        global listid
        if call.message.chat.id not in listid: listid.append(call.message.chat.id)
        print(listid, 'callback')
        try:
            bot.send_message(call.message.chat.id, return_answer(call))
        except Exception:
            e = sys.exc_info()[1]
            print(e.args[0])


    @bot.message_handler(content_types=['text'])
    def main_message_text(message):
        global listmessagetext, listmessagetime
        global flag_pay, list_classes
        global listid
        if message.chat.id not in listid: listid.append(message.chat.id)
        print(listid, 'text')
        inline_markup0 = telebot.types.InlineKeyboardMarkup()
        list_inline_buttons0(inline_markup0)
        inline_markup4 = telebot.types.InlineKeyboardMarkup()
        list_inline_buttons4(inline_markup4)
        pay_text = pay_markup(list_classes)
        text = message.text

        if text == main_button1:
            send_message_wth_markup(message, 'Выберите вид занятия', inline_markup0)  # кнопка "записаться на занятие"
        elif text == main_button2:
            send_message(message, texts.message_2_main)  # кнопка "о клубе"
        elif text == main_button3:
            send_message_wth_markup(message, f'Часто задаваемые вопросы. Какой вопрос интересует Вас?\n',
                                    form_inline_markup_2_0())  # кнопка "часто задаваемые вопросы"
        elif text == main_button4:
            send_message_wth_markup(message, pay_text[0], pay_text[1])  # кнопка оплатить занятие
        elif text == main_button5:
            send_message_wth_markup(message, 'Доступные виды занятий', inline_markup4)  # кнопка "информация о..."
        if flag_pay:
            flag_pay = False
            send_message(message, "Подтвердите операцию и все готово.")

        if text.split(";")[0] == 'new_post':
            part_time = text.split(";")[1]
            part_text = text.split(";")[2]
            listmessagetext[0], listmessagetime[0] = part_text, part_time
