# while loop (⛔ not done)
# 1) accept 10 number from the user and find its average using while loop
# 2) get a number from the user and find the product of all the numbers from 1 to that number
# # 3) get the number from the user and print all the even number between 0 and that number (entered by the user). again write one more program but for odd numbers
# # 4) get the number from the user and find the factorial of that number
# # 5) write a program to reverse the number
# # eg 123 -> 321, 8736 -> 6378


# # i = 0
# # avg = 0
# # while i < 10:
# #     number = int(input("enter any number    :"))
# #     avg = avg + number
# #     i += 1
# # print(avg)

# # number = int(input("enter any number    :"))
# # i = 0
# # product = 1
# # while number >= 1:
# #     product = product*number
# #     number -= 1
# #     i += 1
# # print(product)

# c

# # c = []

# # i = 0
# # j = 0

# # while i < len(a) and j < len(b):
# #     if a[i] < b[j]:
# #         c.append(a[i])
# #         i += 1
# #     else:
# #         c.append(b[j])
# #         j += 1

# # # if i < len(a):
# # #     c.extend(a[i: len(a)])

# # # if j < len(b):
# # #     c.extend(b[j:len(b)])

# # # print(c)


products = [{
    "name": "phone",
    "price": 10000,
    "category": "electronic"
}, {
    "name": "shirt",
    "price": 1000,
    "category": "mens"
}, {
    "name": "watch",
    "price": 5000,
    "category": "accessories"
}, {
    "name": "car",
    "price": 10000,
    "category": "automobile"
},  {
    "name": "ring",
    "price": 1000,
    "category": "accessories"
}, {
    "name": "jeans",
    "price": 1000,
    "category": "mens"
},  {
    "name": "bike",
    "price": 1000,
    "category": "automobile"
}, {
    "name": "shoes",
    "price": 1000,
    "category": "mens"
}]

i = 0
categories = []

while i < len(products):
    curr = products[i]["category"]
    prod = products[i]["name"]

    j = 0
    found = False
    while j < len(categories):
        if categories[j]["category_name"] == curr:
            found = True
            categories[j]["products"].append(prod)
            categories[j]['total_products'] += 1
            break
        j += 1
    if found == False:
        categories.append({
            "category_name": curr,
            "products": [prod],
            "total_products": 1
        })
    i += 1

print(categories)

# output = [
#     {
#         'category_name': 'mens',
#         'products': ['shoes', 'jeans', 'shirt'],
#         'total_products': 3
#     },
#     {
#         'category_name': 'electronic',
#         'products': ['phone'],
#         'total_products': 1
#     },
#     {
#         'category_name': 'accessories',
#         'products': ['watch', 'ring'],
#         'total_products': 2
#     },
#     {
#         'category_name': 'automobile',
#         'products': ['car', 'bike'],
#         'total_products': 2
#     }
# ]


# a = [-20, 2, 30, 50, 90, 160]
# b = [-30, -15, 3, 5, 12, 17, 35, 45, 63, 84, 99, 180]

# c = []

# i = 0
# j = 0

# while i < len(a) and j < len(b):
#     if a[i] < b[j]:
#         c.append(a[i])
#         i += 1
#     else:
#         c.append(b[j])
#         j += 1

# if i < len(a):
#     c.extend(a[i:len(a)])

# if j < len(b):
#     c.extend(b[j:len(b)])
# print(c)


products = [{
    "name": "shoes",
    "price": 1000,
    "category": "mens"
}, {
    "name": "phone",
    "price": 10000,
    "category": "electronic"
}, {
    "name": "shirt",
    "price": 1000,
    "category": "mens"
}, {
    "name": "watch",
    "price": 5000,
    "category": "accessories"
}, {
    "name": "car",
    "price": 10000,
    "category": "automobile"
},  {
    "name": "ring",
    "price": 1000,
    "category": "accessories"
}, {
    "name": "jeans",
    "price": 1000,
    "category": "mens"
},  {
    "name": "bike",
    "price": 1000,
    "category": "automobile"
}]

# output = [
#
# 'category_name': 'accessories',
#         'products': ['watch', 'ring'],
#         'total_products': 2

category = []

i = 0

while i < len(products):
    curr = products[i]["category"]
    prod = products[i]["name"]


j = 0
found = False
while j < len(category):
    if curr == category[j]["cateogry"]:
        found = True
        category.append(category["products"])
        category[j]["total_products"] += 1
        break
    j += 1
    if found == False:
        category.append({
            "category_name": curr,
            "name": prod,
            "total_products": 1
        })
    i += 1
