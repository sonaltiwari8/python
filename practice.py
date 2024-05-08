# # # i = 0
# # # while i <= 100:
# # #     print(i)
# # #     i = i +1

# # # i = 100
# # # while i >=0:
# # #     print(i)
# # #     i = i-1


# # # number = int(input("enter any number"))

# # # i = 1

# # # while i <= 10:
# # #     print(i*number)
# # #     i = i +1


# # # number = int(input("Enter any positive number "))
# # # i = 1

# # # while i <= 10:
# # #     total = number * i
# # #     print(f"{number} * {i} = {total}")
# # #     i += 1

# # # while loop
# # # 1) accept 10 number from the user and find its average using while loop

# i = 1
# sum = 0
# while i <= 10:
#     number  = int(input("enter any number   :"))
#     i += 1
#     sum = sum + number

# print(f"average is  :  {sum/10}")


# # # 2) get a number from the user and find the product of all the numbers from 1
# # # to that number

# # # number  = int(input("enter any number   :"))
# # # x = number
# # # product = 1

# # # while x >= 1:
# # #  product = product*x
# # #  x-= 1


# # # print(f" product of numbers is : {product}")


# # # 3) get the number from the user and print all the even number between 0 and
# #  #that number (entered by the user). again write one more program but for odd numbers
# # #for even

# # number  = int(input("enter any number   :"))
# # i =1
# # while i <= number:
# #   if i % 2 == 0:
# #     print(f"{i}")
# #     i += 1


# # # 4) get the number from the user and find the factorial of that number
# # # 5) write a program to reverse the number
# # # eg 123 -> 321, 8736 -> 6378


# # # n= 1234
# # # while n > 0:
# # #  reminder = n%10
# # #  total = n//10
# # #  total = reminder +total*10

# # # number = int(input("Enter any number "))
# # # total = 0


# # # while number > 0:
# # #     remainder = number % 10
# # #     number = number // 10
# # #     total = (total * 10) + remainder

# # # print(total)


# # # fruits = ("oranges", "banana", "mango", "guava", "pomegranate")

# # # print(fruits(0))   not working ??


# # fruits = { "oranges", "banana", "oranges", "apple", "mango", "guava", "pomegranate", "mango", "banana" }

# # fruits.add = "kiwi"

# # print(fruits)

# acount_balance = 5000
# pin = 1234

# pin_user = int(input("Enter your pin "))

# if pin == pin_user:
#     print("Choices:\n\t1. type \"w\"for withdrawal\n\t2. type \"d\" for deposit\n\t3. type \"c\" for check balance")

#     choice = input("Enter your choice ")
#     if choice == "w":
#         amount = int(input("Enter the amount "))
#         if amount < acount_balance:
#             acount_balance = acount_balance - amount
#             # acount_balance -= amount
#             print(f"✅ withdrawal successfully, remaaining balance {
#                   acount_balance}")
#         else:
#             print("Insufficient balance ❌")
#     elif choice == "d":
#         amount = int(input("Enter the amount "))
#         if amount >= 0:
#             acount_balance = acount_balance + amount
#             # acount_balance += amount
#             print(f"✅ deposit successfully, total balance {acount_balance}")
#         else:
#             print("Invalid deposit amount ❌")
#     elif choice == "c":
#         print(f"your available balance {acount_balance}")
#     else:
#         print("❌ invalid choice ❌")

# else:
#     print("pin in incorrect ⛔")


# pin = 1234
# account_balance = 5000

# pin_user = int(input("enter your pin"))

# if pin == pin_user:
#   print("choices : \n\t1. \"w\" \n\t2.\"d\" \n\t3.\"c\" " )
#   choice = int(input("enter your choice"))

#   if choice == "d":
#     amount = int(input("enter the amount"))
#     if amount <= account_balance:
#     account_balance -= amount
#     print(f"your b is {account_balance}")

