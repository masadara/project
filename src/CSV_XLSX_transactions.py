import os

import pandas as pd


def xlsx_transactions(path: str) -> list[dict]:
    """Функция вывода транзакций с XLSX файла"""
    df = pd.read_excel(path)
    print(df.shape)
    return df.head().to_dict(orient="records")


def csv_transactions(path: str):
    """Функция вывода транзакций с CSV файла"""
    df = pd.read_csv(path)
    print(df.shape)
    return df.head()


path_to_xlsx = os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx")
transactions_full = xlsx_transactions(path_to_xlsx)
print(transactions_full)
