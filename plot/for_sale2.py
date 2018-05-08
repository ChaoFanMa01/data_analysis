#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

# select chinese font.
myfont = font_manager.FontProperties(fname='/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf')

xcoor = np.arange(10, 101, 10)
degree_g = np.array([0.8, 0.86, 0.97, 1.09, 1.21, 1.34, 1.43, 1.6, 1.75, 1.78])
degree_gg = np.array([1.22, 1.38, 1.52, 1.6, 1.63, 1.7, 1.79, 1.83, 1.98, 2])
degree_s = np.array([1.09, 1.25, 1.46, 1.5, 1.53, 1.62, 1.72, 1.83, 1.91, 2.03])
degree_sg = np.array([1.4, 1.52, 1.6, 1.68, 1.75, 1.82, 1.95, 2.08, 2.17, 2.29])
cost_c = np.array([11.8, 17, 20, 23, 26, 26.5, 27.8, 29.3, 30.6, 31])
cost_f = np.array([13, 19, 24.3, 25, 29, 30.2, 30.8, 31.8, 32.6, 33.8])
cost_g = np.array([17, 24.5, 28.3, 31, 32.5, 33.7, 34.7, 35.6, 36.1, 36.8])
time_c = np.array([9, 18, 30, 42, 57, 80, 160, 220, 325, 460])
time_f = np.array([5, 10, 17, 25, 36, 47, 64, 100, 165, 249])
time_g = np.array([5, 8, 9, 10, 14, 18, 23, 27, 35, 48])

# figure on degree
'''
fig, ax = plt.subplots(1, 1)
ax.set_xticks(xcoor)
ax.set_xlabel(u'传感器节点数量', fontsize=15, fontproperties=myfont)
ax.set_ylabel(u'节点度', fontsize=15, fontproperties=myfont)
ax.bar(xcoor, degree_g, width = 1.5, facecolor = 'lightskyblue',
        edgecolor = 'white', label = r'Greedy')
ax.bar(xcoor + 1.5, degree_gg, facecolor = 'blue', edgecolor = 'white',
       label = r'Greedy-GPPS', width = 1.5)
ax.bar(xcoor + 3, degree_s, label = r'Shift', width = 1.5,
        facecolor = 'lime', edgecolor = 'white')
ax.bar(xcoor + 4.5, degree_sg, facecolor = 'orange', edgecolor = 'white',
       label = r'Shift-GPPS', width = 1.5)
plt.grid(axis = 'y', linestyle = '--', color = 'gray', linewidth = 1)
ax.legend(loc = 'best')
plt.show()
'''

# figure on cost
'''
fig, ax = plt.subplots(1, 1)
ax.set_xticks(xcoor)
ax.set_xlabel(u'传感器节点数量', fontsize=15, fontproperties=myfont)
ax.set_ylabel(u'部署中继节点数量', fontsize=15, fontproperties=myfont)
ax.bar(xcoor, cost_c, width = 1.5, facecolor = 'lightskyblue',
        edgecolor = 'white', label = r'CRNP')
ax.bar(xcoor + 1.5, cost_f, facecolor = 'blue', edgecolor = 'white',
       label = r'F1tRNP', width = 1.5)
ax.bar(xcoor + 3, cost_g, label = r'Grid', width = 1.5,
        facecolor = 'lime', edgecolor = 'white')
plt.grid(axis = 'y', linestyle = '--', color = 'gray', linewidth = 1)
ax.legend(loc = 'best')
plt.show()
'''

# figure on running time

fig, ax = plt.subplots(1, 1)
ax.set_yticks(np.arange(0, 500, 50))
ax.set_xticks(xcoor)
ax.set_xlabel(u'传感器节点数量', fontsize=15, fontproperties=myfont)
ax.set_ylabel(ur'执行时间 ($ms$)', fontsize=15, fontproperties=myfont)
ax.plot(xcoor, time_c, color = 'lightskyblue', marker = 'o',
        label = r'CRNP', linestyle = '--', linewidth = 3,
        markersize = 10)
ax.plot(xcoor, time_f, color = 'blue', marker = 'x', linestyle = '-.',
       label = r'F1tRNP', linewidth = 3, markersize = 10)
ax.plot(xcoor, time_g, label = r'Grid', marker = 'v',
        color = 'lime', linewidth = 3, markersize = 10)
ax.legend(loc = 'best')
plt.grid(axis = 'y', linestyle = '--', color = 'gray', linewidth = 1)
plt.show()
