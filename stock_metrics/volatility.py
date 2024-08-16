import pandas as pd
import numpy as np

def calc_volatility(data: pd.Series) -> float:
    """
    Calculate the volatility 

    Parameters:
    - data (pd.Series): Series of data
    
    Returns:
    - (daily volatility, annual volatility) (float, float): Daily and annualized volatility
    """

    daily_ret = data.pct_change()
    daily_volatility = daily_ret.std()
    annualized_volatility = daily_volatility * np.sqrt(252) # 252 trading days
    
    return (daily_volatility, annualized_volatility)







