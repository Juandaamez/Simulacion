import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

ElevatorData = pd.read_csv(
    "C:\Users\judac\OneDrive\Documentos\GitHub\Simulacion\final_project\wed01.csv", 
    header = 0, 
    usecols = ["hora", "ascensor_1"], 
    parse_dates=True, 
    index_col = "hora")

print(ElevatorData.info())
print(ElevatorData.head())
print(ElevatorData.tail())
print(ElevatorData.describe())

plt.figure(figsize=(10, 5))
plt.plot(ElevatorData)
plt.show()

ElevatorDataPctChange = ElevatorData.pct_change()

ElevatorLogReturns = np.log(1 + ElevatorData)
print(ElevatorLogReturns.tail(10))

plt.figure(figsize=(10,5))
plt.plot(ElevatorLogReturns)
plt.show()

MeanLogReturns = np.array(ElevatorLogReturns.mean())
VarLogReturns = np.array(ElevatorLogReturns.var())
StdevLogReturns = np.array(ElevatorLogReturns.std())

Drift = MeanLogReturns - (0.5 * VarLogReturns)
print("Drift = ", Drift)

NumIntervals = 1000     #En el caso de los ascensores es el valor de los viajes
Iterations = 20

np.random.seed(7)
SBMotion = norm.ppf(
    np.random.rand(NumIntervals, Iterations)
)

DailyReturns = np.exp(Drift + StdevLogReturns * SBMotion)

StartStockPrices = ElevatorData.iloc[0]

StockPrice = np.zeros_like(DailyReturns)

StockPrice[0] = StartStockPrices

for t in range(1, NumIntervals):
    StockPrice[t] = StockPrice[t - 1] * DailyReturns[t]

plt.figure(figsize=(10,5))
plt.plot(StockPrice)
plt.show()