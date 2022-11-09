# 2. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

# Solution 1: Using the while loop

names = []

names.append(input("Enter your firstname: "))
names.append(input("Enter your lastname: "))

i = len(names) - 1
while i >= 0:
    print(names[i])
    i -= 1



# Solution 2: Using variables
# firstname = input("Enter your firstname: ")
# lastname = input("Enter your lastname: ")
#
# print("The reversed version of your name is: ", lastname, firstname)