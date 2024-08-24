from typing import Union
import logging
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(rel_file_path)
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(abs_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str, int] = 0) -> str:
    """Функция маскировки номера банковской карты."""
    card_number = str(card_number)
    mask_card_number = card_number[:6] + "*" * 6 + card_number[-4:]
    if len(card_number) == 18:
        logger.info(f"Выполняем маскировку номера банковской карты для {card_number}")
        mask_card_number = mask_card_number[:8] + " " + mask_card_number[-10:]
        return mask_card_number
    elif len(card_number) == 16:
        logger.info(f"Выполняем маскировку номера банковской карты для {card_number}")
        mask_card_number = (
            mask_card_number[:4]
            + " "
            + mask_card_number[4:8]
            + " "
            + mask_card_number[8:12]
            + " "
            + mask_card_number[-4:]
        )
    else:
        logger.error(f"Произошла ошибка, номер карты {card_number} - невалидный")
        return "error"
    return mask_card_number


def get_mask_account(account: Union[str, int]) -> str:
    """Функция маскировки номера банковского счета."""
    account = str(account)
    if len(account) == 20:
        logger.info(f"Выполняем маскировку номера банковского счета для {account}")
        mask_account = "*" * 2 + account[-4:]
        return mask_account
    else:
        logger.error(f"Произошла ошибка, номер счёта {account} - невалидный")
        return "error"


if __name__ == "__main__":
    print(get_mask_card_number("dfggdf"))
    print(get_mask_account("736541084312374305"))
