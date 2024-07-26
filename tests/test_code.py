import pytest

from src.processing import filter_by_state, sort_by_date
from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card


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
