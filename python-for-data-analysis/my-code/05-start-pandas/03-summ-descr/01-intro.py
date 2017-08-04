# Summarizing and Computing Descriptive Statistics
import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame

# methods fall into two categories
#   1. Reductions
#   2. Summarry statistics (single value extractions)
df = DataFrame([[1.4, np.nan], [7.1, -4.5],
                [np.nan, np.nan], [0.75, -1.3]],
               index=['a', 'b', 'c', 'd'],
               columns=['one', 'two'])

df

# *sum* -> Series with COLUMN sums
df.sum()
df.sum(axis=1)

# *skipna* -> N/A's are excluded (to avoid this)
df.mean(axis=1, skipna=False)

# *idxmin/idxmax* -> index value where min max are attained
df.idxmax()

# accumulations
df.cumsum()

df.describe()

# non-numeric describe
obj = Series(['a', 'a', 'b', 'c'] * 4)
obj
obj.describe()
