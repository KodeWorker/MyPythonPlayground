"""
Automate the Boring Stuff with Python
Chapter 9 Organizing Files - Project: Selective Copy
Description:
    Write a program that walks through a folder tree and searches for files 
    with a certain file extension (such as .pdf or .jpg). Copy these files from
    whatever location they are in to a new folder.
"""
import os
import shutil

def selective_copy(search_dir, save_dir, extension):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    for folderName, subfolders, filenames in os.walk(search_dir):
        for file in filenames:
            if file.endswith(extension):
                shutil.copy(folderName + '/' + file, save_dir + '/' + file)

if __name__ == '__main__':
    search_dir = os.path.join(os.path.dirname(__file__), '..', '..')
    extension = '.txt'
    save_dir = os.path.join(os.path.dirname(__file__), 'copied')
    
    selective_copy(search_dir, save_dir, extension)