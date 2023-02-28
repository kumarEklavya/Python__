"reverse of a number"
n=int(input("Enter the value of n:- "))
rev=0
while(n>=1):
    r=n%10
    rev=rev*10+r
    n=n//10

print("Reverse number is ",rev)
