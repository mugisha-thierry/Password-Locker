class Account :
    """
    Class that generates new instances of accounts
    """

    list_of_accounts = [] # Empty account list


    def __init__(self,account_user_name,account_password):
        """
        __init__ method that helps us define properties for our objects.
        """
        self.account_user_name = account_user_name
        self.account_password = account_password

    def save_this_account(self):
        """
        save_this_account method saves account objects into account_list
        """
        Account.list_of_accounts.append(self)

    def delete_account(self):

        '''
        delete_account method deletes a saved account from the account_list
        '''

        Account.list_of_accounts.remove(self)    


    @classmethod
    def check_account(cls,account_username, account_password):
        """
        method to check whether the account is our account_list or not
        """
        real_account = ""
        for account in Account.list_of_accounts:
            if(account.account_user_name == account_user_name and account.account_password == account_password):
                real_account == account.user_name
        return real_account

        

    @classmethod
    def display_account(cls):
        """
        method that displays all signup accounts 
        """
        return cls.list_of_accounts 
