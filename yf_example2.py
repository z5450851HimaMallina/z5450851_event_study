"""
yf_example2.py
Example of a function to download stock prices from Yahoo Finance.
"""
import yfinance as yf

def yf_prc_to_csv(tic, pth, start=None, end=None):
    """
    Downloads stock prices from Yahoo Finance and saves the information in a CSV file.

    Parameters
    ----------
    tic : str
        Ticker
    pth : str
        Location of the output CSV file
    start : str, optional
        Download start date string (YYYY-MM-DD)
        If None (the default), start is set to '1900-01-01'
    end : str, optional
        Download end date string (YYYY-MM-DD)
        If None (the default), end is set to the most current date available
    """
    # Download data from Yahoo Finance
    df = yf.download(tic, start=start, end=end, ignore_tz = True)

    # Save to CSV file
    df.to_csv(pth)


if __name__ == "__main__":
    tic = 'QAN.AX'
    start = '2020-01-01'
    end = '2021-01-01'
    pth = 'qan_stk_prc.csv'
    yf_prc_to_csv(tic, start, end)
    print("yf_example2 bottom line")

    # Example
    if __name__ == '__main__':
        tic = 'QAN.AX'
        pth = 'qan_stk_prc.csv'
        yf_prc_to_csv(tic, pth)
        print('yf_example2 inside if statement')

    pth ='/Users/rohini/PycharmProjects/toolkit/.idea/data/test.csv'
    print(pth)

if __name__ == "__main__":
    import os
    tic = 'QAN.AX'
    datadir = r'C:\Users\wh520\PycharmProjects\toolkit\data'
    # pth = f'{datadir}\\test.csv'
    pth = os.path.join(datadir, 'qan_stk_prc.csv')
    print(pth)

import yfinance as yf

def yf_prc_to_csv(ticker, start_date, end_date, output_file):
    """Download stock price data and save to a CSV file."""
    data = yf.download(ticker, start=start_date, end=end_date)
    if data.empty:
        print(f"Failed to download data for {ticker}")
    else:
        data.to_csv(output_file)

