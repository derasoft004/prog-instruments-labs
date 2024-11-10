import json
import hashlib
from typing import List

from config import EXPRESSIONS, DATA, RESULT, VARIANT
from wrappers import context_manager_wrapper
from regulator import load_regular_expressions, get_data_from_csv, match_expressions_and_data


def calculate_checksum(row_numbers: List[int]) -> str:
    """
    The function calculates checksum using list numbers of nonvalid strings

    :param row_numbers: список целочисленных номеров строк csv-файла, на которых были найдены ошибки валидации
    :return: md5 хеш для проверки через github action
    """
    row_numbers.sort()
    return hashlib.md5(json.dumps(row_numbers).encode('utf-8')).hexdigest()


@context_manager_wrapper
def serialize_result(variant: int, checksum: str) -> None:
    """
    The function serializes result that got using func 'calculate_checksum'

    :param variant: номер варианта
    :param checksum: контрольная сумма, вычисленная через calculate_checksum()
    """
    writing_result = {'variant': variant, 'checksum': checksum}
    with open(RESULT, 'w') as file:
        json.dump(writing_result, file)


if __name__ == "__main__":
    expressions = load_regular_expressions(EXPRESSIONS)
    data = get_data_from_csv(DATA)
    result = match_expressions_and_data(expressions, data)
    checksum = calculate_checksum(result)
    serialize_result(VARIANT, checksum)
