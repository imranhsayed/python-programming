# Variables
# Python automatically identifies the type of the data type. So we don't need to define it.
name = '''Imran is "Superb"'''
color = 'Red'
age = 12
isMale = True

# Print variables.
print(name)

# Print variable type. In python everything is a class object. Result <class 'bool'>
print(type(isMale))

# Operators. https://www.w3schools.com/python/python_operators.asp

# Convert String to integer
a = "1233"
typeCastedNumber = int(a);
print(typeCastedNumber)

# Taking User input.
# userName = input('Enter your name: \n')
# print(userName)  # This will print user input name

# String Concatenation
myNumber = 12
print(str(myNumber) + ' is greatest')

# If elif statement.
if myNumber > 12:
	print('Number is greater than 12')
elif myNumber > 1:
	print('Number is greater than 1')

# Use of "in"
comment = 'You can make a lot of money'
if "lot of money" in comment:
	print('This is a spam')

# While Loop
n = 2
while n < 5:
	print(str(n) + ' is less than 5')
	n = n + 1

# For in Loop
myArray = ['Imran', 'Natalie', 'Mia']
for item in myArray:
	print('Item value is: ' + item)

# Range function.
