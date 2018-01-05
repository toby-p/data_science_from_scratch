from numpy import random
import math
from collections import Counter


def random_kid():
    return random.choice(["boy", "girl"])


def bayes():
    
    prob_T_on_D = 0.99
    prob_D = 0.0001
    prob_T_not_D = 0.01
    prob_not_D = 0.9999
    prob_D_on_T = prob_T_on_D * prob_D / (prob_T_on_D * prob_D + prob_T_not_D*prob_not_D)
    
    return prob_D_on_T


def uniform_pdf(x):
    return 1 if x>=0 and x<1 else 0


def uniform_pdf(x):
    "Returns probability that a uniform variable is <= x"
    if x<0: return 0
    elif x<1: return x
    else: return 1
    
    
def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))

def normal_cdf(x, mu=0, sigma=1):
    # Using Python's math.erf
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """Find approximate inverse using binary search"""
    
    # If not standard, compute standard and rescale.
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_csf(p, tolerance = tolerance)
    
    low_z, low_p = -10.0, 0
    hi_z, hi_p = 10.0, 1
    
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cdf(mid_z)
        
        if mid_p < p:
            # Midpoint too low, search above it.
            low_z, low_p = mid_z, mid_p
        
        elif mid_p > p:
            # Midpoint too high, search below it.
            hi_z, hi_p = mid_z, mid_p
        
        else:
            break
    
    return mid_z


def bernoulli_trial(p):
    """Returns 1 with probability p, and 0 with probability 1 - p"""
    return 1 if random.random() < p else 0

def binomial(n, p):
    """Runs a Bernoulli trial on probability p n times."""
    return sum(bernoulli_trial(p) for _ in range(n))
    
def make_hist(p, n, num_points):
    
    data = [binomial(n, p) for _ in range(num_points)]
    
    # Bar chart to show actual binomial samples.
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
           [v / num_points for v in histogram.values()],
           0.8,
           color="0.75")
    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))
    
    # Line chart to show normal approximation.
    xs = range(min(data), max(data)+1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma) for i in xs]
    plt.plot(xs, ys)
    
    plt.title("Binomial Distribution vs. Normal Distribution")
    plt.show()
