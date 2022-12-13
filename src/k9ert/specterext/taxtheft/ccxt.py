import ccxt
import calendar
from datetime import datetime, date, timedelta
import pandas as pd
import numpy as np

binance = ccxt.binance()
bitstamp = ccxt.bitstamp()

def min_ohlcv(dt, pair, limit):
    # UTC native object
    since = calendar.timegm(dt.utctimetuple())*1000
    ohlcv1 = bitstamp.fetch_ohlcv(symbol=pair, timeframe='1m', since=since, limit=limit)
    ohlcv2 = bitstamp.fetch_ohlcv(symbol=pair, timeframe='1m', since=since, limit=limit)
    ohlcv = ohlcv1 + ohlcv2
    return ohlcv

def ohlcv(the_date, pair, period='1d', limit=0):
    ohlcv = []
    if limit==0:
        if period == '1m':
            limit = 720
        elif period == '1d':
            limit = 365
        elif period == '1h':
            limit = 24
        elif period == '5m':
            limit = 288

    start_dt = datetime.strptime(the_date, "%Y%m%d")
    since = calendar.timegm(start_dt.utctimetuple())*1000
    if period == '1m':
        ohlcv.extend(min_ohlcv(start_dt, pair, limit))
    else:
        ohlcv.extend(bitstamp.fetch_ohlcv(symbol=pair, timeframe=period, since=since, limit=limit))
    df = pd.DataFrame(ohlcv, columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume'])
    df['Time'] = [datetime.fromtimestamp(float(time)/1000) for time in df['Time']]
    df['date'] = pd.to_datetime(df.Time)
    df['Open'] = df['Open'].astype(np.float64)
    df['High'] = df['High'].astype(np.float64)
    df['Low'] = df['Low'].astype(np.float64)
    df['Close'] = df['Close'].astype(np.float64)
    df['Volume'] = df['Volume'].astype(np.float64)
    df['Avg'] = (df['Open']+df['Close']) / 2
    df.set_index('Time', inplace=True)
    return df
