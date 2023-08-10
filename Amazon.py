import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

Amzndata = pd.read_csv('AMZN.csv', header = 0, usecols = ['Date', 'Close'],
                       parse_dates=True, index_col = 'Date')

print(Amzndata.info())
print(Amzndata.head())
print(Amzndata.tail())
print(Amzndata.describe())

plt.figure(figsize=(10, 5))
plt.plot(Amzndata)
#plt.show()

AmznDataPctChange = Amzndata.pct_change()

AmznLogReturns = np.log(1 + AmznDataPctChange)
print(AmznLogReturns.tail(10))

plt.figure(figsize=(10,5))
plt.plot(AmznLogReturns)
#plt.show()

MeanLogReturns = np.array(AmznLogReturns.mean())
VarLogReturns = np.array(AmznLogReturns.var())
StdevLogReturns = np.array(AmznLogReturns.std())

Drift = MeanLogReturns - (0.5 * VarLogReturns)
print("Drift = ", Drift)

NumIntervals = 1000     #En el caso de los ascensores es el valor de los viajes
Iterations = 20

np.random.seed(7)
SBMotion = norm.ppf(
    np.random.rand(NumIntervals, Iterations)
)

DailyReturns = np.exp(Drift + StdevLogReturns * SBMotion)

StartStockPrices = Amzndata.iloc[0]

StockPrice = np.zeros_like(DailyReturns)

StockPrice[0] = StartStockPrices

for t in range(1, NumIntervals):
    StockPrice[t] = StockPrice[t - 1] * DailyReturns[t]

plt.figure(figsize=(10,5))
plt.plot(StockPrice)
plt.show()