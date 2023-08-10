import random

# Definir la función de altura
def altura(x):
  return abs((x - 1) - (-x + 13))

# Definir el número de puntos a generar
n = 1000000

# Definir los límites del rectángulo
x_min = 1
x_max = 13
y_min = 0
y_max = 6

# Contar los puntos que caen dentro del triángulo
count = 0
for i in range(n):
  x = random.uniform(x_min, x_max)
  y = random.uniform(y_min, y_max)
  if y <= altura(x) and y >= 0:
    count += 1

# Calcular el área del triángulo
rect_area = (x_max - x_min) * (y_max - y_min)
tri_area = rect_area * count / n

# Imprimir el resultado
print(tri_area)