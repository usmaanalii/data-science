# Combining Principal Component Analysis with Cluster Analysis
# to represent a two dimensional space data defined in a higher dimension
#
# Using this to group/cluster and the data and find hidden relationships

# PCA
# Reduced data dimensionality by finding principal components, which
# are directions of maximum variation in a datset
# The goal of this, is to be left with the minimum number of variables
# responsible for the amximum amount of variation about the data distribution

# Clustering
# An unsupervised technique, used to organise data samples by proximity
# base don its variables.
# Helps to understand how data points relate to each other.
# By finding centroids (data sample minimising the sum of distances to each
# data point in a cluster), we can define a cluster based on characteristics

# 1. DOWNLOADING FILES AND READING CSV
import urllib.request
import pandas as pd

# Downloading the google spreadsheet data as CSV
tb_existing_url_csv = 'https://docs.google.com/spreadsheets/d/1X5Jp7Q8pTs3KLJ5JBWKhncVACGsg5v4xu6badNs4C7I/pub?gid=0&output=csv'  # NOQA

# csv file names
local_tb_existing_file = 'tb_existing_100.csv'

# create CSV's from the url's
existing_f = urllib.request.urlretrieve(tb_existing_url_csv, local_tb_existing_file)  # NOQA

# Create data frames
existing_df = pd.read_csv(local_tb_existing_file, index_col=0, thousands=',')

existing_df.index.names = ['country']
existing_df.columns.names = ['year']

# In read_csv, index_col is specified to be 0, since we want country names
# to be the row labels
# Also, the thousands seperator is ',' so cells are parsed as numbers

# head() - Check first few lines
existing_df.head()

# 2. DIMENSIONALITY REDUCTION WITH PCA

# Represent each country in two dimensional space
# Each sample is a country defined by 18 variables for a given year (1990-2007)
# PCA will be used to reduce these 18 to 2 that best capture the information
