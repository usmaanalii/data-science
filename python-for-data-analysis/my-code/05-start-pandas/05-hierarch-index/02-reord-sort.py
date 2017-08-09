# Reordering and Sorting Levls
import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame

# Rearranging levels on an axis or sort the data by the values on one level
#   swaplevel() - interchanges two given level numbers or names
frame = DataFrame(np.arange(12).reshape((4, 3)),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=[['Ohio', 'Ohio', 'Colorado'],
                           ['Green', 'Red', 'Green']])

frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']

frame.swaplevel('key1', 'key2')

#   sortlevel() -> sorts using values in a sinle level
#                  commonly used for lexicographically sorting the values
frame.sort_index(1)

frame.swaplevel(0, 1).sort_index(level=0)
