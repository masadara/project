import json
import os

import requests
from dotenv import load_dotenv

load_dotenv(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".env",
    )
)
apikey = os.getenv("API_KEY")


def amount_transaction(transaction: dict) -> float:
    """Функция вывода суммы с конвертацией из USD и EUR в RUB"""
    if (
        transaction["operationAmount"]["currency"]["code"] == "USD"
        or transaction["operationAmount"]["currency"]["code"] == "EUR"
    ):
        amount = transaction["operationAmount"]["amount"]
        code = transaction["operationAmount"]["currency"]["code"]
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"
        headers = {"apikey": apikey}
        response = requests.request("GET", url, headers=headers)
        result = json.loads(response.text)
        return float(result["result"])
    else:
        return float(transaction["operationAmount"]["amount"])


if __name__ == "__main__":
    print(
        amount_transaction(
            {
                "id": 74897425,
                "state": "EXECUTED",
                "date": "2019-02-08T09:09:35.038506",
                "operationAmount": {"amount": "62654.30", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 28429442875257789335",
                "to": "Счет 95473010446151855633",
            }
        )
    )
