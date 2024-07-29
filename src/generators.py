from typing import Iterator, Union

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(
    transaction_info: list[dict], currency: Union[str] = "USD"
) -> Union[Iterator[dict], Iterator[list]]:
    """Функция вывода информации о транзакции с фильтрацией по валюте."""
    filtered_info = []
    for info in iter(transaction_info):
        if info["operationAmount"]["currency"]["code"] == currency:
            filtered_info.append(info)
    if len(filtered_info) == 0:
        yield []
    for info in range(len(filtered_info)):
        yield filtered_info[info]


def transaction_descriptions(transaction_info: list[dict]) -> Iterator[list[dict]]:
    """Функция вывода типа транзакции."""
    for info in transaction_info:
        yield info["description"]


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Функция генерации номера карты."""
    for number in range(start, end + 1):
        card_number_gen = str(number)
        while len(card_number_gen) < 16:
            card_number_gen = "0" + card_number_gen
        formatted_card_number = (
            card_number_gen[:4] + " " + card_number_gen[4:8] + " " + card_number_gen[8:12] + " " + card_number_gen[12:]
        )
        yield formatted_card_number


if __name__ == "__main__":
    usd_transactions = filter_by_currency(transactions, "USD")
    for i in range(1):
        print(next(usd_transactions))
    descriptions = transaction_descriptions(transactions)
    for i in range(4):
        print(next(descriptions))
    for card_number in card_number_generator(2, 3):
        print(card_number)
