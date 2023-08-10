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
import seaborn as sns

N = 1000

mu = 10
sigma = 2
P1 = np.random.normal(mu, sigma, N)

mu = 5
sigma = 2
P2 = np.random.normal(mu, sigma, N)

mu = 15
sigma = 2
P3 = np.random.normal(mu, sigma, N)

mu = 10
sigma = 2
P4 = np.random.normal(mu, sigma, N)

mu = 10
sigma = 1
P5 = np.random.normal(mu, sigma, N)

mu = 10
sigma = 0.5
P6 = np.random.normal(mu, sigma, N)

plot1 = sns.distplot(P1) 
plot2 = sns.distplot(P2) 
plot3 = sns.distplot(P3)

plt.figure()

plot4 = sns.distplot(P4)
plot5 = sns.distplot(P5)
plot6 = sns.distplot(P6)

plt.show()


