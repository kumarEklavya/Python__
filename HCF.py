n1=int(input("Enter n1"))
n2=int(input("Enter n2"))
if n1<n2:
    small=n1
else:
    small=n2
for i in range (small,0,-1):
    if n1%i==0 and n2%i==0:
          print("HCF is ",i)
  
