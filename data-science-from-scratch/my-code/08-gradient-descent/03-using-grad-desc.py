#  * Using the Gradient
#   - Use gradients to find the minumum among three dimensional vectors
from random import randint


def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)


def distance(v, w):
    return math.sqrt(squared_distance(v, w))


def vector_subtract(v, w):
    """subtracts two vectors componentwise"""
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]


def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))


def step(v, direction, step_size):
    """move step_size in the direction from v"""
    return [v_i + step_size * direction_i
            for v_i, direction_i in zip(v, direction)]


# pick a random starting point
v = [randint(-10, 10) for i in range(3)]

tolerance = 0.000001

while True:
    gradient = sum_of_squares_gradient(v)
    next_v = step(v, gradient, -0.01)
    if distance(next_v, v) < tolerance:
        break
    v = next_v
