# To display frequency of each word in a file.

def get_file_words_as_list():
	# Loop through the file words and split the words into a list
	for line in file_handle:
		words = line.split()
		return words


def is_word_in_dictionary(words):
	# Initialize an empty Dictionary.
	dictionary = dict()

	# Loop through the words in the from the file.
	for word in words:

		# If word is already in the dictionary, increment it's count by one, else set it to one.
		if word in dictionary:
			dictionary[word] = dictionary[word] + 1
		else:
			dictionary[word] = 1
	return dictionary


# Take the filename from the user.
file_name = input('Enter the filename with extension ( e.g. test.txt ): ')

try:
	file_handle = open(file_name)
	file_words = get_file_words_as_list()
	the_dictionary = is_word_in_dictionary(file_words)
	print(the_dictionary)

except:
	print('File {0}  does not exist'.format(file_name))
