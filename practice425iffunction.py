# 1) check whether the user is eligible for voting or not
# 2) check whether a number entered by user is even or odd
# 3) check whether a number entered by user is negative or positive
# 4) find the lowest and higest number out of 3 numbers entered by the user (⛔ not done)
# 5) accept the total bill amount from the user and display the final amount after applying the discount
# Alt Text

# 6) write a Python program to calculate the total wage of a worker, which depends on the number of hours they worked. The worker earns Rs. 100 per hour, but if they work more than 40 hours, they will receive Rs. 200 for every extra hour.


# user_input = int(input("enter your age"))

# if user_input > 18:
#     print("elligible   :")
# else:
#     print("not elligible   :")

# user_input = int(input("enter any number   :"))

# if user_input % 2 == 0:
#     print("even")
# else:
#     print("odd")

# user_input = int(input("enter any number   :"))

# if user_input > 0:
#     print("positive")
# else:
#     print("negative")

# bill = int(input("enter your bill amount"))

# discount = 0


# if bill > 1000 and bill <= 2000:
#     discount = 2
# elif bill > 2000 and bill <= 5000:
#     discount = 5
# elif bill > 5000 and bill <= 10000:
#     discount = 10
# total_bill = bill - bill*discount/100

# if discount > 0:
#     print(f"total after discount bill is {total_bill}")
# else:
#     print(f"the bill is {total_bill}")


# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.


# salary = int(input("enter your salary    :"))
# years = int(input("enter the years of service    :"))

# salary_after_bouns_amount = salary + salary*5/100

# if years > 5:
#     print(f"you salary after bonus is {salary_after_bouns_amount}")
# else:
#     print(f"your salary is {salary}")


# Take values of length and breadth of a rectangle from user and check if it is square or not.

# length = int(input("enter length"))
# bredth = int(input("enter bregth"))

# if length == bredth:
#     print("its a square")
# else:
#     print("its not a square")


# Take two int values from user and print greatest among them.

# a = int(input("enter 1st   :"))
# b = int(input("enter 2nd   :"))

# if a > b:
#     print(f"{a}")
# else:
#     print(f"{b}")


# Write a program to print absolute vlaue of a number entered by user. E.g.-
# INPUT: 1        OUTPUT: 1
# INPUT: -1        OUTPUT: 1

# a = int(input("enter 1st   :"))


# if a < 0:
#     print(f"{a*-1}")
# else:
#     print(f"{a}")

# a = int(input("enter any number from 1 to 7"))

# if a == 1:
#     print("monday")
# elif a == 2:
#     print("tuesday")
# elif a == 3:
#     print("wednesday")


# email = "sonal1995pg@gmail.com"
# password = "sonal"

# email_user = input("enter you email")
# password_user = input("enter your password")

# if email == email_user and password == password_user:
#     print("correct email and password are correct")

# if email == email_user:
#     if password != password_user:
#         print("password is not correct")


# account_balance = 5000
# pin = 1234

# pin_user = int(input("enter your pin"))

# if pin == pin_user:
#     print("enter you choice 1. w to withdraw 2. d to depoist 3. c to check balance   :")
#     choice = input("enter your choice")

#     if choice == "w":
#         amount_to_withdraw = int(input("enter the amount   :"))
#         if amount_to_withdraw < account_balance:
#             account_balance -= amount_to_withdraw
#             print(f"sucessfull withdraw account balance is  :  {
#                   account_balance}")
#         else:
#             print("invalid amount")
#     elif choice == "d":
#         amount_to_deposit = int(input("enter the amount   :"))
#         if amount_to_deposit > 0:
#             account_balance += amount_to_deposit
#             print(f"sucessfull withdraw account balance is  :  {
#                   account_balance}")
#         else:
#             print("invalid amount")
#     elif choice == "c":
#         print(f"account balance is  :  {account_balance}")
#     else:
#         print("invalid amount")

# else:
#     print("entered pin is wrong")
