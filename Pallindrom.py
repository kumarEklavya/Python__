
n=int(input("Enter the value of n "))
rev=0
temp=0
while(n>=1):
     r=n%10
     rev=rev*10+r
     n=n+1
     print("reverse of number is :",rev)
if(temp==reverse):
    print("It is a pallindrom number")
else:
    print("Not a pallindrom number")

