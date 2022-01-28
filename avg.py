i=1
sum=0
sum2=2
avg=0
avg2=0
count1=0
count2=0
while i<=50:
    if i%2==0:
        count1=count1+1
        sum=sum+i
        avg=sum/count1
    elif i%2!=0:
        count2=count2+1
        sum2=sum2+i
        avg2=sum2/count2
    else:
        print("no avg")
    i+=1
print(sum)
print(sum2)
print(count1)
print(count2)
print(avg)
print(avg2)

