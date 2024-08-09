import json
import os


def show_transaction_info(path: str) -> list[dict]:
    """Функция вывода транзакций с JSON файла"""
    transaction_info = []
    try:
        with open(path, encoding="utf8") as json_file:
            transaction_info = json.load(json_file)
        print(type(transaction_info))
        return transaction_info
    except FileNotFoundError:
        return transaction_info
    except json.JSONDecodeError:
        return transaction_info


if __name__ == "__main__":
    path_to_json = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")
    print(show_transaction_info(path_to_json))
