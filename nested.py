i=1
while i<=5:
    j=1
    while j<=3:
        print(j)
        j+=1
    i+=1

i=1
while i<=3:
    j=2
    while j<=5:
        print(j+2)
        j+=1
    print()
    i+=1

i=1
while i<=10:
    if i<=6:
        print(i)
    elif i==9 and i==10:
        print(i)
    else:
        print("*")

i=1
while i<=10:
    if i>=3 and i<=8:
        print("*")
    else:
        print(i)
    i+=1