import numpy as np

arr = np.array([1.1, 2.1, 3.1])

new = arr.astype('i')
# new = arr.astype(bool)


print(new)
print(new.dtype)