num=int(input("enter the number:-"))
i=1
while i<=num:
    if num%4==0:
        a=num-4
        b=a-4
        print(a)
        print(b)
        break
    elif num%4!=0:
        a=num+4
        b=a+4
        print(a)
        print(b)
        break
    i+=1