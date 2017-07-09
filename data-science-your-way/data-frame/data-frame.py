# pylint: disable=E501

# 1. DOWNLOADING FILES AND READING CSV

from __future__ import division
import urllib.request
import pandas as pd

# Downloading the google spreadsheet data as CSV
tb_deaths_url_csv = 'https://docs.google.com/spreadsheets/d/12uWVH_IlmzJX_75bJ3IH5E-Gqx6-zfbDKNvZqYjUuso/pub?gid=0&output=CSV'  # noqa
tb_existing_url_csv = 'https://docs.google.com/spreadsheets/d/1X5Jp7Q8pTs3KLJ5JBWKhncVACGsg5v4xu6badNs4C7I/pub?gid=0&output=csv'  # noqa
tb_new_url_csv = 'https://docs.google.com/spreadsheets/d/1Pl51PcEGlO9Hp4Uh0x2_QM0xVb53p2UDBMPwcnSjFTk/pub?gid=0&output=csv'  # noqa

# csv file names
local_tb_deaths_file = 'all_deaths.csv'
local_tb_existing_file = 'existing_cases.csv'
local_tb_new_file = 'new_cases.csv'

# create CSV's from the url's
deaths_f = urllib.request.urlretrieve(tb_deaths_url_csv, local_tb_deaths_file)
existing_f = urllib.request.urlretrieve(tb_existing_url_csv,
                                        local_tb_existing_file)
new_f = urllib.request.urlretrieve(tb_new_url_csv, local_tb_new_file)

# Create data frames
deaths_df = pd.read_csv(local_tb_deaths_file, index_col=0, thousands=',').T
existing_df = pd.read_csv(local_tb_existing_file, index_col=0, thousands=',').T
new_df = pd.read_csv(local_tb_new_file, index_col=0, thousands=',').T

# Exploring the data
existing_df.head()  # Shows the first 5 rows

existing_df.columns  # Access column names
existing_df.index  # Access row names

# Assign proper names to columns/rows
deaths_df.index.names = ['year']
deaths_df.columns.names = ['country']

existing_df.index.names = ['year']
existing_df.columns.names = ['country']

new_df.index.names = ['year']
new_df.columns.names = ['country']

# 2. DATA INDEXING

# Accessing each country series
existing_df['United Kingdom']  # by it's name
existing_df.Spain  # by key value as an attribute

# Accessing multiple series via pythonlists
existing_df[['Spain', 'United Kingdom']]

# Accessing individual cells
existing_df.Spain['1990']  # 44

# Slicing the series using list indexing
existing_df[['Spain', 'United Kingdom']][0:5]

# Slicing the rows
existing_df[0:5]

# NOTE: Production code
#
# It is recommended to use optimized pandas data access methods exposed below

# .iloc - used positional index access
existing_df.iloc[0:2]

# .loc - used for label access
existing_df.loc['1992':'2005']

# Combined to perform series indexing by column
existing_df.loc[['1992', '1998', '2005'], ['Spain', 'United Kingdom']]

# 3. DATA SELECTION
#    How to select data from dataframes based on their values via logical
#    expressions

# logical operators
existing_df > 10
existing_df['United Kingdom'] > 10

# You can use the result of the previous expressions to index vectors
# with .iloc or []
existing_df.Spain[existing_df['United Kingdom'] > 10]

existing_df[existing_df > 10]  # False values will return NaN

# NOTE: Use of where() that accepts a second argument for imputing NaN values
existing_df.where(existing_df > 10, 0)

# 3. FUNCTION MAPPING AND DATA GROUPING
#    Applying functions both, index and element wise

# Total number of TB cases for each country
existing_df.sum()

# Do the same by year (passing axis=1 to use columns instead of index)
existing_df.sum(axis=1)

# Methods to apply other fucntions to data frames

# apply and applymap
existing_df.apply(lambda x: x / 10)  # cases per million (not 100k)

# NOTE: apply works element-wise in this case, producing a data frame

# groupby
# Get the mean no. cases per year in two periods (before/after 2000)
mean_cases_by_period = existing_df.groupby(lambda x: int(x) > 1999).mean()
mean_cases_by_period.index = ['1990-1999', '2000-2007']
mean_cases_by_period

# NOTE: the lambda function is called on each year (element of .index)
#       resulting in two groups

# Can be indexed as usual
mean_cases_by_period[['United Kingdom', 'Spain', 'Colombia']]
