import pandas as pd
from stock_metrics.moving_average import calc_moving_average

def calc_bollinger_bands(data: pd.Series, window=20, std=2) -> pd.DataFrame:
    """
    Calculate the Bollinger Bands.
    
    Parameters:
    - data (pd.Series): Series of asset price data
    - window (int): The period window for calculating the moving average
    - std (int): The number of standard deviations used to define the bands.
    
    Returns:
    - pd.DataFrame: DataFrame with 'Upper Band' and 'Lower Band'.
    """

    middle = calc_moving_average(data, window)
    std = middle.rolling(window=window).std()
    upper = middle + (2 * std)
    lower = middle - (2 * std)
    return pd.DataFrame({'Upper Band': upper, 'Middle Band': middle, 'Lower Band': lower})
