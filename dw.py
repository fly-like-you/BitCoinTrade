import pybithumb
from pandas import DataFrame
import numpy as np
import openpyxl
# df = pybithumb.get_ohlcv("BTC")
# df = df['2021']
# df['range'] = (df['high'] - df['low'])*0.5
# df['target'] = df['open'] + df['range'].shift(1)
#
# df['ror'] = np.where(df['high'] > df['target'],
#                      df['close'] / df['target'], 1) # 고가가 목표값보다 크면 샀다는 의미이므로 ror추가, 이때 수익률은 종가/목표가 이고 아닐시에는 1
# ror = df['ror'].cumprod()[-2]
# print(ror)



def get_hpr(ticker):
    try:
        df = pybithumb.get_ohlcv("BTC")
        df = df['2020']
        df['ma5'] = df['close'].rolling(window=5).mean().shift(1)
        df['range'] = (df['high'] - df['low']) * 0.5
        df['target'] = df['open'] + df['range'].shift(1)
        df['bull'] = df['open'] > df['ma5']

        fee = 0.0032
        df['ror'] = np.where((df['high'] > df['target']) & df['bull'],
                             df['close'] / df['target'] - fee,
                             1)

        df['hpr'] = df['ror'].cumprod()
        df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

        return df['hpr'][-2]
    except:
        return 1

tickers = pybithumb.get_tickers()

hprs = []
for ticker in tickers:
    hpr = get_hpr(ticker)
    hprs.append((ticker, hpr))
sorted_hprs = sorted(hprs, key = lambda x:x[1], reverse = True)
print(sorted_hprs[:5])
