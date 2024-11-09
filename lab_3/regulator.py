import csv
import logging
from typing import List

import chardet

logging.basicConfig(level=logging.INFO)


def get_data_from_csv(file_name: str) -> List:
    """
    Функция получает название csv файла на вход и возвращает список строк
    :param file_name: file's name
    :return: strings list
    """
    data_lst = []

    try:
        with open(file_name, 'rb') as f:
            rawdata = f.read()
            result = chardet.detect(rawdata)
            encoding = result['encoding']

        with open(file_name, 'r', encoding=encoding) as file:
            reader = csv.reader(file)
            for string in reader:
                data_lst.append(string)
    except FileNotFoundError as e:
        logging.error(f'Файла не существует. {e}')
    except Exception:
        logging.error("Невозможно открыть файл")
    return data_lst
