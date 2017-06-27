"""
Automate the Boring Stuff with Python
Chapter 7 Regular Expression - Project: Mad Libs
Description:
    Create a Mad Libs program that reads in text files and lets the user add 
    their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears 
    in the text file. For example, a text file may look like this:
    - The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was 
    unaffected by these events.    
"""

if __name__ == '__main__':
    ADJECTIVE = input("Enter an adjective:\n")
    NOUN_1 = input("Enter a noun:\n")
    VERB = input("Enter a verb:\n")
    NOUN_2 = input("Enter another noun:\n")
    
    text = 'The ' + ADJECTIVE + ' panda walked to the ' + NOUN_1 + ' and then '\
    + VERB + '. A nearby ' + NOUN_2 + ' was unaffected by these events.'
    
    with open('MadLibs.txt','w') as write_file:
        write_file.write(text)