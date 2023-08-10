import numpy as np
import os
import matplotlib.pyplot as plt

class ConwayLife:

    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._board = np.zeros((rows, cols))

    def initialize(self):
        row = -2
        while (row != -1):
            row = -2
            col = -2
            while row < -1 or row > self._rows:
                row = int(input(f"Row (1-{self._rows}, -1 to exit): "))
            if row >= 1:
                while col < 0 or col > self._cols:
                    col = int(input(f"Col (1-{self._cols}, -1 to exit): "))
                self._board[row - 1][col - 1] = 1
                self.print_matrix()


    def print_matrix(self):
        self.simulazao()

        os.system("cls")        # clear
        for row in range(self._rows):
            for col in range(self._cols):
                if self._board[row][col] == 0:
                    print("-", end="")
                elif self._board[row][col] == 1:
                    print("*", end="")

            print("")

    def simulazao(self):
        next_board = np.copy(self._board)
        # Recorrer todas las células de la cuadrícula
        for i in range(self._rows):
            for j in range(self._cols):
                neighbors = np.sum(self._board[max(0, i-1):min(i+2, self._rows), max(0, j-1):min(j+2, self._cols)]) - self._board[i, j]
                
                if self._board[i, j] == 1:
                    if neighbors < 2 or neighbors > 3:
                        next_board[i, j] = 0
                else:
                    if neighbors == 3:
                        next_board[i, j] = 1




life = ConwayLife(15, 15)
life.initialize()