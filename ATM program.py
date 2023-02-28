Balance=10000
Withdraw=int(input("Enter the amount"))
if Balance>Withdraw:
    print("Transition Successfull")
    Balance=Balance-Withdraw
    print("Avalable amount is ",Balance)

else:
    print("Insufficient Balance")
    print("Thankyou")
