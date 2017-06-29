# 1. DOWNLOADING FILES AND READING CSV
Sys.setenv(LANG = "en")
install.packages("RCurl")
install.packages("lintr")

install.packages("dplyr")
library(dplyr)

# Used to get around the https issues with using URL's in read.csv
library(RCurl)

existing_cases_file <- getURL("https://docs.google.com/spreadsheets/d/1X5Jp7Q8pTs3KLJ5JBWKhncVACGsg5v4xu6badNs4C7I/pub?gid=0&output=csv") # nolint

existing_df <- read.csv(text = existing_cases_file, row.names = 1, stringsAsFactor = F) #nolint
existing_df_transposed <- existing_df
existing_df <- as.data.frame(t(existing_df))

# 2. QUESTIONS WE WENT TO ANSWER

#     1. Which are the countries with the highest and infectious TB incidence?
#     2. What is the general world tendency from 1990-2007
#     3. What countries don't follow the tendency
#     4. What other facts about the disease do we know that we can track
#        with the data

# 3. DESCRIPTIVE STATISTICS

# summary() - basic descriptive statistics method in R
existing_summary <- summary(existing_df)
str(existing_summary)

# Returns a table object, with summary stats for each column.
# This isn't good for accessing/indexing

# It's best to access it as a matrix and use positional indexing
existing_summary[, 1]

# which() - Used to access by column name
data.frame(Spain = existing_summary[,which(colnames(existing_df)=='Spain')], UK = existing_summary[,which(colnames(existing_df)=='United Kingdom')]) # nolint

# 4. PLOTTING
#    Many data types have cusotm plot() methods

# Basic line chart
uk_series <- existing_df_[, c("United Kingdom")]
spain_series <- existing_df[, c("Spain")]
colombia_series <- existing_df[, c("Colombia")]

uk_series

xrange <- 1990:2007

plot(xrange, uk_series, type = "1", xlab = "Year", ylab = "Existing cases per 100k", col = "blue", ylim = c(0, 100)) # nolint
lines(xrange, spain_series, col = "darkgreen")
lines(xrange, uk_series, col = "red")
legend(x = 2003, y = 100, lty = 1, col = c("blue", "darkgreen", "red"), legend = c("UK", "Spain", "Colombia")) # nolint

boxplot(uk_series, spain_series, colombia_series, names = c("UK", "Spain", "Colombia"), xlab = "Year", ylab = "Existing cases per 100K") # nolint

lapply(existing_df, class)

# 5. ANSWERING QUESTIONS

# which.max() - gets the maxiumum values position
# lapply() or sapply() - can apply this ^ to every year column
country_names <- rownames(existing_df_transposed)
sapply(existing_df_transposed, function(x) {country_names[which.max(x)]}) # nolint

# world trends in TB cases
deaths_file <- getURL("https://docs.google.com/spreadsheets/d/12uWVH_IlmzJX_75bJ3IH5E-Gqx6-zfbDKNvZqYjUuso/pub?gid=0&output=CSV") # nolint
new_cases_file <- getURL("https://docs.google.com/spreadsheets/d/1Pl51PcEGlO9Hp4Uh0x2_QM0xVb53p2UDBMPwcnSjFTk/pub?gid=0&output=csv") # nolint

deaths_df <- read.csv(text = deaths_file, row.names = 1, stringsAsFactor = F)
new_df <- read.csv(text = new_cases_file, row.names = 1, stringsAsFactor = F)

# Cast data to int (death doesn't need it)
new_df[1:18] <- lapply(new_df[1:18], function(x) {as.integer(gsub(',', '', x))}) # nolint
new_df[1:18]

# Transpose
deaths_df_transposed <- deaths_df
deaths_df <- as.data.frame(t(deaths_df))
new_df_transposed <- new_df
new_df <- as.data.frame(t(new_df))

# sums by row, convert returned vector to data frame
deaths_total_per_year_df <- data.frame(total = rowSums(deaths_df))
existing_total_per_year_df <- data.frame(total = rowSums(existing_df))

new_total_per_year_df <- data.frame(total = rowSums(new_df, na.rm = TRUE))

deaths_total_per_year_df
new_total_per_year_df

# Plot each line, use R data frame indexing by column name for a vector
xrange <- 1990:2007
plot(xrange, deaths_total_per_year_df$total, type = "l", xlab = "Year", ylab = "Count per 100K", col = "blue", ylim = c(0, 5000))  # nolint
lines(xrange, new_total_per_year_df$total, col = "red")
legend(x = 1992, y = 52000, lty = 1, cex = 0.7, ncol = 3, col = c("blue, red"), legend = c("Deaths", "New cases"))  # nolint

# countries out of tendency
deaths_by_country_mean <- data.frame(mean = colMeans(deaths_df))
existing_by_country_mean <- data.frame(mean = colMeans(existing_df))
new_by_country_mean <- data.frame(mean = colMeans(new_df, na.rm = TRUE))

barplot(sort(deaths_by_country_mean$mean))

# quantile outliers
new_super_outlier <- quantile(new_by_country_mean$mean, probs = c(0.5)) * 5.0
super_outlier_countries_by_new_index <- new_by_country_mean > new_super_outlier  # nolint

# proportion
sum(super_outlier_countries_by_new_index) / 208  # nolint

# data fame of outliers
super_outlier_new_df <- new_df[, super_outlier_countries_by_new_index]  # nolint

# plot
xrange <- 1990:2007
plot(xrange, super_outlier_new_df[,1], type = "l", xlab = "Year", ylab = "New cases per 100K", col = 1, ylim = c(0,1800))  # nolint

for (i in seq(2:ncol(super_outlier_new_df))) {lines(xrange, super_outlier_new_df[, i], col = i)}  # nolint

legend(x = 1990, y = 1800, lty = 1, cex  =  0.5, ncol = 7, col = 1:22, legend = colnames(super_outlier_new_df))  # nolint

# country to represent outliers
average_countries_df <- data.frame(averageOutlierMean = rowMeans(super_outlier_new_df, na.rm = T))  # nolint
average_countries_df

# country for rest of world
average_countries_df$averageBetterWorldMean <- rowMeans(new_df[, - super_outlier_countries_by_new_index], na.rm = T)  # nolint
average_countries_df

# plot
xrange <- 1990:2007
plot(xrange, average_countries_df$averageOutlierMean, type = "l", xlab = "Year", ylab = "New cases per 100K", col = "darkgreen", ylim = c(0, 600))
lines(xrange, average_countries_df$averageBetterWorldMean, col = "blue")
legend(x = 1990, y = 600, lty = 1, cex = 0.7, ncol = 2, col = c("darkgreen", "blue"), legend = c("Average outlier country", "Average World Country"))
