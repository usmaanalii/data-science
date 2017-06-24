# 1. DOWNLOADING FILES AND READING CSV  # NOQA

import urllib.request
import pandas as pd

# Downloading the google spreadsheet data as CSV
tb_deaths_url_csv = 'https://docs.google.com/spreadsheets/d/12uWVH_IlmzJX_75bJ3IH5E-Gqx6-zfbDKNvZqYjUuso/pub?gid=0&output=CSV'  # NOQA
tb_existing_url_csv = 'https://docs.google.com/spreadsheets/d/1X5Jp7Q8pTs3KLJ5JBWKhncVACGsg5v4xu6badNs4C7I/pub?gid=0&output=csv'  # NOQA
tb_new_url_csv = 'https://docs.google.com/spreadsheets/d/1Pl51PcEGlO9Hp4Uh0x2_QM0xVb53p2UDBMPwcnSjFTk/pub?gid=0&output=csv'  # NOQA

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
