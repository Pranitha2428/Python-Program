import numpy as np

amounts = np.array([500, 1000, 1500, 2000, 2500])

print("All amounts:", amounts)

# Basic calculations
print("Total:", np.sum(amounts))
print("Average:", np.mean(amounts))
print("Maximum:", np.max(amounts))
print("Minimum:", np.min(amounts))
print("Standard Deviation:", np.std(amounts))

# Prediction using simple linear trend
months = np.array([1, 2, 3, 4, 5])
spending = np.array([2000, 2500, 3000, 3500, 4000])

coeff = np.polyfit(months, spending, 1)

next_month = 6
prediction = coeff[0]*next_month + coeff[1]

print("Predicted next month spending:", prediction)