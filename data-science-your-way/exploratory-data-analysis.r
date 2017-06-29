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
