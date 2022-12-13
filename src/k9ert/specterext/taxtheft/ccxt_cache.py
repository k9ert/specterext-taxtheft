

from datetime import datetime
import os
from .ccxt import ohlcv
import pandas as pd
import logging

logger = logging.getLogger(__name__)

class CcxtCache():

    def __init__(self, datadir):
        self.datadir=datadir
        self.pair_cache= {}


    def ohlcv(self, date, pair, period='1d', limit=1):
        if (os.path.exists(os.path.join(self.datadir, pair))):
            self.pair_cache[pair] = self.load_cache(pair)
        logger.info("check Cache ...")
        if self.contains_date(pair, date):
            logger.info("got it cached!")
            return self.pair_cache[pair].loc(date)
        else:
            result = ohlcv(date, pair, period='1d', limit=1)
            self.pair_cache[pair] = pd.merge(self.pair_cache[pair] , result)
            return result


    def contains_date(self, pair, date):
        cache = self.pair_cache.get(pair)
        if cache is None:
            logger.info(f"Loading cache for pair {pair}")
            self.load_cache(pair)
        return self.pair_cache[pair]['date'].isin([date]).any()

    def load_cache(self, pair):
        cache = self.pair_cache.get(pair)
        if cache is None:
            if (os.path.exists(os.path.join(self.datadir, pair))):
                self.pair_cache[pair] = pd.read_pickle(os.path.join(self.datadir, pair))
            else:
                logger.info("Cache did not exist, creating anew")
                self.pair_cache[pair] = pd.DataFrame({}, columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume'])
                self.pair_cache[pair]['Time'] = [datetime.fromtimestamp(float(time)/1000) for time in self.pair_cache[pair]['Time']]
                self.pair_cache[pair]['date'] = pd.to_datetime(self.pair_cache[pair].Time)
                self.pair_cache[pair]['Avg'] = (self.pair_cache[pair]['Open']+self.pair_cache[pair]['Close']) / 2
                self.pair_cache[pair].set_index('Time', inplace=True)

    