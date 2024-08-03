import pandas as pd

def calc_rsi(data: pd.Series, window=14) -> pd.Series:
    """
    Calculate the Relative Strength Index (RSI).
    
    Parameters:
    - data (pd.Series): Series of asset prices.
    - window (int): The period window for calculating RSI.
    
    Returns:
    - pd.Series: RSI values.
    """
    
    delta = data.diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))

    return rsi