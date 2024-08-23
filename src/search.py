import re
from collections import Counter

def searching(transactions: list[dict], str_search: str) -> list[dict]:
    pattern = re.compile(r'\b{}\b'.format(re.escape(str_search)))
    new_trans = []
    for info in transactions:
        if re.findall(pattern, str(info.get('description')).lower()):
            new_trans.append(info)
    return new_trans

def count_description(transactions: list[dict], list_description: list) -> dict:
    result = {}
    for category in list_description:
        result[category] = Counter([info.get('description') for info in transactions if info.get('description') == category])[category]
    print(type(result))
    return result


# res = [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'открытие вклада', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}]
# print(count_description(res, ['Перевод организации', 'лук']))
