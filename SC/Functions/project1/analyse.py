# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 17:06:01 2014

@author: NSouthor
"""

import numpy as np
from matplotlib import pyplot as plt


def analyse(filename):
    ''' Takes an input file and creates mean, max and min plots for each one in the same figure '''    
    data=np.loadtxt(filename,delimiter=',')
    plt.figure(figsize=(10.0,3.0))

    plt.subplot(1,3,1)
    plt.ylabel('average')
    plt.xlabel('#days')
    plt.plot(data.mean(0))

    plt.subplot(1,3,2)
    plt.ylabel('min')
    plt.xlabel('#days')
    plt.plot(data.min(0))

    plt.subplot(1,3,3)
    plt.ylabel('max')
    plt.xlabel('#days')
    plt.plot(data.max(0))

    plt.tight_layout()
#    plt.show()
    
    
    plotName="inflammation1.png"
    plt.savefig(plotName, format="png")

 # run with analyse('inflammation-01.csv')
    