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

a = 1     # Lower limit
b = 100   # Upper limit
N = 100   # Number of items

X1 = np.random.gamma(a, b, N)

#plt.plot(X1)
#plt.show()

plt.figure()
plt.hist(x = X1, density = True, histtype = 'stepfilled', alpha = 0.2)
plt.show()
