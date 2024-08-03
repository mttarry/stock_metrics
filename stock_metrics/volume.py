import pandas as pd


def calc_on_balance_volume(data: pd.DataFrame) -> pd.Series:
    """
    Calculate the On-Balance Volume
    
    Parameters:
    - data (pd.DataFrame): Dataframe with 'Close' and 'Volume' columns
    
    Returns:
    - pd.Series: Series of on-balance volume.
    """
    if 'Close' not in data.columns or 'Volume' not in data.columns:
        raise ValueError("DataFrame must contain 'Close' and 'Volume' columns")
    
    delta = data['Close'].diff(1)
    up_volume = (delta.where(delta > 0, 0).mask(delta > 0, data['Volume']))
    down_volume = (delta.where(delta < 0, 0).mask(delta < 0, -data['Volume']))
    obv = (up_volume + down_volume).cumsum()
    
    obv.iloc[0] = data['Volume'].iloc[0]

    return obv
    









    