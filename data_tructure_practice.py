# primitives data types
# They are simple and fundamental types of data that are used to represent simple values

# 1.  string
# 2.  number
# 3.  boolean

# non primitives data types
# Non-primitive data types can hold more complex data structures or collections of values.
# Unlike primitive data types, which store single values,
# non-primitive data types can store multiple values.


# # list []
# # set {}
# # tuple ()
# # dict { key : value }

# List
# Lists are ordered collections of items, which can be of different data types.
#  They are mutable, meaning we can modify the elements after creating the list.

# fruits = ["oranges", "banana", "mango", "guava", "pomegranate"]

# ⭐ we can access elements from a list using their index, index starts from
# 0 for the first element

# Index	Fruit
# 0	oranges
# 1	banana
# 2	mango
# 3	guava
# 4	pomegranate
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])
# print(fruits[4])
# print(fruits[5])

# output
# oranges
# banana
# mango
# guava
# pomegranate
# Error ⛔

# Append "coconut" to the end of the list

# fruits.append("coconut")

# Remove the last element

# fruits.pop()

# Update the third element to apple

# fruits[2] = "kiwi"

# Tuple
# Tuples are similar to lists, but they are immutable, meaning once you create a tuple, you cannot change its values.

# fruits = ("oranges", "banana", "mango", "guava", "pomegranate")

# we can access elements of a tuple using their index, just like with lists.
#  index starts from 0 for the first element

# ⭐ One important feature of tuples is that they are immutable, meaning we cannot change their elements after creation. If we try to modify a tuple, we'll get an error

# Set
# Sets are collections of unique elements, meaning they do not allow duplicate values.

# fruits = { "oranges", "banana", "oranges", "apple", "mango", "guava", "pomegranate", "mango", "banana" }

# ⭐ Sets can contain elements of different types, but they can only contain unique elements. Duplicate elements are automatically removed when creating a set

# adding element to the set

# fruits.add("kiwi")

# dict (dictionaries)
# Dictionaries are collections of key-value pairs.
#  Keys are unique and immutable, while values can be of any data type. Dictionaries are created using curly braces {} and key-value pairs separated by colons :

# user_profile = {
#     'username' : 'rohan123'
#     'email' : 'rohansoni123@gmail.com'
#     'active' : False,
#     'followers' : 500,
#     'followings' : 600,
#     'joined_date' : '30 feb 2023',
#     'post' : [{
#         'image' : 'image1.png',
#         'likes' : 45,
#         'comments' : ['good 👍', 'amazing 🤣', 'very nice']
#     }, {
#         'image' : 'image2.png',
#         'likes' : 24,
#         'comments' : []
#     }],
# }

# we can access elements of a dictionary using square bracket [] just like list but with the key

# print(user_profile['email'])
# print(user_profile['active'])
# print(user_profile['username'])
# print(user_profile['followers'])
# print(user_profile['post'][0]['image'])

# output

# rohansoni123@gmail.com
# False
# rohan123
# 500
# image1.png

# we can modify the value associated with a key or add new key-value pairs to a dictionary

# # updating the username
# user_profile['username'] = "rohan321"

# # adding new property gender
# user_profile['gender'] = "male"


# list == [], tuple (), set{}, dict{key:adcas}
# list- append, pop, index , change the variable
# tuple -  index, can have duplicate, immutable
# set -unique,cant have duplicate, add element

# # list = []
# # mutable, append, pop, acces with index

# # list = ["apple", "mango", "banana", "grapes"]

# # print(list[0])
# # list.append("kiwi")
# # print(list)
# # list.pop()
# # print(list)

# # list[2] = "guava"
# # print(list)

# # tuple - immuatable , (),

# # dictt

# # students =  "s" : "student name"}

# # user_profile = {
# #     'username' : 'rohan123'
# #     'email' : 'rohansoni123@gmail.com'
# #     'active' : False,
# #     'followers' : 500,
# #     'followings' : 600,
# #     'joined_date' : '30 feb 2023',
# #     'post' : [{
# #         'image' : 'image1.png',
# #         'likes' : 45,
# #         'comments' : ['good 👍', 'amazing 🤣', 'very nice']
# #     }, {
# #         'image' : 'image2.png',
# #         'likes' : 24,
# #         'comments' : []
# #     }],
# # }
# # print(user_profile['email'])
# # print(user_profile['active'])
# # print(user_profile['username'])
# # print(user_profile['followers'])
# # print(user_profile['post'][0]['image'])

