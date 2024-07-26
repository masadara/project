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
def bank_account_card2() -> Union[str]:
    return "Счет 30135874305"


@pytest.fixture
def right_date() -> Union[str]:
    return "11.03.2024"


@pytest.fixture
def date1() -> Union[str]:
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def date2() -> Union[str]:
    return "2024-03-11"


@pytest.fixture
def date3() -> Union[int]:
    return 2025
