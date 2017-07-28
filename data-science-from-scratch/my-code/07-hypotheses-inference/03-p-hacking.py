# * P-hacking
#   - You can hack the parameters to extract a significant result
#   - Examples include cleaning data, removing outliers etc...
#   - 'Good' science is formulating the hypothesis tests before, so you are not
#   swayed by what you see in the data
import random


def run_experiment():
    """flip a fair coin 1000 times, True = heads, False = tails"""
    return [random.random() < 0.5 for _ in range(1000)]


def reject_fairness(experiment):
    """using the 5% significance levels"""
    num_heads = len([flip for flip in experiment if flip])

    return num_heads < 460 or num_heads > 531


random.seed(0)
experiments = [run_experiment() for _ in range(1000)]
num_rejections = len([experiment
                     for experiment in experiments
                     if reject_fairness(experiment)])

print(num_rejections)
