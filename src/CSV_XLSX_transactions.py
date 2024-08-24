import os

import pandas as pd


def xlsx_transactions(path: str) -> list[dict]:
    """Функция вывода транзакций с XLSX файла"""
    df = pd.read_excel(path)
    # print(df.shape)
    return df.to_dict(orient="records")


def csv_transactions(path: str) -> list[dict]:
    """Функция вывода транзакций с CSV файла"""
    df = pd.read_csv(path, delimiter=';')
    print(df.shape)
    return df.to_dict(orient="records")


# path_to_xlsx = os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx")
# transactions_full = xlsx_transactions(path_to_xlsx)
# path_to_csv = os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv")
# transactions_full = csv_transactions(path_to_csv)
# print(transactions_full)

