def filter_by_state(account_info: list[dict], state="EXECUTED") -> list[dict]:
    """Функция фильтрации по параметру."""
    filtered_info = []
    for info in account_info:
        if info["state"] == state:
            filtered_info.append(info)
    return filtered_info


def sort_by_date(account_info: list[dict], sorting_order="down") -> list[dict]:
    """Функция сортировки по дате."""
    if sorting_order == "up":
        account_info.sort(key=lambda x: x["date"])
    else:
        account_info.sort(key=lambda x: x["date"], reverse=True)
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
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
