# 1) check whether the user is eligible for voting or not

# age = int(input("enter your age  : "))

# if age >= 18 and  age <= 100:
#     print("eligible for voting")
# else:
#     print( "non eligible")


# 2 check whether a number entered by user is even or odd

# number = int(input("enter any number"))

# if number % 2 == 0:
#     print("the number is even")
# else :
#     print("the number is odd")


# 3  check whether a number entered by user is negative or positive

# number = int(input("enter any number"))

# if number > 0:
#     print("the number is positive")
# elif number == 0:
#     print("the number is zero")
# else:
#     print("the number is negative")


# 4write a Python program to calculate the total wage of a worker,
# #which depends on the number of hours they worked. The worker earns Rs. 100 per hour,
# # but if they work more than 40 hours, they will receive Rs. 200 for every extra hour.

# hours = int(input("enter the no of hours worked  :"))

# if hours <= 40 :
#     wage = hours*100
#     print(f"your wage is {wage}")
# elif hours >40:
#     wage_extra = 40*100 + (hours- 40)*200
#     print(f"your wage is {wage_extra}")
# else:
#     print("entered hours cant calculate")


# total_bill = int(input("enter the total bill"))
# discount = 0

# if total_bill >= 1000 and total_bill <=2000:
#     discount = 2
# elif total_bill > 2000 and total_bill <=5000:
#     discount = 5
# elif total_bill > 5000 and total_bill <=10000:
#     discount = 10
# elif total_bill >= 10000 and total_bill <=50000:
#     discount = 15
# else:
#     print("no discount")

# if discount > 0:
#  total_bill= total_bill - (discount/100*total_bill)
#  print(f"your bill after dis {total_bill}")
# else:
#  print(f"your bill is {total_bill}")


# student_name =input("enter your name: ")
# e=int(input("marks in e:"))
# h=int(input("marks in h:"))
# m=int(input("marks in m:"))

# avg = (e+h+m)/3

# if avg >= 80 and avg <100:
#     print("A")
# elif avg>= 50 and avg <80:
#     print("B")
# elif avg >= 30 and avg < 50:
#     print("C")
# else:
#     print("fail")


a = int(input("enter the 1st number :"))
b = int(input("enter the 2nd number :"))
c = int(input("enter the 3rd number :"))

if (a > b):
    if (a > c):
        print("a is the largest number ")
    else:
        ("c is the largest")
else:
    if (b > c):
        print("b is the largest number")
    else:
        print("c is the largest number")


if (a < b):
    if (a < c):
        print("a is the smallest number ")
    else:
        ("c is the smallest")
else:
    if (b < c):
        print("b is the smallest number")
    else:
        print("c is the smallest number")

# pin = 1234

# password = 123

# pin_user = int(input("enter your pin  :"))
# password_user = int(input("enter your password   :"))

# if pin == pin_user and password == password_user:
#     print("login successful")
# else :
#     print ("incorrect pin")
