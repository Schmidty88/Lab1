# Lab 1.2 Team 6

sentence = input("Enter a sentence to analyze:")
# split the string for parsing

word_split = sentence.split(" ")

# variables

maximum_length = 0

index = 0

middle_index = 0

longest = ""

word_length = len(word_split)

reverse = list()

middle = []

# parse through string, get middle words, get longest word, and reverse sentence

if word_length % 2 == 0:

    middleLengths = [word_length // 2 - 1, word_length // 2]

else:

    middleLengths = [word_length // 2]

for word in word_split:

    word_length = len(word)

    if word_length > maximum_length:

        maximum_length, longest = word_length, word

    if len(middleLengths) > middle_index and index == middleLengths[middle_index]:

        middle.append(word)

        middle_index += 1

    word = word[::-1]

    reverse.append(word)

    index += 1

# .join to combine words in index

reverse = ' '.join(reverse)

middle = ' '.join(middle)

# print block for output

print("The middle words are: ", middle)

print("Your sentence in reverse word order is: ", reverse)

print("The longest word in your sentence was: ", longest)
