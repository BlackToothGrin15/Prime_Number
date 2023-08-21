n=int(input("Enter a no:"))
f=0
for i in range(1,n+1):
    if n%i==0:
        f+=1
if f==2:
    print("The no. is prime")
else:
    print("The no. is not prime")
