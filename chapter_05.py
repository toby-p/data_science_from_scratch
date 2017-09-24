from chapter_04 import sum_of_squares, dot
from collections import Counter
import math

def mean(x):
    return sum(x) / len(x)
    
def median(v):
    n = len(v)
    sorted_v = sorted(v)
    mid_point = n // 2

    if n % 2 == 1:
        # Odd, so return mid-point
        return sorted_v[mid_point]
    else:
        lo = mid_point - 1
        hi = mid_point
        return (sorted_v[lo] + sorted_v[hi]) / 2
    
def quantile(x, p):
    """Returns the pth-percentile value in x."""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

def mode(x):
    """Returns a list a may be more than one mode."""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]

def data_range(x):
    return max(x) - min(x)

def de_mean(x):
    """Translate x by subtracting its mean, so result has mean 0."""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    """Assumes x has at least 2 elements."""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
    return math.sqrt(variance(x))

def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

def covariance(x, y):
    n = len(x) # Same a len(y) as both are features of same dataset.
    return dot(de_mean(x), de_mean(y)) / (n - 1)

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # Correlation is zero if no variation.