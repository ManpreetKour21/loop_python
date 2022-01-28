num=int(input("enter the number:-"))
s=0
temp=num
while temp>0:
    f=1
    i=1
    rem=temp%10
    while i<=rem:
        f=f*i
        i=i+1
    s=s+f
    temp=temp//10
if s==num:
    print("strong number")
else:
    print("not strong")
    