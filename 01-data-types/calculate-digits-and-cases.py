# Write a Program that Accepts a Sentence and Calculate
# the Number of Digits, Uppercase and Lowercase Letters

sentence = input("Enter a sentence: ")
construct_dictionary = {"digits": 0, "lowercase": 0, "uppercase": 0}

for character in sentence:
	if character.isdigit():
		construct_dictionary["digits"] += 1
	elif character.islower():
		construct_dictionary["lowercase"] += 1
	elif character.isupper():
		construct_dictionary["uppercase"] += 1

print(f"Number of digits, lowercase, and uppercase letters are: {construct_dictionary}")
