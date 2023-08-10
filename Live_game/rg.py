__author__       = "Juan David Amezquita Nuñez"
__copyright__    = "Copyright 2023, USTA Tunja"
__credits__      = ["JF Mendoza"]
__license__      = "GPL"
__version__      = "1.0.0"
__maintainer__   = "Juan David Amezquita Nuñez"
__email__        = "juan.amezquita@usantoto.edu.co"
__status__       = "In process"

import numpy as np
import pandas as pd
import matplotlib as plt

class RG:
    def __init__(self) -> None:
        self._numbers = list()

    def LCG(self, a, c, m, x, terms):
        """ Linear Congruence Generator (LGC)
            x(k + 1) = (a * xk + c) mod m

        Args:
            a(int): Multiplier
            c(int): Incremente Constant
            m(int): Mode
            x(int): Seed
            terms: Number of random terms
        """
        for i in range(terms):
            x = np.mod(a * x + c, m)
            self._numbers.append(x) 

    def LLG(self, a, c, m, x, terms):
        """ Learmonth and Lewis generator (LLG)
            x(k + 1) = (a * xk + c) mod m

        Args:
            a(int): Multiplier
            c(int): Incremente Constant
            m(int): Mode
            x(int): Seed
            terms: Number of random terms
        """
        for i in range(terms):
            x = np.mod(a * x + c, m)
            self._numbers.append(x / m) 

    def Fibonacci(self, LV, CV, terms):
        """ Fibonacci (LFG)
            x(k + 1) = [x + x(k - 1)] mod m

        Args:
            NV = x(k + 1) = Next value
            CV = x        = Current value
            LV = x(k - 1) = Last Value
            terms: Number of random terms
        """
        for i in range(terms):
            NV = CV + LV
            LV = CV
            CV = NV
            self._numbers.append(LV) 

    def LFG(self, X0, X1, terms):
        """ Fibonacci (LFG)
            x(k + 1) = [x + x(k - 1)] mod m

        Args:
            NV = x(k + 1) = Next value
            CV = x        = Current value
            LV = x(k - 1) = Last Value
            terms: Number of random terms
        """
        m = 2**64
        for i in range (terms):
            X = np.mod(X0 + X1, m)
            X0 = X1
            X1 = X
            self._numbers.append(X)

    def LMMG(self, X0, X1, terms):
        self.LFG(X0, X1, terms)
        x1 = self._numbers[55]
        x2 = self._numbers[24]
        self._numbers = list()
        self.LFG(x1, x2, terms)

    def LLG_V(self, segments):
        generator.LLG(a = 75, c = 0, m = 2**31-1, x = 0.1, terms = 100)
        u = np.array(self._numbers)
        N = 100
        Ns = N / segments
        S = np.arange(0, 1, 0.05)
        counts = np.empty(S.shape, dtype=int)
        V = 0
        for i in range(0, 20):
            counts[i] = len(np.where((u >= S[i]) & (u < S[i] + 0.05))[0])
            V = V + (counts[i] - Ns) ** 2 / Ns

        print("R = ", counts)
        print("V =", V)

    def show_frequencies(self, r):
        Ypos = np.arange(len(r))
        plt.bar(Ypos, r)
        plt.show()


generator = RG()
#generator.LCG(a=2, c=4, m=5, x=3, terms=30)
generator.LLG(a=75, c=0, m=2**31 - 1, x=0.005, terms=100)
#generator.Fibonacci(LV = 0, CV = 1, terms=10)
#generator.LFG(X0 = 1, X1 = 1, terms=100)
#generator.LMMG(X0 = 1, X1 = 1, terms=200)
#generator.LLG_V(segments=20)

print(generator._numbers)