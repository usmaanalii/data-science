# 1. DOWNLOADING FILES AND READING CSV

install.packages("RCurl")
install.packages("lintr")

# Used to get around the https issues with using URL's in read.csv
library(RCurl)

existing_cases_file <- getURL("https://docs.google.com/spreadsheets/d/1X5Jp7Q8pTs3KLJ5JBWKhncVACGsg5v4xu6badNs4C7I/pub?gid=0&output=csv") # nolint

existing_df <- read.csv(text = existing_cases_file,
                        row.names = 1, stringsAsFactor = F)

# str
# Gives information about a variable type
str(existing_df)

# Convert the column names and assign them to its reference in the dataframe *
existing_df[c(1, 2, 3, 4, 5, 6, 15, 16, 17, 18)] <-
    lapply(existing_df[c(1, 2, 3, 4, 5, 6, 15, 16, 17, 18)],
    function(x) {
        as.integer(gsub(",", "", x))
        })
str(existing_df)

# Explore the data
head(existing_df, 3)
nrow(existing_df) # 207 observations (1 for each country)
ncol(existing_df) # 18 variables/features (1 for each year)

# Transpose the data and convert it back to a dataframe
#
# NOTE: transposing will result in a matrix, therefore as.data.frame is used to convert it back

# saving the "transposed" original version for later use (if needed)
existing_df_transposed <- existing_df
existing_df <- as.data.frame(t(existing_df))

head(existing_df, 3)

# rownames is the equivalent of index in pandas
#
# NOTE: - These started as column names (in the transposed original version)
#       - From the definition of a data.frame in R, each column is a vector
#       with a variable name
#       - Columns names can't begin with a digit, so R prefixes them with X
rownames(existing_df) # X1990 X1991 etc...

# colnames are the same as .columns in pandas
colnames(existing_df)

# 2. DATA INDEXING

# Row number is left blank, so it fetches all rows for the first column
#
# NOTE: R has a 1-based indexing schema
existing_df[, 1]

# Using column names via $ (label accessing within a list)
existing_df$Afghanistan

# Since a data.frame is a list of elements, we can access columns as list elements via [[]]
existing_df[[1]]

# NOTE: Unlike Python, R has many ways od foing things, below are recommendations for whcih to use

# Row indexing
existing_df[1, ] # 1990 data for every country

existing_df[1, 1] # First column for 1990
existing_df$Afghanistan[1] # Afghanistan column for 1990
existing_df[[1]][1]

# NOTE: Columns are vectors, the previous examples are accessing the first element of these vectors

# Selecting multiple columns and/or rows by bassing R vectors
existing_df[c(3, 9, 16), c(170, 194)] # vectors
existing_df["X1992", "Spain"] # names

# Combined vectors and names
existing_df[c("X1992", "X1998", "X2005"), c("Spain", "United Kingdom")]

# 3. DATA SELECTION
#    How to select data from dataframes based on their values via logical
#    expressions

# This returns a matrix variable with boolean values
existing_df_gt10 <- existing_df > 10
existing_df_gt10

# When applied to individual columns, the result can be used for indexing
# like in pandas
existing_df["United Kingdom"] > 10
existing_df$Spain[existing_df["United Kingdom"] > 10]

# Use the whole boolean matrix (from before)
existing_df[existing_df_gt10]
# NOTE: - the result is a long vector of values
#       - So, index both dimensions (row/columns separately)

# Use matrix indexing with a data frame to replace elements
existing_df_2 <- existing_df
existing_df_2[existing_df_gt10] <- -1
head(existing_df_2)

# The most expressing way of selecting from a data.frame is by subset()
# NOTE: subset
#       - Applied by row in the data frame
#       - Can take conditions using column names
#       - Can take a list of columns

# Example: Select years when the UK had 10+ cases, return rows for UK, Spain
#          and Colombia

# If a column name contains blanks, we use ` `
subset(existing_df, `United Kingdom` > 10, c("United Kingdom", "Spain", "Colombia")) # nolint
# NOTE: the condition uses backticks

# 3. FUNCTION MAPPING AND DATA GROUPING

# lapply
existing_df_sum_countries <- lapply(existing_df, function(x) { sum(x) }) # nolint
existing_df_sum_countries <- as.data.frame(existing_df_sum_countries)
existing_df_sum_countries

# NOTE: lapply takes a list and function (applied to each element) returning
#       a list

# sum by year, for every country
existing_df_sum_years <- lapply(existing_df_transposed, function(x) { sum(x) }) # nolint
existing_df_sum_years <- as.data.frame(existing_df_sum_years)
existing_df_sum_years

# aggregate

# 1. Define a grouping vector
before_2000 <- c("1990-99", "1990-99", "1990-99", "1990-99", "1990-99", "1990-99", "1990-99", "1990-99", "1990-99", "1990-99", "2000-07", "2000-07", "2000-07", "2000-07", "2000-07", "2000-07", "2000-07", "2000-07") # nolint
before_2000

# 2. Use that column as a grouping element ans use the mean function
mean_cases_by_period <- aggregate(existing_df, list(Period = before_2000), mean)
mean_cases_by_period

# NOTE: allows subsetting the dataframe, passing grouping elements and functions

# Can be indexed as usual
mean_cases_by_period[, c("United Kingdom", "Spain", "Colombia")]
