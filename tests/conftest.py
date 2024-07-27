from typing import Union

import pytest


@pytest.fixture
def error() -> Union[str]:
    return "error"


@pytest.fixture
def list_info() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_info_for_up() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-09-12T08:21:33.419441"},
    ]


@pytest.fixture
def list_info_up() -> list[dict]:
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-09-12T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def list_info_down() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def list_info_wrong() -> list[dict]:
    return [
        {"id": 939719570, "state": "EXECUTE", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELE", "date": "2018-09-12T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELE", "date": "2018-09-12T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTE", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def list_error() -> list[dict]:
    return [{"error": "error"}]


@pytest.fixture
def list_canceled() -> list[dict]:
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_executed() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def bank_account() -> Union[str]:
    return "73654108430135874305"


@pytest.fixture
def bank_account2() -> Union[int]:
    return 545874305


@pytest.fixture
def bank_account_right() -> Union[str]:
    return "**4305"


@pytest.fixture
def bank_card_number2_right() -> Union[str]:
    return "123456** ******2134"


@pytest.fixture
def empty() -> Union[str]:
    return ""


@pytest.fixture
def zero() -> Union[str]:
    return "0"


@pytest.fixture
def bank_card_number1_right() -> Union[str]:
    return "7000 79** **** 6361"


@pytest.fixture
def bank_card_number1() -> Union[int]:
    return 7000792289606361


@pytest.fixture
def bank_card_number2() -> Union[str]:
    return "123456789101112134"


@pytest.fixture
def bank_account_card1_right() -> Union[str]:
    return "Visa Platinum 7000 79** **** 6361"


@pytest.fixture
def bank_account_card2_right() -> Union[str]:
    return "Счет **4305"


@pytest.fixture
def bank_account_card1() -> Union[str]:
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def bank_account_card3() -> Union[str]:
    return "MasterCard 7158300734726758"


@pytest.fixture
def bank_account_card4() -> Union[str]:
    return "Maestro 1596837868705199"


@pytest.fixture
def bank_account_card5() -> Union[str]:
    return "Visa Classic 6831982476737658"


@pytest.fixture
def bank_account_card6() -> Union[str]:
    return "Visa Gold 5999414228426353"


@pytest.fixture
def bank_account_card2() -> Union[str]:
    return "Счет 30135874305"


@pytest.fixture
def right_date() -> Union[str]:
    return "11.03.2024"


@pytest.fixture
def test_date1() -> Union[str]:
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def test_date2() -> Union[str]:
    return "2024-03-11"


@pytest.fixture
def test_date3() -> Union[int]:
    return 2025


@pytest.fixture
def bank_account_card3_right() -> Union[str]:
    return "MasterCard 7158 30** **** 6758"


@pytest.fixture
def bank_account_card4_right() -> Union[str]:
    return "Maestro 1596 83** **** 5199"


@pytest.fixture
def bank_account_card5_right() -> Union[str]:
    return "Visa Classic 6831 98** **** 7658"


@pytest.fixture
def bank_account_card6_right() -> Union[str]:
    return "Visa Gold 5999 41** **** 6353"


@pytest.fixture
def transactions() -> list[dict]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]


@pytest.fixture
def org() -> str:
    return "Перевод организации"


@pytest.fixture
def account_to_account() -> str:
    return "Перевод со счета на счет"


@pytest.fixture
def empty_list() -> list:
    return []


@pytest.fixture
def card_to_card() -> str:
    return "Перевод с карты на карту"