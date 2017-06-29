# 1. DOWNLOADING FILES AND READING CSV  # NOQA
import pandas as pd
import urllib.request

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

# 2. QUESTIONS WE WENT TO ANSWER

#     1. Which are the countries with the highest and infectious TB incidence?
#     2. What is the general world tendency from 1990-2007
#     3. What countries don't follow the tendency
#     4. What other facts about the disease do we know that we can track
#        with the data

# 3. DESCRIPTIVE STATISTICS

# describe() - The most basic descriptive statistics method
#              for pandas.DataFrame (like R's summary())
df_summary = existing_df.describe()
df_summary

# accessing individual summaries
df_summary[['Spain', 'United Kingdom']]

# pct_change() - find percentage change over the years for TB cases in Spain
tb_pct_change_spain = existing_df.Spain.pct_change()
tb_pct_change_spain

# max() - maxiumum value
tb_pct_change_spain.max()

# for UK
existing_df['United Kingdom'].pct_change().max()

# argmax() / idmax() - for index value (year) use 
existing_df['Spain'].pct_change().argmax()
existing_df['United Kingdom'].pct_change().argmax()
