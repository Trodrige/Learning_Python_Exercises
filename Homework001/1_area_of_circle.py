# 1. Write a Python program which accepts the radius of a circle from the user and compute the area.

import math

radius = input("Enter the radius of the cirlce:")

print("The area of the circle with radius "+ radius +" is: ", math.pi * math.pow(int(radius), 2))