import pytest

@pytest.fixture
def error():
    return 'error'

@pytest.fixture
def list_info():
    return [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]

@pytest.fixture
def list_info_for_up():
    return [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-09-12T08:21:33.419441"},
            ]

@pytest.fixture
def list_info_up():
    return [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-09-12T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ]

@pytest.fixture
def list_info_down():
    return [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ]

@pytest.fixture
def list_info_wrong():
    return [
                {"id": 939719570, "state": "EXECUTE", "date": "2018-06-30T02:08:58.425572"},
                {"id": 615064591, "state": "CANCELE", "date": "2018-09-12T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELE", "date": "2018-09-12T21:27:25.241689"},
                {"id": 41428829, "state": "EXECUTE", "date": "2019-07-03T18:35:29.512364"},
            ]

@pytest.fixture
def list_error():
    return [{'error': 'error'}]

@pytest.fixture
def list_canceled():
    return [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]

@pytest.fixture
def list_executed():
    return [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ]

@pytest.fixture
def bank_account():
    return "73654108430135874305"

@pytest.fixture
def bank_account2():
    return 545874305

@pytest.fixture
def bank_account_right():
    return "**4305"

@pytest.fixture
def bank_card_number2_right():
    return "123456** ******2134"

@pytest.fixture
def empty():
    return ''

@pytest.fixture
def bank_card_number1_right():
    return "7000 79** **** 6361"

@pytest.fixture
def bank_card_number1():
    return 7000792289606361

@pytest.fixture
def bank_card_number2():
    return "123456789101112134"

@pytest.fixture
def bank_account_card1_right():
    return "Visa Platinum 7000 79** **** 6361"

@pytest.fixture
def bank_account_card2_right():
    return "Счет **4305"

@pytest.fixture
def bank_account_card1():
    return "Visa Platinum 7000792289606361"

@pytest.fixture
def bank_account_card2():
    return "Счет 30135874305"

@pytest.fixture
def right_date():
    return "11.03.2024"

@pytest.fixture
def date1():
    return "2024-03-11T02:26:18.671407"

@pytest.fixture
def date2():
    return "2024-03-11"

@pytest.fixture
def date3():
    return 2025

