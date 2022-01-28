n=int(input("enter the number:-"))
sum=0
i=1
while i<n:
    if n%i==0:
        sum=sum+1
    i+=1
if n==sum:
    print(i,"perfet number")
else:
    print(i,"not perfet number")
    