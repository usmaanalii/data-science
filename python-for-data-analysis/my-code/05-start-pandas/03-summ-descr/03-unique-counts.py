# * Unique Values, Value Counts and Membership
import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame

#   - Extract information about the values contained in a 1d Series
obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])

# *unique*
uniques = obj.unique()
uniques

# sort the uniques
uniques.sort()
uniques

# *value_counts()* -> Series containing value frequencies
#    - returned in descending order
obj.value_counts()

# Can also be called as a top level method
pd.value_counts(obj.values, sort=False)

# *isin* -> vectorized set membership
mask = obj.isin(['b', 'c'])

# Compute a histogram on multiple related columns in a DF
data = DataFrame({'Qu1': [1, 3, 4, 3, 4],
                  'Qu2': [2, 3, 1, 2, 3],
                  'Qu3': [1, 5, 2, 4, 4]})
data

result = data.apply(pd.value_counts).fillna(0)