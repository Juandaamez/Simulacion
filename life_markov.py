__author__       = "Juan David Amezquita Nuñez"
__copyright__    = "Copyright 2023, USTA Tunja"
__credits__      = ["JF Mendoza"]
__license__      = "GPL"
__version__      = "1.0.0"
__maintainer__   = "Juan David Amezquita Nuñez"
__email__        = "juan.amezquita@usantoto.edu.co"
__status__       = "Successss"

import numpy as np
import matplotlib.pyplot as plt

# Inicializar la cuadrícula con valores aleatorios
grid = np.random.randint(2, size=(10, 10))

def next_generation(grid, prev_grid, transition_matrix):
    # Copiar la cuadrícula actual para la siguiente generación
    next_grid = np.copy(grid)
    
    # Recorrer todas las células de la cuadrícula
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            # Obtener el estado actual y anterior de la célula
            current_state = grid[i, j]
            prev_state = prev_grid[i, j]
            
            # Calcular la probabilidad de transición
            transition_prob = transition_matrix[prev_state, current_state]
            
            # Imprimir la probabilidad de transición
            print(f'Cell ({i}, {j}): {transition_prob}')
            
            # Actualizar el estado de la célula en la siguiente generación
            next_grid[i, j] = np.random.choice([0, 1], p=transition_prob)
    
    return next_grid

# Inicializar la cuadrícula con valores aleatorios
grid = np.random.randint(2, size=(10, 10))
prev_grid = np.copy(grid)

# Definir la matriz de transición
transition_matrix = np.array([[[0.7, 0.3], [0.2, 0.8]], [[0.6, 0.4], [0.1, 0.9]]])

# Crear una figura para mostrar la gráfica
fig = plt.figure()

# Bucle para actualizar la cuadrícula y mostrar el resultado en una gráfica
for i in range(100):
    # Calcular la siguiente generación de células
    grid = next_generation(grid, prev_grid, transition_matrix)
    
    # Actualizar el estado de la cuadrícula en la generación anterior
    prev_grid = np.copy(grid)
    
    # Limpiar la figura anterior y mostrar la nueva cuadrícula
    plt.clf()
    plt.imshow(grid, cmap='binary')
    plt.pause(10)