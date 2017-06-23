install.packages("RCurl")

library(RCurl)

existing_cases_file <- getURL("https://docs.google.com/spreadsheets/d/1X5Jp7Q8pTs3KLJ5JBWKhncVACGsg5v4xu6badNs4C7I/pub?gid=0&output=csv")

existing_df <- read.csv(text = existing_cases_file, row.names=1, stringsAsFactor=F)

str(existing_df)
