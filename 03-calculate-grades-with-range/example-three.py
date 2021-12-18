score = float(input('Enter your score: '))
grade = ''

if 0.0 <= score <= 1.0:
	if score >= 0.9:
		grade = 'A'
	elif score >= 0.8:
		grade = 'B'
	elif score >= 0.7:
		grade = 'C'
	elif score >= 0.6:
		grade = 'D'
	elif score < 0.6:
		grade = 'F'
else:
	grade = 'The Score is out of range'

print(grade)
