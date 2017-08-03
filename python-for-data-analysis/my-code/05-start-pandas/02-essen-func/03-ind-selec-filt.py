# Indexing, selection and filtering
#   - You can use obj['index value'] not only integers obj[0]
import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame

obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])

obj['b']
obj[1]
obj[2:4]
obj[['b', 'a', 'd']]
obj[[1, 3]]
obj[obj < 2]

# Slicing -> endpoint is INCLUSIVE
obj['b':'c']

# Setting values works as you would expect
obj['b':'c'] = 5
obj

# When to index into a DataFrame
# 	- To retrieve 1+ columns with a value or sequence of values
data = DataFrame(np.arange(16).reshape(4, 4),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])

data

data['two']
data[['three', 'one']]

# Special cases for indexing this way
data[:2]

data[data['three'] > 5]

# Indexing with a boolean DataFrame
data < 5
data[data < 5] = 0
data

# Label indexing using *loc*
# 	- less verbose
data.loc['Colorado', ['two', 'three']]

data.ix[['Colorado', 'Utah'], [3, 0, 1]]

data.ix[2]

data.ix[:'Utah', 'two']

data.ix[data.three > 5, :3]
