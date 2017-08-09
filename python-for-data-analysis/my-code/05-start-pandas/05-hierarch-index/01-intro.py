# Hierarchical Indexing
import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame
#   - Allows you to have multiple index levels on an axis
#   - Enables working with higher dimensional data in a lower dimensional form

data = Series(np.random.randn(10),
              index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                     [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])

data

data.index

# Partial indexing is also possible, allowing concise subsetting
data['b']
data['b':'c']
data.loc[['b', 'd']]
data[:, 2]

# Can be used to make pivot tables
#   unstack() -> rearrange the data into a DF
#   stack() -> inverse of ^^
data.unstack()

data.unstack().stack()

# Either axis can have a hierarchical index
frame = DataFrame(np.arange(12).reshape((4, 3)),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=[['Ohio', 'Ohio', 'Colorado'],
                           ['Green', 'Red', 'Green']])

frame

frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
frame

# Use partial column indexing to select groups of columns
frame['Ohio']
