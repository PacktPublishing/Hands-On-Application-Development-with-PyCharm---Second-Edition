import unittest
from bank_account import BankAccount


class BankAccountTestCase(unittest.TestCase):
    def test_init(self):
        test_account = BankAccount("Bruce Van Horn", "123355-23434", 4000)
        self.assertEqual(test_account.name, "Bruce Van Horn")
        self.assertEqual(test_account.account_number, "123355-23434")
        self.assertEqual(test_account.balance, 4000)

    def test_withdraw(self):
        self.fail()

    def test_deposit(self):
        self.fail()

    
if __name__ == '__main__':
    unittest.main()
