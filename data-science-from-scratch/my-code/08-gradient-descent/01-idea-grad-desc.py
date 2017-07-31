# * The Idea Behind Gradient Descent
#   - Sometimes the best model will be the solution to some sort of
#   optimization problem
#   - Such as 'minimizing the error of the model' or
#   'maximize the likelihood of the data'


# Function f, takes a vector of real numbers and returns a real numbers
#   - The idea of minimization/maximization when applied to this problem
#   for example is, finding the vector that produces the largest/smallest value
def sum_of_squares(v):
    """computes the sum of squared elements in v"""
    return sum(v_i ** 2 for v_i in v)
