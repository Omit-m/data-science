import numpy as np

arr=np.array([10,20,30])
# print(arr[2]) # only one element print
# print(arr[0:]) # print all element  , [start:End]
# print(arr[0:3]) # print element [10,20,30]
# print(arr[:2]) # [:End]

print(arr[0:4:2]) # [start:End:step]

# We pass slice instead of index like this: [start:end].

# We can also define the step, like this: [start:end:step].

