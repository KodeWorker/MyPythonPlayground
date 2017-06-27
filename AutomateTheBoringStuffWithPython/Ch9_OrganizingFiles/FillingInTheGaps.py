"""
Automate the Boring Stuff with Python
Chapter 9 Organizing Files - Project: Filling in the Gaps
Description:
    Write a program that finds all files with a given prefix, such as 
    spam001.txt, spam002.txt, and so on, in a single folder and locates any
    gaps in the numbering (such as if there is a spam001.txt and spam003.txt
    but no spam002.txt). Have the program rename all the later files to close
    this gap.

    As an added challenge, write another program that can insert gaps into
    numbered files so that a new file can be added. (x)
"""
import os
import shutil

def filling_the_gaps(search_dir, prefix):
    files = os.listdir(search_dir)
    sorted_num = sorted([int(file[len(prefix):-4]) for file in files if file.startswith(prefix)])
    new_filename = ['%s%03d.txt' %(prefix, sorted_num[0]+i) for i in range(len(sorted_num))]
    for i in range(len(files)):
        shutil.move(search_dir + '/' + files[i], search_dir + '/' + new_filename[i])

if __name__ == '__main__':
    search_dir = os.path.join(os.path.dirname(__file__), 'test_gaps')
    prefix = 'wtf'
    filling_the_gaps(search_dir, prefix)