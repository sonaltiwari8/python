# ask the user to enter their age. If the age is less than 18, print "You are a minor", otherwise print "You are an adult".

# ask the user to enter three sides of a triangle. Check if it's an equilateral triangle (all sides equal), isosceles triangle (two sides equal), or scalene triangle (no sides equal).

# age = int(input("enter your age   :"))

# if age < 18:
#     print("you are a minor")
# else:
#     print("you are an adult")

# side1 = int(input("enter the size of triange   :"))
# side2 = int(input("enter the size of triange   :"))
# side3 = int(input("enter the size of triange   :"))

# if side1 == side2 == side3:
#     print("equilateral triangle")
# elif side1 != side2 != side3 != side1:
#     print("scalene triangle")
# else:
#     print("isoceles triangle")

# print your name 20 times
# i = 0

# while i < 20:
#     print("sonal")
#     i += 1

# print the number from 1 to 100
# i = 1

# while i <= 100:
#     print(i)
#     i += 1

# print the number from 100 to 1
# i = 100

# while i >= 1:
#     print(i)
#     i -= 1

# get a positive number from the user and print its table, if user types some negative number then print a message
# i = 1
# num = int(input("enter any positive number"))

# while i <= 10:
#     print(f"{num} * {i} = {i*num}")
#     i += 1


# print all the even number between 0 and 100 and 200 and 500, and also count the total even number

# i = 0

# while i <= 100:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# j = 200
# while j <= 500:
#     if j % 2 == 0:
#         print(j)
#     j += 1

# print all the odd number between 300 and 500

# i = 300

# while i <= 500:
#     if i % 2 != 0:
#         print(i)
#     i += 1

# ask the user for their name. Keep asking until they enter a name with between 4 to 24 letters. Once they enter a valid name, print 'Hello' followed by their name.

# while True:
#     name = input("enter your name    :")
#     if len(name) >= 4 and len(name) <= 24:
#         print(f"hello {name}")
#         break


# name = input("enter your name    :")
# correct = False
# if len(name) >= 4 and len(name) <= 24:
#     print(f"hello {name}")
# else:
#     while True:
#         name = input("enter your name   :")
#         if len(name) >= 4 and len(name) <= 24:
#             print(f"hello {name}")
#             correct = True
#         if correct == True:
#             break

# ask the user to enter a number representing a day of the week (1 for Monday, 2 for Tuesday, etc.). Keep asking until the user enters any number between 1 to 7. Once they enter a valid number, print the corresponding day name.

# days = ["monday",  "tuesday", "wednesday",
#         "thursday", "friday", "saturday", "sunday"]

# while True:
#     num = int(input("Enter any number "))
#     if num <= 7 and num >= 1:
#         print(days[num - 1])
#         break
#     print("invalid number")

# while True:
#     num = int(input("enter any number   :"))
#     if num == 1:
#         print("monday")
#         break
#     elif num == 2:
#         print("tuesday")
#         break
#     elif num == 3:
#         print("wednesday")
#         break
#     elif num == 4:
#         print("thursday")
#         break
#     elif num == 5:
#         print("friday")
#         break
#     elif num == 6:
#         print("saturday")
#         break
#     elif num == 7:
#         print("sunday")
#         break
#     elif num > 7 and num < 1:
#         print("invalid number")
#         break

# i = 1
# found = False
# while True:
#     num = int(input("enter any number   :"))
#     if num == 1:
#         found = True
#         print("monday")
#     elif num == 2:
#         found = True
#         print("tuesday")
#     elif num == 3:
#         found = True
#         print("wednesday")
#     elif num == 4:
#         found = True
#         print("thursday")
#     elif num == 5:
#         found = True
#         print("friday")
#     elif num == 6:
#         found = True
#         print("saturday")
#     elif num == 7:
#         found = True
#         print("sunday")
#     elif num > 7 and num < 1:
#         print("invalid number")

#     if found:
#         print("Bye Bye")
#         print("Bye Bye")
#         print("Bye Bye")
#         print("Bye Bye")
#         break


