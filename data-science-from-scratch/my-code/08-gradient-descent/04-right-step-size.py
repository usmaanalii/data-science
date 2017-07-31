#  * CHoosing the Right Step Size
#   - Not as clear as which direction to move in
#   - Options include:
#       o Using a fixed step size
#       o Gradually shrinking the step size over time
#       o Choose the step size that minimizes the value of the objective
#       function at each step

# approximate it by trying a variety anfd choosing the one that results
# in the smallest value of the objective function
step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]


# this safeguards against step sizes that result in invalid inputs
def safe(f):
    """return a new function that's the same as f
    except that it outputs infinity whenever f produces an error"""
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return float('inf')

    return safe_f
