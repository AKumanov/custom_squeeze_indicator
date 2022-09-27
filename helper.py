from time import time
import numpy as np
import MetaTrader5 as mt5
import pytz
import datetime
import pandas as pd 

frame_h4 = mt5.TIMEFRAME_H4
now = datetime.datetime.now()

def asset_list(asset_set):
    if asset_set == 1:
        assets = ['EURUSD', 'EURCHF']
    return assets

assets = asset_list(1)

def adder(data, times):
    for i in range(1, times + 1):
        z = np.zeros((len(data), 1), dtype=float)
        data = np.append(data, z, axis=1)
    return data

def deleter(data, index, times):
    for i in range(1, times + 1):
        data = np.delete(data, index, axis=1)
    return data


def get_quotes(time_frame, year=2005, month=1, day=1, asset="EURUSD"):
    if not mt5.initialize():
        print("Initialize failed, error code: {}".format(mt5.last_error()))
        quit()
    
    timezone = pytz.timezone("Europe/Paris")

    utc_from = datetime.datetime(year, month, day, tzinfo=timezone)
    utc_to = datetime.datetime(now.year, now.month, now.day + 1, tzinfo=timezone)
    rates = mt5.copy_rates_range(asset, time_frame, utc_from, utc_to)

    rates_frame = pd.DataFrame(rates)

    return rates_frame

def mass_import(asset, horizon):
    if horizon == 'H4':
        data = get_quotes(frame_h4, 2019, 1, 1, asset=assets[asset])
        data = data.iloc[:, 1:5].values
        data = data.round(decimals=5)
    return data

def jump(data, jump):
    data = data[jump:, ]
    return data