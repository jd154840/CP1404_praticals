"""
Estimation: 30 min
Actual Time: 40 min
"""
from operator import length_hint

# get user text string
# create a blank dictionary
# for words in text word.append() blank dictionary
text = input('Text: ')
words = text.split(' ')
word_dict = {}

for word in words:
    word_dict[word] = word_dict.get(word, 0) + 1

MAX_WORD = max(len(word) for word in list(word_dict.keys()))
for word in word_dict:
    print(f"{word:{MAX_WORD}}: {word_dict[word]}")
