# * Example: Running an A/B Test
import math


def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


def normal_prob_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)


normal_prob_below = normal_cdf


def two_sided_p_value(x, mu=0, sigma=1):
    if x >= mu:
        # if x is greater than the mean, the tail is what's greater than x
        return 2 * normal_prob_above(x, mu, sigma)
    else:
        # if x is less than the mean, the tail is what's less than x
        return 2 * normal_prob_below(x, mu, sigma)


def estimated_parameters(N, n):
    p = n / N
    sigma = math.sqrt(p * (1 - p) / N)
    return p, sigma


# Test the null hypothesis (P(a) and P(b) are the same that is P(a) - P(b) = 0)
def a_b_test_statistic(N_A, n_A, N_B, n_B):
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)

    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)


# If A gets 200/1_000 clicks and B get 180/1_000
z = a_b_test_statistic(1000, 200, 1000, 180)
z

# The probabilty of seeing such a large difference if means are equal is
#   - This is large so you can't conclude a difference exists
two_sided_p_value(z)

# If B got 150/1_000 clicks then...
#   - The two_sided_p_value is 0.003, which means the probabilty of seeing such
#   a large difference with equal means is 0.003%
z = a_b_test_statistic(1000, 200, 1000, 150)
two_sided_p_value(z)  # 0.003
