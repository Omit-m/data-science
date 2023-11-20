import numpy as np
arr=np.array([10,30,50,60,70])

x=arr.copy()
y=arr.view()

print(x.base) # none becouse (x.base  says that  its  my data)
print(y.base) # [10,30,50,60,70] (y.base will refer to the original array )