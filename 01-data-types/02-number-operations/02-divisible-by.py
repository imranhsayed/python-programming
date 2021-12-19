# Write a Python program to find those numbers
# which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included)

for item in range(1500, 2701):
	if item % 7 == 0 and item % 5 == 0:
		print(item)
