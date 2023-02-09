import numpy as np
import random
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# ------------------Tasks ----------------------

print("\n=================== TASK 1 BELOW =====================")
# 1.
# Create a vector with values ranging from 10 to 49. Reverse a vector (first element
# becomes last)

vector = np.arange(10, 50)
print(vector)
print(vector.shape)

vector = vector[::-1]  # reverse vector starting from the last
print(vector)


print("\n=================== TASK 2 BELOW =====================")
# 2.
# Create a 5x5 array with random values and find the minimum and maximum values

array_list = []
for num in range(0, 25):
    array_list.append(random.randint(1, 20))

matrix = np.array(array_list)
matrix = np.reshape(matrix, (5, 5))

matrix_min = np.min(matrix)  # minimum value or matrix
matrix_max = np.max(matrix)  # maximum value of matrix
print(matrix)
print(matrix_min)
print(matrix_max)

average = (matrix_min + matrix_max) / 2

y_values = [matrix_min, average, matrix_max]
x_values = ["Minimum", "Average", "Maximum"]

font = {'family':'serif','color':'blue','size':20}
plt.title("Min., Average & Max. of a matrix", fontdict = font)
plt.bar(x_values, y_values)
plt.xlabel("Values")
plt.ylabel("Numbers")
plt.show()

print("\n=================== TASK 3 BELOW =====================")
# 3. Normalize a 5x5 random matrix

matrix = np.random.randint(5, 25, size=(5, 5))  # random 5x5 matrix
matrix_range = matrix_max - matrix_min
matrix_norm = (matrix - matrix_min) / matrix_range  #
print(matrix_norm)


print("\n=================== TASK 4 BELOW =====================")
# 4. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)

matrix_a = np.random.randint(1, 10, size=(5, 3))
matrix_b = np.random.randint(5, 10, size=(3, 2))
# print(matrix_a)
# print(matrix_b)
matrix_c = np.dot(matrix_a, matrix_b)
print(matrix_c)


print("\n=================== TASK 5 BELOW =====================")
# 5. How to get the dates of yesterday, today and tomorrow?

today = datetime.now().date()
print("Today's date:", today)

yesterday = today - timedelta(days=1)
print("Yesterday's date:", yesterday)

tomorrow = today + timedelta(days=1)
print("Tomorrow's date:", tomorrow)


print("\n=================== TASK 6 BELOW =====================")
# 6. Extract the integer part of a random array using 5 different methods

random_array = np.random.uniform(1, 10, 5)  # random array of 5 float values between 1 and 10
print(random_array)

int_array = np.floor(random_array)  # round each element of the array down to the nearest integer
int_array = int_array.astype(int)  # convert the elements of the array to integers
print(int_array)

int_array = np.trunc(random_array)  # truncate each element of the array to the nearest integer toward zero
int_array = int_array.astype(int)  # convert the elements of the array to integers
print(int_array)

int_array = np.around(random_array)  # round each element of the array to the nearest integer with a specified number
# of decimal places
int_array = int_array.astype(int)  # convert the elements of the array to integers
print(int_array)

int_array = np.rint(random_array)  # round each element of the array to the nearest integer with half-way cases
# rounded to the nearest even integer
int_array = int_array.astype(int)  # convert the elements of the array to integers
print(int_array)

int_array = np.array(random_array, dtype=int)  # this method first convert the array to a numpy array and then
# convert the data type to int using numpy.int().
print(int_array)


print("\n=================== TASK 7 BELOW =====================")
# 7. Create a structured array representing a position ( x,y ) and a color r,g,b

dtype = [('position', [('x', np.int32), ('y', np.int32)]),
         ('color', [('r', np.uint8), ('g', np.uint8), ('b', np.uint8)])]

struct_array = np.array([((1, 2), (3, 4, 5)), ((6, 7), (8, 9, 10))], dtype=dtype)
print(struct_array)



print("\n=================== TASK 1 BELOW =====================")
# 1. Consider a generator function that generates 10 integers and use it to build an
# array

def generator():
    result = []
    for i in range(10):
        result.append(random.randint(0, 20))
    return result


array_ = np.array(generator())
print(array_)

# Show resulting array in Pie chart
font = {'family':'serif','color':'blue','size':20}
plt.title("Random 10 Integers", fontdict = font)
my_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k']

plt.pie(array_, labels = my_labels)
plt.legend()
plt.show()


print("\n")
print("\n=================== TASK 2 BELOW =====================")
# 2. Consider two random array A and B, check  if they are equal

A = np.random.rand(3,3)
B = np.random.rand(3,3)

are_equal = np.array_equal(A,B)
print(are_equal)


print("\n=================== TASK 3 BELOW =====================")
# 3. Consider a random vector with shape (100,2) representing coordinates, find
# point by point distances

random_vector = np.random.rand(100, 2)
distances = np.linalg.norm(random_vector[:, np.newaxis] - random_vector, axis=-1)
print(distances)


print("\n=================== TASK 4 BELOW =====================")
# 4. Subtract the mean of each row of a matrix

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# convert the matrix to a numpy array
matrix = np.array(matrix)

# calculate the mean of each row
row_means = matrix.mean(axis=1)
print(row_means)

# broadcast the mean of each row to subtract it from each element in the corresponding row
matrix = matrix - row_means[:, np.newaxis]

print(matrix)


print("\n=================== TASK 5 BELOW =====================")
# 5. How to I sort an array by the nth column?

nums = np.random.randint(0,  10, (3, 2))
print(nums[0])


print("\n=================== TASK 6 BELOW =====================")
# 6. Compute a matrix rank

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

rank = np.linalg.matrix_rank(A)

print(rank)


print("\n=================== TASK 7 BELOW =====================")
# 7. Consider a 16x16 array, how to get the block sum (block size is 4x4)
# Creates a 16x16 array with random numbers from 0-10 and gets block sum

numbers = np.random.randint(0, 10, (16, 16))
block_size = 4
block_sum = np.add.reduceat(np.add.reduceat(numbers, np.arange(0, numbers.shape[0], block_size), axis=0),
                                                     np.arange(0, numbers.shape[1], block_size), axis=1)
print("Original 16x16 array of random numbers:\n")
print(numbers)
print("Block sum:")
print(block_sum)