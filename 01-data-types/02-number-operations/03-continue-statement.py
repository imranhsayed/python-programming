# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.

for item in range(0, 7):
	if item != 3 and item != 6:
		print(item)
		continue
