from sqlite3 import DatabaseError
import numpy as np
import pandas as pd

def ma(data, lookback, what, where):
    for i in range(len(data)):
        try:
            data[i, where] = (data[i - lookback + 1:i + 1, what].mean())
        except IndexError:
            pass

    return data

def volatility(data, lookback, what, where):
    for i in range(len(data)):
        try:
            data[i, where] = (data[i - lookback + 1:i + 1, what].std())
        except IndexError:
            pass
    return data

def bollinger_bands(data, boll_lookback, standard_distance, what, where):

    # calculating mean
    ma(data, boll_lookback, what, where)

    #calculating vol
    volatility(data, boll_lookback, what, where + 1)

    data[:, where + 2] = data[:, where] + (standard_distance * data[:, where + 1])
    data[:, where + 3] = data[:, where] - (standard_distance * data[:, where + 1])

    return data