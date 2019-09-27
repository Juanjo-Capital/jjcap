import alpaca_trade_api as tradeapi
import yfinance as yf
import matplotlib.pyplot as plt

file = open('finalTechCompanies.txt','r')
stockUniverse = []
for line in file:
    if len(line)>1: #not take into account new line
        stockUniverse.append(line)
        
print("The universe has " + len(stockUniverse)+ " stocks")
'''''
api = tradeapi.REST('PKA6QH67TAYND80CYCT5', '8al2ZjAW2Jn9SXSLFxLSrn780WGbch2YOdCY2RWZ', 'https://paper-api.alpaca.markets', api_version='v2') # or use ENV Vars shown below
# Format the allStocks variable for use in the class.
allStocks = []
for stock in stockUniverse:
  allStocks.append([stock, 0])

positions = self.alpaca.list_positions()
print(allStocks)
'''
data = yf.download('AAPL', '2017-01-01', '2019-09-27')
data.Close.plot()
plt.show()
print(data)