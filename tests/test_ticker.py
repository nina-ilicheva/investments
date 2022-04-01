import json
from typing import NamedTuple
from unittest import TestCase

from investments.ticker import Ticker, TickerKind


class TestTicker(TestCase):
    def test(self):
        ticker = Ticker("symbol_name", TickerKind.Stock)
        print(json.dumps(self.preprocess(ticker), default=self.my_default))

    def my_default(self, obj):
        from investments.ticker import TickerKind
        if isinstance(obj, TickerKind):
            return str(obj)
        return obj

    def preprocess(self, obj) -> object:
        if isinstance(obj, Ticker):
            return obj._asdict()
        else:
            return obj.__dict__