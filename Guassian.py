# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 17:36:37 2018

@author: Mustafa
"""

import pylab as pl
import numpy as np
import math

#gaussian = lambda x: math.exp(-(0.5-x)**2/1.5)
def g(x):
    return math.exp(-(0.5-x)**2/1.5)
    
x = np.arange(-2,2.5,0.01)
#y = gaussian(x)
y = g(x)
pl.ion()
pl.figure()
pl.plot(x,y)
pl.xlabel('x values')
pl.ylabel('exp(..)')
pl.title('Guassian function')
pl.show()