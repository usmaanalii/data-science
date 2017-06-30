# pylint: disable=line-too-long

# 1. DOWNLOADING FILES AND READING CSV
import pandas as pd
import urllib.request
%matplotlib inline

# Downloading the google spreadsheet data as CSV
tb_deaths_url_csv = 'https://docs.google.com/spreadsheets/d/12uWVH_IlmzJX_75bJ3IH5E-Gqx6-zfbDKNvZqYjUuso/pub?gid=0&output=CSV'
tb_existing_url_csv = 'https://docs.google.com/spreadsheets/d/1X5Jp7Q8pTs3KLJ5JBWKhncVACGsg5v4xu6badNs4C7I/pub?gid=0&output=csv'
tb_new_url_csv = 'https://docs.google.com/spreadsheets/d/1Pl51PcEGlO9Hp4Uh0x2_QM0xVb53p2UDBMPwcnSjFTk/pub?gid=0&output=csv'

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

# 4. PLOTTING
#    Basic plotting fucntionality
existing_df[['United Kingdom', 'Spain', 'Colombia']].plot()

# box plots
existing_df[['United Kingdom', 'Spain', 'Colombia']].boxplot()

# 5. ANSWERING QUESTIONS

# Question: Per year, what country has the highest number of existing and new
#           TB cases

# We need to transpose the data since the columns represent the countries
existing_df.apply(pd.Series.argmax, axis=1)

# World trends in TB cases

# 1. sum up every countries' values for the three datasets (per year)
deaths_total_per_year_df = deaths_df.sum(axis=1)
existing_total_per_year_df = existing_df.sum(axis=1)
new_total_per_year_df = new_df.sum(axis=1)

# 2. Create a new DataFrame, with each sum in a series
#    Plot this DataFrame
world_trends_df = pd.DataFrame({'Total deaths per 100K': deaths_total_per_year_df, 'Total existing cases per 100K': existing_total_per_year_df, 'Total new cases per 100k': new_total_per_year_df}, index=deaths_total_per_year_df.index)

world_trends_df.plot(figsize=(6, 3)).legend(loc="center left", bbox_to_anchor=(1, 0.5))

# Counteies out of tendency

# distribution of countries in an average year
deaths_by_country_mean = deaths_df.mean()
deaths_by_country_mean_summary = deaths_by_country_mean.describe()
existing_by_country_mean = existing_df.mean()
existing_by_country_mean_summary = existing_by_country_mean.describe()
new_by_country_mean = new_df.mean()
new_by_country_mean_summary = new_by_country_mean.describe()

deaths_by_country_mean.sort_values().plot(kind="bar", figsize=(24, 6))

# Countries beyond 1.5x IQ range
deaths_outlier = deaths_by_country_mean_summary['50%'] * 1.5
existing_outlier = existing_by_country_mean_summary['50%'] * 1.5
new_outlier = new_by_country_mean_summary['50%'] * 1.5

# Yse these values to get countries beyond these levels
outlier_countries_by_deaths_index = deaths_by_country_mean > deaths_outlier
outlier_countries_by_existing_index = existing_by_country_mean > existing_outlier
outlier_countries_by_new_index = new_by_country_mean > new_outlier

# Proportion of countries out of trend?
num_countries = len(deaths_df.T)
sum(outlier_countries_by_deaths_index) / num_countries

# prevalence (existing cases)
sum(outlier_countries_by_existing_index) / num_countries

# incidence (new cases)
sum(outlier_countries_by_new_index) / num_countries

# use indices to filter out original data frames
outlier_deaths_df = deaths_df.T[outlier_countries_by_deaths_index].T
outlier_existing_df = existing_df.T[outlier_countries_by_existing_index].T
outlier_new_df = new_df.T[outlier_countries_by_new_index].T

# consider an outlier as 5*IQR

# Countries beyond 1.5x IQ range
deaths_super_outlier = deaths_by_country_mean_summary['50%'] * 5
existing_super_outlier = existing_by_country_mean_summary['50%'] * 5
new_super_outlier = new_by_country_mean_summary['50%'] * 5

# Yse these values to get countries beyond these levels
super_outlier_countries_by_deaths_index = deaths_by_country_mean > deaths_super_outlier
super_outlier_countries_by_existing_index = existing_by_country_mean > existing_super_outlier
super_outlier_countries_by_new_index = new_by_country_mean > new_super_outlier

sum(super_outlier_countries_by_deaths_index) / num_countries
sum(super_outlier_countries_by_existing_index) / num_countries
sum(super_outlier_countries_by_new_index) / num_countries

# Concentrate on epidemics control, and have a look at the new cases data frame

# Get the dataframes
# use indices to filter out original data frames
super_outlier_deaths_df = deaths_df.T[super_outlier_countries_by_deaths_index].T
super_outlier_existing_df = existing_df.T[super_outlier_countries_by_existing_index].T
super_outlier_new_df = new_df.T[super_outlier_countries_by_new_index].T

super_outlier_new_df
# Plots
super_outlier_new_df.plot(figsize=(12, 4)).legend(loc='center left', bbox_to_anchor=(1, 0.5))

# We have 22 countries where the number of new cases exceed 5x the average
# Let's make a country that represents the average of these
average_super_outlier_country = super_outlier_new_df.mean(axis=1)
average_super_outlier_country

# create a country that represents the rest of the world
average_better_world_country = new_df.T[ - super_outlier_countries_by_new_index].T.mean(axis=1)
average_better_world_country

# plot this country with the average world country
two_world_df = pd.DataFrame({'Average Better World Country': average_better_world_country, 'Average Outlier Country': average_super_outlier_country}, index=new_df.index)

two_world_df.plot(title="Estimated new TB cases per 100K", figsize=(12, 8))

# The increase in new cases is very strong in outliers

# Exact numbers
two_world_df.pct_change().plot(title="Percentage change in estimated new TB cases", figsize=(12, 8))

# Googling about events and dates in TB
existing_df.China.plot(title="Estimated existing TB cases in China")

new_df.apply(pd.Series.argmax, axis=1)['2007']
