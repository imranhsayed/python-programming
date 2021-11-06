import numpy as np
import matplotlib.pyplot as plt

responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]  # Responses list
uni_responses = {}  # Initialize Dictionary
for r in responses:  # Iterate through the list
	if r in uni_responses:  # Get ratings frequency. if rating already in dictionary
		uni_responses[r] += 1  # Add one to it's value
	else:  # If not present in dictionary
		uni_responses[r] = 1  # Add key value pair

sorted_keys = sorted(uni_responses)  # Get sorted keys list
sort_d = {}  # Initialize dictionary
for f in sorted_keys:  # Iterate through list
	sort_d[f] = uni_responses[f]  # Sort dictionary
prcnt = {}  # Initialize list
for k, v in sort_d.items():  # Iterate through the sorted dictionary
	print(f"Number of {k} ratings = {v}")  # Print frequencies
	prcnt[k] = (v / len(responses)) * 100  # Add percentages of each rating into a dictionary

print(f"Minimum: {min(responses)}")  # print Minimum value
print(f"Maximum: {max(responses)}")  # Print Maximum value
print(f"Range: {max(responses) - min(responses)}")  # Print Range
print(f"Mean: {np.mean(responses)}")  # Print mean
print(f"Median: {np.median(responses)}")  # Print median
print(f"Variance: {np.var(responses)}")  # Print Variance
print(f"Standard Deviation: {round(np.std(responses), 2)}")  # Print standard deviation

figure, ax = plt.subplots(figsize=(10, 12))  # Initialize the figure size
ax.bar(prcnt.keys(), prcnt.values())  # Plot percentages
ax.bar(sort_d.keys(), sort_d.values())  # Plot frequencies
ax.legend(['Percentage', 'Frequency'])  # Set legend
ax.set_xlabel('Ratings')  # Set X label
ax.set_title("Frequency and Percentages vs Rating")  # Set title
