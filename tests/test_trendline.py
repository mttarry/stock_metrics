import pandas as pd
from stock_metrics.extrema import find_local_maxima, find_local_minima
from stock_metrics.trendline import hh_ll_trend

def test_hh_ll_trendline_0():
    data = pd.DataFrame({
        'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
        'Close': [100, 102, 104, 103, 101, 105, 107, 106, 108, 110],
    })

    window = 3

    data['Highs'] = find_local_maxima(data['Close'], window=window)
    data['Lows'] = find_local_minima(data['Close'], window=window)

    data['Trend'] = hh_ll_trend(data, window=window)
    #print(data)

    assert(isinstance(data['Trend'], pd.Series))
    assert(len(data['Trend']) == len(data))

