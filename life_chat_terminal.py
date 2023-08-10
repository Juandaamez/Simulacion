import numpy as np
import os
import time

# Definir el tamaño de la cuadrícula
rows, cols = 50, 50

# Crear la cuadrícula
grid = np.random.randint(2, size=(rows, cols))

# Función para calcular la siguiente generación
def next_generation(grid):
    next_grid = np.copy(grid)
    for i in range(rows):
        for j in range(cols):
            neighbors = np.sum(grid[max(0, i-1):min(i+2, rows), max(0, j-1):min(j+2, cols)]) - grid[i, j]
            if grid[i, j] == 1:
                if neighbors < 2 or neighbors > 3:
                    next_grid[i, j] = 0
            else:
                if neighbors == 3:
                    next_grid[i, j] = 1
    return next_grid

# Bucle para actualizar la cuadrícula en cada iteración
for i in range(100):
    # Limpiar la consola
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Imprimir la cuadrícula actual
    for row in grid:
        for cell in row:
            if cell == 1:
                print(u"\u2588", end="")
            else:
                print(" ", end="")
        print()
    
    # Calcular la siguiente generación de células
    grid = next_generation(grid)
    
    # Esperar un tiempo para que se aprecie la evolución de la cuadrícula
    time.sleep(0.1)