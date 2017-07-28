# * Example: Flipping a Coin
import math


def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


# - Invert normal_cdf to find the value corresponding to a specified
#   probability, since normal_cdf is continuous and strictly increasing
#   weΩ can use a binary search
# - This repeatedly bisects intervals until it narrows in on Z close enough
#   to the desired probability
def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """find approximate inverse using binary search"""
    # if not standard, compute  standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z, low_p = -10.0, 0  # normal_cdf(-10) is (very close to) 0
    hi_z, hi_p = 10.0, 1  # normal_cdf(10) is (very close to) 1

    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2  # consider the midpoint
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            # midpoint is still too low, seach above it
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # midpoint is still too high, search below it
            hi_z, hi_p = mid_z, mid_p
        else:
            break

    return mid_z


def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


def normal_approx_to_binomial(n, p):
    """finds mu and sigma corresponding to a Binomial(n, p)"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)

    return mu, sigma


# the normal cdf _is_ the probability, that the variable is belo w a threshold
normal_prob_below = normal_cdf


# it's above the threshold if it's not below it
def normal_prob_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)


# it's between if it'sless than hi, but not less than lo
def normal_prob_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)


# it's outside if it's not between
def normal_prob_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_prob_between(lo, hi, mu, sigma)


# non-tail region (symmetric interval)
def normal_upper_bound(probability, mu=0, sigma=1):
    """returns the z for which P(Z <= z) = probability"""
    return inverse_normal_cdf(probability, mu, sigma)


def normal_lower_bound(probability, mu=0, sigma=1):
    """returns the z for which P(Z >= z) = probability"""
    return inverse_normal_cdf(1 - probability, mu, sigma)


def normal_two_sided_bounds(probability, mu=0, sigma=1):
    """returns the symmetric (about the mean) bounds
    that contain the specified probability"""
    tail_probability = (1 - probability) / 2
    # upper bound should have tail_probability above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    # lower bound should have tail_probability below it
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)
    return lower_bound, upper_bound


mu_0, sigma_0 = normal_approx_to_binomial(1000, 0.5)

normal_two_sided_bounds(0.95, mu_0, sigma_0)

# 95% bounds based on assumption p is 0.5
lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)

# actual mu and sigma based on p = 0.55
mu_1, sigma_1 = normal_approx_to_binomial(1000, 0.55)

# a type 2 error means we fail to reject the null hypothesis
# which will happen when X is still in our original interval
type_2_probability = normal_prob_between(lo, hi, mu_1, sigma_1)
power = 1 - type_2_probability  # 0.88

# one sided test for p = 0.55
hi = normal_upper_bound(0.95, mu_0, sigma_0)
type_2_probability = normal_prob_below(hi, mu_1, sigma_1)
power = 1 - type_2_probability


# Use p values to test hypothesis
def two_sided_p_value(x, mu=0, sigma=1):
    if x >= mu:
        # if x is greater than the mean, the tail is what's greater than x
        return 2 * normal_prob_above(x, mu, sigma)
    else:
        # if x is less than the mean, the tail is what's less than x
        return 2 * normal_prob_below(x, mu, sigma)


# 529.5 not 530 due to continuity correction
two_sided_p_value(529.5, mu_0, sigma_0)

# simulation to test the code is right
extreme_value_count = 0

for _ in range(100000):
    num_heads = sum(1 if random.random() < 0.5 else 0 for
                    _ in range(1000))
    if num_heads >= 530 or num_heads <= 470:
        extreme_value_count += 1

print(extreme_value_count / 100000)

two_sided_p_value(531.5, mu_0, sigma_1)
