# Handling Missing Data
import pandas as pd
import numpy as np
from numpy import nan as NA
from pandas import Series
from pandas import DataFrame
#   - NaN -> floating point value to rep. missing data
#   - sentinal -> for detection

string_data = Series(['aardvark', 'artichoke', np.nan, 'avocado'])
string_data

string_data.isnull()

# None is also treated as NA
string_data[0] = None

string_data.isnull()

# * Filtering Out Missing Data
data = Series([1, NA, 3.5, NA, 7])

data.dropna()

# Compute ^ via BOOLEAN INDEXING
data[data.notnull()]

# DF -> drop rows OR columns which are NA or thoce with some NA's
# dropna -> drops any NA's
data = DataFrame([[1., 6.5, 3.], [1., NA, NA],
                  [NA, NA, NA], [NA, 6.5, 3.]])

cleaned = data.dropna()

data
cleaned

# *how='all'* -> drops all NA's
data.dropna(how='all')

# axis=1
data[4] = NA

data

data.dropna(axis=1, how='all')

# Filter out rows with low no. observations
# *thresh*
df = DataFrame(np.random.randn(7, 3))

df.loc[:4, 1] = NA

df.loc[:2, 2] = NA

df

df.dropna(thresh=3)

