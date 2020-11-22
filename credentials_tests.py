import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
        Set up method to run before each test cases.
        """

        self.new_credentials = Credentials("instagram","mugisha-thierry","hakiza123")

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """

        self.assertEqual(self.new_credentials.social_media,"instagram")
        self.assertEqual(self.new_credentials.user_name,"mugisha-thierry")
        self.assertEqual(self.new_credentials.password,"hakiza123") 

    def test_save_credentials(self):
        """
        test_save_credentials test case to test if the credentials object is saved into
        the credential list
        """ 

        self.new_credentials.save_this_credentials()
        self.assertEqual(len(Credentials.list_of_credentials),1)

    def test_save_multiple_credentials(self):
        """
        test_save_multiple_credentials to check if we can save multiple credentials
        objects to our credential_list
        """   

        self.new_credentials.save_this_credentials()
        second_credential = Credentials("facebook","Ketsia-a","high123")
        second_credential.save_this_credentials()
        self.assertEqual(len(Credentials.list_of_credentials),2)

    def test_delete_credentials(self):
        """
        test_delete_credentials will help a user to delete the credentials he doesn't want 
        to keep in his or her credentials_list
        """
        
        self.new_credentials.save_this_credentials()
        second_credential = Credentials("facebook","Ketsia-a","high123")
        second_credential.save_this_credentials()
        # self.assertEqual(len(Credentials.list_of_credentials),2)
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.list_of_credentials),1)

    def test_find_credentials_by_socialmedia(self):
        """
        test case to help us to search for credentials of any given social media using social media name
        """
        self.new_credentials.save_this_credentials()
        second_credential = Credentials("facebook","Ketsia-a","high123")
        second_credential.save_this_credentials()
        # self.assertEqual(len(Credentials.list_of_credentials),2)
        self.new_credentials.delete_credentials()

        found_credentials = Credentials.find_credentials("facebook")
        self.assertEqual(found_credentials.social_media,second_credential.social_media)


    def test_password_generate(self):
        """"
        test case to test if a user can log into their credentials
        """
        password_generate = self.new_credentials.password_generate()
        self.assertEqual(len(password_generate),8)

    def test_display_all_credentials(self):
        """
        test case to show all credentails in credential_list
        """
        self.assertEqual(Credentials.display_credentials(),Credentials.list_of_credentials)

    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''
        self.new_credentials.save_this_credentials()
        second_credential = Credentials("facebook","Ketsia-a","high123")
        second_credential.save_this_credentials()
        
        contact_exists = Contact.contact_exist("0711223344")

        self.assertTrue(contact_exists)





    def tearDown(second_account): 
        Credentials.list_of_credentials= []   

if __name__ == '__main__':
    unittest.main()  