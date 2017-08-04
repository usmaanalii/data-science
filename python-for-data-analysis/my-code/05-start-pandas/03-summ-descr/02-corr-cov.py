# * Correlation and Covariance
import pandas as pd
import numpy as np
import pandas_datareader as web
from pandas import Series
from pandas import DataFrame

# %% Yahoo Finance DF's - stock prices and volumes
all_data = {}
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2000', '1/1/2010')

price = DataFrame({tic: data['Adj Close']
                   for tic, data in all_data.items()})

volume = DataFrame({tic: data['Volume']
                   for tic, data in all_data.items()})

returns = price.pct_change()

returns.tail()

# *corr* -> computes the correlation of the overlapping, non NA aligned by
#           index values in two Series
returns.MSFT.corr(returns.IBM)

# *cov* -> computes the covariance of the overlapping, non NA aligned by
#           index values in two Series
returns.MSFT.cov(returns.IBM)

# DF's corr/cov return matrices of values
returns.corr()

returns.cov()

# *corrwith* -> pairwise correlations between DF cols/rows w/ another S or DF
returns.corrwith(returns.IBM)

# Passing a DF computes correlations of matching column names
#   - percent change with volume
returns.corrwith(volume)

