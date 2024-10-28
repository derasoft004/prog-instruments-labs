from tg_bot_handler import *
import threading


def main():
    e1 = threading.Event()
    e2 = threading.Event()

    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=schedule_handler)

    t1.start()
    t2.start()

    bot.infinity_polling()


if __name__ == '__main__':
    main()
