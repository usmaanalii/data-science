# * Arithmetic and data alignment
import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame
#   - Behaviour of arithmetic between objects with different indexes
#   - Uses unions for non matching indexes

s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'b', 'c', 'd'])
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])

s1
s2

# N/A's in indexes that don't overlap
s1 + s2

# For DataFrames, the alignment is performed on both rows and columns
df1 = DataFrame(np.arange(9).reshape((3, 3)), columns=list('bcd'),
                index=['Ohio', 'Texas', 'Colorado'])

df2 = DataFrame(np.arange(12).reshape((4, 3)), columns=list('bde'),
                index=['Utah', 'Ohio', 'Texas', 'Oregon'])

df1
df2

# Adding these, returns a DF whose rows/cols are the unions
df1 + df2

# ** Arithmetic methods with fill values
#   - Fill in values when dealing with unmatched objects
df1 = DataFrame(np.arange(12).reshape((3, 4)), columns=list('abcd'))
df2 = DataFrame(np.arange(20).reshape((4, 5)), columns=list('abcde'))

df1
df2

# NA's from unmatched (row, col) elements
df1 + df2

# *add* method
#   o fill_value
df1.add(df2, fill_value=0)

# Similar functionality can be applied when reindexing
df1.reindex(columns=df2.columns, fill_value=0)

# ** Operations between DF and S

#   - consider the difference between a 2d array and one of its rows
arr = np.arange(12).reshape((3, 4))
arr
arr[0]
arr - arr[0]  # broadcasting*

# Same with DF and S
frame = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                  index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.iloc[0]

frame
series

# Arithmetic between DF and S by default broadcasts DOWN the rows
frame - series

series2 = Series(range(3), index=['b', 'e', 'f'])

frame + series2

# Broadcasting over columns instead
#   - Use the named methods (add and sub etc...)
series3 = frame['d']

frame
series3

frame.sub(series3, axis=0)
