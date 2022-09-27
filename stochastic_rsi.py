import numpy as np

def adder(Data, times):
    for i in range(1, times + 1):
        new = np.zeros((len(Data), 1), dtype=float)
        Data = np.append(Data, new, axis=1)
    return Data

def deleter(Data, index, times):
    for i in range(1, times + 1):
        Data = np.delete(Data, index, axis=1)
    return Data

def jump(Data, jump):
    Data = Data[jump:, ]
    return Data

def ma(Data, lookback, close, where):
    Data = adder(Data, 1)

    for i in range(len(Data)):
        try:
            Data[i, where] = (Data[i - lookback + 1:i + 1, close].mean())
        except IndexError:
            pass
    
    Data = jump(Data, lookback)

    return Data

def ema(Data, alpha, lookback, what, where):
    alpha = alpha / (lookback + 1.0)
    beta = 1 - alpha

    # First value is a simple SMA
    Data = ma(Data, lookback, what, where)

    # Calculating First EMA
    Data[lookback + 1, where] = (Data[lookback + 1, what] * alpha) + (Data[lookback, where] * beta)

    #Calculating the rest of EMA
    for i in range(lookback + 2, len(Data)):
        try:
            Data[i, where] = (Data[i, what] * alpha) + (Data[i - 1, where] * beta)
        
        except IndexError:
            pass
    return Data


def rsi(Data, lookback, close, where, width=1, genre='Smoothed'):
    Data = adder(Data, 7)

    # Calculating differences
    for i in range(len(Data)):
        Data[i, where] = Data[i, close] - Data[i - width, close]
    
    for i in range(len(Data)):
        if Data[i, where] > 0:
            Data[i, where + 1] = Data[i, where]
        elif Data[i, where] < 0:
            Data[i, where + 2] = abs(Data[i, where])
    
    # Calculating the Smoothed Moving Average on Up and Down abs values
    if genre == 'Smoothed':
        lookback = (lookback * 2) - 1 # From exponential to smoothed
        Data = ema(Data, 2, lookback, where + 1, where + 3)
        Data = ema(Data, 2, lookback, where + 2, where + 4)
    
    if genre == 'Simple':
        Data = ma(Data, lookback, where + 1, where + 3)
        Data = ma(Data, lookback, where + 2, where + 4)

   # Calculating the Relative Strength
    Data[:, where + 5] = Data[:, where + 3] / Data[:, where + 4]

    # Calculating the Relative Strength Index
    Data[:, where + 6] = (100 - (100 / (1 + Data[:, where + 5])))

    # Cleaning
    Data = deleter(Data, where, 6)
    Data = jump(Data, lookback)

    return Data


def stochastic(Data, lookback, high, low, close, where, genre='High-Low'):

    Data = adder(Data, 1)

    if genre == 'High-Low':
        for i in range(len(Data)):
            try:
                Data[i, where] = (Data[i, close] - min(Data[i - lookback + 1:i + 1, low]) / max(Data[i - lookback + 1: 1 + 1, high]) - min(Data[i - lookback + 1:1 + 1, low]))

            except ValueError:
                pass
    
    if genre == 'Normalization':
        for i in range(len(Data)):
            try:
                Data[i, where] = (Data[i, close] - min(Data[i - lookback + 1:i + 1, close]) / max(Data[i - lookback + 1:i + 1, close]) - min(Data[i - lookback + 1:i + 1, close]))
            except ValueError:
                pass
    
    Data[:, where] = Data[:, where] * 100
    Data = jump(Data, lookback)
    return Data

lookback = 5

def get_rsi(my_data):
    my_data = rsi(my_data, lookback, 3, 4)
    return my_data

def get_stoch_rsi(my_data):

    normalization_lookback = 100

    my_data = stochastic(my_data, normalization_lookback, 1, 2, 4, 5, genre='Normalization')
    return my_data
