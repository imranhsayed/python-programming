# To first n lines from the file.

# Take the filename from the user.
file_name = input('Enter the filename with extension ( e.g. test.txt ): ')

try:
	file_handle = open(file_name)
	no_of_lines = int(input('Enter the number of file lines to print: '))

	if no_of_lines > 0:

		"""
		- Iterates from 1 to no_of_lines + 1. 'i' is the index during each iteration.
		- This loop will start from index 1.
		- Then print the line. e.g. if user enters no_of_lines as 1, this loop will iterate
		- from 1(start) to 2(end), means once. And only one line will be printed.
		- When readline() is run multiple times, it reads one line from the top and then the next one
		- the second time it's called. 
		"""
		for i in range(1, no_of_lines + 1):
			line = file_handle.readline()
			print(line)
	else:
		print('Enter a number greater than 0')

except:
	print('File {0}  does not exist'.format(file_name))
