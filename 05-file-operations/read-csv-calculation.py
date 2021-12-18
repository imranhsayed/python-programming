import statistics
import pandas as pd

filename = 'data.csv'
data = pd.read_csv(filename)

names = data['Name']
ages = data['Age']
salaries = data['Salary']

# Print data( Columns of the dataset ).
print(data)
print("\n")

# Print Maximum values
print(f"Maximum Age: {max(ages)}")
print(f"Maximum Salary: {max(salaries)}")

# print Minimum value
print(f"Minimum Age: {min(ages)}")
print(f"Minimum Salary: {min(salaries)}")

# Print Mean values
print(f"Mean Age: {round(statistics.mean(ages), 2)}")
print(f"Mean Salary: {round(statistics.mean(salaries), 2)}")

# Print Median values
print(f"Median Age: {statistics.median(ages)}")
print(f"Median Salary: {statistics.median(salaries)}")

# Print Count
print(f"Count Age: {len(ages)}")
print(f"Count Salary: {len(salaries)}")

# Print Variance values
print(f"Variance Age: {round(statistics.variance(ages), 2)}")
print(f"Variance Salary: {round(statistics.variance(salaries), 2)}")

# Print Standard Deviation values
print(f"Standard Deviation Age: {round(statistics.stdev(ages), 2)}")
print(f"Standard Deviation Salary: {round(statistics.stdev(salaries), 2)}")
