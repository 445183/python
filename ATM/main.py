class ATM_simulator:
    def __init__(self,user_name,pin,balance):
        self.user=user_name
        self.pin=pin
        self.bal=balance

    def withdraw_cash(self):
        user=input("Enter your username: ")
        pin=input("Enter your pin: ")
        
        print("")

        if pin==self.pin and user==self.user:
            amount=int(input("Enter the amount you would like to withdraw: "))
            print("")

            if amount<=self.bal:
                self.bal=self.bal-amount
                print("Cash withdrawn successfully ,$ ",amount,".")
            else:
                print("Your balance isn't enough to withdraw money !")

        else:
            print("Your username or pin seems to be incorrect !")

    def deposit_cash(self):
        user=input("Enter your username: ")
        pin=input("Enter your pin: ")

        print("")

        if pin==self.pin and user==self.user:
            amount=int(input("Enter the amount you would like to deposit: "))

            print("")

            self.bal=self.bal+amount
            print("Cash deposited successfully ,$ ",amount,".")

        else:
            print("Your username or pin seems to be incorrect !")

    def see_balance(self):
        user=input("Enter your username: ")
        pin=input("Enter your pin: ")
        
        print("")

        if pin==self.pin and user==self.user:
            print("Your current balance is, $ ",self.bal)
        else:
            print("Your username or pin seems to be incorrect !")

print("Welcome to IDBA bank !")

print("")

user=input("Enter you username: ")
pin=input("Enter your pin code: ")
bal=int(input("Enter your balance :"))

newUser=ATM_simulator(user,pin,bal)

while True:
    print("")

    print("If you have a account enter,")
    print("'see' to see your balance ;")
    print("'deposit' to deposit money ;")
    print("'withdraw' to withdraw money .")

    print("")
    a=input("")
    print("")

    if a=="see":
        newUser.see_balance()
    elif a=="deposit":
        newUser.deposit_cash()
    elif a=="withdraw":
        newUser.withdraw_cash()