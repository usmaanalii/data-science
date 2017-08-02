# * DataFrame
import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame

#   - represents a tabular, spreadsheet-like data structure, with
#       o ordered collection of multi value type columns
#   - like a dict of series (all sharing the same index)
#   - data is stored as one+ 2d blocks not lists/dicts

# DataFrame from
#   - dict of equal-length lists of numpy arrays
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
frame

# Passing a sequence of columns
# - The columns will match your order
DataFrame(data, columns=['year', 'state', 'pop'])

# Passing a column that isn't in the data will result in NA's
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                   index=['one', 'two', 'three', 'four', 'five'])
frame2
frame2.columns

# Columns can be retrieved as Series by
#   1. Dot notation
#   2. Attribute selection
frame2['state']
frame2.year

# Rows can be retrieved by
#   1. Position
#   2. Name
#   3. loc -> indexing field
frame2.loc['three']

# Modify columnss
#   - By assignment
frame2['debt'] = 16.5
frame2

frame2['debt'] = np.arange(5.)
frame2

# Assigning lists/arrays to columns
#   - Length must match
# Assogmomg Series
#   - Will be conformed and ,ising values will be inserted
val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
frame2

# Assign column that doesn't exist -> creates column
# Del -> delete columns
frame2['eastern'] = frame2.state == 'Ohio'
frame2
del frame2['eastern']
frame2.columns

# Nested dict of dicts
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

frame3 = DataFrame(pop)
frame3

# Transpose the result
frame3.T

# Explicit index specified
DataFrame(pop, index=[2001, 2002, 2003])

# Dict of Series
pdata = {'Ohio': frame3['Ohio'][:-1],
         'Nevada': frame3['Nevada'][:2]}

DataFrame(pdata)

# If index and columns have *name* attributes set, they will be displayed
frame3.index.name = 'year'
frame3.columns.name = 'state'
frame3

# *values* attribute returns the values as a 2d ndarray
frame3.values
frame2.values
