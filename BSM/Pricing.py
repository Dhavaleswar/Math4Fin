import numpy as np
from scipy.stats import norm

class BlackScholesModel:
    """
    A class to compute option prices using BSM model

    Attributes
    ----------
    S = Underlying asset price
    K = Option strike price
    T = Time to expiration in years
    r = Risk-free interest rate
    sigma = Volatility of underlying asset


    Methods
    -------

    d1():
        returns the d1 parameter
    d2():
        returns the d2 parameter
    call_price():
        returns the call price
    put_price():
        returns the put price
    call_bounds():
        returns the lower and upper bounds for the call price
    put_bounds():
        returns the lower and upper bounds for the put price
    """

    def __init__(self, S, K, T, r, sigma):
        self.put_price = None
        self.call_price = None
        self.d2 = None
        self.d1 = None
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma

    def d1(self):
        numerator_ = np.log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T
        denominator_ = self.sigma * np.sqrt(self.T)
        self.d1 = numerator_ / denominator_
        return self.d1

    def d2(self):
        self.d2 = self.d1() - self.sigma * np.sqrt(self.T)
        return self.d2

    def call_price(self):
        self.call_price = self.S * norm.cdf(self.d1) - self.K * np.exp(-self.r * self.T) * norm.cdf(self.d2)
        return self.call_price

    def put_price(self):
        self.put_price = self.K * np.exp(-self.r * self.T) * norm.cdf(-self.d2) - self.S * norm.cdf(-self.d2)
        return self.put_price

    def call_bounds(self):
        min_call_price = max(0, self.S - self.K * np.exp(-self.r * self.T))
        max_call_price = self.S

        return min_call_price, max_call_price

    def put_bounds(self):
        min_put_price = max(0, self.K * np.exp(-self.r * self.T) - self.S)
        max_put_price = self.K

        return min_put_price, max_put_price

    def run(self):
        self.d1()
        self.d2()
        self.call_price()
        self.put_price()

