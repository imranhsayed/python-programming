from area.circle import calc_circle_area
from area.square import calc_square_area
from area.rectangle import calc_rectangle_area


def calculate_area(shape):
	if shape == 'circle':

		radius = int(input('Enter a radius value: '))
		print('Area of the circle is: ', calc_circle_area(radius))

	elif shape == 'square':
		side = int(input('Enter side value: '))
		print('Area of the square is: ', calc_square_area(side))

	elif shape == 'rectangle':

		length = int(input("Enter a rectangle's length: "))
		breadth = int(input("Enter a rectangle's breadth: "))
		print('Area of the rectangle is: ', calc_rectangle_area(length, breadth))


# Get the shape names from the user.
shape_name = input('Enter a shape name( circle, square or rectangle ), to calculate the area: ')
allowed_shape_names = ['circle', 'square', 'rectangle']

if shape_name in allowed_shape_names:
	calculate_area(shape_name)
else:
	print('Shape name is not correct. Please rerun the program and try again')
