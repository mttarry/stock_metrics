import pandas as pd
import numpy as np


def find_local_minima(data: pd.Series, window=5) -> pd.Series:
    """
    Find the local minima
    
    Parameters:
    - data: Series of asset prices
    - window (int): Period window for finding local minima
    
    Returns:
    - pd.Series: Series of local minima
    """

    return data.rolling(window=window).min()


def find_local_maxima(data: pd.Series, window=5) -> pd.Series:
    """
    Find the local maxima
    
    Parameters:
    - data: Series of asset prices
    - window (int): Period window for finding local maxima
    
    Returns:
    - pd.Series: Series of local maxima
    """

    return data.rolling(window=window).max()