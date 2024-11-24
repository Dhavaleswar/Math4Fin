## Light Read on d1, d2

In the Black-Scholes-Merton model for pricing options, $d_1$ and $d_2$ are  intermediate variables that help simplify the pricing formula. They are defined as follows:

$$ d1 = \frac{ln(\frac{S}{K}) + (r + \frac{\sigma^2}{2})T}{\sigma\sqrt{T}} $$
$$ d2 = d1 - \sigma\sqrt{T} $$

where:
- $S$ is the current stock price
- $K$ is the option strike price
- $r$ is the risk-free rate
- $\sigma$ is the stock's volatility 
- T is the time to expiration
- $ln$ is the natural logarithm

### Meaning of $d_1$ and $d_2$: 

[Resource](https://www.finance-tutoring.fr/the-roles-of-n(d1)-and-n(d2)-in-the-black-scholes-model-simply-explained/#:~:text=N(d2)%20reflects%20the%20probability,the%20stock%2C%20making%20it%20higher.)

1. N($d_2$) reflects the probability that the option will be exercised. It is the probability that the option will be in the money at expiration.  
2. N($d_1$) reflects above probability $+$ and expected stock price if the option is exercised.
3. $d1 > d2$, so $N(d1) > N(d2)$
4. The term $S*N(d_1)$ represents the present value of the expected stock price, while $X*exp^{-rT}*N(d_2)$ represents the present value of the exercise price.
5. Since $N(d_2) > N(d_2)$, the PV of the stock received (adjusted by $N(d_1)$) is higher than the PV of the exercise price (adjusted by $N(d_2)$).





