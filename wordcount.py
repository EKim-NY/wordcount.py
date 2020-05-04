# Return each unique word and how many times it appears in the input file

# def get_(filename): 

file = open("test.txt")
all_words = {}
list_all_words = []  # to house all words in entire text


for line in file: 
    # split each line into words
    # then add each word to list_all_words 
    list_all_words.extend (line.split())

    # Converting list_all_words into a set will return only unique words
    # but the words will be in random order when called by item
    # -- Keep it as a list. -- 


# for each word in list_all_words
# search for the word, update its count if found
# if not, add the new word to the list with a count of 1
for word in list_all_words: 
    all_words[word] = all_words.get(word, 0) + 1


# Prints each key-value pair on its own line
for key, value in all_words.items():
    print("{} {}".format(key,value))










