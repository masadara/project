from typing import Union


def get_mask_card_number(card_number: Union[str, int] = 0) -> str:
    """Функция маскировки номера банковской карты."""
    card_number = str(card_number)
    if len(card_number) == 1 or len(card_number) == 0:
        return 'error'
    mask_card_number = card_number[:6] + "*" * 6 + card_number[-4:]
    if len(card_number) == 18:
        mask_card_number = mask_card_number[:8] + " " + mask_card_number[-10:]
        return mask_card_number
    mask_card_number = (
        mask_card_number[:4] + " " + mask_card_number[4:8] + " " + mask_card_number[8:12] + " " + mask_card_number[-4:]
    )
    return mask_card_number


def get_mask_account(account: Union[str, int]) -> str:
    """Функция маскировки номера банковского счета."""
    account = str(account)
    mask_account = "*" * 2 + account[-4:]
    return mask_account


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account('73654108430135874305'))
