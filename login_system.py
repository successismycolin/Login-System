import string

class InvalidLoginDetails(Exception):
    pass

def username_is_valid(username):
    """Check if a username is valid."""
    has_alphabet = False
    has_digit = False
    has_no_space = True
    has_no_punctuation = True

    for char in username:
        if char.isalpha():
            has_alphabet = True
        if char.isdigit():
            has_digit = True
        if ' ' in char:
            has_no_space = False
        if char in string.punctuation:
            has_no_punctuation =  False        
    
    return has_alphabet and has_digit and has_no_space and has_no_punctuation

def password_is_valid(password):
    """Check if a password is valid."""
    if len(password) < 8: # Determine if length is valid first and exit early if false.
        return False
    
    has_alphabet = False
    has_digit = False
    has_punctuation = False
    has_no_space = True

    for char in password:
        if char.isalpha():
            has_alphabet = True
        if char.isdigit():
            has_digit = True
        if char in string.punctuation:
            has_punctuation = True
        if ' ' in char:
            has_no_space = False

    return has_alphabet and has_digit and has_punctuation and has_no_space

def create_account(username, password):
    """Create an account and write the details entered to the textfile."""
    file_path = r'C:\Users\DELL\Desktop\Python Projects\Login System\user_log.txt'
    if username_is_valid(username) and password_is_valid(password):
        with open(file_path, 'a') as f:
            f.write(f"{username} - {password}")
            f.write("\n")
        print("Account successfully created.")
    else:
        print("Login details invalid.")


def login(username, password):
    """Use the details provided to login to an existing account."""
    file_path = r'C:\Users\DELL\Desktop\Python Projects\Login System\user_log.txt'
    with open(file_path, 'r') as f:
        contents = f.readlines()

    account_exists = False

    for user in contents:
        if username in user and password in user:
            account_exists = True
            break

    if account_exists:
        print("You've logged in successfully.")
    else:
        raise InvalidLoginDetails("Login Details Invalid.")