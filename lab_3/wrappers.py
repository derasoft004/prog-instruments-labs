import logging

logging.basicConfig(level=logging.INFO)


def context_manager_wrapper(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError as e:
            logging.error(f'Файла не существует. {e}')
        except Exception:
            logging.error("Невозможно открыть файл")

    return wrapper
