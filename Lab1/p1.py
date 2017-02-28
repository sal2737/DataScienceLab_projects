import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#empty array for appending of random samples
sampleArray1 = []
sampleArray2 = []
#specifications for non-standard normal distribution
sigma = 5
mu1 = -10
mu2 = 10

for sample in range(1000):
	sampleArray1.append(sigma * np.random.randn() + mu1)

for sample in range(1000):
	sampleArray2.append(sigma * np.random.randn() + mu2)

additiveArray = sampleArray1 + sampleArray2

plt.hist(additiveArray)
plt.title("Addition of two Gaussian distributions, (mu1 = -10, mu2 = 10, sigma = 5)")
plt.xlabel("Frequency")
plt.ylabel("Value")
plt.show()