# fruits = ["oranges", "banana", "mango", "guava", "pomegranate"]

# fruits.pop()

# print(fruits)

# print(fruits[0])

# fruits = ("oranges", "banana", "mango", "guava", "pomegranate", "mango")

# print(fruits)

# enter_fruit = input("enter any fruit")

# x = False


# for f in fruits:
#     f == enter_fruit
#     x = True
#     break
# if x == True:
#     print("found")
# else:
#     print("NOT FOUND")

#    i = 0

# while i <= len(fruits):
#     if fruits(i) == enter_fruit
#     x= True
#     break


# number = int(input("Enter any positive number "))
# i = 1

# while i <= 10:
#     total = number * i
#     print(f"{number} * {i} = {total}")
#     i += 1

# i = 1

# while i <=10:
#     total  = number*i
#     print(f"{total}")
#     i += 1

# number = int(input("Enter any number "))
# sum = 0
# i = 1

# while i <= number:
#     sum = sum + i
#     sum += 1
#     i += 1

# list fruits = ["banana", "mango", "guava", "pomegranate", "apple", "orange"]

# print(fruits[0])

# len = len(fruits)
# i = 0

# while i < len:
#     print(fruits[i])
#     i += 1


# fruits.append("kiwi")

# print(f"{fruits}")

# fruits.pop()

# print(f"{fruits}")

# tupple fruits = ("oranges", "banana", "mango", "guava", "pomegranate")

# print(fruits[1])


# x = input("enter any fruit  :")
# i = 0
# found = False

# while i < len(fruits):
#     if fruits[i] == x:
#         found = True
#         break
#     i += 1
# if found:
#     print("found")
# else:
#     print("not found")


# a = input("enter any fruit")
# x= False
# i = 0
# while i <= len(fruits):
#     if fruits[i]== a:
#      x== True
#     break
#     if x == True :
#       print("found")
#     else :
#       print (" not found")


# user = {
#     "joined_at": "01 april",
#     'email': "rohansoni123@gmail.com",
#     "mobile_number": 1234567890,
#     "username": "rohan",
#     "colors": ["red", "black", "blue"],
#     "address": {
#         "city": "Delhi",
#         "country": "India"
#     }
# }


# print(user["email"])
# print(user["colors"][2])
# print(user["address"]["country"])

# Q1) Get two values from the user, the first value must be less than the second value. Print all the even numbers and odd numbers between them.


# a = int(input("enter the first number"))
# b = int(input("enter the second number"))
# if a > b:
#     print("a cant be greater than b")
# else:
#     while a <= b:
#         if a % 2 == 0:
#             print(a)
#         a += 1

# Q2) Find the maximum and minimum number from this list.


# numbers = [20, 60, -40, 10, 100, -90, 70, 80, -30, 120, 40, 140, -70]


# min = numbers[0]
# l = len(numbers)
# i = 1
# while i < l:
#     if numbers[i] < min:
#         min = numbers[i]
#     i += 1
# print(min)


# Q3) Remove all the names from the list which has more than 5 letters in it.


# friends = ['rohan', 'priyanshi',  'shivani', 'aryan', 'sonal', 'puja', 'muskan',
#            'amisha', 'suraj', 'rohit', 'anuj', 'mrityunjay']

# i = 0

# l = len(friends)

# while i < l:
#     if len(friends[i]) > 5:
#         friends.pop(i)
#         l -= 1
#     else:
#         i += 1
# print(friends)

# Q4) Create 2 empty lists call them positive_numbers and negative_numbers append all the positives numbers into the positive_numbers list and negative numbers into the negative_numbers list using while loop.

# numbers = [10, -20, 30, -40, 50, 60, 70, -10, -30, 80, 90, 100, -80, 120]

# positive = []
# negative = []


# l = len(numbers)
# i = 0

# while i < l:
#     if numbers[i] >= 0:
#         positive.append(numbers[i])
#     else:
#         negative.append(numbers[i])
#     i += 1
# print(positive)
# print(negative)


