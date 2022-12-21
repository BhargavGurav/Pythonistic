import csv
import time
from playsound import playsound


class Atm:
    all = []

    def __init__(self, name: str, pin: int, balance: float):
        assert pin >= 1000, "PIN code cannot be less than 4 digit"
        assert balance >= 0, "Balance should be greater than equal to 0"
        self.name = name
        self.pin = pin
        self.balance = balance

        Atm.all.append(self)

    def printBalance(self):
        return self.balance

    @classmethod
    def getDataFromFile(cls):
        with open(r"F:\Bhargav_Data\Documents\coding_programmes\PyCharm Community Edition 2021.2.3\atmdata.csv", 'r') as f:
            reader = csv.DictReader(f)
            members = list(reader)

        for x in members:
            Atm(
                name=x.get('name'),
                pin=int(x.get('pin')),
                balance=float(x.get('balance'))
            )

    def __repr__(self):
        return f"Name: {self.name}    PIN: {self.pin}"


Atm.getDataFromFile()
for x in Atm.all:
    pass


def valid_user():
    userpin = int(input("Enter PIN: "))
    for x in Atm.all:
        if userpin == x.pin:
            return 1
        else:
            return 0


print("------------------------------------------------------------")
print("|                                                           |")
print("|                   Welcome to ATM                          |")
print("|                 Operations Available                      |")
print("|   1. Balance Check                                        |")
print("|   2. Withdraw money                                       |")
print("|   3. Add money                                            |")
print("------------------------------------------------------------")

while True:
    choice = int(input("\nEnter operation number: "))
    if choice == 1:
        userpin = int(input("Enter PIN: "))
        for x in Atm.all:
            if userpin == x.pin:
                print("Hello ", x.name, " Your balance is: ", x.printBalance(), " Rs")
                break
            else:
                print("No data found!")
                playsound("C:\\Users\\Haresh\\Downloads\\alert.mp3")
                break


    elif choice == 2:
        userpin = int(input("Enter PIN: "))
        for x in Atm.all:
            if userpin == x.pin:
                print(f"Hello {x.name}")
                wishmoney = int(input("How much do you want: "))
                if wishmoney <= x.balance:
                    print("Processing please wait!")
                    time.sleep(5)
                    print("Collect money")
                    x.balance = x.balance - wishmoney
                    time.sleep(5)
                    break
                elif x.balance > 0:
                    print("you have only ", x.balance, " Rs")
                    ch = input("Want to continue? y->yes : ")
                    if ch == 'y' or ch == 'Y':
                        wishmoney = int(input("Enter amount to withdraw : "))
                        time.sleep(5)
                        print("Collect money")
                        x.balance = x.balance - wishmoney
                        time.sleep(5)
                        break
                else:
                    print("Sorry your balance is over")

            else:
                print("No data found!")
                playsound("C:\\Users\\Haresh\\Downloads\\alert.mp3")
                break

    else:
        userpin = int(input("Enter PIN: "))
        for x in Atm.all:
            if userpin == x.pin:
                print(f"Hello {x.name}")
                adder = float(input("Enter how much you wanna add: "))
                x.balance = x.balance + adder
                print("Added successfully.")
                break
            else:
                print("No data found")
                playsound("C:\\Users\\Haresh\\Downloads\\alert.mp3")
                break


"""
atmdata.csv 

name,pin,balance
"Bhargav Gurav",8003,75000
"Haresh Gurav",7961,10000

"""