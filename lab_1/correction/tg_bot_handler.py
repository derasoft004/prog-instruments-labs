import sys

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

from additional_functions import (
    bot,
    send_message_wth_markup,
    make_day,
    adm_link,
    make_day_buttons,
    app_mdb,
    send_message,
    LISTID,
    pay_markup,
    LISTMESSAGETIME,
    list_classes,
)
from constants import LISTMESSAGETEXT, DATA


def list_inline_buttons0(inline_markup0: InlineKeyboardMarkup) -> None:
    texts = DATA['list_inline_buttons0']
    for index in range(len(texts)):
        inline_button = InlineKeyboardButton(text=texts[f'inline_button0_{index}'],
                                             callback_data=f'inline_button0_{index}')
        inline_markup0.add(inline_button)


def list_inline_buttons4(inline_markup4: InlineKeyboardMarkup) -> None:
    texts = DATA['list_inline_buttons4']
    for index in range(len(texts)):
        inline_button = InlineKeyboardButton(text=texts[f'inline_button4_{index}'],
                                             callback_data=f'inline_button4_{index}')
        inline_markup4.add(inline_button)


def form_inline_markup_0_0() -> InlineKeyboardMarkup:
    inline_markup_0_0 = InlineKeyboardMarkup()
    inline_button_0_0_0 = InlineKeyboardButton(text='Подтвердить запись', callback_data="accept")  # pay - оплата
    inline_button_0_0_1 = InlineKeyboardButton(text='Отмена', callback_data="exit")
    inline_markup_0_0.add(inline_button_0_0_0)
    inline_markup_0_0.add(inline_button_0_0_1)
    return inline_markup_0_0


def form_inline_markup_2_0() -> InlineKeyboardMarkup:
    texts = DATA['form_inline_markup_2_0']
    inline_markup_2_0 = InlineKeyboardMarkup()
    for index in range(len(texts)):
        inline_button = InlineKeyboardButton(text=texts[f'inline_button_2_0_{index}'],
                                             callback_data=f'inline_button_2_0_{index}')
        inline_markup_2_0.add(inline_button)

    return inline_markup_2_0


def return_answer(call) -> None:
    print(call.data)
    global tmps, flag_pay
    return_message = ' '
    if call.data == 'inline_button4_0':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_message_wth_markup(call.message, "Совершите операцию в личном чате с администратором", adm_link())
    elif call.data == 'inline_button4_1':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return_message += DATA['gymnastik'] + '\n\nРасписание занятий\n' + make_day([2], [0, 1, 2, 3, 4],
                                                                                    [5, 1, 5, 1, 5])
    elif call.data == 'inline_button4_2':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return_message += DATA['dzudo'] + '\n\nРасписание занятий\n' + make_day([0, 0, 1, 1], [0, 3, 2, 4],
                                                                                [11, 11, 11, 11])
    elif call.data == 'inline_button4_3':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return_message += DATA['gymnastik'] + '\n\nРасписание занятий\n' + make_day([3], [2, 4], [11, 11])
    elif call.data == 'inline_button4_4':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return_message += DATA['fitnes'] + '\n\nРасписание занятий\n' + make_day([4], [0, 1, 2, 4, 5],
                                                                                 [4, 14, 15, 14, 4])
    elif call.data == 'inline_button4_5':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return_message += DATA['dzudo'] + '\n\nРасписание занятий\n' + make_day([0, 0, 0, 1, 1, 1], [0, 3, 5, 0, 2, 4],
                                                                                [13, 13, 2, 0, 0, 0])
    elif call.data == 'inline_button4_6':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return_message += DATA['dzudo'] + '\n\nРасписание занятий\n' + make_day([0, 0, 0, 1, 1, 1], [1, 3, 5, 0, 2, 4],
                                                                                [6, 6, 2, 8, 8, 8])
    elif call.data == 'inline_button4_7':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return_message += DATA['lkf4_6'] + DATA['lkf']
    elif call.data == 'inline_button4_8':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return_message += DATA['lkf7_10'] + DATA['lkf']
    elif call.data == 'inline_button4_9':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_message_wth_markup(call.message, "Совершите операцию в личном чате с администратором", adm_link())
    elif call.data == '':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return_message += ''
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
    for i in range(6):
        if call.data == f'day_button_{str(i)}':
            bot.delete_message(call.message.chat.id, call.message.message_id)
            send_message_wth_markup(call.message, f'Подтвердите запись на {tmps[0]}\n{app_mdb(i)}',
                                    form_inline_markup_0_0())
            list_classes.append(f'{tmps[0]}{app_mdb(i)}\n')
            break
    if call.data == 'inline_button_2_0_0':
        send_message(call.message, DATA['faq1'])
    elif call.data == 'inline_button_2_0_1':
        send_message(call.message, DATA['faq2'])
    elif call.data == 'inline_button_2_0_2':
        send_message(call.message, DATA['faq3'])
    elif call.data == 'inline_button_2_0_3':
        send_message(call.message, DATA['faq4'])
    elif call.data == 'inline_button_2_0_4':
        send_message(call.message, DATA['faq5'])
    elif call.data == "exit":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        print('до выхода ', list_classes)
        list_classes.remove(list_classes[len(list_classes) - 1])
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


