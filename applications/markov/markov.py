import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
def print_random_sentence(input_string):
    lookup = {}
    individual_words = input_string.split()
    for idx in range(len(individual_words)):
        if individual_words[idx] in lookup:
            lookup[individual_words[idx]].append(individual_words[idx + 1])
        else:
            if idx == len(individual_words) - 1:
                pass
            else:
                lookup[individual_words[idx]] = [individual_words[idx + 1]]
    # start_words = []
    # for word in individual_words:
    #     if word.istitle() or (word[0] == '"' and word[1].isupper()):
    #         start_words.append(word)
    start_words = {}
    for key, value in lookup.items():
        if (key.istitle() or (key[0] == '"' and key[1].isupper())) and (key[-1] != "." and key[-1] != "?" and key[-1] != '"' and key[-1] != '!'):
            start_words[key] = value

    stop_words = {}
    for key, value in lookup.items():
        if key[-1] == "." or key[-1] == "?" or key[-1] == "!" or (key[-1] == '"' and key[-2] == ".") or (key[-1] == '"' and key[-2] == "?") or (key[-1] == '"' and key[-2] == "!"):
            stop_words[key] = value

    random_start = random.choice(list(start_words.keys()))
    
    print(random_start, end=" ")

    next_word = random.choice(list(lookup[random_start]))
    while next_word in lookup:
        if next_word in start_words:
            pass
        else:
            print(next_word, end=" ")
            if next_word in stop_words:
                print("\n")
                return
        next_word = random.choice(list(lookup[next_word]))

# TODO: construct 5 random sentences
# Your code here

print_random_sentence(words)
print_random_sentence(words)
print_random_sentence(words)
print_random_sentence(words)
print_random_sentence(words)
