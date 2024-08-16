import pandas as pd
from stock_metrics.extrema import find_local_maxima, find_local_minima


def test_local_minima_0():
    data = pd.Series([1, 0, 3, 7, 2, 0, 8, 14, 6, 5, 1])
    local_minima = find_local_minima(data, window=5)

    assert(isinstance(local_minima, pd.Series))
    assert(len(local_minima) > 0)

def test_local_maxima_0():
    data = pd.Series([1, 0, 3, 7, 2, 0, 8, 14, 6, 5, 1])
    local_maxima = find_local_maxima(data, window=5)

    assert(isinstance(local_maxima, pd.Series))
    assert(len(local_maxima) > 0)