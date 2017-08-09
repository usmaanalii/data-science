# Summary Statistics by Level
import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame

#   - *level* -> summary stats have this option
#       o uses *groupby* machinery
frame = DataFrame(np.arange(12).reshape((4, 3)),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=[['Ohio', 'Ohio', 'Colorado'],
                           ['Green', 'Red', 'Green']])

frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']


frame.sum(level='key2')
frame.sum(level='color', axis=1)

