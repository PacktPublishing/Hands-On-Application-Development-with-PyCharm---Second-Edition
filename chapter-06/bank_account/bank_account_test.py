import unittest
from bank_account import BankAccount


class BankAccountTestCase(unittest.TestCase):
    def test_init(self):
        test_account = BankAccount("Bruce Van Horn", "123355-23434", 4000)
        self.assertEqual(test_account.name, "Bruce Van Horn")
        self.assertEqual(test_account.account_number, "123355-23434")
        self.assertEqual(test_account.balance, 4000)

    def test_withdraw(self):
        test_account = BankAccount("Bruce Van Horn", "123355-23434", 4000)
        test_account.withdraw(2000)
        self.assertEqual(test_account.balance, 2000)

    def test_overdraft(self):
        test_account = BankAccount("Bruce Van Horn", "123355-23434", 4000)
        self.assertRaises(ValueError, test_account.withdraw, 5000)

    def test_deposit(self):
        test_account = BankAccount("Bruce Van Horn", "123355-23434", 0)
        test_account.deposit(4000)
        self.assertEqual(test_account.balance, 4000)

    def test_deposit_negative_number_fail(self):
        test_account = BankAccount("Bruce Van Horn", "123355-23434", 4000)
        self.assertRaises(ValueError, test_account.deposit, -2000)
