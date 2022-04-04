import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from stock_analysis import *

# Range from which data will be taken:
# Analyzing data from 2020 and predicting 2021 results...
start_date = "2019-01-01"
end_date = "2019-12-31"
pred_date = "2020-12-26"  # Date for a stock (stock market is about 250 days/year of information)
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

# To test the how well the program works, I will analyze all of the stocks in DOW
dow_stocks = "AXP AMGN AAPL BA CAT CSCO CVX GS HD HON IBM INTC JNJ KO JPM MCD MMM MRK MSFT NKE PG TRV UNH CRM " \
             "VZ V WBA WMT DIS DOW"
comp_stocks = dow_stocks + " VOO"
sp500 = "VOO"

print("\n[------------------- Downloading all stock data from yfinance -------------------]\n")
# Downloading the data from yfinance
data = yf.download(tickers=comp_stocks, group_by="ticker", start=start_date,
                   end=end_date)

real_data = yf.download(tickers=comp_stocks, group_by="ticker", start=pred_date,
                   end="2020-12-30")

analysis_results = []
stock_initial_prices = []
num_simulations = 50000
print("\nStarting Monte Carlo simulation all the stocks in the DOW. Number of simulations: {}".format(num_simulations))
for ticker in comp_stocks.split():
    analysis_results.append(analysis(ticker, data, num_simulations))
    stock_initial_prices.append(initial_price(ticker, data))
print("\n[------------------- Monte Carlo simulation of all stocks completed successfully -------------------]")

# analysis_results = [So, S, stock_ticker_symbol]

threshold = 1.2
confidence = []
for ticker in analysis_results:
    confidence.append(stock_prob(ticker[0], ticker[1], ticker[2], threshold, num_simulations))

# confidence = [prob]

confidence_level = 0.6
suggestions = []
i = 0
for ticker in analysis_results:
    suggestions.append(buy_stock(ticker[2], confidence[i], confidence_level))
    i += 1

# suggestions = [ticker_symbol, True/False] # True if we should buy the stock and False if we should not

# print("Here are the probabilities of the stocks:")
# print(confidence)

# print("\nHere are the suggestions: ")
# print(suggestions)

real_results = []
for ticker in comp_stocks.split():
    np_real_data = real_data[ticker]["Close"].to_numpy()
    real_results.append([ticker, np_real_data[-1]])

# real_results = [ticker_symbol, actual_stock_price]

predicted_correctly = 0
predicted_incorrectly = 0
num_predictions = 0

for num in range(0,len(real_results)):
    if real_results[num][0] == suggestions[num][0]:
        if real_results[num][1] > 1.2*stock_initial_prices[num] and suggestions[num][1] == "Buy":
            predicted_correctly += 1
            num_predictions += 1
            print("\nTicker Symbol:{}\tSuggestion:{}\t20% Gain Price:{}\tReal Price:{}\tDecision: {}".format(suggestions[num][0],
                                                                                                   suggestions[num][1],
                                                                                                   1.2 *
                                                                                                   stock_initial_prices[
                                                                                                       num],
                                                                                                   real_results[num][1],
                                                                                                    "Predicted Correctly 1st Step"))
        elif real_results[num][1] < 1.2*stock_initial_prices[num] and suggestions[num][1] == "Next stock":
            predicted_correctly += 1
            num_predictions += 1
            print("\nTicker Symbol:{}\tSuggestion:{}\t20% Gain Price:{}\tReal Price:{}\tDecision: {}".format(
                suggestions[num][0],
                suggestions[num][1],
                1.2 *
                stock_initial_prices[
                    num],
                real_results[num][1],
                "Predicted Correctly 2nd Step"))
        else:
            predicted_incorrectly += 1
            num_predictions += 1
            print("\nTicker Symbol:{}\tSuggestion:{}\t20% Gain Price:{}\tReal Price:{}\tDecision: {}".format(
                suggestions[num][0],
                suggestions[num][1],
                1.2 *
                stock_initial_prices[
                    num],
                real_results[num][1],
                "Predicted INCorrectly"))
    else:
        print("Ticker symbols of stocks are not matching...")

print("\nNumber of correct predictions: {}".format(predicted_correctly))
print("Percent of correct predictions: {}%".format(round(100*predicted_correctly/num_predictions), 2))

print("\nNumber of INcorrect predictions: {}".format(predicted_incorrectly))
print("Percent of INcorrect predictions: {}%".format(round(100*predicted_incorrectly/num_predictions), 2))

print("\nNumber of predictions: {}".format(num_predictions))


