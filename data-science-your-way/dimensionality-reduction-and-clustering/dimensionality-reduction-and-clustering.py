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
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
from sklearn.cluster import KMeans
%matplotlib inline

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

# Use sklearn scipy.linalg

# Specify in advance, the number of principal components to use
pca = PCA(n_components=2)
pca.fit(existing_df)  # gives an object to use for transforming the data

# lower dimension representation of data frame as a numPy array
existing_2d = pca.transform(existing_df)

# Put it in a new data frame
existing_df_2d = pd.DataFrame(existing_2d)
existing_df_2d.index = existing_df.index
existing_df_2d.columns = ['PC1', 'PC2']
existing_df_2d.head()

# Print the explained variance ratio as follows

# First PC explains 92% of the variance, and PC2 accounts for 6%
print(pca.explained_variance_ratio_)

# Plot the lower dimensionality version of the dataset
ax = existing_df_2d.plot(kind='scatter', x='PC2', y='PC1', figsize=(16, 8))

for i, country in enumerate(existing_df.index):
    ax.annotate(country, (existing_df_2d.iloc[i].PC2, existing_df_2d.iloc[i].PC1))  # NOQA

existing_df_2d['country_mean'] = pd.Series(existing_df.mean(axis=1), index=existing_df_2d.index)  # NOQA
country_mean_max = existing_df_2d['country_mean'].max()
country_mean_min = existing_df_2d['country_mean'].min()
country_mean_scaled = (existing_df_2d.country_mean - country_mean_min) / country_mean_max  # NOQA
existing_df_2d['country_mean_scaled'] = pd.Series(country_mean_scaled, index=existing_df_2d.index)  # NOQA
existing_df_2d.head()

# Plot using this variable size (omitting country names)
existing_df_2d.plot(kind="scatter", x="PC2", y="PC1", s=existing_df_2d['country_mean_scaled'] * 100, figsize=(12, 8))  # NOQA

# Do the same with sum instead of mean
existing_df_2d['country_sum'] = pd.Series(existing_df.sum(axis=1), index=existing_df_2d.index)  # NOQA

country_sum_max = existing_df_2d['country_sum'].max()
country_sum_min = existing_df_2d['country_sum'].min()

country_sum_scaled = (existing_df_2d.country_sum - country_sum_min) / country_sum_max  # NOQA

existing_df_2d['country_sum_scaled'] = pd.Series(country_sum_scaled, index=existing_df_2d.index)  # NOQA

existing_df_2d.plot(kind="scatter", x="PC2", y="PC1", s=existing_df_2d['country_sum_scaled'] * 100, figsize=(16, 8))  # NOQA

# Associate the size with the change between 1990 and 2007
existing_df_2d["country_change"] = pd.Series(existing_df["2007"] - existing_df["1990"], index=existing_df_2d.index)  # NOQA

country_change_max = existing_df_2d['country_change'].max()
country_change_min = existing_df_2d['country_change'].min()

country_change_scaled = (existing_df_2d.country_change - country_change_min) / country_change_max  # NOQA

existing_df_2d['country_change_scaled'] = pd.Series(country_change_scaled, index=existing_df_2d.index)  # NOQA

existing_df_2d.plot(kind="scatter", x="PC2", y="PC1", s=existing_df_2d['country_change_scaled'] * 100, figsize=(16, 8))  # NOQA

# PCA Results

# Most variation happens along the y axis assigned to PC1/
# At the top of the charts, a concentration of developed countries exist,
# descending the axis, the countries are more sparse (less developed)
#
# Colour changes correlate with this dispersion
#
# PC2 - Is laregely affected by change over time (color gradient changed
# across x axis for time change data)

# 3. EXPLORING DATA STRUCTURE WITH K MEANS CLUSTERING
kmeans = KMeans(n_clusters=5)
clusters = kmeans.fit(existing_df)

# Store the cluster assignments together with each country
# in our data frame. Labels are returned in clusters.labels_
existing_df_2d['cluster'] = pd.Series(clusters.labels_, index=existing_df_2d.index)  # NOQA

# Plot, using cluster column as color
existing_df_2d.plot(kind="scatter", x="PC2", y="PC1", c=existing_df_2d.cluster.astype(np.float), figsize=(16, 8))   # NOQA
