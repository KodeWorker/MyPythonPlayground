"""
Automate the Boring Stuff with Python
Chapter 9 Organizing Files - Project: Deleting Unneeded Files
Description:
    Write a program that walks through a folder tree and searches for 
    exceptionally large files or folders—say, ones that have a file size of
    more than 100MB. (Remember, to get a file’s size, you can use
    os.path.getsize() from the os module.) Print these files with their
    absolute path to the screen.
"""
import os

def search_large_file(search_dir):
    for folderName, subfolders, filenames in os.walk(search_dir):
        for file in filenames:
            if os.path.getsize(folderName + '/' + file) >= 100000000:
                print('abs. path: %s (%d bytes)' %(folderName + '/' + file, os.path.getsize(folderName + '/' + file)))

if __name__ == '__main__':
    search_dir = "D:/"
    search_large_file(search_dir)