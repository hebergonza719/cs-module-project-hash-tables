import re

def word_count(s):
    # Your code here
    pattern = '[\"\:\;\,\.\-\+\=\/\\\|[\]\{\}\(\)\*\^\&]'
    s = re.sub(pattern, '', s)
    lookup = {}
    s = s.lower()
    s = s.split()

    for word in s:
        if word not in lookup:
            lookup[word] = 1
        else:
            lookup[word] += 1
    return lookup

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))