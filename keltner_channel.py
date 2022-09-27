from audioop import mul
import numpy as np
from bollinger_bands import ma
import helper as helper_tools
from stochastic_rsi import deleter, ema, jump
import simple_indicators


def atr(data, lookback, high, low, close, where, genre='Smoothed'):
    # adding required columns
    data = helper_tools.adder(data, 1)

    # True Range Calculation
    for i in range(len(data)):
        try:
            data[i, where] = max(data[i, high] - data[i, low], \
                abs(data[i, high] - data[i - 1, close]), \
                    abs(data[i, low] - data[i - 1, close]))

        except ValueError:
            pass
    data[0, where] = 0

    if genre == 'Smoothed':
        # Average True Range Calculation
        data = simple_indicators.ema(data, 2, lookback, where, where + 1)
    
    if genre == 'Simple':
        # Average True Range Calculation
        data = simple_indicators.ma(data, lookback, where, where + 1)
    
    # Cleaning
    data = deleter(data, where, 1)
    data = jump(data, lookback)

    return data

def keltner_channel(data, ma_lookback, atr_lookback, multiplier, what, where):
    data = simple_indicators.ema(data, 2, ma_lookback, what, where)
    data = atr(data, atr_lookback, 2, 1, 3, where + 1)

    data[:, where + 2] = data[:, where] + (data[:, where + 1] * multiplier)
    data[:, where + 3] = data[:, where] - (data[:, where + 1] * multiplier)

    return data