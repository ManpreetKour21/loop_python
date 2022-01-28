# x=int(input("enter the number"))
# print("factors of ",x,"is:")
# for i in range (1,x+1):
#     if X%i==0:
#         print(i)


n=int(input("enter factors number="))
i=1
while i<=n:
    if n%i==0:
        print(i)
    i+=1