acount_balance = 5000
pin = 1234

pin_user = int(input("Enter your pin "))


def withdraw(amount):
    global acount_balance
    if amount < acount_balance:
        acount_balance -= amount
        print(f"✅ withdrawal successfully, remaaining balance {
            acount_balance}")
    else:
        print("Insufficient balance ❌")


def deposit(amount):
    if amount >= 0:
        global acount_balance
        acount_balance += amount
        print(f"✅ deposit successfully, total balance {
            acount_balance}")
    else:
        print("Invalid deposit amount ❌")


def checkbalance():
    # global acount_balance
    print(f"your available balance {acount_balance}")


if pin == pin_user:
    print("Choices:\n\t1. type \"w\"for withdrawal\n\t2. type \"d\" for deposit\n\t3. type \"c\" for check balance\n\t4. type \"e\" for exit")
    while True:
        choice = input("Enter your choice ")
        if choice == "w":
            amount = int(input("Enter the amount "))
            withdraw(amount)

        elif choice == "d":
            amount = int(input("Enter the amount "))
            deposit(amount)

        elif choice == "c":
            checkbalance()

        elif choice == "e":
            print("Thankyou ✅✅")
            break
        else:
            print("❌ invalid choice ❌")

else:
    print("pin in incorrect ⛔")


while True:
    print("hello world")
