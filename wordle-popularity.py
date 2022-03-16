#/usr/bin/env python3

# See https://magnusviri.com/wordle.html

# use with https://github.com/tabatkins/wordle-list

from string import ascii_lowercase
from pprint import pprint
from os.path import expanduser 

# Set all chars to 0

char_scores = []
for i in range(6):
    char_scores.append({})
    for char in ascii_lowercase:
        char_scores[i][char] = 0

# Read the word file, save the words, count the chars in each position

fh = open(expanduser("~/Wordle_Solver/.words.txt"))
words = {}
for line in fh:
    words[line.rstrip()] = 0
    for i, char in enumerate(line.rstrip()):
        char_scores[i][char] += 1
        char_scores[5][char] += 1
fh.close()

# Give each word a score

for word in words:
    for i, char in enumerate(word):
        words[word] += char_scores[i][char]

# Sort the words by score

sorted_words = sorted(words.items(), key=lambda x:x[1], reverse=True)

# Remove words with duplicate chars

uniq_words = []
for word_hash in sorted_words:
    chars = {}
    uniq = True
    for i, char in enumerate(word_hash[0]):
        if not char in chars:
            chars[char] = 1
        else:
            uniq = False
    if uniq:
        uniq_words.append((word_hash[0], word_hash[1], chars))
#        uniq_words.append(word_hash)
# pprint(uniq_words)

# Find word sets

def build_word_set(depth, word_index, max_words, word_data, word_sets):
    counter = word_index+1
    asdf = True
    if (depth < 4):
        while counter < len(uniq_words):

            word1 = uniq_words[counter]
            uniq = 0

            # Make sure word is different enough

            for i, char in enumerate(word1[0]):
                for word, points, chars in word_data:
                    if char in chars:
                        uniq += 1
#                     if word[i] == char:
#                         uniq += 1
#                     if word[0] == "s":
#                         uniq += 1

            if uniq < 1 or depth >= 2 and uniq < depth:
                build_word_set(depth+1, counter, max_words, word_data+[word1], word_sets)
                asdf = False
                break
            else:
                counter += 1


    if asdf:
        words = []
        score = 0
        for word, points, chars in word_data:
            words.append(word)
            score += points 
        word_sets[", ".join(words)] = score
         

word_sets = {}
max_words = 40
for i in range(max_words):
    words = build_word_set(0, i, max_words, [uniq_words[i]], word_sets)


sorted_word_sets = sorted(word_sets.items(), key=lambda x:x[1], reverse=True)

# Print word scores

pprint(sorted_words)

# Print letter scores

ranked_chars = []
for i in range(6):
    ranked_chars.append(sorted(char_scores[i].items(), key=lambda x:x[1], reverse=True))
pprint(ranked_chars)

# Print word sets

pprint(sorted_word_sets)