def run() -> None:
    s_buttons_main = DATA['main_buttons']

    @bot.message_handler(commands=['start', 'command'])
    def start_message(message):
        if message.chat.id not in LISTID: LISTID.append(message.chat.id)
        print(LISTID, 'commands')
        markup = ReplyKeyboardMarkup(resize_keyboard=True)  # one_time_keyboard=True
        for index in range(1, 3):
            markup.add(s_buttons_main[f'main_button{index * 2 - 1}'], s_buttons_main[f'main_button{index * 2}'])
        markup.add(s_buttons_main['main_button5'])
        send_message_wth_markup(message, DATA['hello'], markup)


    @bot.callback_query_handler(func=lambda call: True)
    def main_messages_callback(call):
        print(call.data)
        if call.message.chat.id not in LISTID: LISTID.append(call.message.chat.id)
        print(LISTID, 'callback')
        try:
            bot.send_message(call.message.chat.id, return_answer(call))
        except Exception as e:
            e = sys.exc_info()[1]
            print(e.args[0])

    @bot.message_handler(content_types=['text'])
    def main_message_text(message):
        global flag_pay
        if message.chat.id not in LISTID: LISTID.append(message.chat.id)
        inline_markup0 = InlineKeyboardMarkup()
        list_inline_buttons0(inline_markup0)
        inline_markup4 = InlineKeyboardMarkup()
        list_inline_buttons4(inline_markup4)
        pay_text = pay_markup(list_classes)
        text = message.text

        if text == s_buttons_main['main_button1']:
            send_message_wth_markup(message, 'Выберите вид занятия', inline_markup0)  # кнопка "записаться на занятие"
        elif text == s_buttons_main['main_button2']:
            send_message(message, DATA['message_2_main'])  # кнопка "о клубе"
        elif text == s_buttons_main['main_button3']:
            send_message_wth_markup(message, f'Часто задаваемые вопросы. Какой вопрос интересует Вас?\n',
                                    form_inline_markup_2_0())  # кнопка "часто задаваемые вопросы"
        elif text == s_buttons_main['main_button4']:
            send_message_wth_markup(message, pay_text[0], pay_text[1])  # кнопка оплатить занятие
        elif text == s_buttons_main['main_button5']:
            send_message_wth_markup(message, 'Доступные виды занятий', inline_markup4)  # кнопка "информация о..."
        if flag_pay:
            flag_pay = False
            send_message(message, "Подтвердите операцию и все готово.")

        if text.split(";")[0] == 'new_post':
            part_time = text.split(";")[1]
            part_text = text.split(";")[2]
            LISTMESSAGETEXT[0], LISTMESSAGETIME[0] = part_text, part_time
