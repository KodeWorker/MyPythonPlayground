"""
Automate the Boring Stuff with Python
Chapter 7 Regular Expression - Practice Projects #1 Strong Passwoard Detection
Description: detect the password with at least 8 characters long, contains both
uppercase and lowercase characters, and has at least 1 digit.
"""

import re

def password_is_valid(password):
    # at least 8 characters
    condition_1 = len(password) >= 8
    # contains both uppercase and lowercase characters
    lower_case = re.search(r"[a-z]", password)
    upper_case = re.search(r"[A-Z]", password)
    condition_2 = lower_case != None and upper_case != None
    # at least 1 digit
    one_digit = re.search(r"\d+", password)
    condition_3 = one_digit != None

    if condition_1 and condition_2 and condition_3:
        return True
    else:
        return False

if __name__ == "__main__":
    password = "KDisFukinAwesome2"
    #password = "aaaaaaaaaaaaaaaaa"
    #password = "AAAAAAaaaa"
    #password = "aaa"
    print(password_is_valid(password))
