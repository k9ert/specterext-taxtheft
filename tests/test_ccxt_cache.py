import logging
from k9ert.specterext.taxtheft.ccxt_cache import CcxtCache


def test_CcxtCache(caplog, empty_data_folder):
    caplog.set_level(logging.DEBUG)
    cc = CcxtCache(empty_data_folder)
    date = '20190101'
    mydf = cc.ohlcv(date, 'BTC/EUR', '1d', limit=5)
    print(mydf)
    mydf = cc.ohlcv(date, 'BTC/EUR', '1d', limit=5)
    print(mydf)
