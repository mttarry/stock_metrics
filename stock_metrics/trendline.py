import pandas as pd
import numpy as np
from stock_metrics.extrema import find_local_maxima, find_local_minima
from stock_metrics.donchian_channel import calc_donchian_channel


def hh_ll_trend(data: pd.DataFrame, window=5) -> pd.DataFrame:
    """
    Find asset price movement trend based on higher highs and lower lows. 
    Modifies 'Highs' and 'Lows' columns by interpolating between plateaus 

    Parameters:
    - data (pd.DataFrame): DataFrame with columns for 'Highs' and 'Lows'
    - window (int): The period window for determining if highs are increasing and lows are decreasing
    
    Returns:
    - pd.Series: Trend values 'Downtrend', 'Sideways', 'Uptrend'
    """

    diff = data.diff(1)    
    combined = diff['Highs'] + diff['Lows']

    data['Highs'] = data['Highs'].mask(diff['Highs'] == 0, np.nan).interpolate()
    data['Lows'] = data['Lows'].mask(diff['Lows'] == 0, np.nan).interpolate()

    return combined.mask(combined > 0, 'Uptrend').mask(combined < 0, 'Downtrend').mask(combined == 0, 'Sideways')



