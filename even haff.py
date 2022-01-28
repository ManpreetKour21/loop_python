user=int(input("enter the number:-"))
if user%2==0:
    i=1
    while i<=user:
        print(user)
        i+=1
else:
    i=0
    while i<user//2:
        print(user)
        i+=1
