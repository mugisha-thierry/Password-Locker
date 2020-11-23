import unittest
from account import Account

class TestAccount(unittest.TestCase):
    """
    Test class that defines test cases for the account class behaviours.
    """

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_account = Account("mugisha-thierry","hakiza123")

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_account.account_user_name,"mugisha-thierry")
        self.assertEqual(self.new_account.account_password,"hakiza123") 

    def test_save_account(self):
        """
        test_save_account test case that saves new account
        """
        self.new_account.save_this_account()
        self.assertEqual(len(Account.list_of_accounts),1)

    def test_display_all_accounts(self):
        """
        test case to show all accounts in account_list
        """
        self.assertEqual(Account.display_account(),Account.list_of_accounts)    



    def tearDown(second_account):
        """
        tearDown method that does clean up after each test case has run.
        """
        Account.list_of_accounts= [] 


if __name__ == '__main__':
    unittest.main()
