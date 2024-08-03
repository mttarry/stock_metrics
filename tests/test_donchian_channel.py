import pandas as pd
from stock_metrics.donchian_channel import calc_donchian_channel

def test_donchian_channel_0():
    data = pd.DataFrame({
        'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
        'High': [100, 102, 104, 103, 101, 105, 107, 106, 108, 110],
        'Low': [95, 97, 99, 98, 96, 100, 102, 101, 103, 105]
    })

    donchian = calc_donchian_channel(data, window=5)

    assert isinstance(data, pd.DataFrame)
    assert(len(donchian['Upper Band']) == len(data['High']))
    assert(len(donchian['Lower Band']) == len(data['Low']))

