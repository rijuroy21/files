class bank:
    def __init__(self):
        self.pin=1234
        self.balance=2000
    def deposit(self):
        upin=int(input("Enter your pin to continue:"))
        if upin==self.pin:
            udep=int(input("Enter your deposit amount:"))
            self.balance=self.balance+udep
            print("Amount credited")
        else:
            print("Incorrect pin")
    def withdraw(self):
        upin=int(input("Enter your pin to continue:"))
        if upin==self.pin:
            uwid=int(input("Enter amount:"))
            self.balance=self.balance-uwid
            print("Amount withdrawed")
        else:
            print("Incorrect pin")            
    def blnc(self):
        upin=int(input("Enter your pin to continue:"))
        if upin==self.pin:
            print(self.balance)
        else:
            print("Incorrect pin")  
user1=bank()
while True:
    print('''
          1.Deposit
          2.Withdraw
          3.balance
          4.Exit''')
    choice=int(input("Enter your choice:"))
    if choice==1:
        user1.deposit()
    elif choice==2:
        user1.withdraw()
    elif choice==3:
        user1.blnc()
    elif choice==4:
        break            