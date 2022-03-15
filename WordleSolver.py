#!/usr/bin/python3
'''
portions of this code were copied from https://gist.github.com/magnusviri/a93b5ab02663f30eac176ca49b0250e3
ty m8!
'''

import sys
from os.path import exists
from os.path import expanduser

#full file name
wordFilePath = expanduser("~/Wordle_Solver/.words.txt")


#open file
if exists(wordFilePath):
    fh = open(wordFilePath, 'r')
    print("File Open")
else:
    print("File Not Found.")


#add each word to list
masterList = []


#while there is more than 1 possible word:

    #analize letter frequency

    #sort words by sum of letter frequency

    #select word with greatest score

    #get updated word information from guess



