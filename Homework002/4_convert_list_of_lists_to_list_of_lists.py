#  4. Write a Python program to convert a given list of strings into list of lists using map function
import ast

inputString = input("Enter a list of strings to convert to list of lists: ")

inputList = list(ast.literal_eval(inputString))

output = list(map(list, inputList))

print(output)