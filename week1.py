# 1. Import a package to interact with Yahoo! Finance. No need to create a shortform like yf
# 2. Create a variable to store Qantas ticker.
# 3. Create variables to store the start and end dates. Date format : year-month-date
# 4. Issue a download command.
# 5. Issue another command to save the file

import yfinance
tic = "QAN.AX"
start = "2020-01-01"
end = None
df = yfinance.download(tic, start, end, ignore_tz=True)
print(df)
df.to_csv('qan_stk_prc.csv')







