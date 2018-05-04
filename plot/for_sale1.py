#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

# select chinese font.
myfont = font_manager.FontProperties(fname='/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf')

xcoor = np.arange(10, 101, 10)
cost_spt12 = np.array([19, 24.2, 23.9, 23.6, 23.5, 20.1, 18.8, 17.9, 
                      17.5, 15.8])
cost_spt15 = np.array([12.2, 14, 14.3, 13.8, 13.9, 12.2, 11.9, 10.5, 
                      9.5, 8.3])
cost_my12 = np.array([17.6, 22.3, 21.1, 20, 19.6, 17.2, 14.5, 13.5,
                      13.2, 12.9])
cost_my15 = np.array([11.8, 12.9, 13.4, 13.1, 12.8, 11.3, 10.3, 8.9, 
                      8, 6.3])
time_spt12 = np.array([0.2, 0.23, 0.24, 0.25, 0.27, 0.48, 0.75, 0.84,
                      0.92, 1.03])
time_spt15 = np.array([0.2, 0.23, 0.24, 0.25, 0.26, 0.32, 0.434, 0.53,
                      0.52, 0.54])
time_my12 = np.array([0.2, 0.23, 0.24, 0.25, 0.27, 0.34, 0.43, 0.535,
                      0.52, 0.55])
time_my15 = np.array([0.2, 0.23, 0.24, 0.245, 0.25, 0.3, 0.4, 0.44,
                      0.48, 0.51])
delay_spt12 = np.array([12.5, 14, 14.2, 14.6, 14.8, 14.9, 15, 15,
                      14.9, 15])
delay_spt15 = np.array([14.2, 15.1, 16.2, 17, 17.3, 17.4, 17.5, 17.5,
                      17.8, 17.7])
delay_arnpc = np.array([19.8, 25.7, 30.2, 32, 34, 35, 35.3, 35.4,
                      37, 39.8])
delay_my12 = np.array([12.6, 13.8, 14, 14.5, 14.8, 14.8, 14.9, 15,
                      14.8, 15])
delay_my15 = np.array([14, 15, 16.1, 17, 17, 17.2, 17.1, 17.2, 17.4,
                      17.5])
reliable_spt12 = np.array([0.855, 0.845, 0.83, 0.823, 0.83, 0.857,
                      0.825, 0.823, 0.83, 0.836])
reliable_spt15 = np.array([0.83, 0.827, 0.823, 0.82, 0.824, 0.83,
                      0.822, 0.823, 0.824, 0.826])
reliable_arnpc = np.array([0.86, 0.847, 0.858, 0.826, 0.81, 0.812, 
                      0.803, 0.82, 0.78, 0.75])
reliable_my12 = np.array([0.846, 0.858, 0.853, 0.847, 0.853, 0.849,
                      0.848, 0.851, 0.846, 0.834])
reliable_my15 = np.array([0.842, 0.854, 0.85, 0.841, 0.85, 0.845, 0.842,
                     0.847, 0.841, 0.83])

# figure on cost comparison

fig, ax = plt.subplots(1, 1)
ax.set_xticks(xcoor)
ax.set_xlabel(u'传感器节点数量', fontsize=15, fontproperties=myfont)
ax.set_ylabel(u'部署中继节点数量', fontsize=15, fontproperties=myfont)
ax.bar(xcoor, cost_spt12, width = 1.5, facecolor = 'lightskyblue',
        edgecolor = 'white', label = r'SPTiRP $\Delta = 12$')
ax.bar(xcoor + 1.5, cost_spt15, facecolor = 'blue', edgecolor = 'white',
       label = r'SPTiRP $\Delta = 15$', width = 1.5)
ax.bar(xcoor + 3, cost_my12, label = r'SPLS $\Delta = 12$', width = 1.5,
        facecolor = 'lime', edgecolor = 'white')
ax.bar(xcoor + 4.5, cost_my15, facecolor = 'orange', edgecolor = 'white',
       label = r'SPLS $\Delta = 15$', width = 1.5)
plt.grid(axis = 'y', linestyle = '--', color = 'gray', linewidth = 1)
ax.legend(loc = 'best')
plt.show()


