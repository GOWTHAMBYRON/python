# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 16:39:19 2025

@author: admin
"""

import numpy as np

a = np.arange(1,6)
print("The Array:",a,"\nAnd its type :", type(a))

print("Size of array:",a.size)
print("Dimension of array:",a.ndim)

print("Sum of elements:", np.sum(a))
print("Mean of elements:", np.mean(a))
print("Minimum value:", np.min(a))
print("Maximum value:", np.max(a))