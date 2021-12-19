# Write a Python program to convert temperatures to and from celsius, fahrenheit.

temperature = input("Enter the temperature you want to convert e.g. 21C, or 60F: ")
temp_degree = float(temperature[:-1])
temp_type = temperature[-1:]

if temp_type.upper() == 'C':
	# Formula: (9*degree/5)+32
	result = float((9 * temp_degree) / 5 + 32)
	print(f"The temperature in celsius is {result}")
elif temp_type.upper() == 'F':
	# Formula: (degree-32)*5/9
	result = float((temp_degree - 32) * 5 / 9)
	print(f"The temperature in fahrenheit is {result}")
else:
	print("Please enter proper temperature format")