# figure on running time
'''
fig, ax = plt.subplots(1, 1)
ax.set_xticks(xcoor)
ax.set_xlabel(u'传感器节点数量', fontsize=15, fontproperties=myfont)
ax.set_ylabel(ur'执行时间 ($ms$)', fontsize=15, fontproperties=myfont)
ax.plot(xcoor, time_spt12, color = 'lightskyblue', marker = 'o',
        label = r'SPTiRP $\Delta = 12$', linestyle = '--', linewidth = 3)
ax.plot(xcoor, time_spt15, color = 'blue', marker = 'x', linestyle = '-.',
       label = r'SPTiRP $\Delta = 15$', linewidth = 3)
ax.plot(xcoor, time_my12, label = r'SPLS $\Delta = 12$', marker = 'v',
        color = 'lime', linewidth = 3)
ax.plot(xcoor, time_my15, color = 'orange', marker = '|', linestyle = ':',
       label = r'SPLS $\Delta = 15$', linewidth = 3)
ax.legend(loc = 'best')
plt.grid(axis = 'y', linestyle = '--', color = 'gray', linewidth = 1)
plt.show()
'''

# figure on end-to-end delay
'''
fig, ax = plt.subplots(1, 1)
ax.set_xticks(xcoor)
ax.set_xlabel(u'传感器节点数量', fontsize=15, fontproperties=myfont)
ax.set_ylabel(ur'端到端时延 ($ms$)', fontsize=15, fontproperties=myfont)
ax.plot(xcoor, delay_spt12, color = 'lightskyblue', marker = 'o',
        label = r'SPTiRP $\Delta = 12$', linestyle = '--', linewidth = 3,
        markersize = 10)
ax.plot(xcoor, delay_spt15, color = 'blue', marker = 'x', linestyle = '-.',
       label = r'SPTiRP $\Delta = 15$', linewidth = 3, markersize = 10)
ax.plot(xcoor, delay_my12, label = r'SPLS $\Delta = 12$', marker = 'v',
        color = 'lime', linewidth = 3, markersize = 10)
ax.plot(xcoor, delay_my15, color = 'orange', marker = '|', linestyle = ':',
       label = r'SPLS $\Delta = 15$', linewidth = 3, markersize = 10)
ax.plot(xcoor, delay_arnpc, color = 'fuchsia', marker = 'p', markersize = 10, label = r'ARNPC', linewidth = 3)
ax.legend(loc = 'best')
plt.grid(axis = 'y', linestyle = '--', color = 'gray', linewidth = 1)
plt.show()
'''

# figure on reliable
'''
fig, ax = plt.subplots(1, 1)
plt.ylim((0.6, 1))
ax.set_xticks(xcoor)
ax.set_yticks(np.arange(0.6, 1.01, 0.05))
ax.set_xlabel(u'传感器节点数量', fontsize=15, fontproperties=myfont)
ax.set_ylabel(ur'收包率 (%)', fontsize=15, fontproperties=myfont)
ax.bar(xcoor, reliable_spt12, width = 1.5, facecolor = 'lightskyblue',
        edgecolor = 'white', label = r'SPTiRP $\Delta = 12$')
ax.bar(xcoor + 1.5, reliable_spt15, facecolor = 'blue', edgecolor = 'white',
       label = r'SPTiRP $\Delta = 15$', width = 1.5)
ax.bar(xcoor + 3, reliable_my12, label = r'SPLS $\Delta = 12$', width = 1.5,
        facecolor = 'lime', edgecolor = 'white')
ax.bar(xcoor + 4.5, reliable_my15, facecolor = 'orange', edgecolor = 'white',
       label = r'SPLS $\Delta = 15$', width = 1.5)
ax.bar(xcoor + 6, reliable_arnpc, facecolor = 'fuchsia', edgecolor = 'white', label = r'ARNPC ', width = 1.5)
ax.legend(loc = 'best')
plt.grid(axis = 'y', linestyle = '--', color = 'lightgray', linewidth = 1)
plt.show()
'''
