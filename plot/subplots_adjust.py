#!/usr/bin/env python

import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, sharex = True, sharey = True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(randn(500), bins = 50, color = 'k', alpha = 0.5)
plt.subplots_adjust(wspace = 0, hspace = 0.1)
plt.show()
