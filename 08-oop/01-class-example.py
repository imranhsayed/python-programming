class Student:
	roll_no = 1

	def __init__(self):
		self.name = 'Imran'
		self.age = 30

	def print_name(self):
		print(self.name, self.roll_no)

	def increment_age(self, num):
		print(self.age + num, self.roll_no)


# Instantiation
studentOne = Student()

# Class method call
studentOne.increment_age(2)
