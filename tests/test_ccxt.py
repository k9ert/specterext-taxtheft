import ccxt
import pandas as pd

from k9ert.specterext.spotbit.ccxt import ohlcv
import datetime

# manual: https://docs.ccxt.com/en/latest/manual.html

def test_essentials():
    
    print(ccxt.exchanges) # print a list of all available exchange classes
    print("Bitstamp:")
    print(ccxt.exchanges["bitstamp"])
    assert False



def test_ohlcv():
    date = '20190101'
    df = ohlcv(date, 'BTC/EUR', '1d', limit=5)
    print(df)
    print("-----------")
    assert False
    df = ohlcv(date, 'BTC/EUR', '1d', limit=5)

    df = ohlcv(date, 'BTC/EUR', '1d', limit=5)
    
    print( df['date'].isin(['2019-01-02T01:00:00.000000000']).any())
    print( df['date'].isin([datetime.datetime(2018,1,2,1,0,0)]).any())
    
    #print(df['date'].values)
    
    assert False