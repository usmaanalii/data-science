# * Putting It All Together
#   - Generally, we will have a target function (to minimize) and it's
#   gradient function
#   - The target function could represent the errors in a model as a function
#   of its parameters, and the goal is to find the parameters that make
#   the errors as small as possible


# Given a starting value for *theta_0*, implement gradient descent like so...
def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):

    """use gradient descent to find theta that minimizes target function"""
    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]
    theta = theta_0  # set theta to initial value
    target_fn = safe(target_fn)  # safe version of target_fn
    value = target_fn(theta)  # value we're minimizing
    while True:
        gradient = gradient_fn(theta)
        next_thetas = [step(theta, gradient, -step_size)
                       for step_size in step_sizes]
    # choose the one that minimizes the error function
    next_theta = min(next_thetas, key=target_fn)
    next_value = target_fn(next_theta)
    # stop if we're "converging"
    if abs(value - next_value) < tolerance:
        return theta
    else:
        theta, value = next_theta, next_value


# maximize
def negate(f):
    """return a function that for any input x returns -f(x)"""
    return lambda *args, **kwargs: -f(*args, **kwargs)


def negate_all(f):
    """the same when f returns a list of numbers"""
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]


def maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    return minimize_batch(negate(target_fn),
                          negate_all(gradient_fn),
                          theta_0,
                          tolerance)
