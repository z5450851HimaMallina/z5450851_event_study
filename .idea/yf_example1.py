import yfinance                                           # (1)
tic = "QAN.AX"                                            # (2)
start = '2020-01-01'                                      # (3)
end = None                                                # (4)
df = yfinance.download(tic, start, end, ignore_tz=True)   # (5)
print(df)                                                 # (6)
df.to_csv('qan_stk_prc.csv')

import os

# Define the root project directory
PRJDIR = os.path.join(os.path.expanduser('~'), 'PycharmProjects', 'toolkit')
ROOTDIR = os.path.join(PRJDIR, 'project1')
DATDIR = os.path.join(ROOTDIR, 'data')
TICPATH = os.path.join(ROOTDIR, 'TICKERS.txt')

def get_tics(pth):
    formatted_tickers = []

    with open(pth, 'r') as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if '=' in line:
                exchange, ticker = line.split('=')

                # Format exchange and ticker
                exchange = ''.join(filter(str.isalpha, exchange)).lower()
                ticker = ''.join(filter(str.isalpha, ticker)).lower()

                # Add to dictionary if neither is empty
                if exchange and ticker:
                    formatted_tickers.append((ticker, exchange))

    return formatted_tickers

pth = TICPATH

# Check if the script is being run directly
if __name__ == "__main__":
    tics = get_tics(pth)
    print(tics)

