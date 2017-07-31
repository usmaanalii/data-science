# * Estimating the Gradient
#   - If f is a function of one variable, the derivative at point x,
#   f(x) measures the rate of change of f as x changes
import matplotlib.pyplot as plt
from functools import partial


def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h


# For many functions, it's easy to exactly calculate derivatives
def square(x):
    return x * x


def derivative(x):
    return 2 * x


# estimating derivatives by evaluating the differene quotient for small e
derivative_estimate = partial(difference_quotient, square, h=0.00001)

# TODO: line 28 error
# plot to show they're basically the same
x = range(-10, 10)
plt.title("Actual Derivatives vs. Estimates")
plt.plot(x, map(derivative, x), 'rx', label="Actual")
plt.plot(x, map(derivative_estimate, x), 'b+', label="Estimate")
plt.legend(loc=9)
plt.show()


# Calculating the ith partial derivative by treating it as a function
# of the ith variable, holding others fixed
def partial_difference_quotient(f, v, i, h):
    """compute the ith partial difference quotient of f at v"""
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]

    return (f(w) - f(v)) / h


# estimate the gradient the same way
def estimate_gradient(f, v, h=0.00001):
    return [partial_difference_quotient(f, v, i, h)
            for i, _ in enumerate(v)]
