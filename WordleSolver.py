#!/usr/bin/python3
'''
portions of this code were copied from https://gist.github.com/magnusviri/a93b5ab02663f30eac176ca49b0250e3
ty m8!
https://magnusviri.com/wordle.html
'''

#TODO add elimination guess 
#TODO add frequency guess OR elemination heuristic


from os.path import exists
from os.path import expanduser
from string import ascii_lowercase
from pprint import pprint

#sums frequency of each letter in letters
#returns sorted list of tuple (s, w) where s is the sum of the frequency of each unique letter in w
def letterFrequencySort(words, letters):
    frequencyScores = []
    letterFrequency = {}
    for l in letters:
        letterFrequency[l] = 0
    for w in words:
        for l in w:
            if l in letters:
                letterFrequency[l] = letterFrequency[l]+1
    for w in words:
        score = 0
        for i in range(len(w)):
            if w[i] in letters and w[i] not in w[:i]: 
                score = score + letterFrequency[w[i]]
        frequencyScores.append((score, w))

    return sorted(frequencyScores, reverse=True)

#iterates over each word in words, returns list of values where:
    #word[n] = l for pLetteres[i] = (n, l) 
    #word contians all in inLetters
    #word does not contain any of outLetters
def filterWords(words, outLetters, inLetters, pLetters): 
    filteredWords = []
    for w in words:
        notMatch = 0
        for o in outLetters:
            if o in w:
                notMatch = 1
        #        print(o+" in "+w)
                break
        if notMatch == 0:
            for i in inLetters:
                #print(i)
                #print(w[i[0]])
                if i[1] not in w or w[i[0]] == i[1]:
                    notMatch = 1
         #           print(i+" not in "+w)
                    break
            if notMatch == 0:
                for p in pLetters:
                    if w[p[0]] != p[1]:
                        notMatch = 1
         #               print(w[p[0]]+" != "+p[1])
                        break
                if notMatch == 0:
                    filteredWords.append(w)
    return filteredWords
                    
#translates correctly formated input string into input data sturcture            
def fwArgFormat(inStr):
    argv = [[], [], []]
    letterArgs = inStr.split()
    #print(letterArgs[0][0])
    for i in range(5):
        if letterArgs[i][0] == '!':
            argv[0].append(letterArgs[i][1])
        elif letterArgs[i][0] == '*':
            argv[1].append((i, letterArgs[i][1]))
        else:
            argv[2].append((i, letterArgs[i][0]))
    return argv
#full file name
wordFilePath = expanduser("~/Wordle_Solver/words.txt")


#open file
if exists(wordFilePath):
    fh = open(wordFilePath, 'r')
   #print("File Open")
'''
else:
    pprint("File Not Found.")
'''

#add each word to list
masterList = []
for line in fh:
   masterList.append(line.strip())
#pprint(masterList)

#pprint(letterFrequencySort(masterList, ascii_lowercase))

#testList = ['a', 'e', 'i', 'o', 'u']
#pprint(letterFrequencySort(masterList, testList)) 
#pprint(letterFrequencySort(filterWords(masterList, [], [], [(1, 'o'), (2, 'u'), (3, 'l'), (4, 'd')]), ascii_lowercase))

''''
inStr = input("test format: ")

testArg = fwArgFormat(inStr)

print(testArg)

curList = filterWords(masterList, testArg[0], testArg[1], testArg[2])

print(curList)
'''
curList = masterList

while(True):
#while there is more than 1 possible word:

    #analize letter frequency
    #sort words by sum of letter frequency
    wordScores = letterFrequencySort(curList, ascii_lowercase)
    #select word with greatest score
    print("Best guess: "+str(wordScores[0]))

    inStr = input("Input guess result or press 'q' to exit\n")
    if inStr == 'q':
        break

    #get updated word information from guess
    testArg = fwArgFormat(inStr)
    curList = filterWords(curList, testArg[0], testArg[1], testArg[2])
   

print("Exiting")
