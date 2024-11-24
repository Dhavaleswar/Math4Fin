import numpy as np
import pandas as pd

def calculate_historical_volatility(stock_price:pd.DataFrame, price_column:str='Close', window=252, ):
    """
    Calculate the historical volatility of a time series.
    """
    log_return = np.log(stock_price[price_column] / stock_price[price_column].shift(1))
    volatility = 252*log_return.rollling(window).std()
    return volatility