import pandas as pd
from stock_metrics.rsi import calc_rsi

def test_rsi_0():
    data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    rsi = calc_rsi(data, window=5)
    assert isinstance(data, pd.Series)
    assert(len(rsi) == len(data))

def test_rsi_1():
    data = pd.Series([1, 2, 1, 2, 1, 2, 1, 2, 1, 2])

    rsi = calc_rsi(data, window=5)
    assert isinstance(data, pd.Series)
    assert(len(rsi) == len(data))

def test_rsi_2():
    data = pd.Series([1, 2, 1, 2, 1, 2, 1, 2, 1, 2])

    rsi = calc_rsi(data, window=2)
    assert isinstance(data, pd.Series)
    assert(len(rsi) == len(data))

