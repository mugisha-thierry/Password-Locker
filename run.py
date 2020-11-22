#!/usr/bin/env python3.8
from account import Account
from credentials import Credentials

def create_account(user_name,password):
    """
    Function to create a new account
    """
    new_account = Account(user_name,password)
    return new_account

def save_account(account):
    '''
    Function to save contact
    '''
    account.save_this_account()

def display_accounts(account):
    """
    Function to display saved account
    """
    return Account.display_account()

def delete_accounts(account):
    """
    Function to delete account
    """
    account.delete_account()

def create_credentials(social_media ,user_name,password):
    """
    Function to create a new credential
    """
    new_credentials = Credentials(social_media ,user_name,password)
    return new_credential 

def save_credentials(credentials):
    """
    Function to save credential
    """
    credentials.save_this_credentials()

def display_all_credential():
    """
    Function that displays all credentials
    """
    return Credentials.display_credentials()

def password_creator():
    """
    Function that creates a password for the user
    """
    return Credentials.password_generate()        

def delete_credential(credentials):
    """
    Function to delete credentials
    """
    credential.delete_credentials()

def find_credential(social_media):
    """
    Function that finds in credential socialmedia and returns the credentials that matches that socialmedia.
    """
    return Credential.find_credentials(social_media)

def credential_exists(social_media):
    """
    Function that checks if a credential exists and return true or false.
    """
    return Credentials.credentials_exist(social_media)





def main():
    print("Hello Welcome to your contact list. What is your name?")



if __name__ == '__main__':
    main()
