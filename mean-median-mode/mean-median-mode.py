from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x.sort()
    n = len(x)
    count = Counter(x)
    sum = 0
    mode = x[0]
    for num in x:
        sum += num
        if count[num] > count[mode]:
            mode = num
        if num < mode and count[num] == count[mode]:
            mode = num
    mean = sum / n
    median = (x[n // 2] + x[(n-1) // 2]) / 2
    return {"mean" : mean, "median" : median, "mode" : float(mode)}
        
        