from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция маскировки номера банковской карты."""
    card_number = str(card_number)
    mask_card_number = card_number[:6] + "*" * 6 + card_number[12:]
    mask_card_number = (
        mask_card_number[:4] + " " + mask_card_number[4:8] + " " + mask_card_number[8:12] + " " + mask_card_number[12:]
    )
    return mask_card_number


def get_mask_account(account: Union[str, int]) -> str:
    """Функция маскировки номера банковского счета."""
    account = str(account)
    mask_account = "*" * 2 + account[16:]
    return mask_account


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
