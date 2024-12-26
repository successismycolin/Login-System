import unittest
import login_system

class TestLoginSystem(unittest.TestCase):
    def test_valid_login_username(self):
        username = 'sphume123'
        self.assertTrue(login_system.username_is_valid(username))

        username = 'sphume 123'
        self.assertFalse(login_system.username_is_valid(username))

    def test_valid_login_password(self):
        password = 'Password123@' # Capital letter, small letter, digit, special character, length >= 8
        self.assertTrue(login_system.password_is_valid(password))

        password = 'password123'
        self.assertFalse(login_system.password_is_valid(password))

    def test_new_details_written_to_textfile(self):
        username = 'sphume123'
        password = 'Password123@'
        
        login_system.create_account(username, password)  # this function writes the new details to the textfile

        file_path = r'C:\Users\DELL\Desktop\Python Projects\Login System\user_log.txt'

        with open(file_path, 'r') as f:  # reading the file to see if the new details have been written to the textfile
            contents = f.readlines()

        self.assertEqual(f'{username} - {password}\n', contents[-1])

    def test_incorrect_details(self):
        username = 'sphue123'
        password = 'Password123@'

        with self.assertRaises(login_system.InvalidLoginDetails):
            login_system.login(username, password)

        file_path = r'C:\Users\DELL\Desktop\Python Projects\Login System\user_log.txt'

        with open(file_path, 'r') as f:
            contents = f.readlines()

        # Ensure that invalid login does not log the user to the file
        self.assertNotIn(f"{username} - {password}\n", contents)


if __name__ == '__main__':
    unittest.main()