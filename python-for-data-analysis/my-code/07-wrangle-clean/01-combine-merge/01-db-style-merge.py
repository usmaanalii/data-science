# Combining and Merging Data Sets
import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame
#   - pandas.merge -> connects rows based on keys, like a SQL join
#   - pandas.concat -> glues/stacks objects along an axis
#   - combine_first -> enables splicing together overlapping data to fill
#                      missing values

# * Database-style DataFrame Merges
#   - Merge or join combine data sets by linking rows using 1+ keys
#   - merge -> the entry point for ^^

df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})

df2 = DataFrame({'key': ['a', 'b', 'd'],
                 'data2': range(3)})

df1
df2

#   - This is an example of a many-to-one merge situation
pd.merge(df1, df2)

pd.merge(df1, df2, on='key')  # best practice to specify the key

# If the column names are different in each object, you can specify them
df3 = DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})

df4 = DataFrame({'rkey': ['a', 'b', 'd'],
                 'data2': range(3)})

pd.merge(df3, df4, left_on='lkey', right_on='rkey')

# By default, you get inner joins, but you can get
#   - left
#   - right
#   - outer
pd.merge(df1, df2, how='outer')

# Many to many merges are more tricky
#   - Form the cartesian product of the rows
df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                 'data1': range(6)})

df2 = DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                 'data2': range(5)})

df1
df2

pd.merge(df1, df2, on='key', how='left')

pd.merge(df1, df2, how='inner')

# Merging with multiple keys
#   - Pass multiple keys on=['one', 'two']
left = DataFrame({'key1': ['foo', 'foo', 'bar'],
                  'key2': ['one', 'two', 'one'],
                  'lval': [1, 2, 3]})

right = DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                   'key2': ['one', 'one', 'one', 'two'],
                   'rval': [4, 5, 6, 7]})

pd.merge(left, right, on=['key1', 'key2'], how='outer')  # (key1, key2) tuples

# Overlapping column names
#   - use merge *suffixes* -> options for specifying strings to append to
#                             overlappint names in left and right DFs
pd.merge(left, right, on='key1')

pd.merge(left, right, on='key1', suffixes=('_left', '_right'))
