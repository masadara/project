

def get_mask_card_number(card_number: int):
    card_number = str(card_number)
    mask_card_number = card_number[:6] + "*" * 6 + card_number[12:]
    return mask_card_number


def get_mask_account(account: int):
    account = str(account)
    mask_account = "x" * 2 + account[16:]
    return mask_account


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
