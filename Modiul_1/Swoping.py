# a = 10
# b = 15
#
# a = a+b
# b = a-b
# a = a-b
#
# # print(" A = ", a," B = ",b)
# print(f"A = {a} B = {b}")  #f_string
#
a = int(input(" Enter the value A : "))
b = int(input(" Enter the value  B : "))

temp = a
a = b
b = temp
print(" A = ",a, "\n"," B = ",b )
