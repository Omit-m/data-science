'''
Generate an array of 100 linearly spaced points between 50 and 60

Then convert the vector array to matrix array by (10, 10)

Then perform the operation, array % 5 == 0
'''

import numpy as np

array = np.linspace(50, 60, 100)
matrix = array.reshape(10, 10)


result = matrix % 5 == 0
print(result)
