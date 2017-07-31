# * Delimited Files
import csv
import os
path = f'{os.getcwd()}/my-code/09-getting-data/02-reading-files'

#   - You will often deal with items that have different data on the same line
#   separated by tabs, commas and other delimiters
#   - Use csv or pandas library
#   - Always work in binary mode with csv's by attaching 'b' to 'r' or 'w'
#   for example 'wb' or 'rb'

#   - If your file has no headers you can use -> csv.reader to split each line
#   into separate lists

"""
Example delimited txt file.

stock_prices.txt

6/20/2014 AAPL 90.91
6/20/2014 MSFT 41.68
6/20/2014 FB 64.5
6/19/2014 AAPL 91.86
6/19/2014 MSFT 41.51
6/19/2014 FB 64.34
"""


def process(date, symbol, price):
    print(date, symbol, price)


# TODO: each row is being parsed as a string, so not being split at comma
with open(f'{path}/stock-prices-comma.txt', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        process(date, symbol, closing_price)


with open(f'{path}/stock-prices-colon.txt', 'r') as f:
    reader = csv.DictReader(f, delimiter=':')
    for row in reader:
        date = row["date"]
        symbol = row["symbol"]
        closing_price = float(row["closing_price"])
        process(date, symbol, closing_price)

# write out delimited data using csv.writer
today_prices = {
    'AAPL': 90.91,
    'MSFT': 41.68,
    'FB': 64.5
}

with open(f'{path}/stock-prices-colon-write.txt', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    for stock, price in today_prices.items():
        writer.writerow([stock, price])
