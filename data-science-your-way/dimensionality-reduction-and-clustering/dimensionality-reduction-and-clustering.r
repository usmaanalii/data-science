# 1. DOWNLOADING FILES AND READING CSV
Sys.setenv(LANG = "en")
library(RCurl)
library(scales)
install.packages("lintr")

# Get and process existing cases file
existing_cases_file <- getURL("https://docs.google.com/spreadsheets/d/1X5Jp7Q8pTs3KLJ5JBWKhncVACGsg5v4xu6badNs4C7I/pub?gid=0&output=csv") # nolint
existing_df <- read.csv(text = existing_cases_file, row.names=1, stringsAsFactor=F)

existing_df[c(1, 2, 3, 4, 5, 6, 15, 16, 17, 18)] <- lapply(existing_df[c(1, 2, 3, 4, 5, 6, 15, 16, 17, 18)], function(x) {as.integer(gsub(",", "", x))})  # nolint

head(existing_df)

# 2. DIMENSIONALITY REDUCTION WITH PCA

# Represent each country in two dimensional space
# Each sample is a country defined by 18 variables for a given year (1990-2007)
# PCA will be used to reduce these 18 to 2 that best capture the information
pca_existing <- prcomp(existing_df, scale = TRUE)

# Interested in these scores
pca_existing$x

# How much variation is explained in each variable?
plot(pca_existing)

# Most variation is explained by the first, so use the first two to represent
# all countries
scores_existing_df <- as.data.frame(pca_existing$x)

# Show first two PCs for head countries
head(scores_existing_df[1:2])

# Use with plot
plot(PC1~PC2, data = scores_existing_df, main = "Existing TB cases per 100K distribution", cex = 0.1, lty = "solid") # nolint
text(PC1~PC2, data = scores_existing_df, labels = rownames(existing_df), cex = 0.8) # nolint

# Set the color associated with the mean value for all the years
# Use rgb, ramp and rescale to create a color palette (yellow to blue)
ramp <- colorRamp(c("yellow", "blue"))

# associate colour by mean
colours_by_mean <- rgb(ramp(as.vector(rescale(rowMeans(existing_df), c(0, 1)))), max = 255) # nolint
plot(PC1~PC2, data = scores_existing_df, main = "Existing TB cases per 100K distribution", cex = 0.1, lty = "solid", col = colours_by_mean) # nolint
text(PC1~PC2, data = scores_existing_df, labels = rownames(existing_df), cex = 0.8, col = colours_by_mean) # nolint

# associate colour by sum
colours_by_sum <- rgb(ramp(as.vector(rescale(rowSums(existing_df), c(0, 1)))), max = 255) # nolint
plot(PC1~PC2, data = scores_existing_df, main = "Existing TB cases per 100K distribution", cex = 0.1, lty = "solid", col = colours_by_sum) # nolint
text(PC1~PC2, data = scores_existing_df, labels = rownames(existing_df), cex = 0.8, col = colours_by_sum) # nolint

existing_df_change <- existing_df$X2007 - existing_df$X1990
colours_by_change <- rgb(ramp(as.vector(rescale(existing_df_change, c(0, 1)))), max = 255) # nolint
plot(PC1~PC2, data = scores_existing_df, main = "Existing TB cases per 100K distribution", cex = 0.1, lty = "solid", col = colours_by_change) # nolint
text(PC1~PC2, data = scores_existing_df, labels = rownames(existing_df), cex = 0.8, col = colours_by_change) # nolint


# 3. EXPLORING DATA STRUCTURE WITH K MEANS CLUSTERING

# Group countries based on how similar their situation has been year by year
# Cluster the data based on the 18 variables we have

# Determine the right number of groups using an intuitive approach

# kmeans via elbow criterion
wss <- (nrow(existing_df) - 1) * sum(apply(existing_df, 2, var))

for (i in 2:15) {wss[i] <- sum(kmeans(existing_df, centers = i, iter.max = 1000)$withinss)} # nolint

plot(1:15, wss, type = "b", xlab = "Number of Clusters", ylab = "Within group sum of squares") # nolint

# We can see, most variance is explained with 3 clusters
# These can be categorised as countries conditions being
#   1. good
#   2. average
#   3. poor

# Result contains a list with components:
#   Cluster - Vector of integers indicating the cluster to which each point
#             is allocated
#   Centers - Matrix of cluster centres
#   Withinss - The within-cluster sum of square distances for each cluster
#   Size - Number fo points in each cluster

# Colour our previous scatter plot based on the cluster each country belongs to
set.seed(1234)
existing_clustering <- kmeans(existing_df, center = 3)
existing_cluster_groups <- existing_clustering$cluster

