# * Bayesian Inference
import math
#   - Treating unknown parameters themselves as random variables
#   - Start with a prior distribution for the parameters
#   - Use observed values and bayes to get an updated posterior distribution
#
#   - Rather than making probability judgements about the trsts, you make them
#   about the parameters themselves


#   - When the unknown parameter is a probability (like the coin toss), then
#   a prior from the Beta distribution is commonly used (0 < x < 1)
def B(alpha, beta):
    """a normalizing constant so that the total probability is 1"""
    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)


# The larger alpha and beta are the *tighter* the distribution is
#   - a = 1 and b = 1 -> uniform distribution
#   - a >> b -> weighted towards 1
#   - a << b -> weighted towards 0
def beta_pdf(x, alpha, beta):
    if x < 0 or x > 1:
        return 0

    return x ** (alpha - 1) * (1 - x) ** (beta - 1) / B(alpha, beta)