# # rohansoni123@gmail.com
# # False
# # rohan123
# # 500
# # image1.png

students = [{
    "student_id": 300692,
    "student_name": "Aditi Sharma",
    "roll_number": 1,
    "gender": "F",
    "maths": 81,
    "english": 51,
    "computer": 41,
    "science": 74,
    "drawing": 82
}, {
    "student_id": 470699,
    "student_name": "Alok Patel",
    "roll_number": 2,
    "gender": "M",
    "maths": 75,
    "english": 76,
    "computer": 30,
    "science": 36,
    "drawing": 63
}, {
    "student_id": 647219,
    "student_name": "Ananya Das",
    "roll_number": 3,
    "gender": "F",
    "maths": 97,
    "english": 98,
    "computer": 95,
    "science": 92,
    "drawing": 92
}, {
    "student_id": 509478,
    "student_name": "Ankit Mehta",
    "roll_number": 4,
    "gender": "M",
    "maths": 52,
    "english": 48,
    "computer": 85,
    "science": 52,
    "drawing": 81
}, {
    "student_id": 556350,
    "student_name": "Arjun Singh",
    "roll_number": 5,
    "gender": "M",
    "maths": 22,
    "english": 63,
    "computer": 73,
    "science": 43,
    "drawing": 96
}, {
    "student_id": 145415,
    "student_name": "Ayush Gupta",
    "roll_number": 6,
    "gender": "M",
    "maths": 32,
    "english": 50,
    "computer": 64,
    "science": 98,
    "drawing": 34
}, {
    "student_id": 379533,
    "student_name": "Bhavya Reddy",
    "roll_number": 7,
    "gender": "F",
    "maths": 64,
    "english": 21,
    "computer": 40,
    "science": 100,
    "drawing": 34
}, {
    "student_id": 599735,
    "student_name": "Chetan Kumar",
    "roll_number": 8,
    "gender": "M",
    "maths": 55,
    "english": 84,
    "computer": 54,
    "science": 22,
    "drawing": 86
}, {
    "student_id": 293429,
    "student_name": "Deepika Verma",
    "roll_number": 9,
    "gender": "F",
    "maths": 25,
    "english": 45,
    "computer": 37,
    "science": 42,
    "drawing": 81
}, {
    "student_id": 510140,
    "student_name": "Devendra Yadav",
    "roll_number": 10,
    "gender": "M",
    "maths": 74,
    "english": 32,
    "computer": 75,
    "science": 54,
    "drawing": 72
}, {
    "student_id": 248625,
    "student_name": "Divya Jain",
    "roll_number": 11,
    "gender": "F",
    "maths": 88,
    "english": 48,
    "computer": 70,
    "science": 68,
    "drawing": 87
}, {
    "student_id": 580873,
    "student_name": "Gaurav Mishra",
    "roll_number": 12,
    "gender": "M",
    "maths": 67,
    "english": 65,
    "computer": 31,
    "science": 43,
    "drawing": 23
}, {
    "student_id": 135688,
    "student_name": "Isha Singh",
    "roll_number": 13,
    "gender": "F",
    "maths": 63,
    "english": 21,
    "computer": 52,
    "science": 51,
    "drawing": 75
}, {
    "student_id": 358085,
    "student_name": "Jatin Shah",
    "roll_number": 14,
    "gender": "M",
    "maths": 39,
    "english": 95,
    "computer": 43,
    "science": 81,
    "drawing": 58
}, {
    "student_id": 579275,
    "student_name": "Kriti Sharma",
    "roll_number": 15,
    "gender": "F",
    "maths": 94,
    "english": 72,
    "computer": 42,
    "science": 69,
    "drawing": 95
}, {
    "student_id": 578282,
    "student_name": "Manish Tiwari",
    "roll_number": 16,
    "gender": "M",
    "maths": 26,
    "english": 98,
    "computer": 40,
    "science": 50,
    "drawing": 48
}, {
    "student_id": 381391,
    "student_name": "Mohan Raj",
    "roll_number": 17,
    "gender": "M",
    "maths": 47,
    "english": 35,
    "computer": 70,
    "science": 86,
    "drawing": 73
}, {
    "student_id": 468795,
    "student_name": "Neha Gupta",
    "roll_number": 18,
    "gender": "F",
    "maths": 86,
    "english": 80,
    "computer": 49,
    "science": 60,
    "drawing": 63
}, {
    "student_id": 615654,
    "student_name": "Nikhil Patel",
    "roll_number": 19,
    "gender": "M",
    "maths": 30,
    "english": 74,
    "computer": 73,
    "science": 80,
    "drawing": 90
}, {
    "student_id": 505388,
    "student_name": "Pooja Desai",
    "roll_number": 20,
    "gender": "F",
    "maths": 82,
    "english": 92,
    "computer": 43,
    "science": 76,
    "drawing": 32
}, {
    "student_id": 608198,
    "student_name": "Prakash Kumar",
    "roll_number": 21,
    "gender": "M",
    "maths": 53,
    "english": 91,
    "computer": 22,
    "science": 63,
    "drawing": 57
}, {
    "student_id": 528544,
    "student_name": "Priya Joshi",
    "roll_number": 22,
    "gender": "F",
    "maths": 22,
    "english": 35,
    "computer": 48,
    "science": 67,
    "drawing": 38
}, {
    "student_id": 255585,
    "student_name": "Rahul Singh",
    "roll_number": 23,
    "gender": "M",
    "maths": 63,
    "english": 32,
    "computer": 64,
    "science": 33,
    "drawing": 20
}, {
    "student_id": 495898,
    "student_name": "Ravi Kumar",
    "roll_number": 24,
    "gender": "M",
    "maths": 61,
    "english": 77,
    "computer": 48,
    "science": 59,
    "drawing": 46
}, {
    "student_id": 252540,
    "student_name": "Rohan Gupta",
    "roll_number": 25,
    "gender": "M",
    "maths": 46,
    "english": 76,
    "computer": 43,
    "science": 36,
    "drawing": 62
}, {
    "student_id": 299442,
    "student_name": "Sagar Mehta",
    "roll_number": 26,
    "gender": "M",
    "maths": 31,
    "english": 76,
    "computer": 65,
    "science": 20,
    "drawing": 26
}, {
    "student_id": 154201,
    "student_name": "Sanya Sharma",
    "roll_number": 27,
    "gender": "F",
    "maths": 38,
    "english": 36,
    "computer": 30,
    "science": 51,
    "drawing": 84
}, {
    "student_id": 425733,
    "student_name": "Siddharth Verma",
    "roll_number": 28,
    "gender": "M",
    "maths": 20,
    "english": 20,
    "computer": 32,
    "science": 68,
    "drawing": 66
}, {
    "student_id": 318111,
    "student_name": "Tanvi Patel",
    "roll_number": 29,
    "gender": "F",
    "maths": 51,
    "english": 38,
    "computer": 65,
    "science": 68,
    "drawing": 56
}, {
    "student_id": 412652,
    "student_name": "Vaibhav Gupta",
    "roll_number": 30,
    "gender": "M",
    "maths": 84,
    "english": 55,
    "computer": 77,
    "science": 47,
    "drawing": 32,
}]


