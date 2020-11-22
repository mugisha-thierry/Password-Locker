class Account :

    list_of_accounts = []


    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password

    def save_this_account(self):
        Account.list_of_accounts.append(self)
