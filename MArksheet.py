marks=int(input("Enter the marks of the students:"))
if marks>100:
    print("Invalid Marks")
if marks>=85 and marks<=100:
    print("Grade A")
elif marks>=75 and marks<=84:
    print("Grade B")
elif marks>=55 and marks<=74:
    print("Grade C")
else:
    print("You Are Fail ! ")
