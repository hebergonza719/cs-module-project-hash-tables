def no_dups(s):
    # Your code here
    s = s.split()
    word_array = []

    for word in s:
        if word not in word_array:
            word_array.append(word)

    output = ' '.join(word_array)

    return output

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))