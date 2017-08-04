# * Function application and mapping
import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame

#   - ufunc -> element wise array method work fine with pandas objects
frame = DataFrame(np.random.randn(4, 3), columns=list('bde'),
                  index=['Utah', 'Ohio', 'Texas', 'Oregon'])

frame
np.abs(frame)

# Applying a function on 1D arrays to each column or row
f = lambda x: x.max() - x.min()

frame.apply(f)
frame.apply(f, axis=1)


# sum and mean can be applied directly (no need for apply)
def f(x):
    return Series([x.min(), x.max()], index=['min', 'max'])


frame.apply(f)

# Element-wise python functions can be used too
format = lambda x: '%.2f' % x

# applymap, not map, because Series.map -> apply function element-wise
frame.applymap(format)

frame['e'].map(format)

