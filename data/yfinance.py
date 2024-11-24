import yfinance as yf
import datetime as dt
import pandas as pd

def fetch_options_data(ticker_symbol:str):
    ticker = yf.Ticker(ticker_symbol)
    option_dates = ticker.options

    options_data = ticker.option_chain(option_dates[0])

    return options_data.calls, options_data.puts

def fetch_underlying_stock_data(ticker_symbol:str, start_date:dt.date, end_date:dt.date) -> pd.DataFrame:
    ticker = yf.Ticker(ticker_symbol)
    return ticker.history(start=start_date, end=end_date)

