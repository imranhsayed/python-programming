# Program to Swap Two Numbers without Using
# Intermediate/Temporary Variable. Prompt the User for Input

# Solution: Here we create a tuple (a,b) and assign its value as (b,a)
#
# One of the unique syntactic features of the Python language is the ability to
# have a tuple on the left side of an assignment statement. This allows one to
# assign more than one variable at a time when the left side is a sequence.
# e.g. a,b = b,a
#
# The contents of variables a and b are reversed. The tuple variables are on the
# left side of the assignment operator and, on the right side, are the tuple
# values. The number of variables on the left and the number of values on the
# right has to be the same. Each value is assigned to its respective variable

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

b, a = a, b
print(f"The two numbers after swapping are {a} and {b}")
