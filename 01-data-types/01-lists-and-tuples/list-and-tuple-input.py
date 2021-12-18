# Question - Insert items into a tupe:
# Solution:
# Items are inserted into the tuple using two methods:
# 1. Using continuous concatenation += operator or,
# 2. By converting list items to tuple items.

# Explanation: In the below code, tuple_items is of the type 'tuple'. In both the methods, the total number of
# items are specified which will be inserted to the tuple beforehand. Based on
# this number, the for loop is iterated using the range() function.
# range() generates an iterable list from the number 0 to the given range in param

# 1. Method One: Using continuous concatenation += operator
#
# In the first method, the user entered items are continuously concatenated to the tuple
# using += operator. Tuples are immutable and are not supposed to be changed.
# During each iteration, each original tuple is replaced by original tuple + (new_element),
# thus creating a new tuple. Notice a comma after new element.

tuple_items = ()
total_items = int(input("Enter total no of tuple items: "))

for i in range(total_items):
	user_input = int(input("Enter a tuple number: "))
	tuple_items += (user_input,)

print(f"User entered tuple is: {tuple_items}")

# 2. Method two: By converting list items to tuple items
#
# In the second method, a list is created. For each iteration, the
# user entered value is appended to the list_items. This list is then converted
# to tuple type using tuple() function.

list_items = []
total_items = int(input("Enter total no of list items: "))

for i in range(total_items):
	user_input = int(input("Enter a list number"))
	list_items.append(user_input)

items_of_tuple = tuple(list_items)
print(f"Tuple items are {items_of_tuple}")
