import numpy as np

filename = 'data.csv'

# Open the file in 'rb' - read binary mode
raw_data = open(filename, 'r')
data = np.loadtxt(raw_data, str, '#', delimiter=',')
print(data[0])  # first row
print(data[0])  # last row
