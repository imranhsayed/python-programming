# Print this pattern
# *
# **
# ***

myList = []

for i in range(1, 4):
	myList.append("*" * i)
print("\n".join(myList))
