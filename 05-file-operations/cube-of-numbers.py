# Find a cube of numbers in a list using lambda(anonymous) function

# Lists are one of the 4 built in data types in python, to store collection of data.
numbers_list = [1, 2, 3, 4]

"""
- map function executes this lambda function for each item in the list. It takes the iterables as a second parameter
It returns object.
- list function Converts the map into a list for readability
- x ** 3 means x to the power 3 ( It's same as x * x * x ).
** is the exponential operator. 
"""
cube_of_numbers = list(map(lambda x: x ** 3, numbers_list))

print(cube_of_numbers)
