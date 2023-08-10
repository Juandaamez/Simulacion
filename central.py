import random
import numpy as np
import matplotlib.pyplot as plt

a = 1
b = 100
N = 10000

DataPop = list(np.random.uniform(a, b, N))

plt.hist(DataPop, density=True, histtype='stepfilled', alpha=0.2)
plt.show()

SampleMeans = []

for _ in range (100):
    DataExtracted = random.sample(DataPop, k=100)
    DataExtractedMean = np.mean(DataExtracted)
    SampleMeans.append(DataExtractedMean)

plt.figure()
plt.hist(SampleMeans, density=True, histtype='stepfilled', alpha=0.2)

plt.show()