# friends = [
#     {'name': 'rohan',
#      'online': True
#      },
#     {'name': 'shivani',
#         'online': False
#      },
#     {'name': 'aryan',
#         'online': True
#      },
#     {'name': 'sonal',
#         'online': True
#      },
#     {'name': 'puja',
#         'online': False
#      },
#     {'name': 'muskan',
#         'online': True
#      },
#     {'name': 'amisha',
#         'online': True
#      },
#     {'name': 'suraj',
#         'online': False
#      },
#     {'name': 'rohit',
#         'online': True
#      },
#     {'name': 'anuj',
#         'online': False
#      },
#     {'name': 'priyanshi',
#         'online': True
#      },
#     {'name': 'mrityunjay',
#         'online': False
#      }
# ]
# Q5) Print the name of all friends who are online right now, also find how many friends are online and how many are offline.
# i = 0
# l = len(friends)
# c = 0
# while i < l:
#     if friends[i]["online"] == True:
#         c += 1
#         print(friends[i]["name"])
#     i += 1
# print(c)
# offline = l - c
# print(offline)

# # Q6) Find the total sales and also update the stocks based on the orders list.

# products = [
# {"product_id": 1, "product_name": "T-shirt", "price": 15, "stock": 52},
# {"product_id": 2, "product_name": "Jeans", "price": 25, "stock": 28},
# {"product_id": 3, "product_name": "Sneakers", "price": 30, "stock": 83},
# {"product_id": 4, "product_name": "Backpack", "price": 40, "stock": 14},
# {"product_id": 5, "product_name": "Sunglasses", "price": 20, "stock": 37},
# {"product_id": 6, "product_name": "Watch", "price": 50, "stock": 95},
# {"product_id": 7, "product_name": "Headphones", "price": 35, "stock": 62},
# {"product_id": 8, "product_name": "Jacket", "price": 45, "stock": 45},
# {"product_id": 9, "product_name": "Mouse", "price": 55, "stock": 73},
# {"product_id": 10, "product_name": "Medicine", "price": 60, "stock": 91}
# ]

# orders = [
# {"product_id": 8, "quantity": 7},
# {"product_id": 5, "quantity": 3},
# {"product_id": 2, "quantity": 10},
# {"product_id": 4, "quantity": 5},
# {"product_id": 9, "quantity": 2}
# ]

# Q7) Get a string from the user and reverse it. for example sonal should become lanos and HELLO MY NAME IS ROHAN should become NAHOR SI EMAN YM OLLEH

# user = input("enter any string    :")

# l = len(user)
# s = ""
# i = l-1

# while i >= 0:
#     s += user[i]
#     i -= 1

# print(s)


# # Q8) write a simple login and signup program


# # users = []
# # while True:
# #     a = input("enter your choice whether you want to login or sign up  for login enter L and for sign up enter S enter e to exit     :")
# #     if a == "s":
# #         n = input("enter your name   :")
# #         e = input("enter your email id    :")
# #         i = 0
# #         l = len(users)
# #         d = False
# #         while i < l:
# #             if users[i]["email_id"] == e:
# #                 print(
# #                     "this email id already exists in the system enter another email id")
# #                 d = True
# #                 break
# #             i += 1
# #         if d == True:
# #             continue
# #         p = input("enter your password    :")
# #         details = {"email_id": e, "password": p, "name": n}
# #         users.append(details)
# #         print("signup sucessfull")
# #     elif a == "e":
# #         break
# #     elif a == "l":
# #         e = input("enter the email id")
# #         p = input("enter the password")
# #         i = 0
# #         l = len(users)
# #         while i < l:
# #             if users[i]["email_id"] == e and users[i]["password"] == p:
# #                 print(f"hello {users[i]["name"]} ")
# #                 break
# #             i += 1
# #         print("try again ")


