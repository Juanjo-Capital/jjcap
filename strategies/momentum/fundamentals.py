'''
Vedant, Shyon, and Dean

We will "filter" our universe of tech stocks further according to the following ratios:

1. Liquidity Ratios
    a. Quick Ratio = (cash + accounts receivable + short-term or marketable securities) / (current liabilities)
        i. 3.0 < x < 20.0

2. Financial Leverage Ratios
    a. Debt-to-Equity Ratio = (total debt) / (total equity)
        i. -0.1 < x < 0.2

3. Profitability Ratios
    a. Gross Profit Margin = (sales - COGS) / (sales)
        i. 0.5 < x
'''

import finviz
import pandas as pd

# Fundamental indicators we're interested in
keys = ['Market Cap', 'Quick Ratio', 'Debt/Eq', 'Gross Margin']

# Our universe of stocks; this will just be the output of signals.py in the future
FAANG = ['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOGL']

stock_list = []

# Iterate through each ticker to retrieve our figures of interest via finviz
for ticker in FAANG:
    stock_list.append({k: finviz.get_stock(ticker)[k] for k in keys})

data = pd.DataFrame(data=stock_list, index=FAANG)
print(data)