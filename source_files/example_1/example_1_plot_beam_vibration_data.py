#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 16:05:28 2019

@author: austin
"""


import IPython as IP
IP.get_ipython().magic('reset -sf')

import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.close('all')

#%% Load and plot data
D = np.loadtxt('vibration_data/Vibration_measurement.txt',skiprows=23)

tt = D[:,0]
ac = D[:,1]

plt.figure(figsize=(6.5,3))
plt.plot(tt,ac,'-',label='test 1')
plt.plot(tt+0.1,ac,'--',label='test 1')
plt.plot(tt+0.2,ac,':',label='test 1')
plt.plot(tt+0.3,ac,'-.',label='test 1')
plt.grid(True)
plt.xlabel('time (s)')
plt.ylabel('acceleration (m/s$^2$)')
plt.legend(loc=2)
plt.tight_layout()
plt.savefig('example_1_150.png',dpi=150)
plt.savefig('example_1_300.png',dpi=300)
plt.savefig('example_1_pdf.pdf')




#
#tt = D[:,0]
#dd = D[:,1]
#
#plt.figure('beam data',figsize=(6.5,3))
#plt.plot(tt,dd,'-',label='data 1')
#plt.grid(True)
#plt.xlabel('time (s)')
#plt.ylabel('acceleration (ms$^2$)')
#plt.title('beam data')
#plt.xlim([-0.1,45])
#plt.legend(framealpha=1,loc=0)
#plt.tight_layout()
#plt.savefig('plot.pdf')
#plt.savefig('plot_1.png')
#plt.savefig('plot_2.png',dpi=300)





























































