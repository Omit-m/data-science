import numpy as np
arr=np.array([10,30,50,60,70])

x=arr.copy()
y=arr.view()

print(x.base)
print(y.base)