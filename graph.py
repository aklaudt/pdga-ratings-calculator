import numpy as np
import matplotlib.pyplot as plt
from database import Database
# A custom function to calculate
# probability distribution function


def pdf(x):
    mean = np.mean(x)
    std = np.std(x)
    y_out = 1/(std * np.sqrt(2 * np.pi)) * \
        np.exp(- (x - mean)**2 / (2 * std**2))
    return y_out


def inverse_percentile(arr, num):
    arr = sorted(arr)
    i_arr = [i for i, x in enumerate(arr) if x > num]

    return i_arr[0] / len(arr) if len(i_arr) > 0 else 1


conn = Database.createConnection("./pdga.db")

# To generate an array of x-values
# x = np.arange(-2, 2, 0.1)
tuples = Database.getAllCurrentRatings(conn)
x = list(map(lambda x: x[0], tuples))

# x = list(filter(lambda rating: rating >= 500, x))
x.sort()

print(inverse_percentile(x, 937))  # 0.8488318976768467
print(inverse_percentile(x, 950))  # 0.6652321335419927
print(inverse_percentile(x, 1003))  # 0.6652321335419927
exit()
# exit()
# To generate an array of
# y-values using corresponding x-values
y = pdf(x)

# Plotting the bell-shaped curve
plt.style.use('seaborn')
plt.figure(figsize=(6, 6))
plt.plot(x, y, color='black',
         linestyle='dashed')

plt.scatter(x, y, marker='o', s=25, color='red')
plt.show()
