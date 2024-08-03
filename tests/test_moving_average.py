import pandas as pd
from stock_metrics.moving_average import calc_moving_average

def test_rsi_0():
    data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ma = calc_moving_average(data, window=5)
    
    assert isinstance(data, pd.Series)
    assert(len(ma) == len(data))
