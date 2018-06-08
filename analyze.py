#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt

p = np.loadtxt('populated.dat')
for i in range(0,6):
    var = p[:,i]
    print('[{0}] mean, std = {1:9.6f}, {2:9.6f}'.format(i, np.mean(var), np.std(var)))

print('corr = \n', np.corrcoef(p[:,0:6], rowvar=False))
plt.figure(0)
plt.plot(p[:,4], p[:,5], '.')
plt.figure(1)
plt.hist(p[:,0],50)
plt.figure(2)
plt.hist(p[:,1],50)
plt.show()

