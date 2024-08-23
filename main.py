from src.processing import filter_by_state, sort_by_date
from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from src.utils import show_transaction_info
from src.decorators import log
from src.external_api import amount_transaction
from src.search import searching
from src.search import count_description
from src.CSV_XLSX_transactions import xlsx_transactions
from src.CSV_XLSX_transactions import csv_transactions
import logging
import os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "../qweqwe/logs/main.log")
abs_file_path = os.path.abspath(rel_file_path)
logger = logging.getLogger("main")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(abs_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

def main():
    trans_variant = input('Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n Выберите необходимый пункт меню:\n 1. Получить информацию о транзакциях из JSON-файла\n 2. Получить информацию о транзакциях из CSV-файла \n 3. Получить информацию о транзакциях из XLSX-файла\n')
    try:
        trans_variant = int(trans_variant)
    except ValueError as ex:
        logger.error(f"Произошла ошибка:{ex}, пользователь ввёл {trans_variant}")
        print('ошибка')
    if int(trans_variant) == 1:
        print("Программа: Для обработки выбран JSON-файл.")
        logger.info(f"Вариант {trans_variant}, выбран JSON-файл.")
        path_to_json = os.path.join(os.path.dirname(__file__), "..", "qweqwe", "data", "operations.json")
        transactions_full = show_transaction_info(path_to_json)
    elif int(trans_variant) == 2:
        print("Программа: Для обработки выбран CSV-файл.")
        logger.info(f"Вариант {trans_variant}, выбран CSV-файл.")
        path_to_csv = os.path.join(os.path.dirname(__file__), "..", "qweqwe", "data", "transactions.csv")
        transactions_full = csv_transactions(path_to_csv)
    elif int(trans_variant) == 3:
        print("Программа: Для обработки выбран XLSX-файл.")
        logger.info(f"Вариант {trans_variant}, выбран XLSX-файл.")
        path_to_xlsx = os.path.join(os.path.dirname(__file__), "..", "qweqwe", "data", "transactions_excel.xlsx")
        transactions_full = xlsx_transactions(path_to_xlsx)
    else:
        logger.error(f"Произошла ошибка: пользователь ввёл {trans_variant}")
        transactions_full = []
        print('ошибка')
    trans_filter_by_state = []
    while len(trans_filter_by_state) == 0:
        status_trans = input('Программа: Введите статус, по которому необходимо выполнить фильтрацию. \nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n')
        logger.info(f"Выбрана фильтрация: {status_trans}")
        if len(filter_by_state(transactions_full, status_trans.upper())) == 0:
            print(f'Статус операции {status_trans} недоступен.')
        else:
            trans_filter_by_state = filter_by_state(transactions_full, status_trans.upper())
    sorting_by_date = input('Отсортировать операции по дате? Да/Нет\n')
    if sorting_by_date.lower() == 'да':
        sorting_by_date_upper_lower = input('Отсортировать по возрастанию или по убыванию?\n')
        if sorting_by_date_upper_lower.lower() == 'по возрастанию':
            trans_filter_by_state = sort_by_date(trans_filter_by_state, 'up')
            logger.info(f"Выбрана сортировка {sorting_by_date_upper_lower}")
        else:
            trans_filter_by_state = sort_by_date(trans_filter_by_state, 'down')
            logger.info(f"Выбрана сортировка {sorting_by_date_upper_lower}")
    code_filter = input('Выводить только рублевые тразакции? Да/Нет\n')
    if code_filter.lower() == 'да':
        trans_filter_by_state = filter_by_currency(trans_filter_by_state, 'RUB')
    search_filter = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n')
    if search_filter.lower() == 'да':
        str_search = input('Введите слово для поиска\n')
        trans_filter_by_state = searching(trans_filter_by_state, str_search)
    print(f'Распечатываю итоговый список транзакций...\n Всего банковских операций в выборке: {len(trans_filter_by_state)}\n')
    for info in trans_filter_by_state:
        print(f'{get_date(info.get("date"))} {info.get("description")}')
        if info.get("description") == 'Открытие вклада':
            print(f'{mask_account_card(info.get("to"))}')
        else:
            print(f'{mask_account_card(info.get("from"))} -> {mask_account_card(info.get("to"))}')
        print(f'Сумма: {info.get("operationAmount").get("amount")} {info.get("operationAmount").get("currency").get("code")}\n')



if __name__ == "__main__":
    main()