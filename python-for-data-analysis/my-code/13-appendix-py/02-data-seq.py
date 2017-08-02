# Data Structures and Sequences *
import bisect
from collections import defaultdict
import re
from functools import partial
import pandas
import itertools

tup = (4, 5, 6)
tup

tuple([0, 1, 2])  # can convert any iterbale to a tuple

tup = tuple('string')
tup  # ('s',  't', ...)
tup[0]

# tuples support concatenation
# multiplying tuples by integers will amplify it accordingly
tup = (1, 2)
tup * 2

# unpacking
tup = (4, 5, 6)
a, b, c = tup
b

tup = 4, 5, (6, 7)
a, b, (c, d) = tup  # even nested tuples can be unpacked
d

# swapping variable names
tmp = a
a = b
b, a = a, b

# common use of unpacking variables -> iterationg over seq of lists/tuples
seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
    print(a + 1)  # 2, 5, 8

a = (1, 2, 2)
a.count(2)  # counts how many 2's are in a

# List * - can be assigned using list() or []
b_list = ['foo', 'bar', 'baz']
b_list.insert(1, 'red')  # inserting at the index specified
b_list
b_list.pop(2)  # inverse of insert
b_list.remove('foo')
b_list

'baz' in b_list

everything = []

for chunk in list_of_lists:
    everything.extend(chunk)

# faster than
everything = []
for chunk in list_of_lists:
    everything = everything + chunk

# sorting
a = [7, 5, 4, 3]
a.sort()
print(a)

# sort has the ability to pass a secondary 'sort key'
b = ['word', 'second word', 'third word', 'longestlongestlongest']
b.sort(key=len)
print(b)

# Binary search and maintaining a sorted list
c = [1, 2, 2, 2, 3, 4]

# finds the element where 2 should be inserted maintaining order
# bisect doesn't check whether it was sorted to begin with
bisect.bisect(c, 2)
bisect.insort(c, 4)  # inserts 4 in the correct location
c

# Slicing [start:stop] --> [...) --> inclusive...exlusive
seq = [1, 2, 3]
seq[1:]  # 2, 3
seq[:-1]  # 1, 2

seq[::2]  # :: represents a 'step --> take every other element (2n)
seq[::-1]  # this reverses the list (clever use)


# Built-in Sequence Funcitions*

# enumerate - keeping track of the current items index when seq iterationg
i = 0
for value in collection:  # the DIY approach for which enumerate was made
    # do something with value
    i += 1

for i, value in enumerate(collection):
    # do something with value
    pass

# dict mapping
some_list = ['foo', 'bar', 'baz']
mapping = dict((v, i) for i, v in enumerate(some_list))  # why i, v not v, i ?
mapping

# getting a sorted list of unique elements
sorted(set('this is just some string'))

# zip
seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
seq3 = [False, True]
zip(seq1, seq2, seq3)  # shortest sequence termination

# common use -> iterating over two sequences simultaneously
for i, (a, b) in enumerate(zip(seq1, seq2)):
    print('%d: %s, %s' % (i, a, b))

# using zip to 'unzip' --> conv. list of rows into list of columns
pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clem'), ('Tyler', 'Cole')]
first_names, last_names = zip(*pitchers)
first_names
last_names

# reversed --> iterates in reverse order
list(reversed(range(10)))

# Dict *
d1 = {}
d1[5] = 'some value'
d1['dummy'] = 'another value'
del d1[5]
ret = d1.pop('dummy')
ret
d1.keys()
d1.values()

d1.update({'a': 'one'})
d1

# creating dict from two sequences
mapping = {}
for key, value in zip(key_list, value_list):
    mapping[key] = value

mapping = dict(zip(range(5), reversed(range(5))))  # passing list of tuples
mapping

# default values
if key in some_dict:
    value = some_dict[key]
else:
    value = default_value

value = some_dict.get(key, default_value)  # which will be None

# values in a dict to be a list --> categorize list of words by first letters
words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)

by_letter  # {'a': ['apple', 'atom']...}

by_letter.setdefault(letter, []).append(word)

# valid dict key types --> Have to be 'immutable' --> int, float, string, tuple
# this is for hashability
hash('string')
hash((1, 2, (2, 3)))
hash((1, 2, [2, 3]))  # fails because lists are Mutable

# to use a list as a key, convert it to a tuple
d = {}
d[tuple([1, 2, 3])] = 5
d

# List, Set and Dict Comprehensions
# [expression for value in collection if condition]
result = []
for val in collection:
    if condition:
        result.append(expression)

strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
[x.upper() for x in strings if len(x) > 2]

# dict comprhension --> dict_comp = {k-exp: val-exp for val in coll if cond}
unique_lengths = {len(x) for x in strings}
unique_lengths

loc_mapping = {val: index for index, val in enumerate(strings)}
loc_mapping

# Nested list Comprehensions
all_data = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
            ['Susie', 'Casey', 'Jill', 'Ana', 'Eva', 'Jennifer', 'Stephanie']]

# list of all names with two or more "e's"
names_of_interest = []
for names in all_data:
    enough_es = [name for name in names if name.count('e') > 2]
    names_of_interest.extend(enough_es)

# the above, wrapped into nested comprhension
result = [name for names in all_data for name in names if name.count('e') >= 2]
result

some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
flattened = [x for tup in some_tuples for x in tup]
flattened

# understanding the order of the for loop
flattened = []
for tup in some_tuples:
    for x in tup:
        flattened.append(x)
