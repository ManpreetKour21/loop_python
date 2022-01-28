num=int(input("enter the number🥰🥰🥰🥰:-"))
i=num
while i>9:
    sum=0
    while i!=0:
        rem=i%10
        sum=sum+rem
        i=int(i/10)
    i=sum
if sum==1:
    print(num,"is a magic number")
else:
    print(num,"i__s a not magic number")