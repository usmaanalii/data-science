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
