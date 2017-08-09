# * Merging on Index
import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame

#   - In some cases, the merge key(s) in a DF, will be found in its index
#   - In this case, you can pass left_index=True, right_index=True
left1 = DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
                   'value': range(6)})

right1 = DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])

left1
right1

# default to inner join
pd.merge(left1, right1, left_on='key', right_index=True)

# form the union with an outer join
pd.merge(left1, right1, left_on='key', right_index=True, how='outer')

# Hierarchicallly-indexed data
lefth = DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                   'key2': [2000, 2001, 2002, 2001, 2002],
                   'data': np.arange(5.)})

righth = DataFrame(np.arange(12).reshape((6, 2)),
                   index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
                          [2001, 2000, 2000, 2000, 2001, 2002]],
                   columns=['event1', 'event2'])

pd.merge(lefth, righth, left_on=['key1', 'key2'],
         right_index=True)

pd.merge(lefth, righth, left_on=['key1', 'key2'],
         right_index=True, how='outer')

# Using the indexes of both sides od the merge
left2 = DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=['a', 'c', 'e'],
                  columns=['Ohio', 'Nevada'])

right2 = DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                   index=['b', 'c', 'd', 'e'], columns=['Missouri', 'Alabama'])

left2
right2

pd.merge(left2, right2, how='outer', left_index=True, right_index=True)

# You can combine many DF's aving the same index with different columns
left2.join(right2, how='outer')

# Also supports, joining the index of the passed DF on one of the DF's columns
left1.join(right1, on='key')

# Index on index merges need a list of DF's to join (alternative to concat)
another = DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],
                    index=['a', 'c', 'e', 'f'], columns=['New York', 'Oregon'])

another

left2.join([right2, another])

left2.join([right2, another], how='outer')
