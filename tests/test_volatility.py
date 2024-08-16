import pandas as pd
from stock_metrics.volatility import calc_volatility

def test_volatility():
    data = pd.DataFrame({
        'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
        'Close': [100, 102, 104, 103, 101, 105, 107, 106, 108, 110],
    })

    vol, ann_vol = calc_volatility(data['Close'])

    print(vol)
    print(ann_vol)

    assert isinstance(vol, float)
    assert isinstance(ann_vol, float)
