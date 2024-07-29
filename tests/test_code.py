import pytest

from src.processing import filter_by_state, sort_by_date
from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.mark.parametrize(
    "account_number, expected_result",
    [("bank_account", "bank_account_right"), ("bank_account2", "bank_account_right")],
)
def test_mask_account(request, account_number, expected_result):
    assert get_mask_account(request.getfixturevalue(account_number)) == request.getfixturevalue(expected_result)


@pytest.mark.parametrize(
    "card_number, expected_result",
    [
        ("bank_card_number1", "bank_card_number1_right"),
        ("empty", "error"),
        ("bank_card_number2", "bank_card_number2_right"),
    ],
)
def test_mask_card_number(request, card_number, expected_result):
    assert get_mask_card_number(request.getfixturevalue(card_number)) == request.getfixturevalue(expected_result)


@pytest.mark.parametrize(
    "account_card, expected_result",
    [
        ("bank_account_card1", "bank_account_card1_right"),
        ("bank_account_card2", "bank_account_card2_right"),
        ("bank_account_card3", "bank_account_card3_right"),
        ("bank_account_card4", "bank_account_card4_right"),
        ("bank_account_card5", "bank_account_card5_right"),
        ("bank_account_card6", "bank_account_card6_right"),
        ("empty", "error"),
        ("zero", "error"),
        (
            "list_info",
            "error",
        ),
    ],
)
def test_mask_account_card(request, account_card, expected_result):
    assert mask_account_card(request.getfixturevalue(account_card)) == request.getfixturevalue(expected_result)


@pytest.mark.parametrize(
    "date, expected_result",
    [("test_date1", "right_date"), ("test_date2", "right_date"), ("empty", "error"), ("test_date3", "error")],
)
def test_get_date(request, date, expected_result):
    assert get_date(request.getfixturevalue(date)) == request.getfixturevalue(expected_result)


@pytest.mark.parametrize(
    "filter, state, expected_result",
    [
        ("list_info", "EXECUTED", "list_executed"),
        ("list_info", "CANCELED", "list_canceled"),
        ("list_info", "EXECUT", "list_error"),
    ],
)
def test_filter_by_state(request, filter, state, expected_result):
    assert filter_by_state(request.getfixturevalue(filter), state) == request.getfixturevalue(expected_result)


@pytest.mark.parametrize(
    "fixture_name, order, expected_result",
    [("list_info", "down", "list_info_down"), ("list_info_for_up", "up", "list_info_up")],
)
def test_sort_by_date(request, fixture_name, order, expected_result):
    assert sort_by_date(request.getfixturevalue(fixture_name), order) == request.getfixturevalue(expected_result)


@pytest.mark.parametrize("expected", [("Перевод организации"), ("Перевод со счета на счет")])
def test_transaction_descriptions(transactions, expected):
    assert next(transaction_descriptions(transactions)) == expected


@pytest.mark.parametrize("start, end, expexted", [(1, 1, "0000 0000 0000 0001"), (2, 3, "0000 0000 0000 0002")])
def test_card_number_generator(start, end, expexted):
    assert next(card_number_generator(start, end)) == expexted


@pytest.mark.parametrize(
    "currency, expected",
    [
        (
            "USD",
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
        ),
        (
            "RUB",
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160",
            },
        ),
        ("EUR", []),
    ],
)
def test_filter_by_currency(transactions, currency, expected):
    assert next(filter_by_currency(transactions, currency)) == expected