plot(PC1~PC2, data = scores_existing_df, main = "Existing TB Cases Per 100K Distribution", cex = 0.1, lty = "solid", col = existing_cluster_groups) # nolint
text(PC1~PC2, data = scores_existing_df, labels = rownames(existing_df), cex = 0.8, col = existing_cluster_groups)

# Most clusters are based on PC1 (Clusters are defined in terms of total Number
# of cases per 100K and not how data evolved in time (PC2))

# Try k = 4. and see if some are refined in PC2's direction
set.seed(1234)
existing_clustering <- kmeans(existing_df, center = 4)
existing_cluster_groups <- existing_clustering$cluster

plot(PC1~PC2, data = scores_existing_df, main = "Existing TB Cases Per 100K Distribution", cex = 0.1, lty = "solid", col = existing_cluster_groups) # nolint
text(PC1~PC2, data = scores_existing_df, labels = rownames(existing_df), cex = 0.8, col = existing_cluster_groups) # nolint

# Try with k = 5
set.seed(1234)
existing_clustering <- kmeans(existing_df, center = 5)
existing_cluster_groups <- existing_clustering$cluster

plot(PC1~PC2, data = scores_existing_df, main = "Existing TB Cases Per 100K Distribution", cex = 0.1, lty = "solid", col = existing_cluster_groups) # nolint
text(PC1~PC2, data = scores_existing_df, labels = rownames(existing_df), cex = 0.8, col = existing_cluster_groups) # nolint

# Cluster Interpretation

# Add a column in our data frame for cluster ID
existing_df$cluster <- existing_clustering$cluster
table(existing_df$cluster)

# Centroids comparison charts

# Create a line chart that compares the time series for each cluster centroid
# To help with better understanding cluster results
xrange <- 1990:2007
plot(xrange, existing_clustering$centers[1, ], type = "l", xlab = "Year", ylab = "New cases per 100K", col = 1, ylim = c(0, 1000)) # nolint
for (i in 2:nrow(existing_clustering$centers)) {lines(xrange, existing_clustering$centers[i, ], col = i)} # nolint
legend(x = 1990, y = 1000, lty = 1, cex = 0.5, col = 1:(nrow(existing_clustering$centers) + 1), legend = paste("Cluster", 1:nrow(existing_clustering$centers))) # nolint

# Cluster 1
# ---------

# Contains just 16 countries
rownames(subset(existing_df, cluster == 1))

# Centroid representing them - means with most TB cases every year
existing_clustering$centers[1, ]

# Cluster 2
# Larger cluster, lots of cases (less than 1). Fastest decrease in cases
# ---------

# Contains 30 countries
rownames(subset(existing_df, cluster == 2))

# Centroid representing them - means with most TB cases every year
existing_clustering$centers[2, ]

# Cluster 3
# Only cluster, where cases increased per year, overtaking 1 in 2007
# In the middle of crisis, being affected by other disease like HIV
# ---------

# Contains 20 countries
rownames(subset(existing_df, cluster == 3))

# Centroid representing them - means with most TB cases every year
existing_clustering$centers[3, ]

# Cluster 4
# Close to the last and larger one, contains american countries,
# some european etc. Some large and rich (Russia/Brazil)
# ---------

# Contains 251 countries
rownames(subset(existing_df, cluster == 4))

# Centroid representing them - means with most TB cases every year
existing_clustering$centers[4, ]

# Cluster 5
# Largest, needs further refinement
# ---------

# Contains 251 countries
rownames(subset(existing_df, cluster == 5))

# Centroid representing them - means with most TB cases every year
existing_clustering$centers[5, ]

# Plot, to see actual differences between 4/5

# subset the original dataset
cluster5_df <- subset(existing_df, cluster == 5)
# do the clustering
set.seed(1234)
cluster5_clustering <- kmeans(cluster5_df[, -19], centers = 2)
# assign sub-cluster number to the data set for Cluster 5
cluster5_df$cluster <- cluster5_clustering$cluster

xrange <- 1990:2007
plot(xrange, cluster5_clustering$centers[1, ], type = "l", xlab = "Year", ylab = "New cases per 100K", col = 1, ylim = c(0, 200)) # nolint

for (i in 2:nrow(cluster5_clustering$centers)) {lines(xrange, cluster5_clustering$centers[i, ], col = i)} # nolint

legend(x = 1990, y = 1000, lty = 1, cex = 0.5, ncol = 1:(nrow(cluster5_clustering$centers) + 1), legend = paste("Cluster 5.", 1:nrow(cluster5_clustering$centers))) # nolint
