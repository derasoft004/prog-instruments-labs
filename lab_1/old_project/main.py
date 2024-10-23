import sys
import time
from datetime import datetime

import schedule
import telebot
import threading
from telebot import TeleBot

import texts

bot = TeleBot('6026455101:AAH1asLKyOZpfc3kSf105EYAsHmVo-g7c9c')
listid = []

def send_message(message, message_text):
    bot.send_message(message.chat.id, message_text)


def send_message_wth_markup(message, message_text, markup):
    bot.send_message(message.chat.id, message_text, reply_markup=markup)


main_button1, main_button2 = 'Записаться на занятие', 'О клубе'
main_button3, main_button4 = 'Часто задаваемые вопросы', 'Оплатить занятие'
main_button5 = 'Информация об услугах и стоимости'
s_buttons_main = [main_button1, main_button2, main_button3, main_button4, main_button5]


def counter(s):
    count = 1
    tmp1 = s[0]
    for i in range(1, len(s)):
        if s[i] == tmp1: count += 1
    return count


trainer = ['Глота Дмитрий Александрович', 'Гульченский Анатолий Игоревич', 'Янаева Франческа Александра',
           'Мария Алексеевна', 'Шнайдер Виктория Валерьевна']
week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
time_s = ['9.00-10.00', '9.00-10.30', '10.00-11.30', '11.00-12.00', '12.00-13.00', '14.00-15.00', '14.30-15.30',
          '15.30-16.30', '16.15-17.15', '17.30-18.30', '18.00-19.00', '19.00-19.45', '19.00-20.00', '20.00-21.00',
          '18.00-19.00; 19.00-20.00', '12.00-13.00; 18.00-19.00']
old = ['', '4-6 лет', '7-10 лет', '10-12 лет']
types_classes = ['Гимнастика', 'Дзюдо', 'Фитнес для взрослых', 'ЛФК']
list_classes = []


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

s_buttons_d = []
def make_day_buttons(days_list, time_list, type_class):
    global s_buttons_d
    stmp = []
    keyboard_button_day = telebot.types.InlineKeyboardMarkup()
    for i in range(len(days_list)):
        stmp.append(f'{week[days_list[i]]} {time_s[time_list[i]]} ')
        keyboard_button_day.add(telebot.types.InlineKeyboardButton(text=f'{week[days_list[i]]} {time_s[time_list[i]]} ',
                                                                   callback_data=f'day_button_{str(i)}'))
    s_buttons_d = stmp
    return_message = f'{types_classes[type_class]}\n ' # {week[days_list[i]]} {time[time_list[i]]}
    return return_message, keyboard_button_day

def app_mdb(index):
    global s_buttons_d
    return s_buttons_d[index]

def adm_link():
    return telebot.types.InlineKeyboardMarkup().add(telebot.types.InlineKeyboardButton("Администратор ",
                                                                                       "t.me/ch_chrissy"))


