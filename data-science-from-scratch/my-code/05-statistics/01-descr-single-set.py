# * Describing a Single Set of Data
from matplotlib import pyplot as plt
import random
import math
from collections import Counter

num_friends = [random.randrange(1, 50, 1) for _ in range(204)]
friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]

plt.bar(xs, ys)
plt.axis([0, 50, 0, 15])
plt.title("Histogram of Frend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()

# generate some statistics
num_points = len(num_friends)
largest_value = max(num_friends)
smallest_value = min(num_friends)

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]


# ** Central Tendencies
def mean(x):
    return sum(x) / len(x)


mean(num_friends)


def median(v):
    """finds the 'middle most' value of v"""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        # if odd, return the middle value
        return sorted_v[midpoint]
    else:
        # if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2


median(num_friends)


def quantile(x, p):
    """returns the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]


quantile(num_friends, 0.10)
quantile(num_friends, 0.25)
quantile(num_friends, 0.75)
quantile(num_friends, 0.90)


def mode(x):
    """returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]


mode(num_friends)


# ** Dispersion
#   - How spread our data is
#   - Typically, 0 means not spread out at all
def data_range(x):
    return max(x) - min(x)


data_range(num_friends)


def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)


def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def variance(x):
    """assume x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)


variance(num_friends)


def standard_deviation(x):
    return math.sqrt(variance(x))


standard_deviation(num_friends)


def iq_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)


iq_range(num_friends)
