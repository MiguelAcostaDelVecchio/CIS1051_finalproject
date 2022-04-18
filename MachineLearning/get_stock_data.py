import pandas as pd
import yfinance as yf
import datetime
import time
import requests
import io

start = datetime.datetime(2020,2,1)
end = datetime.datetime(2020,10,11)

url="https://pkgstore.datahub.io/core/nasdaq-listings/nasdaq-listed_csv/data/7665719fb51081ba0bd834fde71ce822/nasdaq-listed_csv.csv"
s = requests.get(url).content
companies = pd.read_csv(io.StringIO(s.decode('utf-8')))

#Symbols = companies['Symbol'].tolist()
Symbols = companies['Symbol'][0]

# create empty dataframe
stock_final = pd.DataFrame()
# iterate over each symbol
for i in Symbols:

    # print the symbol which is being downloaded
    print(str(Symbols.index(i)) + str(' : ') + i, sep=',', end=',', flush=True)

    try:
        # download the stock price
        stock = []
        stock = yf.download(i, start=start, end=end, progress=False)

        # append the individual stock prices
        if len(stock) == 0:
            None
        else:
            stock['Name'] = i
            stock_final = stock_final.append(stock, sort=False)
    except Exception:
        None

stock_final.head()