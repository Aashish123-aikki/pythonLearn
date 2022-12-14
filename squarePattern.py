a=3
for i in range (a):
    if(i==0 or i==(a-1)):
        print("*" * a)
    else:
        print("*",end="")
        print(" "*(a-2),end="")
        print("*")