n=int(input("Enter the value of n : "))
def fact():
    fact=1
    for i in range(1,n+1,1):
        fact=fact*i
    return fact
print("Factorial of a given number is : ",fact())