# i = 1
# found = False
# while i <= 7:
#     num = int(input("enter any number   :"))
#     if num == 1:
#         found = True
#         print("monday")
#         if found == True:
#             break
#     elif num == 2:
#         found = True
#         print("tuesday")
#         if found == True:
#             break
#     elif num == 3:
#         found = True
#         print("wednesday")
#         if found == True:
#             break
#     elif num == 4:
#         found = True
#         print("thursday")
#         if found == True:
#             break
#     elif num == 5:
#         found = True
#         print("friday")
#         if found == True:
#             break
#     elif num == 6:
#         found = True
#         print("saturday")
#         if found == True:
#             break
#     elif num == 7:
#         found = True
#         print("sunday")
#         if found == True:
#             break


# ask a number from the user, reverse it and print it.

# user = int(input("enter any number"))
# total = 0
# i = 0


# while user > 0:
#     reminder = user % 10
#     user = user // 10
#     total = (total*10) + reminder
# print(total)


# Q1) Get two values from the user, the first value must be less than the second value. Print all the even numbers and odd numbers between them.
# num1 = int(input("enter any number   :"))
# num2 = int(input("enter any number   :"))

# if num1 > num2:
#     print("not possible")
# else:
#     while num1 < num2:
#         print(num1)
#         num1 += 2


# if num1 > num2:
#     print("not possible")
# elif num1 % 2 == 0:
#     while num1 <= num2:
#         print(num1)
#         num1 += 2
# elif num1 % 2 != 0:
#     while num1 <= num2:
#         print(num1)
#         num1 += 2
# else:
#     print("invalid number")

# i = num1
# if num1 < num2:
#     while i <= num2:
#         if i % 2 == 0:
#             print(i)
#         i += 1
# else:
#     print("cant enter number2 greater than number1")

# Q2) Find the maximum and minimum number from this list.
# numbers = [20, 60, -40, 10, 100, -90, 70, 80, -30, 120, 40, 140, -70]

# i = 0

# min = numbers[0]
# max = numbers[0]

# while i < len(numbers):
#     if numbers[i] < min:
#         min = numbers[i]
#     i += 1
# print(min)
# i = 0
# while i < len(numbers):
#     if numbers[i] > max:
#         max = numbers[i]
#     i += 1
# print(max)

# Q3) Remove all the names from the list which has more than 5 letters in it.

# friends = ['rohan', 'shivani', 'aryan', 'sonal', 'puja', 'muskan',
#            'amisha', 'suraj', 'rohit', 'anuj', 'priyanshi', 'mrityunjay']

# i = 0

# while i < len(friends):
#     if len(friends[i]) > 5:
#         friends.pop(i)
#     else:
#         i += 1
# print(friends)


# Q4) Create 2 empty lists call them positive_numbers and negative_numbers append all the positives numbers into the positive_numbers list and negative numbers into the negative_numbers list using while loop.

# positive = []
# negative = []
# numbers = [20, 60, -40, 10, 100, -90, 70, 80, -30, 120, 40, 140, -70]

# i = 0

# while i < len(numbers):
#     if numbers[i] > 0:
#         positive.append(numbers[i])
#     i += 1
# print(positive)
# i = 0
# while i < len(numbers):
#     if numbers[i] < 0:
#         negative.append(numbers[i])
#     i += 1
# print(negative)

# numbers = [10, -20, 30, -40, 50, 60, 70, -10, -30, 80, 90, 100, -80, 120]


# Q5) Print the name of all friends who are online right now, also find how many friends are online and how many are offline.

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

# i = 0
# found = False
# count_friends_online = 0

# while i < len(friends):
#     if friends[i]["online"] == True:
#         found = True
#         count_friends_online += 1
#         print(friends[i]["name"])
#     i += 1
# print(count_friends_online)

# offline = len(friends) - (count_friends_online)

# print(offline)

# a little tricky 🤔


# Q6) Find the total sales and also update the stocks based on the orders list.

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
# user = input("enter the name   :")
# l = len(user)
# i = l-1

# while i >= 0:
#     print(user[i], end="")
#     i -= 1


# Q8) write a simple login and signup program

# pattterns

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6

i = 1

while i <= 1:
    print(i)
    i += 1
i = 1
while i <= 2:
    print(i)
    i += 1
print(end="\n")
i = 1
while i <= 3:
    print(i)
    i += 1
# i = 1
# while i <= 4:
#     print(i, end="\n")
#     i += 1
# i = 1
# while i <= 5:
#     print(i, end="\n")
#     i += 1
# i = 1
# while i <= 6:
#     print(i, end="\n")
#     i += 1
# i = 1
# while i <= 7:
#     print(i, end="\n")
#     i += 1
