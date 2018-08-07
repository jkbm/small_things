import matplotlib.pyplot as plt
import numpy as np
from math import exp

"""
loc, scale = 10, 1
s = np.random.logistic(loc, scale, 10000)
count, bins, ignored = plt.hist(s, bins=50)
def logist(x, loc, scale):
     return exp((loc-x)/scale)/(scale*(1+exp((loc-x)/scale))**2)
plt.plot(bins, logist(bins, loc, scale)*count.max()/logist(bins, loc, scale).max())
plt.show()
"""

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()