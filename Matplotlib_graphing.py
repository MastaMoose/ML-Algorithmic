# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 21:25:55 2018
Purpose: Just the pyplot/matplotlib turotial
@author: Mustafa
"""

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X,C)
plt.plot(X,S)

plt.show()