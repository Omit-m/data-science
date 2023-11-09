from collections import defaultdict

t =[1,5,6,5,1,2,3]
d = defaultdict(int)

for i in t:
    d[i] = d[i] + 1

for y in d:
    if d[y] > 1:
     print(y)

