"""
Automate the Boring Stuff with Python
Chapter 8 Reading and Writing Files - Project: Regex Search
Description:
    Opens all .txt files in a folder and searches for any line that matches a 
    user-supplied regular expression. The results should be printed to the 
    screen.
"""
import os
import re

def RegEx_Search(folder, RegEx):
    files = [x for x in os.listdir(folder) if x.endswith('.txt')]
    for file in files:
        with open(folder + '/' + file, 'r') as read_file:
            line_text = read_file.readlines()
            for line in line_text:
                Regex_results = re.search(RegEx, line)
                print(Regex_results.group())

if __name__ == '__main__':
    folder = os.path.dirname(__file__)
    RegEx = ".*"    
    RegEx_Search(folder, RegEx)