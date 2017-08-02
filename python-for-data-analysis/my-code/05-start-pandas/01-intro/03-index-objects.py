# * Index Objects
import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame
#   - Hold the axis labels
#   - Metadata such as
#       - axis name(s)
#   - Sequences are converted to indexes when constructing Series or DataFrames
obj = Series(range(3), index=['a', 'b', 'c'])
index = obj.index
index
index[1:]

# Index Objects are immutable
#   - Allows indexes to be shared across data structures
#   - Function as *fixed-size set*
index[1] = 'd'  # error

index = pd.Index(np.arange(3))

obj2 = Series([1.5, -2.5, 0], index=index)

obj2.index is index

pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

frame3 = DataFrame(pop)

frame3

'Ohio' in frame3.columns
2003 in frame3.index
