n = int(input(" enter the number : "))
m = int(input(" enter the number :  "))
# sum2 = n+m
# print(sum2)

if (n%2==0 and m%2==0):
    print(n+m)
elif(n%2==0 and m%2>0):
    print(n*m)
elif(n%2>0 and m%2==0):
    print(n/m)
else:
    print((n-m))