def list_inline_buttons0(inline_markup0):
    inline_button0_0 = telebot.types.InlineKeyboardButton(text='Пробная неделя',
                                                          callback_data='inline_button0_0')
    inline_button0_1 = telebot.types.InlineKeyboardButton(text='Гимнастика 7-10 лет 3000р',
                                                          callback_data='inline_button0_1')
    inline_button0_2 = telebot.types.InlineKeyboardButton(text='Дзюдо 4-6 лет 2500р',
                                                          callback_data='inline_button0_2')
    inline_button0_3 = telebot.types.InlineKeyboardButton(text='Гимнастика 4-6 лет 2500р',
                                                          callback_data='inline_button0_3')
    inline_button0_4 = telebot.types.InlineKeyboardButton(text='Фитнес для взрослых 2500р',
                                                          callback_data='inline_button0_4')
    inline_button0_5 = telebot.types.InlineKeyboardButton(text='Дзюдо 7-10 лет 3000р',
                                                          callback_data='inline_button0_5')
    inline_button0_6 = telebot.types.InlineKeyboardButton(text='Дзюдо 10-12 лет 3000р',
                                                          callback_data='inline_button0_6')
    inline_button0_7 = telebot.types.InlineKeyboardButton(text='ЛФК 4-6 лет 2500р/час',
                                                          callback_data='inline_button0_7')
    inline_button0_8 = telebot.types.InlineKeyboardButton(text='ЛФК 7-10 лет 2500р/час',
                                                          callback_data='inline_button0_8')
    inline_button0_9 = telebot.types.InlineKeyboardButton(text='Индивидуальные тренировки 1000р/час',
                                                          callback_data='inline_button0_9')

    inline_markup0.add(inline_button0_0)
    inline_markup0.add(inline_button0_1)
    inline_markup0.add(inline_button0_2)
    inline_markup0.add(inline_button0_3)
    inline_markup0.add(inline_button0_4)
    inline_markup0.add(inline_button0_5)
    inline_markup0.add(inline_button0_6)
    inline_markup0.add(inline_button0_7)
    inline_markup0.add(inline_button0_8)
    inline_markup0.add(inline_button0_9)


def list_inline_buttons4(inline_markup4):
    inline_button4_0 = telebot.types.InlineKeyboardButton(text='Пробная неделя',
                                                          callback_data='inline_button4_0')
    inline_button4_1 = telebot.types.InlineKeyboardButton(text='Гимнастика 7-10 лет 3000р',
                                                          callback_data='inline_button4_1')
    inline_button4_2 = telebot.types.InlineKeyboardButton(text='Дзюдо 4-6 лет 2500р',
                                                          callback_data='inline_button4_2')
    inline_button4_3 = telebot.types.InlineKeyboardButton(text='Гимнастика 4-6 лет 2500р',
                                                          callback_data='inline_button4_3')
    inline_button4_4 = telebot.types.InlineKeyboardButton(text='Фитнес для взрослых 2500р',
                                                          callback_data='inline_button4_4')
    inline_button4_5 = telebot.types.InlineKeyboardButton(text='Дзюдо 7-10 лет 3000р',
                                                          callback_data='inline_button4_5')
    inline_button4_6 = telebot.types.InlineKeyboardButton(text='Дзюдо 10-12 лет 3000р',
                                                          callback_data='inline_button4_6')
    inline_button4_7 = telebot.types.InlineKeyboardButton(text='ЛФК 4-6 лет 2500р/час',
                                                          callback_data='inline_button4_7')
    inline_button4_8 = telebot.types.InlineKeyboardButton(text='ЛФК 7-10 лет 2500р/час',
                                                          callback_data='inline_button4_8')
    inline_button4_9 = telebot.types.InlineKeyboardButton(text='Индивидуальные тренировки 1000р/час',
                                                          callback_data='inline_button4_9')
    inline_markup4.add(inline_button4_0)
    inline_markup4.add(inline_button4_1)
    inline_markup4.add(inline_button4_2)
    inline_markup4.add(inline_button4_3)
    inline_markup4.add(inline_button4_4)
    inline_markup4.add(inline_button4_5)
    inline_markup4.add(inline_button4_6)
    inline_markup4.add(inline_button4_7)
    inline_markup4.add(inline_button4_8)
    inline_markup4.add(inline_button4_9)


def pay_markup(list_classes):
    return_message = 'Ваша запись на: \n'
    murk = telebot.types.InlineKeyboardMarkup()
    butn = telebot.types.InlineKeyboardButton(text="Оплатить", callback_data="pay")
    murk.add(butn)
    for i in range(len(list_classes)):
        return_message += str(list_classes[i])
    return return_message, murk


flag_pay = False


