# To display size of a file in bytes.

from pathlib import Path

# Take the filename from the user.
file_name = input('Enter the filename with extension ( e.g. test.txt ): ')

try:
	file_handle = open(file_name)

	# Calculate
	file_size = Path(file_name).stat().st_size
	print('The File {0} size is {1} Bytes'.format(file_name, file_size))

except:
	print('File {0}  does not exist'.format(file_name))
