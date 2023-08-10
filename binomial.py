__author__       = "Juan David Amezquita Nuñez"
__copyright__    = "Copyright 2023, USTA Tunja"
__credits__      = ["JF Mendoza"]
__license__      = "GPL"
__version__      = "1.0.0"
__maintainer__   = "Juan David Amezquita Nuñez"
__email__        = "juan.amezquita@usantoto.edu.co"
__status__       = "In process"

import numpy as np
import matplotlib.pyplot as plt
    
n = 10   
N = 1000  
p = 0.5

P1 = np.random.binomial(n = n, p = p, size = N)

plt.plot(P1)
plt.show()

plt.figure()
plt.hist(x = P1, density = True, alpha = 0.8, histtype = 'bar', color = 'green', ec = 'black')
plt.show()