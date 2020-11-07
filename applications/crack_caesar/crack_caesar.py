# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
with open("ciphertext.txt") as f:
  text = f.read()

char_list = [char for char in text]

char_dict = {}

for char in char_list:
  if char in char_dict and char.isalpha():
    char_dict[char] = char_dict[char] + 1
  elif char not in char_dict and char.isalpha():
    char_dict[char] = 1

list_char_dict = list(char_dict.items())

list_char_dict.sort(key=lambda tuple_pair: tuple_pair[1], reverse=True)

freq_list = []
for x in range(len(list_char_dict)):
  freq_list.append(list_char_dict[x][0])

freq_list.pop()

freq_analysis = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

decode_table = {}
for x in range(len(freq_list)):
  decode_table[freq_list[x]] = freq_analysis[x]

# print(char_list)
new_text = ''

for char in char_list:
  if char.isalpha() and char != 'â':
    new_text = new_text + decode_table[char]
  else:
    new_text = new_text + char

print(new_text)