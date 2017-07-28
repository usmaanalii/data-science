# * Correlation
import random
import math

#   - covariance measures how to variables vary in randem from their means
num_friends = [random.randrange(1, 50, 1) for _ in range(204)]
daily_minutes = [random.randrange(1, 50, 1) for _ in range(50)]


def mean(x):
    return sum(x) / len(x)


def variance(x):
    """assume x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)


def standard_deviation(x):
    return math.sqrt(variance(x))


def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)


# "Large" positive = x tends to be large when y is large
# "Large" negative = x tends to be small when y is large
covariance(num_friends, daily_minutes)


# Correlation divides out the dtandard deviations of both variables
def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0


correlation(num_friends, daily_minutes)

# Watch out for outliers
