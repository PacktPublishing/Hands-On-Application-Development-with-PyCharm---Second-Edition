from bank_account import BankAccount


class Item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class Transaction:
    def __init__(self, buyer: BankAccount, seller: BankAccount, item: Item):
        self.buyer = buyer
        self.seller = seller
        self.item = item

    def do_transaction(self):
        original_buyer_balance = self.buyer.balance
        original_seller_balance = self.seller.balance
        try:
            self.buyer.withdraw(self.item.price)
            self.seller.deposit(self.item.price)
        except ValueError:
            self.buyer.balance = original_buyer_balance
            self.seller.balance = original_seller_balance
            raise ValueError("Transaction failed and was rolled back")
