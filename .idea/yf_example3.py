""" Module Name - yf_example3.py
 This modeule dowloads the financial data of Quantas for the year 2020 """
data_folder = "/Users/rohini/PycharmProjects/toolkit/data"

import os
import toolkit_config as cfg
import yf_example2


def qan_prc_to_csv(year):
    tic = 'QAN.AX'
    start = f'{year}-01-01'
    end = f'{year}-12-31'
    pth = os.path.join(cfg.DATADIR,f'qan_prc_{year}.csv')
    yf_example2.yf_prc_to_csv(tic = tic, start=start,end=end,pth=pth)


if __name__ == "_main_":
    year = 2020
    qan_prc_to_csv(year)