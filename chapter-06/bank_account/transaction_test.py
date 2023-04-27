from unittest import TestCase
from bank_account import BankAccount
from transaction import Transaction, Item

initial_seller_balance = 4000
seller_account = BankAccount("PacktPub", "839423-38402",
                             initial_seller_balance)
item = Item("Python book", 39.95)


class TestTransaction(TestCase):
    def test_do_transaction(self):
        buyer_account = BankAccount("Bruce Van Horn", "123355-23434", 99)

        test_transaction = Transaction(buyer_account, seller_account,
                                       item)

        test_transaction.do_transaction()

        self.assertEqual(buyer_account.balance, 99 - 39.95)
        self.assertEqual(seller_account.balance, initial_seller_balance +
                         39.95)

    def test_transaction_overdraw_fault(self):
        seller_account.balance = 4000
        buyer_account = BankAccount("Bruce Van Horn", "123355-23434", 5)
        test_transaction = Transaction(buyer_account, seller_account,
                                       item)

        try:
            test_transaction.do_transaction()
        except ValueError as e:
            self.assertEqual(str(e), "Transaction failed and was rolled "
                                        "back")
        finally:
            self.assertEqual(buyer_account.balance, 5)
            self.assertEqual(seller_account.balance, initial_seller_balance)
