import unittest
from account import Account

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.new_account = Account("mugisha-thierry","hakiza123")

    def test_init(self):
        self.assertEqual(self.new_account.account_user_name,"mugisha-thierry")
        self.assertEqual(self.new_account.account_password,"hakiza123") 

    def test_save_account(self):
        self.new_account.save_this_account()
        self.assertEqual(len(Account.list_of_accounts),1)

    # def test_save_multiple_accounts(self):
    #     self.new_account.save_this_account()
    #     second_account = Account("Ketsia-a","high123")
    #     second_account.save_this_account()
    #     self.assertEqual(len(Account.list_of_accounts),2)





    def tearDown(second_account):
        Account.list_of_accounts= [] 


if __name__ == '__main__':
    unittest.main()
