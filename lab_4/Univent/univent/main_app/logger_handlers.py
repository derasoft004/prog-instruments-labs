import logging
from functools import wraps

logging.basicConfig(level=logging.INFO, filename="main_app_views.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")


def logger_info_join_page(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"User requested {func.__name__} page")
        return func(*args, **kwargs)
    return wrapper