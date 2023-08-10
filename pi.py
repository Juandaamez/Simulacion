import math
import random
import numpy as np
import matplotlib.pyplot as plt

N = 100000       # Total
M = 0           # Exitos
XCircle = []    # Inner circle x-coordinate
YCircle = []    # Inner circle y-coordinate
XSquare = []    # Outter circle x-coordinate
YSquare = []    # Outter circle y-coordinate

for _ in range (N):
    x = random.random()
    y = random.random()

    if x**2 + y**2 <= 1:
        M += 1
        XCircle.append(x)
        YCircle.append(y)
    else:
        XSquare.append(x)
        YSquare.append(y)

Pi = 4 * M / N
print(f"N = {N}, M = {M}, Pi = {Pi}")

XLin = np.linspace(0, 1)
YLin = []

for x in XLin:
    YLin.append(math.sqrt(1-x**2))

plt.axis('equal')
plt.grid(which = 'major')
plt.scatter(XCircle, YCircle, color='yellow', marker='.')
plt.scatter(XSquare, YSquare, color='blue', marker='.')
plt.plot(XLin, YLin, color='red', linewidth='4')
plt.title('Monte Carlo Method for Pi estimation')
plt.show()


