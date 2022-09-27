import numpy as np
import helper as helper_func

def ma(data, lookback, what, where):
    data = helper_func.adder(data, 1)
    for i in range(len(data)):
        try:
            data[i, where] = (data[i - lookback + 1:i + 1, what].mean())
        except IndexError:
            pass
    data = helper_func.jump(data, lookback)
    
    return data


def ema(data, alpha, lookback, what, where):
    alpha = alpha / (lookback + 1.0)
    beta = 1 - alpha

    # First value is a simple SMA
    data = ma(data, lookback, what, where)

    # Calculating First EMA
    data[lookback + 1, where] = (data[lookback + 1, what] * alpha) + \
        (data[lookback, where] * beta)
    
    # Calculating the rest of EMA
    for i in range(lookback + 2, len(data)):
        try:
            data[i, where] = (data[i, what] * alpha) + \
                (data[i - 1, where] * beta)
        except IndexError:
            pass
    return data