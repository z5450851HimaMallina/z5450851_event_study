import pandas as pd

# Part (a)
# Create a pandas series called series_abc with
# index ['a', 'b', 'c'] and values [1, 2, 3]
series_abc = {'a':1, 'b':2, 'c':3}

# Part (b)
# Given the stock price-date dictionary prc_date
# listed below, create a pandas series series_stk
# with the dates as indices and the prices as values.
prc_date = {
    7.1600: '2020-01-02',
    7.1900: '2020-01-03',
    7.0000: '2020-01-06',
    7.1000: '2020-01-07',
    6.8600: '2020-01-08',
    6.9500: '2020-01-09',
    7.0000: '2020-01-10',
    7.0200: '2020-01-13',
    7.1100: '2020-01-14',
    7.0400: '2020-01-15',
    }
series_stk = pd.Series(values,keys)

# Part c
# Given the dictionary
dic = {i:i+1 for i in range(10000)}
# create a Pandas series called series_ones
# with indices from 0 through 9999 and with
# all values equal to 1.
# Do not use a secondary dictionary to create the series in Pandas.
# Instead, specify the data and index arguments directly.
series_ones = pd.Series(data=?, index=?)

