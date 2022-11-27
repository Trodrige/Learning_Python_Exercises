# 2. Write a Python function to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
import ast

# input = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

input = input("Enter a list of tuples you which to sort by the second element: ")

output = list(ast.literal_eval(input)) #converts the string to a list of tuples

output.sort(key=lambda tup: tup[1])

print(output)


