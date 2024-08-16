import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt



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

def fetch_stock_info(symbol):
    """
    Fetch stock info from Yahoo Finance.
    
    Parameters:
    - symbol (str): Stock ticker symbol.
    
    Returns:
    - pd.DataFrame: Stock data.
    """

    stock = yf.Ticker(symbol)
    return stock.info

def plot(data, columns, title, xlabel, ylabel, line_styles=None, show=True):
    if line_styles is None:
        line_styles = ['-'] * len(columns)

    for column, line_style in zip(columns, line_styles):
        plt.plot(data[column], label=column, linestyle=line_style)

    plt.legend()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if (show):
        plt.show()