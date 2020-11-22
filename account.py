class Account :

    list_of_accounts = []


    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password

    def save_this_account(self):
        Account.list_of_accounts.append(self)

    def delete_account(self):

        '''
        delete_account method deletes a saved account from the account_list
        '''

        Account.list_of_accounts.remove(self)    


    @classmethod
    def check_account(cls,username, password):
        """
        method to check whether the account is our account_list or not
        """
        real_account = ""
        for account in Account.list_of_accounts:
            if(account.user_name == user_name and account.password == password):
                real_account == account.user_name
        return real_account

        

    @classmethod
    def display_account(cls):
        return cls.list_of_accounts         
