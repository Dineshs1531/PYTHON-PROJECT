st=[["DINESH ",1000]]
def credit():
    amount=float(input("how many amount credit : "))
    st[0][1]=st[0][1]+amount
    print(st[0][1])
def debit():
    debitamount=float(input("how many amount debit : "))
    st[0][1]=st[0][1]-debitamount
    print("your debit amount : ",debitamount)
    remainingamount()
def remainingamount():
    print("your amount : ",st[0][1])
o=1234
print("WELCOME TO TATA ATM")
print("please insert the card")
pin=int(input("please enter the pin number: "))
if pin==o:
    while True:
        print("selected the choice 1.CREDIT 2.DEPOSIT 3.REMAINING AMOUNT 4.QUIT")
        choice=int(input("enter the choice : "))
        if choice==1:
            credit()
        elif choice==2:
            debit()
        elif choice==3:
            remainingamount()
        else:
            print("please enter the valid option")
        con=input("Do you want to continue press (yes) ")
        if con=="yes":
            continue
  
#i am simply created atm operation for one account
