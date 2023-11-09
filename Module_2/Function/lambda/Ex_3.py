def myfunc(n):
  return lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(10))
print(mytripler(5))