# Getting Started with pandas
import pandas as pd
from pandas import Series
from pandas import DataFrame
# 	- Contains high-level data structures and manipulation tools for analysis
# 	- Built on top of of NumPy so plays well with it

# * Introduction to pandas Data Structures
#   - Need to be familiar with Series and DataFrame

# %% ** Series
#   - One dimensional array like object, containing
#       o array
#       o index -> array of data labels
obj = Series([4, 7, -5, 3])
obj  # -> index  value

# array representation
obj.values
obj.index

# Create a series with an index identifying each data point
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj2

# You can use values in the index when selecting values
obj2['a']
obj2['d']
obj2[['c', 'a', 'd']]

# The index-value link will be preserved
obj2

# Series are dict like, in that they map index values to data values
'b' in obj2
'e' in obj2

# You can create a Series from a dict
# 	- The dict keys will be in sorted order
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
obj3

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index=states)
obj4  # will fill in missing value with NaN

# Useful for detecting missing data
# 	- isnull
# 	- notnull
pd.isnull(obj4)
pd.notnull(obj4)

# They are also instance methods
obj4.isnull()
obj4.notnull()

# Series also automaticallly align differently indexed data
obj3
obj4
obj3 + obj4

# *name* attribute
obj4.name = 'population'
obj4.index.name = 'state'
obj4

# Series index' can be altered in place by assignment
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
obj
