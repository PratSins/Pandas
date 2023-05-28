import numpy as np
import pandas as pd

#used to grab the stock prices, with yahoo

# import pandas_datareader.data as web

from datetime import datetime
from pandas_datareader import data as pdr
import yfinance as yfin

#to visualize the results
import matplotlib.pyplot as plt
import seaborn
yfin.pdr_override()

start = datetime(2017, 1, 1)
end = datetime(2022,12,23)
symbols_list = ['AAPL', 'F', 'AAL', 'AMZN', 'GOOGL', 'GE']

#array to store prices
symbols=[]

#pull price using iex for each symbol in list defined above
for ticker in symbols_list: 
    r = pdr.get_data_yahoo(ticker, start, end)
    # add a symbol column
    r['Symbol'] = ticker 
    symbols.append(r)

# concatenate into df
df = pd.concat(symbols)
df = df.reset_index()
df = df[['Date', 'Close', 'Symbol']]
print(df)
print()
print()

# df_pivot = df.pivot('Date','Symbol','Close').reset_index() # deprecated
df_pivot = pd.pivot_table(df, values='Close', index='Date', columns='Symbol')
print(df_pivot.head())


corr_df = df_pivot.corr(method='pearson')
#reset symbol as index (rather than 0-X)
corr_df.head().reset_index()
# del corr_df.index.name
print()
print(corr_df.head(10))

print()
print()

#take the bottom triangle since it repeats itself
mask = np.zeros_like(corr_df)
mask[np.triu_indices_from(mask)] = True
#generate plot
seaborn.heatmap(corr_df, cmap='RdYlGn', vmax=1.0, vmin=-1.0 , mask = mask, linewidths=2.5)
plt.yticks(rotation=0) 
plt.xticks(rotation=90) 
plt.show()