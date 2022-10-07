# To swap variables
# Use the temporary variable

from re import X
from tkinter import Y


a = 5
y = 10

temp = a
a = y 
y = temp   # Create a temporary variable to store a then y

print("The value of a after swapping: {}".format(a))
print("The value of y after swapiing: {}".format(y))
