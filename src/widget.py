from typing import Union


def mask_account_card(account: Union[str] = '0') -> str:
    """Функция маскировки аккаунта."""
    if isinstance(account, str):
        if len(account) == 1:
            return 'error'
        if "Счет" in account:
            mask_account = account[:5] + "*" * 2 + account[-4:]
        elif "Maestro" in account:
            mask_account = account[:14] + "*" * 6 + account[20:]
            mask_account = (
                mask_account[:12] + " " + mask_account[12:16] + " " + mask_account[16:20] + " " + mask_account[20:]
            )
        elif "MasterCard" in account:
            mask_account = account[:17] + "*" * 6 + account[23:]
            mask_account = (
                mask_account[:15] + " " + mask_account[15:19] + " " + mask_account[19:23] + " " + mask_account[23:]
            )
        elif "Visa Classic" in account:
            mask_account = account[:18] + "*" * 6 + account[24:]
            mask_account = (
                mask_account[:16] + " " + mask_account[16:20] + " " + mask_account[20:24] + " " + mask_account[24:]
            )
        elif "Visa Platinum" in account:
            mask_account = account[:20] + "*" * 6 + account[26:]
            mask_account = (
                mask_account[:18] + " " + mask_account[18:22] + " " + mask_account[22:26] + " " + mask_account[26:]
            )
        elif "Visa Gold" in account:
            mask_account = account[:16] + "*" * 6 + account[22:]
            mask_account = (
                mask_account[:14] + " " + mask_account[14:18] + " " + mask_account[18:22] + " " + mask_account[22:]
            )
        else:
            return 'error'
        return mask_account
    else:
        return 'error'


def get_date(date: Union[str] = '0') -> str:
    """Функция форматирования даты."""
    if isinstance(date, str):
        if len(date) == 1 or len(date) == 0:
            return "error"
        date_in_the_format = date[8:10] + "." + date[5:7] + "." + date[:4]
        return date_in_the_format
    else:
        return 'error'


if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Счет 35383033474447895560"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
