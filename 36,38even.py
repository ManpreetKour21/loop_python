num=int(input("enter the number:-"))
i=1
while i<=num:
    if num%2==0:
        a=num-2
        b=a-2
        print(a)
        print(b)
        break
    elif num%2!=0:
        a=num+2
        b=a+2
        print(a)
        print(b)
        break
    i+=1

# n=int(input("enter the number of rows:-"))
# for i in range(n):
#     print((chr(65+i)+"")*(i+1))