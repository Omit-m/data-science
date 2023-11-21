
"""
np.searchsorted is aNumPy function used to find the indices where elements should be
inserted to maintain the array  sorted order. It performs a  binary search and
returns the index location(s) where the specified values can be inserted in the array.
"""

import numpy as np

arr = np.array([7, 6, 8, 9])

x = np.searchsorted(arr, 5)
print(x)






