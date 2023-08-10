__author__       = "Juan David Amezquita Nuñez"
__copyright__    = "Copyright 2023, USTA Tunja"
__credits__      = ["JF Mendoza"]
__license__      = "GPL"
__version__      = "1.0.0"
__maintainer__   = "Juan David Amezquita Nuñez"
__email__        = "juan.amezquita@usantoto.edu.co"
__status__       = "SUCCESSSSS!!!"

import math
import random
import numpy as np
import matplotlib.pyplot as plt

N = 100000       # Total
M = 0           # Exitos

# definir los puntos del triángulo
p1 = (1,0)
p2 = (7,6)
p3 = (13,0)

XTriangle = []    # Inner Triangle x-coordinate
YTriangle = []    # Inner Triangle y-coordinate

# encontrar los límites del rectángulo que encierra el triángulo
x_min = min(p1[0], p2[0], p3[0])
x_max = max(p1[0], p2[0], p3[0])
y_min = min(p1[1], p2[1], p3[1])
y_max = max(p1[1], p2[1], p3[1])

# generar puntos aleatorios y contar cuántos caen dentro del triángulo
for i in range(N):
    # generar un punto aleatorio dentro del rectángulo
    x = random.uniform(x_min, x_max)
    y = random.uniform(y_min, y_max)
    
    # comprobar si el punto está dentro del triángulo
    if (p2[0]-p1[0])*(y-p1[1])-(x-p1[0])*(p2[1]-p1[1]) > 0:
        continue
    if (p3[0]-p2[0])*(y-p2[1])-(x-p2[0])*(p3[1]-p2[1]) > 0:
        continue
    if (p1[0]-p3[0])*(y-p3[1])-(x-p3[0])*(p1[1]-p3[1]) > 0:
        continue
        
    # si el punto está dentro del triángulo, incrementar el contador
    XTriangle.append(x)
    YTriangle.append(y)
    M += 1

print(f"N = {N}, M = {M}")

# crear una figura y ejes
fig, ax = plt.subplots()

# trazar las líneas del triángulo
ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'b-') # línea de p1 a p2
ax.plot([p2[0], p3[0]], [p2[1], p3[1]], 'b-') # línea de p2 a p3
ax.plot([p3[0], p1[0]], [p3[1], p1[1]], 'b-') # línea de p3 a p1

# establecer límites de los ejes
ax.set_xlim([0, 14])
ax.set_ylim([-1, 7])

# calcular el área del triángulo como la fracción de puntos dentro del triángulo multiplicado por el área del rectángulo
rect_area = (x_max - x_min) * (y_max - y_min)
triangle_area = rect_area * (M / N)
print(f"Area {triangle_area}")


plt.axis('equal')
plt.grid(which = 'major')
plt.scatter(XTriangle, YTriangle, color='yellow', marker='.')
#plt.scatter(XSquare, YSquare, color='blue', marker='.')
plt.title('Monte Carlo Method for triangle area')
plt.show()
