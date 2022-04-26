import pandas as pd
import numpy as np
from matplotlib.pylab import rcParams
rcParams['figure.figsize']=20,10
import matplotlib.pyplot as plt
import datetime as dt
import pandas_datareader as web
from keras.models import Sequential
from keras.layers import LSTM,Dropout,Dense
from sklearn.preprocessing import MinMaxScaler


company = 'FB'
#Date from which we are collecting the data (year, month, date)
start = dt.datetime(2012,1,1)
end = dt.datetime(2021,1,1)
df = web.DataReader(company, 'yahoo', start, end)

df = [company]['Close']
all_weekdays = pd.date_range(start=start, end=end, freq='B')
df = df.reindex(all_weekdays)
df = df.fillna(method='ffill')

df["Date"]=pd.to_datetime(df.Date,format="%Y-%m-%d")
df.index=df['Date']

plt.figure(figsize=(16,8))
plt.plot(df["Close"],label='Close Price history')
plt.show()
