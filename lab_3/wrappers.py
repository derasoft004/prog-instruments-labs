import logging

logging.basicConfig(level=logging.INFO)


def context_manager_wrapper(func):
    """
    The wrapper using to wrap functions that open files

    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError as e:
            logging.error(f"File not exists; {e}")
        except Exception as e:
            logging.error(f"It's impossible to open file; {e}")

    return wrapper
