import unittest

from tools import deposit, withdraw


class TestBank(unittest.TestCase):

    def test_deposit(self):
        balance = 500

        result = deposit(balance, 100)

        self.assertEqual(result, 600)

    def test_withdraw(self):
        balance = 500

        result = withdraw(balance, 200)

        self.assertEqual(result, 300)

    def test_insufficient_balance(self):
        balance = 500

        with self.assertRaises(ValueError):
            withdraw(balance, 600)


if __name__ == "__main__":
    unittest.main()
