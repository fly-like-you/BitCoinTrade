import sys
import pybithumb
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import time
import pykorbit
import requests
import datetime
con_key = "31363190a625d2e343de5aa897e1e9ce"
sec_key = "4b47a30af3597d54b8c5c562914f7465"
bithumb = pybithumb.Bithumb(con_key, sec_key)
def get_target_price(ticker):
    df = pybithumb.get_ohlcv("BTC")
    yesterday = df.iloc[-2]

    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * 0.5
    return target

def sell_crypto_currency(ticker):    # 코인 매도 함수
    unit = bithumb.get_balance(ticker)[0]
    bithumb.sell_market_order(ticker, unit)

def get_yesterday_ma5(ticker):  # 이동평균 구하기
    df = pybithumb.get_ohlcv(ticker)
    close = df['close']
    ma = close.rolling(window = 5).mean()
    return ma[-2]

def buy_crypto_currency(ticker):    # 코인 매수 함수
    krw = bithumb.get_balance(ticker)[2]
    orderbook = pybithumb.get_orderbook(ticker)
    sell_price = orderbook['asks'][0]['price']
    unit = krw/float(sell_price)
    bithumb.buy_market_order(ticker, unit)
now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
target_price = get_target_price("BTC")
while True:     #변동성 돌파 + 이동평균 매수
    try:
        now = datetime.datetime.now()                       # 현재 시각을 구해서
        if mid < now < mid + datetime.delta(seconds = 10):  # 자정과 자정 + 10초 사이에 현재시간이 있으면
            target_price = get_target_price("BTC")          # 비트코인 시세를 구하고
            now = datetime.datetime.now()                   # 현재시각을 다시구하고
            mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)       #그 다음날 자정 시각 설정
            ma5 = get_yesterday_ma5("BTC")                  # 전일 5일동안의 이동평균 구하고
            sell_crypto_currency("BTC")                     # 모두 판매
        current_price = pybithumb.get_current_price("BTC")
        if ( current_price > target_price ) and ( current_price > ma5 ): # 목표가 + 이동평균 비교

            buy_crypto_currency("BTC")
    except:
        print("에러발생")

    current_price = pybithumb.get_current_price("BTC")
    print(current_price)
    time.sleep(1)