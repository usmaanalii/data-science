# * Sorting and ranking
import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame

# Sorting a dataset by some criterion
#   - *sort_index* ->lexographically
obj = Series(range(4), index=['b', 'c', 'a', 'd'])

obj.sort_index()

# DataFrames -> You can sort by index on either axis
frame = DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'],
                  columns=['d', 'a', 'b', 'c'])

frame.sort_index()
frame.sort_index(axis=1)

# descending order
frame.sort_index(axis=1, ascending=False)

# *sort_values* -> sort a series by values
obj = Series([4, 7, -3, 2])
obj.sort_values()

obj = Series([4, np.nan, 7, np.nan, -3, 2])

# NaN are grouped at the bottom
obj.sort_values()

# Sort by the values in one or more columns
#   'by'
frame = DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})

frame

frame.sort_values(by='b')

# Sort by multiplecolumns
#   - pass list of names
frame.sort_values(by=['a', 'b'])

# Ranking is closely related to sorting
#   - assigns ranks to each point
#   - ties -> assigns the mean rank
obj = Series([7, -5, 7, 4, 2, 0, 4])
obj.rank()

# Assign rank by first observed in the data
obj.rank(method='first')

# Rank in descending order
obj.rank(ascending=False, method='max')

# Compute ranks over rows or columns
frame = DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1],
                   'c': [-2, 5, 8, -2.5]})

frame

frame.rank(axis=1)
