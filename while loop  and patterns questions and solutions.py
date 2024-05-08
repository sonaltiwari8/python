# while loop (⛔ not done)

# 1) accept 10 number from the user and find its average using while loop

# i = 0
# sum = 0
# while i < 10:
#     a = int(input("enter any number"))
#     sum += a
#     i += 1
# print({sum/10})


# 2) get a number from a number from the user and find the product of all the numbers from 1 to that number

# a = int(input("enter any number"))
# x = a
# product = 1
# i = 1

# while x >= 1:
#     product = product*x
#     x -= 1
# print(f"{product}")

# 3) get the number from the user and print all the even number between 0 and that number (entered by the user). again write one more program but for odd numbers

# a = int(input("enter any number  :"))

# while a >= 0:
#     if a % 2 != 0:
#         print(a)
#     a -= 1

# 4) get the number from the user and find the factorial of that number

# 5) write a program to reverse the number
# eg 123 -> 321, 8736 -> 6378

# a = int(input("enter any number  :"))

# while a > 0:
#     remainder = a % 10
#     num = a // 10
#     total = total*10 + remainder

# fruits = ["apple", "mango", "banana", "kiwi"]
# i = 0

# a = input("enter any fruit  :")

# while i < len(fruits):
#     if fruits[i] == a:
#         print("found")
#     i += 1

# for f in fruits:
#     if f == a:
#         print("found")


# Q1) Get two values from the user, the first value must be less than the second value. Print all the even numbers and odd numbers between them.

# a = int(input("enter any number  :"))
# b = int(input("enter any number  :"))

# if a > b:
#     print("enter any other")

# while a <= b:
#     if b % 2 == 0:
#         print(b)
#     b -= 1


# Q2) Find the maximum and minimum number from this list.

# numbers = [20, 60, -40, 10, 100, -90, 70, 80, -30, 120, 40, 140, -70]

# max = numbers[0]
# i = 0
# while i < len(numbers):
#     if max < numbers[i]:
#         max = numbers[i]
#     i += 1
# print(max)


# Q3) Remove all the names from the list which has more than 5 letters in it.

# friends = ['rohan', 'shivani', 'aryan', 'sonal', 'puja', 'muskan',
#            'amisha', 'suraj', 'rohit', 'anuj', 'priyanshi', 'mrityunjay']

# i = 0
# l = len(friends)

# while i < len(friends):
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

# i = 0
# while i < len(numbers):
#     if numbers[i] >= 0:
#         positive.append(numbers[i])
#     else:
#         negative.append(numbers[i])
#     i += 1
# print(positive)
# print(negative)

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
# l = len(friends)
# c = 0
# while i < l:
#     if friends[i]["online"] == True:
#         c += 1
#         print((friends[i]))

#     i += 1
# print(f"{c}")

# o = l-c
# print(o)

# # Q6) Find the total sales and also update the stocks based on the orders list.

# products = [
#     {"product_id": 1, "product_name": "T-shirt", "price": 15, "stock": 52},
#     {"product_id": 2, "product_name": "Jeans", "price": 25, "stock": 28},
#     {"product_id": 3, "product_name": "Sneakers", "price": 30, "stock": 83},
#     {"product_id": 4, "product_name": "Backpack", "price": 40, "stock": 14},
#     {"product_id": 5, "product_name": "Sunglasses", "price": 20, "stock": 37},
#     {"product_id": 6, "product_name": "Watch", "price": 50, "stock": 95},
#     {"product_id": 7, "product_name": "Headphones", "price": 35, "stock": 62},
#     {"product_id": 8, "product_name": "Jacket", "price": 45, "stock": 45},
#     {"product_id": 9, "product_name": "Mouse", "price": 55, "stock": 73},
#     {"product_id": 10, "product_name": "Medicine", "price": 60, "stock": 91}
# ]
# orders = [
#     {"product_id": 8, "quantity": 7},
#     {"product_id": 5, "quantity": 3},
#     {"product_id": 2, "quantity": 10},
#     {"product_id": 4, "quantity": 5},
#     {"product_id": 9, "quantity": 2}
# ]


# o = 0
# while o < len(orders):
#     o_id = orders[o]["product_id"]
#     print(o_id)
#     p = 0
#     while p < len(products):
#         p_id = products[p]["product_id"]
#         if o_id == p_id:
#             q = orders[o]["quantity"]
#             p = products[p]["price"]
#         p += 1
#     o += 1

# print(f"sale is {p*q}")


#  Get a string from the user and reverse it. for example sonal should become lanos and HELLO MY NAME IS ROHAN should become NAHOR SI EMAN YM OLLEH

# u = input("enter any letter   :")

# l = len(u)
# i = l-1
# s = " "
# while i >= 0:
#     s += u[i]
#     i -= 1
# print(s)


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# # 1 2 3 4 5 6
# j = 1
# while j <= 6:
#     i = 1
#     while i <= j:
#         print(i, end=" ")
#         i += 1

#     print("\n")
#     j += 1

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# j = 0
# while j <= 6:
#     i = 0
#     while i <= j:
#         print(i+1, end=" ")
#         i += 1

#     print("\n")
#     j += 1
1
12


i = 1

while i <= 2:
    print(i, end=" ")
    i += 1
print("\n")
i = 1

while i <= 3:
    print(i, end=" ")
    i += 1
print("\n")
i = 1

while i <= 4:
    print(i, end=" ")
    i += 1

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6
# j = 1
# while j < 9:
#     i = 1
#     while i <= 5:
#         print(j, end=" ")
#         i += 1
#     print("\n")
#     j += 1

# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5
# j = 1
# while j <= 5:
#     i = 1
#     while i <= 5:
#         print(j, end=" ")
#         i += 1
#     print("\n")
#     i = 1
#     j += 1


# i = 1

# while i <= 5:
#     print(1, end=" ")
#     i += 1
# print("\n")
# i = 1
# while i <= 5:
#     print(2, end=" ")
#     i += 1
# print("\n")
# i = 1
# while i <= 5:
#     print(3, end=" ")
#     i += 1
# print("\n")


# i = 1

# while i <= 1:
#     print(i, end=" ")
#     i += 1
# print("\n")
# i = 1
# while i <= 2:
#     print(i, end=" ")
#     i += 1
# print("\n")
# i = 1
# while i <= 3:
#     print(i, end=" ")
#     i += 1
# print("\n")
# i = 1
# while i <= 4:
#     print(i, end=" ")
#     i += 1

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# i = 1
# j = "*"
# while i <= 8:
#     print(f"{J}")
#     i += 1
# j += "*"


# Q1) Get two values from the user, the first value must be less than the second value. Print all the even numbers and odd numbers between them.

    # a = int(input("enter any number  :"))
    # b = int(input("enter any number  :"))

    # if a > b:
    #     print("enter any other")

    # while a <= b:
    #     if b % 2 == 0:
    #         print(b)
    #     b -= 1

    # Q2) Find the maximum and minimum number from this list.

    # numbers = [20, 60, -40, 10, 100, -90, 70, 80, -30, 120, 40, 140, -70]

    # max = numbers[0]
    # i = 0
    # while i < len(numbers):
    #     if max < numbers[i]:
    #         max = numbers[i]
    #     i += 1
    # print(max)

    # Q3) Remove all the names from the list which has more than 5 letters in it.

    # friends = ['rohan', 'shivani', 'aryan', 'sonal', 'puja', 'muskan',
    #            'amisha', 'suraj', 'rohit', 'anuj', 'priyanshi', 'mrityunjay']

    # i = 0
    # l = len(friends)

    # while i < len(friends):
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

    # i = 0
    # while i < len(numbers):
    #     if numbers[i] >= 0:
    #         positive.append(numbers[i])
    #     else:
    #         negative.append(numbers[i])
    #     i += 1
    # print(positive)
    # print(negative)

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
    # l = len(friends)
    # c = 0
    # while i < l:
    #     if friends[i]["online"] == True:
    #         c += 1
    #         print((friends[i]))

    #     i += 1
    # print(f"{c}")

    # o = l-c
    # print(o)

    # 1
    # 1 2
    # 1 2 3
    # 1 2 3 4
    # 1 2 3 4 5
    # # 1 2 3 4 5 6
    # j = 1
    # while j <= 6:
    #     i = 1
    #     while i <= j:
    #         print(i, end=" ")
    #         i += 1

    #     print("\n")
    #     j += 1

    # 1
    # 2 3
    # 4 5 6
    # 7 8 9 10
    # 11 12 13 14 15
    # j = 0
    # while j <= 6:
    #     i = 0
    #     while i <= j:
    #         print(i+1, end=" ")
    #         i += 1

    #     print("\n")
    #     j += 1

    # i = 1

    # while i <= 2:
    #     print(i, end=" ")
    #     i += 1
    # print("\n")
    # i = 1

    # while i <= 3:
    #     print(i, end=" ")
    #     i += 1
    # print("\n")
    # i = 1

    # while i <= 4:
    #     print(i, end=" ")
    #     i += 1

    # 1
    # 2 2
    # 3 3 3
    # 4 4 4 4
    # 5 5 5 5 5
    # 6 6 6 6 6 6
    # j = 1
    # while j < 9:
    #     i = 1
    #     while i <= 5:
    #         print(j, end=" ")
    #         i += 1
    #     print("\n")
    #     j += 1

    # 1 1 1 1 1
    # 2 2 2 2 2
    # 3 3 3 3 3
    # 4 4 4 4 4
    # 5 5 5 5 5
    # j = 1
    # while j <= 5:
    #     i = 1
    #     while i <= 5:
    #         print(j, end=" ")
    #         i += 1
    #     print("\n")
    #     i = 1
    #     j += 1

    # i = 1

    # while i <= 5:
    #     print(1, end=" ")
    #     i += 1
    # print("\n")
    # i = 1
    # while i <= 5:
    #     print(2, end=" ")
    #     i += 1
    # print("\n")
    # i = 1
    # while i <= 5:
    #     print(3, end=" ")
    #     i += 1
    # print("\n")

    # i = 1

    # while i <= 1:
    #     print(i, end=" ")
    #     i += 1
    # print("\n")
    # i = 1
    # while i <= 2:
    #     print(i, end=" ")
    #     i += 1
    # print("\n")
    # i = 1
    # while i <= 3:
    #     print(i, end=" ")
    #     i += 1
    # print("\n")
    # i = 1
    # while i <= 4:
    #     print(i, end=" ")
    #     i += 1

    # *
    # * *
    # * * *
    # * * * *
    # * * * * *
    # * * * * * *
    # i = 1
    # j = "*"
    # while i <= 8:
    # print(f"{J}")
    # i += 1
    # j += "*"

    # list = [10, 20, 39, 40, 50, 60, 70]
    # start = 0
    # end = len(list)-1
    # to_find = int(input("enter any number"))

    # while start <= end:
    # mid= (start+end)//2
    # if to_find == list[mid]:
    #     print("found")
    #     break
    # if to_find < list[mid]:
    #     end= mid - 1
    # else:
    #     to_find > list[mid]
    #     start= mid + 1
