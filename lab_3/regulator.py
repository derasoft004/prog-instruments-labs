import csv
import json
from typing import List
import re

import chardet

from wrappers import context_manager_wrapper


@context_manager_wrapper
def get_data_from_csv(file_name: str) -> List:
    """
    The function gets the name of the csv file as input and returns a list of strings

    use get_data_from_csv('72.csv') to open '72.csv' file

    :param file_name:
    :return: strings list
    """
    data_lst = []

    with open(file_name, 'rb') as f:
        rawdata = f.read()
        result = chardet.detect(rawdata)
        encoding = result['encoding']

    with open(file_name, 'r', encoding=encoding) as file:
        reader = csv.reader(file)
        for row in reader:
            data_lst.append(''.join(row))
    return data_lst


@context_manager_wrapper
def load_regular_expressions(file_name: str) -> dict:
    """
    The function gets the name of the .json file as input
     and loads regular expressions from this file
     and return list expressions

    use load_regular_expressions('expressions.json') to open 'expressions.json' file

    :param file_name:
    :return: list expressions
    """
    with open(file_name, 'r') as file:
        data_dict = json.load(file)

    return data_dict


def match_expressions_and_data(expressions: dict, data: list) -> List:
    """
    The function matching expressions with data

    :param expressions:
    :param data:
    :return:
    """
    categories = data[0].replace("\"", '').split(';')
    nonvalid_strings = []
    for row_index, row in enumerate(data[1:]):
        normalised_row = row.replace("\"", '').split(';')
        valid = True
        for index, category in enumerate(categories):
            match = re.fullmatch(expressions[category], normalised_row[index])
            if not match:
                valid = False
                break
        if not valid:
            nonvalid_strings.append(row_index)

    return nonvalid_strings
