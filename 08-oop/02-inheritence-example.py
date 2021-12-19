class StudentParent:

	def __init__(self):
		self.roll_no = 0

	def print_roll_no(self, roll_no):
		print(roll_no)


class StudentChild(StudentParent):
	def print_name(self, name):
		print(name)


student_one = StudentChild()

student_one.print_roll_no(2)
student_one.print_name("Imran")
