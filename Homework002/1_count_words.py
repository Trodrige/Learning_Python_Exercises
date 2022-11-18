#1. Write a function which will return how many times a word (symbols separated with space, comma and dot) meet in the string
# Input: s – string
# Output: word1 = number, word2 = number
# Input: s= “Tom eats and eats”
# Output: Tom = 1, eats = 2, and = 1

myString = input("Enter a string to count it words: ")

myString = myString.replace(',', ' ')
myWords = myString.replace('.', ' ').split(' ')

uniqueWords = set(myWords)

for val in uniqueWords:
    print(val + " = ", myWords.count(val))







