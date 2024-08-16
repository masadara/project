import json
import os
import logging


current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "../logs/utils.log")
abs_file_path = os.path.abspath(rel_file_path)
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(abs_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def show_transaction_info(path: str) -> list[dict]:
    """Функция вывода транзакций с JSON файла"""
    transaction_info = []
    try:
        logger.info(f"Попытка получить транзакции из json файла по пути: {path}")
        with open(path, encoding="utf8") as json_file:
            transaction_info = json.load(json_file)
        print(type(transaction_info))
        return transaction_info
    except FileNotFoundError as ex:
        logger.error(f"Произошла ошибка:{ex}")
        return transaction_info
    except json.JSONDecodeError as ex:
        logger.error(f"Произошла ошибка:{ex}")
        return transaction_info


if __name__ == "__main__":
    path_to_json = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")
    print(show_transaction_info(path_to_json))
