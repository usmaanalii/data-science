# Summary Statistics by Level
import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame

# Using 1+ columns from a DF as the row index
# Moving row index into columns
frame = DataFrame({'a': range(7), 'b': range(7, 0, -1),
                   'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                   'd': [0, 1, 2, 0, 1, 2, 3]})

frame

# set_index() -> creates a new DataFrame using 1+ columns as the index
frame2 = frame.set_index(['c', 'd'])
frame2

# leave the columns in
frame.set_index(['c', 'd'], drop=False)

# reset_index() -> inverse of set_index
frame2.reset_index()
