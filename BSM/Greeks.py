from scipy.stats import norm
import numpy as np


from BSM.Pricing import BlackScholesModel

class BSMGreeks(BlackScholesModel):
    """
    A class to compute option greeks using BSM model

    Attributes
    ----------
    S = Underlying asset price
    K = Option strike price
    T = Time to expiration in years
    r = Risk-free interest rate
    sigma = Volatility of underlying asset
    delta_call = Call delta
    delta_put = Put delta
    gamma = Gamma
    theta_call = Call theta
    theta_put = Put theta
    vega_call = Call vega
    vega_put = Put vega
    rho_call = Call rho
    rho_put = Put rho


    Methods
    -------
    compute_delta_call():
        returns the call delta
    compute_delta_put():
        returns the put delta
    compute_gamma():
        returns the  gamma
    compute_theta_call():
        returns the call theta
    compute_theta_put():
        returns the put theta
    compute_vega_call():
        returns the call vega
    compute_vega_put():
        returns the put vega
    compute_rho_call():
        returns the call rho
    compute_rho_put():
        returns the put rho
    compute_greeks():
        computes all the greeks

    """
    def __init__(self, S, K, T, r, sigma):
        super().__init__(S, K, T, r, sigma)

        self.delta_call = None
        self.delta_put = None
        self.gamma = None
        self.theta_call = None
        self.theta_put = None
        self.vega = None
        self.rho_call = None
        self.rho_put = None

    def compute_delta_call(self):
        self.delta_call = norm.cdf(self.d1)
        return self.delta_call

    def compute_delta_put(self):
        self.delta_put = -norm.cdf(-self.d1)
        return self.delta_put

    def compute_gamma(self):
        self.gamma = norm.pdf(self.d1)/(self.S * self.sigma * np.sqrt(self.T))
        return self.gamma

    def compute_theta_call(self):
        self.theta_call = -(self.S * norm.pdf(self.d1) * self.sigma)/(2 * np.sqrt(self.T)) - self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(self.d2)
        return self.theta_call

    def compute_theta_put(self):
        self.theta_put = -(self.S * norm.pdf(self.d1) * self.sigma)/(2 * np.sqrt(self.T)) + self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(-self.d2)
        return self.theta_put

    def compute_vega(self):
        self.vega = self.S * norm.pdf(self.d1) * np.sqrt(self.T)
        return self.vega

    def compute_rho_call(self):
        self.rho_call = self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(self.d2)
        return self.rho_call

    def compute_rho_put(self):
        self.rho_put = -self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(-self.d2)
        return self.rho_put

    def compute_greeks(self):
        self.compute_delta_call()
        self.compute_delta_put()
        self.compute_gamma()
        self.compute_theta_call()
        self.compute_theta_put()
        self.compute_vega()
        self.compute_rho_call()
        self.compute_rho_put()


