import random 
import string


class Credentials:


    list_of_credentials = []

    def __init__(self,social_media,user_name,password):
        self.social_media = social_media
        self.user_name = user_name
        self.password = password

    def save_this_credentials(self):
        Credentials.list_of_credentials.append(self)

    def delete_credentials(self):
        Credentials.list_of_credentials.remove(self)

    @classmethod    
    def find_credentials(cls,name_of_social_media):
        for credentials in cls.list_of_credentials:
            if credentials.social_media == name_of_social_media:
                return credentials

    @classmethod
    def password_generate(cls):
        """
        Generate a random password using string of letters and digits and special characters
        """
        size = 8
        charact = string.ascii_letters + string.digits + string.punctuation
        pass_word = ''.join(random.choice(charact)for i in range(size))
        return pass_word            
    @classmethod
    def display_credentials(cls):
        """
        This will display all credentials we have in our credential list
        """
        return cls.list_of_credentials

    @classmethod
    def credentials_exist(cls,name_of_social_media):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for credentials in cls.list_of_credentials:
            if credentials.social_media == name_of_social_media:
                    return True

        return False    