import yfinance as yf
import pandas as pd

def fetch_stock_data(symbol, start_date, end_date):
    """
    Fetch stock data from Yahoo Finance.
    
    Parameters:
    - symbol (str): Stock ticker symbol.
    - start_date (str): Start date in 'YYYY-MM-DD' format.
    - end_date (str): End date in 'YYYY-MM-DD' format.
    
    Returns:
    - pd.DataFrame: Stock data.
    """

    stock = yf.Ticker(symbol)
    return stock.history(start=start_date, end=end_date)