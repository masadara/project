from typing import Union


def filter_by_state(account_info: list[dict], state: Union[str] = "EXECUTED") -> list[dict]:
    """Функция фильтрации по параметру."""
    filtered_info = []
    for info in account_info:
        if info.get("state") == state:
            filtered_info.append(info)
    return filtered_info
    # if len(filtered_info) == 0:
    #     return ValueError
    # else:
    #     return filtered_info


def sort_by_date(account_info: list[dict], sorting_order: Union[str] = "down") -> list[dict]:
    """Функция сортировки по дате."""
    if sorting_order == "up":
        account_info.sort(key=lambda x: x.get("date"))
    elif sorting_order == "down":
        account_info.sort(key=lambda x: x.get("date"), reverse=True)
    else:
        return [{"error": "error"}]
    return account_info


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
    print(
        sort_by_date(
            [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'открытие вклада', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}],
            "up",
        )
    )

