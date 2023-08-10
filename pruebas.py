import matplotlib.pyplot as plt

# definir los puntos del triángulo
p1 = (1,0)
p2 = (7,6)
p3 = (13,0)

# crear una figura y ejes
fig, ax = plt.subplots()

# trazar las líneas del triángulo
ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'b-') # línea de p1 a p2
ax.plot([p2[0], p3[0]], [p2[1], p3[1]], 'b-') # línea de p2 a p3
ax.plot([p3[0], p1[0]], [p3[1], p1[1]], 'b-') # línea de p3 a p1

# establecer límites de los ejes
ax.set_xlim([0, 14])
ax.set_ylim([-1, 7])

# mostrar la figura
plt.show()





