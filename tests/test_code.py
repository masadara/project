import pytest
from src.widget import get_date, mask_account_card
from src.processing import filter_by_state, sort_by_date
from src.masks import get_mask_account, get_mask_card_number

@pytest.mark.parametrize("account, expected_result", [
    ("73654108430135874305", "**4305"),
    (545874305, "**4305")])
def test_mask_account(account, expected_result):
    assert get_mask_account(account) == expected_result

@pytest.mark.parametrize("card_number, expected_result", [
    (7000792289606361, "7000 79** **** 6361"),
    ('', 'error'), ("123456789101112134", "123456** ******2134")])
def test_mask_card_number(card_number, expected_result):
    assert get_mask_card_number(card_number) == expected_result

@pytest.mark.parametrize("account_card, expected_result", [("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"), ("Счет 30135874305", "Счет **4305"), ('', "error"), ([
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ], "error")])
def test_mask_account_card(account_card, expected_result):
    assert mask_account_card(account_card) == expected_result


@pytest.mark.parametrize("date, expected_result", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2024-03-11", "11.03.2024"), ('', "error"), (2025, "error")])
def test_get_date(date, expected_result):
    assert get_date(date) == expected_result

@pytest.mark.parametrize("filter, state, expected_result", [([
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ], "EXECUTED" ,[
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]), ([
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],"CANCELED" ,[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]), ([
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],"EXECUTE" ,'error')])
def test_filter_by_state(filter, state, expected_result):
    assert filter_by_state(filter, state) == expected_result

@pytest.mark.parametrize("sorted_date, order, expected_result",[([
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],'down' , [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]), ([
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-09-12T08:21:33.419441"},
            ], 'up', [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-09-12T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}])])
def test_sort_by_date(sorted_date, order, expected_result):
    assert sort_by_date(sorted_date, order) == expected_result

