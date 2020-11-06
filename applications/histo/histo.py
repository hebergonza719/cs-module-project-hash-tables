# Your code here
import re

with open("robin.txt") as f:
    words = f.read()

words = words.lower()

pattern = '[\"\:\;\,\.\-\+\=\/\\\|[\]\{\}\(\)\*\^\&]'
words = re.sub(pattern, '', words)

words_split = words.split()

biggest_word = 0
for word in words_split:
	if len(word) > biggest_word:
		biggest_word = len(word)

lookup = {}
for word in words_split:
	if word not in lookup:
		lookup[word] = "#"
	else:
		lookup[word] = lookup[word] + "#"

list_lookup = list(lookup.items())

list_lookup.sort()

list_lookup.sort(key=lambda tuple_pair: tuple_pair[1], reverse=True)

for i in list_lookup:
	print(i[0] + "  " + (" " * (biggest_word - len(i[0]))) + i[1])