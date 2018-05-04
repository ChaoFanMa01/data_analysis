#!/usr/bin/env python

import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt

data1 = randn(30).cumsum()
data2 = randn(30).cumsum()
data3 = randn(30).cumsum()

fig, axes = plt.subplots(2, 2)

axes[0, 0].plot(data1, 'ko--')
axes[0, 1].plot(data2, color = 'r', linestyle = 'dashed', marker = 'o')
axes[1, 0].plot(data3, 'k-', drawstyle = 'steps-post', label = 'steps-post')
axes[1, 0].plot(data3, 'ro--')
#axes[1, 1].plot(np.arange(30), data3, 'k--', np.arange(30), data3, drawstyle = 'steps-post')

plt.show()