i = 0
while i < len(students):
    if total_marks = students[i]["maths"]+students[i]["english"] + \
        students[i]["computer"]+students[i]["science"]+students[i]["drawing"]

    i += 1


# topper = students[0]


# while i < len(students):
#     if students[0]["total_marks"] < students[i]["total_marks"]:
#         topper = students[i]
#     i += 1
# print(topper)

# while i < len(students):
#     if students[i]["gender"] == "M":
#         print(f"{students[i]["student_name"]} and {
#               students[i]["roll_number"]}")
#     i += 1

# products = [
#     {
#         "name": "charger",
#         "price": 200,
#         "stock": 300
#     },
#     {
#         "name": "t-shirt",
#         "price": 500,
#         "stock": 100
#     },
#     {
#         "name": "watch",
#         "price": 2200,
#         "stock": 50
#     },
#     {
#         "name": "headphone",
#         "price": 1200,
#         "stock": 40
#     },
#     {
#         "name": "chips",
#         "price": 20,
#         "stock": 4000
#     },
#     {
#         "name": "biscuit",
#         "price": 10,
#         "stock": 500
#     },
#     {
#         "name": "laptop",
#         "price": 60000,
#         "stock": 10
#     },
#     {
#         "name": "keyboard",
#         "price": 600,
#         "stock": 40
#     },
# ]

# i = 0
# while i < len(products):
#     if products[i]["price"] > 500:
#         print(f"product name is {products[i]["name"]} and stock is {
#               products[i]["stock"]}")
#     i += 1


# you have 2 sorted list

