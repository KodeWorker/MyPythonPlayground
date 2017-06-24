"""
Automate the Boring Stuff with Python
Chapter 7 Regular Expression - Practice Projects #2 RegEx. Version of strip()
Description: implement strip(string, character) function. It removes character
from string. If pass nothing to the second parameter, it removes whitespaces
from string.
"""

import re

def strip(string, character=None):
    if character == None:
        character = " "
    stripRegex = re.compile(character)
    striped = stripRegex.sub("", string)
    return striped

if __name__ == "__main__":
    string = "What the fuck you are talking about?"
    character = "k"
    print(strip(string, character))
    print(strip(string))
