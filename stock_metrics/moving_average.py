import pandas as pd

def calc_moving_average(data: pd.Series, window=20) -> pd.Series:
    """
    Calculate the Moving Average
    
    Parameters:
    - data (pd.Series): Series of asset prices
    - window (int): The period window for calculating the moving average.
    
    Returns:
    - pd.Series: Moving Average values.
    """

    return data.rolling(window=window).mean()