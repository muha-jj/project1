def deposit(balance, amount):
    return balance + amount


def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")
    return balance - amount
