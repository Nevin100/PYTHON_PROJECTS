#ATM Simulator...
#DEFAULT BALANCE:1000,pin=1234
def pinj(a):
    if(a==1234):
        print("The PIN is correct!!!")
        K=True
        return K
   
    else:
        print("Wrong pin!!!!")
        K=False
        return K

Balance=1000.0

print("Welcome to the ATM simulator!!!!")
l=int(input("Enter your pin please:"))
C= pinj(l)

while (C==True):
    print("The Menu options are as follows:" )
    print("1.Check Balance:" )
    print("2.Deposit Money?:" )
    print("3.Withdraw Money:" )
    print("4.Exit")
    ch=int(input("Enter your choice:"))
    if (ch==1):
        print("Your Balance by default is: \t",Balance)
    
    elif (ch==2):
        money=float(input("Enter the Amount you want to deposit in your account:"))
        Balance+=money
        print("THE FiNAL BALANCE IS:",Balance)
    
    elif(ch==3):
        money1=int(input("Enter the amount you want to withdraw from the account"))
        
        if (money1>Balance):
            print("CAN'T DEDUCT... INSUFFICIENT BALANCE IN THE ACCOUNT")
        
        else:
            Balance=Balance-money1
            print("YOUR BALANCE AFTER WITHDRAWING",Balance,"YOUR AMOUNT:",money1)
            print("Thank you!!! HAVE A GREAT DAY AHEAD!")
                        
    elif(ch==4):
        print("EXITED SUCCESFULLY!!!!")
        print("Thank you!!! HAVE A GREAT DAY AHEAD!")
        break
    
    else:
        print("WRONG option")
        break
else:
    print("Sorry..")
    C==False
    
    
    