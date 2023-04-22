class BankAccount:
    def __init__(self, name: str, account_number: str, balance: float):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount: float) -> None:
        new_balance = self.balance - amount
        if new_balance > 0:
            self.balance = new_balance
        else:
            raise ValueError("Account overdrawn!")

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be greater than 0.")
