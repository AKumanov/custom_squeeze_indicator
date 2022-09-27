import matplotlib.pyplot as plt
import helper as helper_tools
import bollinger_bands
import squeeze_indicator


horizon = 'H4'
my_data = helper_tools.mass_import(0, horizon)
my_data = helper_tools.adder(my_data, 20)
my_data = bollinger_bands.bollinger_bands(my_data, 20, 2, 3, 4)
boll_lookback = 20
boll_vol = 2
kelt_lookback = 20
kelt_vol = 1.5

my_data = squeeze_indicator.squeeze(my_data, boll_lookback, boll_vol, kelt_lookback, kelt_vol, 3, 4)
squeeze_indicator.indicator_plot_squeeze(my_data, my_data)
# my_data = squeeze_indicator.singal(my_data)

