import pybithumb
from pandas import DataFrame
import numpy as np
import openpyxl
df = pybithumb.get_ohlcv("BTC")
df = df['2021']
df['range'] = (df['high'] - df['low'])*0.5
df['target'] = df['open'] + df['range'].shift(1)

df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'], 1) # 고가가 목표값보다 크면 샀다는 의미이므로 ror추가, 이때 수익률은 종가/목표가 이고 아닐시에는 1
ror = df['ror'].cumprod()[-2]
print(ror)