# 3. Count number of vowels (a,o,u,e,i) in the string s
# Intput: s – string
# Output: Number of vowels = XX

string = input("Enter a string to count its vowels: ")

count_vowels = 0

for x in string:
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        count_vowels += 1

print("The string "+ string +" has " + str(count_vowels) + " vowels")




# Using 'match' in Python 3.10
# for x in string:
#     match x:
#         case 'a':
#             count_vowels += 1
#         case 'e':
#             count_vowels += 1
#         case 'i':
#             count_vowels += 1
#         case 'o':
#             count_vowels += 1
#         case 'u':
#             count_vowels += 1
#
# print("The string "+ string +" has " + str(count_vowels) + " vowels")