# Parameter Definitions

# So    :   initial stock price
# dt    :   time increment -> a day in our case
# T     :   length of the prediction time horizon(how many time points to predict, same unit with dt(days))
# N     :   number of time points in the prediction time horizon -> T/dt
# t     :   array for time points in the prediction time horizon [1, 2, 3, .. , N]
# mu    :   mean of historical daily returns
# sigma :   standard deviation of historical daily returns
# b     :   array for brownian increments
# W     :   array for brownian path

# Formula -> dS = So * ((mu * dt) + (sigma * random_num * sqrt(dt)))

import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Range from which data will be taken
start_date = "2020-01-01"
end_date = "2020-12-31"
pred_date = "2021-12-20"

# ETFs that track the S&P500 include: VOO, IVV, and SPLG
stock = input("Please input stock to analyze: ").upper()
comp_stocks = stock + " VOO"
sp500 = "VOO"

# Downloading the data from yfinance
data = yf.download(tickers=comp_stocks, group_by="ticker", start=start_date,
                   end=end_date)

# Plotting the stock data
stock_close = data[stock]['Close']
ax = stock_close.plot(title='Comparison between {} and {}'.format(stock, sp500), label=stock)
ax.set_xlabel('Date')
ax.set_ylabel('Close')

# Plotting the ETF data
sp500_close = data[sp500]["Close"]
ax1 = sp500_close.plot(label=sp500)
ax1.grid()

# Show plot
plt.legend()
# plt.show()

# [----------------- Evaluate needed parameters for Monte Carlo Simulation ------------]
# Evaluate So
np_data = data[stock]["Close"].to_numpy()
So = np_data[-1]
# print(So)

# Evaluate dt
dt = 1

# Evaluate T
T = len(np_data)
# print(T)

# Evaluate N
N = T/dt
# print(N)

# Evaluate t
t = np.arange(1,int(N)+1)
# print(t)

# Evaluate mu
returns = []
for ele in range(0,len(t)):
    if ele == 0:
        returns.append((np_data[ele] - np_data[ele - 1]) / (np_data[-1]*100))
    else:
        returns.append((np_data[ele] - np_data[ele - 1]) / np_data[-1])
# print(returns)
mu = np.mean(returns)
# print(mu)

# Evaluate Sigma
sigma = np.std(returns)
# print(sigma)

# Evaluate b
num_simulations = 50
b = {str(num): np.random.normal(0, 1, int(N)) for num in range(1, num_simulations + 1)}
# print(b)

# Evaluate W
W = {str(num): b[str(num)].cumsum() for num in range(1, num_simulations + 1)}
# print(W)

# Evaluating drift and diffusion
drift = (mu - 0.5 * sigma**2) * t
# print("drift:\n", drift)
diffusion = {str(num): sigma * W[str(num)] for num in range(1, num_simulations + 1)}
# print("diffusion:\n", diffusion)

S = np.array([So * np.exp(drift + diffusion[str(num)]) for num in range(1, num_simulations + 1)])
S = np.hstack((np.array([[So] for num in range(num_simulations)]), S))
# print(S)

# Plotting the simulations
plt.figure(figsize=(10, 8))

for i in range(num_simulations):
    plt.title("Daily Volatility: " + str(sigma))
    plt.plot(pd.date_range(start=end_date,
                           end=pred_date, freq='D').map(lambda x:
                                                            x if x.isoweekday() in range(1, 6) else np.nan).dropna(),
             S[i, :])
    plt.ylabel('Stock Prices')
    plt.xlabel('Prediction Days')

plt.show()
