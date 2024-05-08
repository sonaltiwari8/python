# fruits = ("apple", "mango", "guava", "papaya", "coconut")
# fruits = ["apple", "mango", "guava", "papaya", "coconut"]

# fruit1 = fruits[0]
# fruit2 = fruits[1]
# fruit3 = fruits[2]

# python is a 
# general purpose
# high level
# open source
# programming language


# fruit1, fruit2, *remaining_fruit = fruits

# print(fruit1)
# print(fruit2)
# print(fruit3)
# print(fruit4)

# print(fruit1)
# print(fruit2)
# print(remaining_fruit)

# a = 100
# b = 200

# b, a = a, b # a, b in the right hand side is a tuple (a, b)
# print(f"a = {a} and b = {b}")

# b, a, *all = [100, 200, 300, 500, 600]

# # b = 100, a = 200, all = [300, 500, 600]

# print(all)

# types of arguments that we can pass into the function

# positional arguments
# keyword-only argument
# default argument

# def sum(first, second):
#     return first + second

# sum(10,30)
# # 10 and 30 are positional arguments

# sum(first=40, second=50)
# # first=40 and second=70 are keyword argument
# # order doesn't matter
# sum(second=70, first=90)


# def sum(*total):
#     print(total[0])
#     print(total[1])
#     print(f"doing something....")

# def sum(first, second, third, *forth, five):
#     print(first, second, third, forth, five)


# default arguments
# def multiple(first=0, second=0):
#     print(first, second)
#     return first, second


# print(f"result = {multiple(2, 3)}")

# sum(10, 20, 30, 40, 50, 60, 70, five=100)

# version 1
def sum_1(*values):
    i = 0
    sum = 0
    while i < len(values):
        sum += values[i]
        i += 1
    return sum

# version 2


def sum_2(*values, multiple=1):
    i = 0
    sum = 0
    while i < len(values):
        sum += values[i] * multiple
        i += 1
    return sum


# version 3
def sum_3(*values, multiple=1, message="total = "):
    i = 0
    sum = 0
    while i < len(values):
        sum += values[i] * multiple
        i += 1
    return f"{message} {sum}"


print(sum_3(1, 2, 3, multiple=10, message="we add all the numbers we get"))
