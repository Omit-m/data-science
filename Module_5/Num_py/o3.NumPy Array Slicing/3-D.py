# import numpy as np
#
# arr=np.array([[[10,20,30],[40,50,60]],[[100,200,300],[400,500,600]]])
# # print(arr[1,1]) # 01
# print(arr[1,1,0:3]) # 02 (01 and 02 are same element print


import numpy as np

arr = np.array(([[[10,20,30],[40,50,60]],[[100,200,300],[400,500,600]]]))

# print(arr[0:2,1:2 ,0:2]) # [ paction, block,element ]
print(arr[0:2,1:2 ,0:2])
