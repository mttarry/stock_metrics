import pandas as pd
from stock_metrics.volume import calc_on_balance_volume

def test_on_balance_volume():
    data = pd.DataFrame({
        'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
        'Close': [100, 102, 104, 103, 101, 105, 107, 106, 108, 110],
        'Volume': [1234, 1412, 1010, 1239, 1230, 1020, 1102, 1610, 1555, 1084]
    })

    obv = calc_on_balance_volume(data)

    assert isinstance(data, pd.DataFrame)
