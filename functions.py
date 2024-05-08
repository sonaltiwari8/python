

def find_value(group, value):
    i = 0
    while i < len(group):
        if group[i] == value:
            return i
        i += 1
    return -1


a = find_value([1, 2, 3, 4, 5, 6], 6)
print(a)


# def basic(list, number):
#     i = 0
#     while i < len(list):
#         if list[i] == number:
#             return i
#         i += 1
#     return -1


# a = basic([1, 2, 3, 4, 5, 6, 7], 7)
# print(a)


fruits = ['apple', "mango", "banana", "coconut"]
name = input("Enter any fruit name ")
index = find_value(fruits, name)



print(index)
name = "rohan"
num = 30


def sum(a, b):
print(name)
global num
num += a + b
return a + b


# def subtract(x, y):
#     print(name)
#     global num
#     num += x - y
#     return x - y


# def multiplication(p, q):
#     print(name)
#     global num
#     num += p * q
#     return p*q


# print(multiplication(subtract(sum(1, 2), 20), 2))

# print(num)


# for f in fruits:
#     if f == name:
#         print("found")
#         break


# def sum(a, b, c):
#     print(f"this is a sum funciton {a + b}")
#     return a + b


# print(sum(12, 30, 400))
# print(sum(50, 30))
# print(sum(120, 30))
# print(sum(120, 300))
# sum(500, 30)
# sum(120, 300)


# value = int("1200")
# print(value)


# def reverse(number):
#     total = 0
#     while number > 0:
#         remainder = number % 10
#         number = number // 10
#         total = (total * 10) + remainder
#     return total


# print(reverse(123))
# print(reverse(885112122))
# print(reverse(34535))

# fibonacci series
# 0 1 1 2 3 5 8 13 21 34....
#   1  1

# i = 0
# first = 1
# second = 1
# while i <= 100:
#     total = first + second
#     second = first
#     second += i
# i += 1

# print(i)

# for i in range(100,1, -5):
#     print(i)


# def reverse(list):
#     i = len(list)-1
#     new_list = []
#     while i >= 0:
#         el = list[i]
#         new_list.append(el)
#         i -= 1
#     return new_list


# def reverse(list):
#     new_list = []
#     for f in range(len(list) - 1, -1, -1):
#         el = list[f]
#         new_list.append(el)
#     return new_list


# print(reverse(['a', "b", "c", "d"]))
