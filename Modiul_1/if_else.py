n = int(input(" Enter thr value of N : "))
m = int(input(" Enter thr value of m : "))

if n % 2 == 0 and m % 2 == 0:
    sum1 = n + m
    print(" Sum of to number (n + m): ", sum1)
else:
    sum1 = n - m
    print(" minus of to number (n + m): ", sum1)
