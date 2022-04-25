#import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.io
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 20,10
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM

# Range from which data will be taken:
# Analyzing data from 2020 and predicting 2021 results...
start_date = "2017-01-01"
end_date = "2017-12-31"
pred_date = "2018-12-26"  # Date for a stock (stock market is about 250 days/year of information)
# pred_date = "2023-05-26" # Date for crypto (Crypto is 365 days/year of information)

# Analyzing data from 2021 and predicting 2022 results...
# start_date = "2020-01-01"
# end_date = "2020-12-31"
# pred_date = "2021-12-26"  # Date for a stock (stock market is about 250 days/year of information)
# pred_date = "Put 2021 date here..." # Date for crypto (Crypto is 365 days/year of information)


# Analyzing data from 2021 and predicting 2022 results...
# start_date = "2021-01-01"
# end_date = "2021-12-31"
# pred_date = "2022-12-19"  # Date for a stock (stock market is about 250 days/year of information)
# pred_date = "2023-05-26" # Date for crypto (Crypto is 365 days/year of information)

# To test how well the program works, I will analyze all of the stocks in DOW
dow_stocks = "AXP AMGN AAPL BA CAT CSCO CVX GS HD HON IBM INTC JNJ KO JPM MCD MMM MRK MSFT NKE PG TRV UNH CRM " \
             "VZ V WBA WMT DIS"
comp_stocks = dow_stocks + " VOO"
sp500 = "VOO"

print("\n[------------------- Downloading all stock data from yfinance -------------------]\n")
# Downloading the data from yfinance
data = yf.download(tickers=comp_stocks, group_by="ticker", start=start_date,
                   end=end_date)

# real_data = yf.download(tickers=comp_stocks, group_by="ticker", start=pred_date,
#                    end="2018-12-30")

def stock_info (ticker, data, info):
    np_data = data[ticker][info]
    return np_data
ticker = "AAPL"

df = data[ticker]['Close']
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')
df = df.reindex(all_weekdays)
df = df.fillna(method='ffill')

# df = stock_info(ticker, data, "Open")
#
# print(type(df))
# df_date = data["Date"]
#
# setting index as date
#df['Date'] = pd.to_datetime(df.Date,format='%Y-%m-%d')
#df.index = df['Date']

# print(df_date)

#plot
plt.figure(figsize=(16,8))
plt.plot(df, label='Close Price history')

#creating dataframe
data = df.sort_index(ascending=True, axis=0)
new_data = pd.DataFrame(index=range(0,len(df)),columns=['Date', 'Close'])
for i in range(0,len(data)):
    new_data['Date'][i] = all_weekdays[i]
    new_data['Close'][i] = df[i]

#setting index
new_data.index = new_data.Date
new_data.drop('Date', axis=1, inplace=True)

#creating train and test sets
dataset = new_data.values

train = dataset[0:987,:]
valid = dataset[987:,:]

#converting dataset into x_train and y_train
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(dataset)

x_train, y_train = [], []
for i in range(60,len(train)):
    x_train.append(scaled_data[i-60:i,0])
    y_train.append(scaled_data[i,0])
x_train, y_train = np.array(x_train), np.array(y_train)

x_train = np.reshape(x_train, (x_train.shape[0],x_train.shape[1],1))

# create and fit the LSTM network
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1],1)))
model.add(LSTM(units=50))
model.add(Dense(1))

model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(x_train, y_train, epochs=1, batch_size=1, verbose=2)

#predicting 246 values, using past 60 from the train data
inputs = new_data[len(new_data) - len(valid) - 60:].values
inputs = inputs.reshape(-1,1)
inputs  = scaler.transform(inputs)

X_test = []
for i in range(60,inputs.shape[0]):
    X_test.append(inputs[i-60:i,0])
X_test = np.array(X_test)

X_test = np.reshape(X_test, (X_test.shape[0],X_test.shape[1],1))
closing_price = model.predict(X_test)
closing_price = scaler.inverse_transform(closing_price)

plt.show()