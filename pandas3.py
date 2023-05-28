import pandas
from pandas_datareader import data as pdr
import yfinance as yfin


yfin.pdr_override()

spy = pdr.get_data_yahoo('SPY', start='2022-10-24', end='2022-12-23')

print(spy)