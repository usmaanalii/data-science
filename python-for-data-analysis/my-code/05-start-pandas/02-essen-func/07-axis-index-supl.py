# * Axis indexes with duplicate values
import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame
#   - Series with duplicate indices
obj = Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
obj

# *is_unique* -> tells you whether a value is unique or not
obj.index.is_unique

# If you request a duplicated index, then a Series is returned (not a scalar)
obj['a']
obj['c']

# Same logic applies to rows of a DF
df = DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
df

df.loc['b']
