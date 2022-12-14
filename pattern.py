#pattern
a=int(4)
# c=2*(a-1)   #4
# for i in range (0,a):
#     for j in range (int(c)):
#         print(" ",end="")
#     c=c-2
#     for x in range ((2*i)+1):
#         print(" *",end="")
#     print("\n")

#Another Way

for i in range (a):
    print(" " * (a-i-1),end="")
    print("*" *((2*i)+1),end="")
    print(" "* (a-i-1))