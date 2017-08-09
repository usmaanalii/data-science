# * Filling in Missing Data
import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame
#   - fill in the "holes"

# *fillna* -> takes a value to fill with
df = DataFrame(np.random.randn(7, 3))

df.loc[:4, 1] = NA
df.loc[:2, 2] = NA

df.fillna(0)

# *fillna* -> call with a dict to provide different fill valus for columns
df.fillna({1: 0.5, 3: -1})

# *fillna* -> returns a new object, but you can modify the original

# always returns a reference to the filled object
_ = df.fillna(0, inplace=True)

df

# Reindexing
df = DataFrame(np.random.randn(6, 3))

df.loc[2:, 1] = NA
df.loc[4:, 2] = NA

df

df.fillna(method='ffill')

df.fillna(method='ffill', limit=2)