def form_inline_markup_0_0(calldata: str): # на случай перестройки
    inline_markup_0_0 = telebot.types.InlineKeyboardMarkup()
    inline_button_0_0_0 = telebot.types.InlineKeyboardButton(text='Подтвердить запись', callback_data="accept") # pay -
                                                                                                                # оплата
    inline_button_0_0_1 = telebot.types.InlineKeyboardButton(text='Отмена', callback_data="exit")
    inline_markup_0_0.add(inline_button_0_0_0)
    inline_markup_0_0.add(inline_button_0_0_1)
    return inline_markup_0_0


def form_inline_markup_2_0():
    inline_markup_2_0 = telebot.types.InlineKeyboardMarkup()
    inline_button_2_0_0 = telebot.types.InlineKeyboardButton(text='- Хочу записаться в клуб.',
                                                             callback_data='inline_button_2_0_0')
    inline_button_2_0_1 = telebot.types.InlineKeyboardButton(text='- Какими тренеры и какие виды тренировок '
                                                                  'у вас есть?', callback_data='inline_button_2_0_1')
    inline_button_2_0_2 = telebot.types.InlineKeyboardButton(text='- Какие у вас цены на тренировки?',
                                                             callback_data='inline_button_2_0_2')
    inline_button_2_0_3 = telebot.types.InlineKeyboardButton(text='- Какие у вас графики работы клуба?',
                                                             callback_data='inline_button_2_0_3')
    inline_button_2_0_4 = telebot.types.InlineKeyboardButton(text=' Как связаться с вами, у меня есть '
                                                                  'вопрос или проблема?',
                                                             callback_data='inline_button_2_0_4')
    inline_markup_2_0.add(inline_button_2_0_0)
    inline_markup_2_0.add(inline_button_2_0_1)
    inline_markup_2_0.add(inline_button_2_0_2)
    inline_markup_2_0.add(inline_button_2_0_3)
    inline_markup_2_0.add(inline_button_2_0_4)

    return inline_markup_2_0


