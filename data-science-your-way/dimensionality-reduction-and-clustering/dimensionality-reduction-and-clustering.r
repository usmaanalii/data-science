# nolint start
# 1. DOWNLOADING FILES AND READING CSV
Sys.setenv(LANG = "en")
library(RCurl)
library(scales)
install.packages("lintr")

# Get and process existing cases file
existing_cases_file <- getURL("https://docs.google.com/spreadsheets/d/1X5Jp7Q8pTs3KLJ5JBWKhncVACGsg5v4xu6badNs4C7I/pub?gid=0&output=csv")
existing_df <- read.csv(text = existing_cases_file, row.names=1, stringsAsFactor=F)

existing_df[c(1, 2, 3, 4, 5, 6, 15, 16, 17, 18)] <- lapply(existing_df[c(1, 2, 3, 4, 5, 6, 15, 16, 17, 18)], function(x) {as.integer(gsub(",", "", x))})

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
plot(PC1~PC2, data = scores_existing_df, main = "Existing TB cases per 100K distribution", cex = 0.1, lty = "solid")
text(PC1~PC2, data = scores_existing_df, labels = rownames(existing_df), cex = 0.8)

# Set the color associated with the mean value for all the years
# Use rgb, ramp and rescale to create a color palette (yellow to blue)
ramp <- colorRamp(c("yellow", "blue"))

# associate colour by mean
colours_by_mean <- rgb(ramp(as.vector(rescale(rowMeans(existing_df), c(0, 1)))), max = 255)
plot(PC1~PC2, data = scores_existing_df, main = "Existing TB cases per 100K distribution", cex = 0.1, lty = "solid", col = colours_by_mean)
text(PC1~PC2, data = scores_existing_df, labels = rownames(existing_df), cex = 0.8, col = colours_by_mean)

# associate colour by sum
colours_by_sum <- rgb(ramp(as.vector(rescale(rowSums(existing_df), c(0, 1)))), max = 255)
plot(PC1~PC2, data = scores_existing_df, main = "Existing TB cases per 100K distribution", cex = 0.1, lty = "solid", col = colours_by_sum)
text(PC1~PC2, data = scores_existing_df, labels = rownames(existing_df), cex = 0.8, col = colours_by_sum)

existing_df_change <- existing_df$X2007 - existing_df$X1990
colours_by_change <- rgb(ramp(as.vector(rescale(existing_df_change,c(0,1)))), max = 255)
plot(PC1~PC2, data = scores_existing_df, main = "Existing TB cases per 100K distribution", cex = 0.1, lty = "solid", col = colours_by_change)
text(PC1~PC2, data = scores_existing_df, labels = rownames(existing_df), cex = 0.8, col = colours_by_change)
# nolint end
