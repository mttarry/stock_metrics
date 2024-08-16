import pandas as pd
from stock_metrics.bollinger_bands import calc_bollinger_bands

def test_bollinger_bands_0():
    data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    bollinger_bands = calc_bollinger_bands(data, window=5)

    assert(len(bollinger_bands) == len(data))
    assert('Upper Band' in bollinger_bands)
    assert('Lower Band' in bollinger_bands)
    assert isinstance(bollinger_bands, pd.DataFrame)
    assert isinstance(bollinger_bands['Upper Band'], pd.Series)
    assert isinstance(bollinger_bands['Lower Band'], pd.Series)
    assert(len(bollinger_bands['Upper Band']) == len(data))
    assert(len(bollinger_bands['Lower Band']) == len(data))
    