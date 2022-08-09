#import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math

from api_secrets import IEX_CLOUD_API_TOKEN

stocks = pd.read_csv("sp_500_stocks.csv")

my_columns = ['Ticker', 'Price', 'Market Capitalization', 'Number of Shares to Buy']

final_dataframe = pd.DataFrame(columns = my_columns)

for symbol in stocks['Ticker']:
    try:
        api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}'
        print(api_url)
        data = requests.get(api_url).json()
        final_dataframe = final_dataframe.append(pd.Series([symbol, data['latestPrice'], data['marketCap'], 'N/A'], index=my_columns), ignore_index=True)
    except Exception as e:  
        print(str(e))       
print(final_dataframe.head(10))