"""
Required Condition to be met: For a year to be a leap year, it needs to be divisible by 4
and if it's a century year then it also needs to be divisible by 400.
"""

# Take the input from the user and store the number into a variable called year.
# Also convert the number into integer so we can perform conditional numeric operations.
year = int(input('Enter the year: '))
is_leap_year = False

# Condition one - If number is divisible by 4 and has remainder as zero.
if year % 4 == 0:

	# Check if it's a century year. If it is then it will be completely divisible by 100.
	if year % 100 == 0:
		# When it's  a century year, we also need to check if it's divisible by 400.
		if year % 400 == 0:
			is_leap_year = True
		else:
			is_leap_year = False
	else:
		is_leap_year = True  # If not century year and divisible by 4.

else:
	is_leap_year = False

# If is_leap_year is True, then print the message.
if is_leap_year:
	print('{0} is a leap year'.format(year))
else:
	print('{0} is not leap year'.format(year))
