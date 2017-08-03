# * Dropping entries from an axis
#   - *drop* method returns a new object with the values deleted
import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame

obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])

new_obj = obj.drop('c')
new_obj

obj.drop(['d', 'c'])

# index calues can be deleted from either axis
data = DataFrame(np.arange(16).reshape((4, 4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])

data.drop(['Colorado', 'Ohio'])

data.drop('two', axis=1)

data.drop(['two', 'four'], axis=1)

