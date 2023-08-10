import random
import numpy as np
import matplotlib.pyplot as plt

random.seed(2)

f = lambda x: x**2 

a = 0
b = 3
NumSteps = 1000

XIntegral = []      #Inner function
YIntegral = []      

XRectangle = []     #Outter function
YRectangle = []

ymin = f(a)         #Initial point
ymax = ymin

for i in range (NumSteps):
    x = a + (b - a) * float(i) / NumSteps
    y = f(x)

    if y < ymin: ymin = y
    if y > ymax: ymax = y

print(f"Max = {ymax}, Min = {ymin}" )

A = (b-a) * (ymax - ymin)
M = 0           #Succes

for _ in range(NumSteps):
    x = a + (b - a) * random.random()           #Width
    y = ymin + (ymax - ymin) * random.random()  #Height

    if y < f(x):
        M += 1
        XIntegral.append(x)
        YIntegral.append(y)

    else:
        XRectangle.append(x)
        YRectangle.append(y)

NumericalIntegral = M / NumSteps * A
print(f"Numerical integration: {NumericalIntegral}")

XLin = np.linspace(a, b)
YLin = []
for x in XLin:
    YLin.append(f(x))

plt.axis([a, b, ymin, ymax])
plt.plot(XLin, YLin, color='red', linewidth=4)
plt.scatter(XIntegral, YIntegral, color='blue', marker='.')
plt.scatter(XRectangle, YRectangle, color='yellow', marker='.')
plt.title("Numerical integration using MonteCarlo method")

plt.show()