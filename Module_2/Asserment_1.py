# from collections import defaultdict
#
# t =[1,5,6,5,1,2,3]
# d = defaultdict(int) # not wrong but ....!
#
# for i in t:
#     d[i] = d[i] + 1
#
# for y in d:
#     if d[y] > 1:
#      print(y)


n = int(input(" Enter the Rang : "))
t = []
for j in range(n):
    t.append(int(input(" Enter Number : ")))

N_d = []
D = []
for i in t:
    if i not in N_d:
        N_d.append(i)
    else:
        D.append(i)
print(D)

