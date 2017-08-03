# * Reindexing
import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame

# 	- create a new object with the data conformed to a new index
obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj

# *reindex* - rearranges the data according to the new index
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
obj2

# missing values
obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)

# *ffill* - fill values with some interpolation or filling of values
#         - fill (carry) values forward
obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj3

obj3.reindex(range(6), method='ffill')

# reindex can
#   - alter the row (index)
#   - alter the columns
#   - alter both
frame = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],
                  columns=['Ohio', 'Texas', 'California'])
frame

frame2 = frame.reindex(['a', 'b', 'c', 'd'])
frame2

# *columns* - columns can be reindexed using the keyword
states = ['Texas', 'Utah', 'California']
frame.reindex(columns=states)

# Reindex in one shot, but interpolation will happen ROW wise (axis=0)
frame.reindex(index=['a', 'b', 'c', 'd'], method='ffill')

frame.loc[['a', 'b', 'c', 'd'], states]

# reindex function arguments
#   - index -> sequence to use as rows
#   - method -> fill method
#   - fill_value -> substitue value for missing data
#   - limit -> max size to fill
#   - level -> TODO: what is the level method?
#   - copy -> DonCopy rule for matching indexes




