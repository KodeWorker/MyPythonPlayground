"""
Automate the Boring Stuff with Python
Chapter 7 Regular Expression - Project: Multiclipboard implementation
Description:
    - The command line argument for the keyword is checked.
    - If the argument is save, then the clipboard contents are saved to the keyword.
    - If the argument is list, then all the keywords are copied to the clipboard.
    - Otherwise, the text for the keyword is copied to the keyboard.    
"""

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()