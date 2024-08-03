import pandas as pd

def calc_donchian_channel(data: pd.DataFrame, window=20) -> pd.DataFrame:
    """
    Calculate the Donchian Channel.
    
    Parameters:
    - data (pd.DataFrame): DataFrame with 'High' and 'Low' columns.
    - window (int): The period window for calculating the channel.
    
    Returns:
    - pd.DataFrame: DataFrame with 'Upper Band' and 'Lower Band'.
    """
    if 'High' not in data.columns or 'Low' not in data.columns:
        raise ValueError("DataFrame must contain 'High' and 'Low' columns")
    
    high = data['High'].rolling(window=window).max()
    low = data['Low'].rolling(window=window).min()
    return pd.DataFrame({'Upper Band': high, 'Lower Band': low})