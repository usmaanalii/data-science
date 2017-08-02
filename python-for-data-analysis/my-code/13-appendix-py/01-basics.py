# * Basics
import bisect
from collections import defaultdict
import re
from functools import partial
import pandas
import itertools


def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:  # not isiterablee
        return False


isiterable('a string')
isiterable([1, 2, 3])
isiterable(5)

x = 1
print(type(x))

if not isinstance(x, float):
    x = float(x)

print(type(x))

# use import numpy 'as' np to make life easier!!!

# Binary operators and comparisons *

a = [1, 2, 3]
b = a
c = list(a)  # because list function creates a new list, NOT a reference
a is b
a is not c

# a common use of 'is' can be to check if a variable is None
a = None
a is None

# Strictness vs Laziness *
# python will assign variables right away and not wait until their use
# laziness helps when expensive computations aren't commonly used and can be
# acheived via generators/iterators

# Mutable and immutable objects *
a_list = ['foo', 2, [4, 5]]
a_list[2] = (3, 4)
a_list

# strings and tuples are immutable
a_tuple = (3, 5, (4, 5))
a_tuple[1] = 'four'  # produces an ERROR

# Scalar Types *
3 // 2  # drop the remainder
3 / float(2)  # gives 1.5 as opposed to 1 when not using float()

a = 'this is a string'
a[1] = '2'  # produces an ERROR because str are immutable

s = 'python'
s[:3]
list(s)

# empty sequences are treated as False
a = [1, 2, 3]
if a:
    print("I found something")

b = []
if not b:
    print("Empty")

bool('')  # False
bool('a')  # True
bool(0)  # False
bool(1)  # True

# Control Flow *
for value in collection:
    # do something with value
    pass

sequence = [1, 2, None, 4, None, 5]
total = 0
for value in sequence:
    if value is None:
        continue  # advancing the for loop to the next iteration
    total += value

print(total)

# using the break keyword to exit a loop
seq = [1, 2, 3]
total_until_2 = 0
for value in seq:
    if value == 2:
        break
    total_until_2 += value
print(total_until_2)

# if the element in the collection or iterator are sequences
# they can be upacked into variables
for a, b, c in iterator:
    # do something
    pass

# pass is useful as a placeholder for code not yet ready
if x < 0:
    print('negative')
elif x == 0:
    # TODO: put something smart here
    pass
else:
    print('positive')

# Exception handling *
float('1.2345')
float('something')  # ValueError


def attempt_float(x):
    try:
        return float(x)
    except ValueError:
        return x


attempt_float('1.2345')
attempt_float('something')


# Don't do this for TypeError but for ValueError
def attempt_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):  # can catch tuple of errors
        return x


# a common use for range, is to iterate through sequences by index
seq = [1, 2, 3, 4, 5]
for i in range(len(seq)):
    val = seq[i]

# for larger ranges, use range, since this generates integers one by one
# as opposed to up front
sum_ = 0
for x in range(10000):
    if x % 3 == 0 or x % 5 == 0:
        sum_ += i

print(sum_)

# ternary expression allows you to combine if-else producing values into
# a single line --> value = true-expr if condition else false-expr, identical..
if condition:
    value = 'true-expr'
else:
    value = 'false-expr'

x = 5

'None negative' if x >= 0 else 'Negative'  # these can make code less readable
