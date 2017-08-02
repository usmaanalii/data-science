# Functions *
import bisect
from collections import defaultdict
import re
from functools import partial
import pandas
import itertools
#   - keyword arguments are commonly used to specify default values
#   if none given
#   - def function(x, y, z=1.5) --> x, y are positional arguments, z is keyword
#   - variable scope in python --> namespace
#   - after a function is called, the local namespace is destroyed
#   (exceptions tho)


def func():
    a = []
    for i in range(5):
        a.append(i)


a = []


def func():
    for i in range(5):
        a.append(i)  # global a must be specified using 'global'


a = None


def bind_a_variable():
    global a
    a = []


bind_a_variable()

print(a)


# you can dynamically create functions when another is called...
def outer_function(x, y, z):
    def inner_function(a, b, c):
        pass  # inner function can access outer function variables (it's root?)
    pass


# Returning multiple values *
def f():
    a = 5
    b = 6
    c = 7
    return a, b, c  # the function is returing a tuple object (5, 6, 7)


a, b, c = f()  # tuple unpacking
returned_value = f()
returned_value


# likewise, you can return to a dict
def f():
    a = 5
    b = 6
    c = 7
    return{'a': a, 'b': b, 'c': c}


returned_dict = f()
returned_dict

# Functions are objects *
states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda',
          'south carolina##', 'West virginia?']  # will need lots of cleaning


# import re (done at the top of the file)
def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)  # remove punctuation
        value = value.title()
        result.append(value)
    return result


clean_strings(states)


# alternative approach
def remove_punctuation(value):
    return re.sub('[!#?]', '', value)


clean_ops = [str.strip, remove_punctuation, str.title]


def clean_strings(strings, ops):  # a more functional pattern --> more usable
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result


clean_strings(states, clean_ops)

map(remove_punctuation, states)  # using function as argument for another


# Anonymous Lambda Functions *
# lambda --> 'we are declaring an anoynmous function'
# anonymous because, the function is never given a name attribute
def short_function(x):
    return x * 2


# equiv_anonymous_lambda_function = lambda x: x * 2
def apply_to_list(some_list, f):
    return [f(x) for x in some_list]


ints = [4, 0, 1, 5, 6]
apply_to_list(ints, lambda x: x * 2)  # applying custom operator to a function
[x * 2 for x in ints]


# sorting a colleciton of strings by the number of distinct letters
strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
strings.sort(key=lambda x: len(set(list(x))))
strings


# Closures: Functions that Return Functions
# a closure is a dynamically-generated function that returns other functions
# the function created has access to the local namespace in which it was made
def make_closure(a):
    def closure():
        print('I know the secret: %d' % a)
    return closure


closure = make_closure(5)
closure()


# the closure will continue to have access to scope, even after execution
def make_watcher():
    have_seen = {}

    def has_been_seen(x):
        if x in have_seen:
            return True
        else:
            have_seen[x] = True
            return False

    return has_been_seen


watcher = make_watcher()
vals = [5, 6, 1, 5, 1, 6, 3, 5]
[watcher(x) for x in vals]


# you can mutate (add key to dict) but can't BIND variables to enclosing scope
# work around --> modify dict/list rather than bind variables
def make_counter():
    count = [0]

    def counter():
        # increment and return current count
        count[0] += 1
        return count[0]

    return counter


counter = make_counter()

counter()


# string formatting function
def format_and_pad(template, space):
    def formatter(x):
        return (template % x).rjust(space)

    return formatter


fmt = format_and_pad('%.4f', 15)
fmt(1.76)


# Extended Call Syntax with *args, **kwargs *
# positional and keyword arguments --> packed into a tuple and dict
# func(a, b, c, d=some, e=value)
# a, b, c = args
# d = kwards.get('d', d_default_value)
def say_hello_then_call_f(f, *args, **kwargs):
    print('args is', args)
    print('kwargs is', kwargs)
    print('Hello! Now I\'m going to call %s' % f)
    return f(*args, **kwargs)


def g(x, y, z=1):
    return (x + y) / z


say_hello_then_call_f(g, 1, 2, z=5.)


# Currying: Partial Argument Application *
# deriving new functions from existing ones by partial argument Application
def add_numbers(x, y):
    return x + y


add_five = lambda y: add_numbers(5, y)

# from functools import partial (dont at the top)
add_five = partial(add_numbers, 5)

# Generators * --> construct a new iterable object
some_dict = {'a': 1, 'b': 2, 'c': 3}
for key in some_dict:
    print(key)

# python attempts to create an iterator out of some_dict
dict_iterator = iter(some_dict)
dict_iterator

# iterator --> an object that will yield objects when used in a for loop(rough)
list(dict_iterator)


# normal functions return singles, generators return sequences
def squares(n=10):
    for i in range(1, n + 1):
        print('Generating squares from 1 to %d' % (n ** 2))
        yield i ** 2


gen = squares()
gen

for x in gen:
    print(x)


def make_change(amount, coins=[1, 5, 10, 25], hand=None):
    hand = [] if hand is None else hand
    if amount == 0:
        yield hand
    for coin in coins:
        # ensures we don't give too much change, and coins are unique
        if coin > amount or (len(hand) > 0 and hand[-1] < coin):
            continue

        for result in make_change(amount - coin,
                                  coins=coins, hand=hand + [coin]):
            yield result


for way in make_change(100, coins=[10, 25, 50]):
    print(way)

# Generator expressions
gen = (x ** 2 for x in range(100))
gen


# equivalent to ^^
def _make_gen():
    for x in range(100):
        yield x ** 2


gen = _make_gen()


sum(x ** 2 for x in range(100))
dict((i, i ** 2) for i in range(5))

# itertools module
# import itertools (^^)
first_letter = lambda x: x[0]

names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']

for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names))  # names is a generator
