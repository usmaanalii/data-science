# * Concatenating Along an Axis
import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame

# concatenating, binding or stacking
# Numpy has a concatenate() function for this
arr = np.arange(12).reshape((3, 4))
arr

np.concatenate([arr, arr], axis=1)

# Labeled axes allow you to generalize array concatenation
s1 = Series([0, 1], index=['a', 'b'])
s2 = Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = Series([5, 6], index=['f', 'g'])

pd.concat([s1, s2, s3])
pd.concat([s1, s2, s3], axis=1)

s4 = pd.concat([s1 * 5, s3])

pd.concat([s1, s4], axis=1)

pd.concat([s1, s4], axis=1, join='inner')
pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']])

# The concatenated peices are not identifiable in the result
#   - Create a hierarchical index on the concatenation axis via *keys*
result = pd.concat([s1, s2, s3], keys=['one', 'two', 'three'])
result

result.unstack()
# combining Series along axis=1
pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three'])

# Same applied to DF's
df1 = DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'],
                columns=['one', 'two'])

df2 = DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'],
                columns=['three', 'four'])

pd.concat([df1, df2], axis=1, keys=['level1', 'level2'])

# Passing a dict of objects is easier
pd.concat({'level1': df1, 'level2': df2}, axis=1)

# other arguments dictating the indexing
pd.concat([df1, df2], axis=1, keys=['level1', 'level2'],
          names=['upper', 'lower'])

# DF's in which the row index is not meaningful
df1 = DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
df2 = DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])

df1
df2

pd.concat([df1, df2], ignore_index=True)
