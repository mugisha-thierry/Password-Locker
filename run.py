#!/usr/bin/env python3.8
from account import Account
from credentials import Credentials


def create_account(account_user_name,account_password):
    """
    Function to create a new account
    """
    new_account = Account(account_user_name,account_password)
    return new_account

def save_account(account):
    '''
    Function to save contact
    '''
    account.save_this_account()

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
    return new_credentials 

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
    credentials.delete_credentials()

def find_credential(social_media):
    """
    Function that finds in credential socialmedia and returns the credentials that matches that socialmedia.
    """
    return Credentials.find_credentials(social_media)

def credential_exists(social_media):
    """
    Function that checks if a credential exists and return true or false.
    """
    return Credentials.credentials_exist(social_media)



def main():
    print('='*80)
    print('*' *80)
    print('-' *80)
    print("                   PASSWORD LOCKER (enjoy your safety)")
    print('-' *80)
    print('*' *80)
    print('='*80)
    print("\n What is your name")
    name = input()
    print(f"\n Hello {name},Good to see you. Use the following short codes to:")
    print('\n')
    print("-Create New account: CNA\n-Login to your account: LG  \n")
    short_code = input("").lower().strip()
    
    if short_code == "cna":
        print('\n')
        print("Sign Up")
        print('-' * 40)
        account_user_name = input("username:")
        print('\n')

        while True:
            print("-Type your password: TP\n-Generate random Password: RP \n")
            option = input().lower().strip()
            if option == 'tp':
                account_password = input("Enter password of your choice\n")
                break

            elif option == 'rp':
                password = password_creator()
                print(f"random password is {password} \n enter CH to use it or \n enter TP to type password of your choice")
                choice = input().lower().strip()
                if choice == 'ch':
                    account_password = password
                elif choice =='tp':
                    account_password = input("Enter password of your choice\n")
                else:
                    print("Invalid password please try again") 
                break

            else:
                print("Invalid password please try again")
        save_account(create_account(account_user_name,account_password)) # create and save new account. 
        print('\n')
        print("*"*65)
        print(f"Thanks {account_user_name}, Your account has been created succesfully!")
        print(f"Your Username is: {account_user_name}")
        print(f"Your  password is: {account_password}")
        print("*"*65)
        print('\n')


    elif short_code == "lg" :
        username = input("username: ")
        password = input("password: ")
        print("\n")
        print("You don't seem to have a signed up account,\n please try to start again and sign up. \n Byee ****")
        print("*"*65)
        print("\n")
        import sys
        sys.exit() 

        
    else:
        print("Use specified short Codes!!!!\n Byeee****")
        print("\n")
        import sys
        sys.exit()


    while True:
        print("Use these short codes:")
        print('-'*40)
        print("  -Save already existing credentials: SC\n  -Create new credentials:CC\n  -Dispaly credentials: DC\n  -Find a credential saved credentials using social media name : FC\n  -Delete credential: RC\n  -Exit the application:EX\n")
        short_code = input().lower().strip()

        if short_code == 'sc':
            print("Enter social media name")
            social_media = input()
            print(f"Enter {social_media} username")
            user_name = input()
            print(f"Enter {social_media} password")
            password = input()

            save_credentials(create_credentials(social_media ,user_name,password)) # create and save credentails.
            print ('\n')
            print("*"*65)
            print(f"Thefollowing credentails are saved:\n Social media name: {social_media}\n Username {user_name}\n Password {password}\n")
            print("*"*65)

        elif short_code == 'cc':
            print("Create social media name")
            social_media = input()
            print(f"Create {social_media} username")
            user_name = input()
            print(f"Create password for {social_media}")
            print("-Type your password: TP\n-Generate random Password: RP \n")
            option = input().lower().strip()
            if option == 'tp':
                password = input("Enter password of your choice\n")
                
            elif option == 'rp':
                passwords = password_creator()
                print(f"random password is {passwords} \n enter CH to use it or \n enter TP to type password of your choice")
                choice = input().lower().strip()
                if choice == 'ch':
                    password = passwords
                elif choice =='tp':
                    password = input("Enter password of your choice\n")
                else:
                    print("Invalid password please try again")     
            else:
                print("Invalid password please try again")

            save_credentials(create_credentials(social_media ,user_name,password)) # create and save credentails.
            print ('\n')    
            print("*"*65)
            print(f"Thefollowing credentails are created:\n Social media name: {social_media}\n Username {user_name}\n Password {password}\n")
            print("*"*65)    
        elif short_code == 'dc':
            if display_all_credential():
                print("Here is a list of all your credentials")
                print('-'*40) 
                print('\n')

                for credentials in display_all_credential():   
                    print(f"Social media: {credentials.social_media}       username: {credentials.user_name}     password: {credentials.password}")
                print("*"*70)    
                print('\n')

            else:
                print('\n')
                print("You dont seem to have any contacts saved yet")
                print('\n')     

        elif short_code == 'fc':
            print("Enter the social media name you want to search for")
            print('\n')
            search_name = input()
            if credential_exists(search_name):
                search_social_media = find_credential(search_name)
                print(f"username:{search_social_media.user_name}\n password: {search_social_media.password} ")
                
            else:
                print("That social media does not exist")

            print('*'*50)    

            print('\n')





        elif short_code == 'rc':
            print('\n')
            print("Enter the name of social media you want to delete it's credentials")
            print('\n')
            search_name = input()
            if credential_exists(search_name):
                search_social_media = find_credential(search_name)
                search_social_media.delete_credentials()
                print(f"{search_social_media.social_media} credentials were succefully deleted")
                print('*'*50)
                print('\n')

            else:
                print("That social media does not exist")
                print('*'*50)
                print('\n')       
    

        elif short_code == "ex":
            print("Bye see you next time **")
            break

        else:
            print("I really didn't get that. Please use the short codes")        

                

if __name__ == '__main__':
    main()
