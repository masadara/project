import re
from collections import Counter

def searching(transactions: list[dict], str_search: str) -> list[dict]:
    pattern = re.compile(r'\b{}\b'.format(re.escape(str_search)))
    new_trans = []
    for info in transactions:
        try:
            if info.get('descriprion') == 'Открытие вклада':
                info['from'] = ''
        except NameError:
            info['from'] = ''
        if re.findall(pattern, str(info.get('description')).lower()):
            new_trans.append(info)
    return new_trans

def count_description(transactions: list[dict], list_description: list) -> dict:
    result = {}
    for category in list_description:
        result[category] = Counter([info.get('description') for info in transactions if info.get('description') == category])[category]
    print(type(result))
    return result


res = [{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0, 'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'}, {'id': 3598919.0, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740.0, 'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'}, {'id': 593027.0, 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': 30368.0, 'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097', 'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'}, {'id': 366176.0, 'state': 'EXECUTED', 'date': '2020-08-02T09:35:18Z', 'amount': 29482.0, 'currency_name': 'Rupiah', 'currency_code': 'IDR', 'from': 'Discover 0325955596714937', 'to': 'Visa 3820488829287420', 'description': 'Перевод с карты на карту'}, {'id': 5380041.0, 'state': 'CANCELED', 'date': '2021-02-01T11:54:58Z', 'amount': 23789.0, 'currency_name': 'Peso', 'currency_code': 'UYU', 'from': nan, 'to': 'Счет 23294994494356835683', 'description': 'Открытие вклада'}]
print(searching(res, 'перевод'))
