# * The Not-So-Basics
from functools import partial, reduce

# ** Sorting
#   - You have two options
#       1. sorted(list) will create a NEW sorted version of the list
#       2. list.sort() will sort the CURRWNT list
#   - There is a reverse=true option for largest to smallest sorting

# ** List Comprehensions
#   - Used when you want to construct a new list from am existing list
#   - You can create dicts and sets from a list this way as well
#
#   - An example of using the previous for loop is shown below,
#   in this case, the x iterant is used as the starting integer
#   for the second for loops range
increasing_pairs = [(x, y)
                    for x in range(10)
                    for y in range(x + 1, 10)]
increasing_pairs

# ** Generators and Iterators


#   - Generators are something that can be iterated over, but where the
#   values are produced lazily
def lazy_range(n):
    """a lazy version of a range"""
    i = 0
    while i < n:
        yield i
        i += 1


for i in lazy_range(10):
    print(i)

#   - xrange is an in built lazy range function

# ** Randomness
#   - If you wish to get reproducable results, you can use seed numbers
#   this will base the random number on a given state
#   - Example methods of random include random, randrange, shuffle, choice
#   and sample

# ** Functional Tools


#   - Currying is when you partially apply functions to create new functions
def exp(base, power):
    return base ** power


#   - Let's say you want a specific case for the base 2
#   - Use functools.partial
two_to_the = partial(exp, 2)
print(two_to_the(3))

#   - You can also use partial to fill in later arguments if you specify
#   their names
square_of = partial(exp, power=2)
print(square_of(3))


#   - Map, reduce and filter can do the work of list comprehensions
#   - If you provide two lists, then map functions with two parameters
#   can be applied (dot product)
def multiply(x, y):
    return x * y


#   - list_product takes multiply as its function to map
xs = [1, 2, 3, 4]
x_product = reduce(multiply, xs)
list_product = partial(reduce, multiply)
x_product = list_product(xs)

# ** enumerate
#   - Provides tuples (index, element) that allow you to iterate
#   whilst keeping track of the index

# ** zip and Argument Unpacking
#   - If the lists are uneven lengths, then the zip stops at the shortest
#   length

#   - unzip (using a trick)
#   - Using *argument implements argument unpacking
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)


#   - Further example of argument unpacking
def add(a, b):
    return a + b


add(1, 2)
add([1, 2])  # TypeError
add(*[1, 2])


# ** args and kwargs
def doubler(f):
    def g(x):
        return 2 * f(x)
    return g


def f1(x):
    return x + 1


g = doubler(f1)
print(g(3))
print(g(-1))


#   - This will break down with functions that take more than one argument.
#   so we need a way to specify a function that takes in an arbitrary
#   number of arguments
#   - This uses argument unpacking
def magic(*args, **kwargs):
    print("unnamed args:", args)
    print("keyword args:", kwargs)


magic(1, 2, key="word", key2="word2")


def doubler_correct(f):
    """works no matter what kind of inputs f expects"""
    def g(*args, **kwargs):
        """whatever arguments g is supplied, pass them through to f"""
        return 2 * f(*args, *kwargs)
    return g


def f2(x, y):
    return x + y


g = doubler_correct(f2)
print(g(1, 2))
