# * Continuous Distributions


# density function for the uniform distribution
def uniform_pdf(x):
    return 1 if x >= 0 and x < 1 else 0


# cumulatice distrbution function for the uniform distribution
def uniform_cdf(x):
    """returns the probability that a uniform random variable is <= x"""
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1
