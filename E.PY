for row in range (7):
    for cal in range (4):
        if (row==0 or row==3 or row==6)or((cal==0)and(row!=0 and row!=3 and row!=6)):
            print("*",end=" ")
        else:
            print(end=" ")
    print()

# i=4
# row=0
# cal=0
# while i<=4:
#     if row==0 or row==3 or row==6 or cal==0 and row!=0 and row!=3 and row!=6:
#         print("*",end=" ")
#     else:
#         print(end=" ")
# print()
# i+=1


# sum=0
# n=int(input("enter the number"))
# c=0
# while c>0:
#     r=c%10
#     sum=sum+r
#     c=c//10
#     c
# if n%sum==0:
#     print("harsad number")
# else:
#     print("not harsad")
    