tmps = make_day_buttons([0], [0], 0) # переменная записывающая в себя тмпшную категорию
def return_answer(call):
    global tmps, flag_pay, list_classes
    return_message = ' '
    if call.data == 'inline_button4_0':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_message_wth_markup(call.message, "Совершите операцию в личном чате с администратором", adm_link())
    elif call.data == 'inline_button4_1':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return_message += texts.gymnastik + '\n\nРасписание занятий\n' + make_day([2], [0, 1, 2, 3, 4], [5, 1, 5, 1, 5])
    elif call.data == 'inline_button4_2':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return_message += texts.dzudo + '\n\nРасписание занятий\n' + make_day([0, 0, 1, 1], [0, 3, 2, 4],
                                                                              [11, 11, 11, 11])
    elif call.data == 'inline_button4_3':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return_message += texts.gymnastik + '\n\nРасписание занятий\n' + make_day([3], [2, 4], [11, 11])
    elif call.data == 'inline_button4_4':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return_message += texts.fitnes + '\n\nРасписание занятий\n' + make_day([4], [0, 1, 2, 4, 5], [4, 14, 15, 14, 4])
    elif call.data == 'inline_button4_5':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return_message += texts.dzudo + '\n\nРасписание занятий\n' + make_day([0, 0, 0, 1, 1, 1], [0, 3, 5, 0, 2, 4],
                                                                              [13, 13, 2, 0, 0, 0])
    elif call.data == 'inline_button4_6':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return_message += texts.dzudo + '\n\nРасписание занятий\n' + make_day([0, 0, 0, 1, 1, 1], [1, 3, 5, 0, 2, 4],
                                                                              [6, 6, 2, 8, 8, 8])
    elif call.data == 'inline_button4_7':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return_message += texts.lkf4_6 + texts.lkf
    elif call.data == 'inline_button4_8':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return_message += texts.lkf7_10 + texts.lkf
    elif call.data == 'inline_button4_9':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_message_wth_markup(call.message, "Совершите операцию в личном чате с администратором", adm_link())
    elif call.data == '':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return_message += ''
    # todo ======================================== КНОПКИ "Записаться на занятие" =====================================
    elif call.data == 'inline_button0_0':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_message_wth_markup(call.message, "Совершите операцию в личном чате с администратором", adm_link())
    elif call.data == 'inline_button0_1':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        tmps = make_day_buttons([0, 1, 2, 3, 4], [5, 1, 5, 1, 5], 0)
        send_message_wth_markup(call.message, f'Ваша запись на: Гимнастика ',
                                tmps[1])
    elif call.data == 'inline_button0_2':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        tmps = make_day_buttons([0, 3, 2, 4], [11, 11, 11, 11], 1)
        send_message_wth_markup(call.message, f'Ваша запись на: Дзюдо ',
                                tmps[1])
    elif call.data == 'inline_button0_3':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        tmps = make_day_buttons([2, 4], [11, 11], 0)
        send_message_wth_markup(call.message, f'Ваша запись на: Гимнастика ', tmps[1])
    elif call.data == 'inline_button0_4':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        tmps = make_day_buttons([0, 1, 2, 4, 5], [4, 14, 15, 14, 4], 2)
        send_message_wth_markup(call.message, f'Ваша запись на: Фитнес для взрослых ',
                                tmps[1])
    elif call.data == 'inline_button0_5':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        tmps = make_day_buttons([0, 3, 5, 0, 2, 4], [13, 13, 2, 0, 0, 0], 1)
        send_message_wth_markup(call.message, f'Ваша запись на: Дзюдо ',
                                tmps[1])
    elif call.data == 'inline_button0_6':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        tmps = make_day_buttons([1, 3, 5, 0, 2, 4], [6, 6, 2, 8, 8, 8], 1)
        send_message_wth_markup(call.message, f'Ваша запись на: Дзюдо ',
                                tmps[1])
    elif call.data == 'inline_button0_7':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_message_wth_markup(call.message, "Совершите операцию в личном чате с администратором", adm_link())
    elif call.data == 'inline_button0_8':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_message_wth_markup(call.message, "Совершите операцию в личном чате с администратором", adm_link())
    elif call.data == 'inline_button0_9':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_message_wth_markup(call.message, "Совершите операцию в личном чате с администратором", adm_link())
    # todo ======================================== КНОПКИ выбранных дней ==============================================
    for i in range(6):
        if call.data == f'day_button_{str(i)}':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            send_message_wth_markup(call.message, f'Подтвердите запись на {tmps[0]}\n{app_mdb(i)}',
                                    form_inline_markup_0_0(f'day_button_{str(i)}'))
            list_classes.append(f'{tmps[0]}{app_mdb(i)}\n')
            break
    # todo ======================================== КНОПКИ "Часто задаваемые вопросы" ==================================
    if call.data == 'inline_button_2_0_0':
        send_message(call.message, texts.faq1)
    elif call.data == 'inline_button_2_0_1':
        send_message(call.message, texts.faq2)
    elif call.data == 'inline_button_2_0_2':
        send_message(call.message, texts.faq3)
    elif call.data == 'inline_button_2_0_3':
        send_message(call.message, texts.faq4)
    elif call.data == 'inline_button_2_0_4':
        send_message(call.message, texts.faq5)
    elif call.data == "exit":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        print('до выхода ', list_classes)
        list_classes.remove(list_classes[len(list_classes)-1])
        send_message(call.message, "Вы прервали операцию.")
        print('выход ', list_classes)
    elif call.data == "adm_link":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_message_wth_markup(call.message, "Совершите операцию в личном чате с администратором", adm_link())
    elif call.data == "pay":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_message(call.message, "Введите номер карты")
        flag_pay = True
        print('оплата', list_classes)
    elif call.data == "accept":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_message(call.message, "Запись подтверждена")
        print('подтверждение', list_classes)


    return return_message


listmessagetext = ["_", ';']
listmessagetime = [0, 0]


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


e1 = threading.Event()
e2 = threading.Event()

t1 = threading.Thread(target=run)
t2 = threading.Thread(target=sh)

t1.start()
t2.start()

bot.infinity_polling()