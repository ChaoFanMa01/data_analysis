#!/usr/bin/env python

import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt

data = randn(1000).cumsum()
data1 = randn(1000).cumsum()
data2 = randn(1000).cumsum()
data3 = randn(1000).cumsum()
fig, axes = plt.subplots(2, 2)
axes[0, 0].plot(data)
# set_xticks instructs matplotlib where to place the ticks along the 
# data range; by default these locations will also be labels.
axes[0, 1].set_xticks([0, 250, 500, 750, 1000])
# set_xticklabels set the labels located at previously determined points.
axes[0, 1].set_xticklabels(['one', 'two', 'three', 'four', 'five'],
                        rotation = 30, fontsize = 'small')
axes[0, 1].set_title('My first matplotlib plot')
axes[0, 1].set_xlabel('Stages')
axes[0, 1].plot(data)
axes[1, 0].plot(data1, 'k', label='one')
axes[1, 0].plot(data2, 'k--', label='two')
axes[1, 0].plot(data3, 'k.', label='three')
# you can either call ax.legend() or plt.legend() to automatically 
# create a legend. The loc tells matplotlib where to place the plot.
# If you are not picky 'best' is a good option, as it will choose a
# location that is most out of the way.
axes[1, 0].legend(loc='best')
plt.show()
