# fizzbuz
#  range function is an iterator
# shift control R to run
# learn vim
# () are Tuples
# [] is array
# {} with key value pair {"key":10, "key2":15}
# flask and django are frameworks I need to look into for python. understand the idea behind each one.
# django is app or component driven and flask is a micro
# tutorialspoint.com is a good resource
# style guide pep8

#scopeing no indent is global scope,

#
# for i in range(1, 101):
#     if i % 15 == 0:
#         print("FizzBuzz")
#     elif i % 5 == 0:
#         print("Fizz")
#     elif i % 3 == 0:
#         print("buzz")
#     else:
#         print(i)
#

# length of city

# strList = ('Alb', 'santa fe', 'mississippi')

# for string in strList:
#     if len(string) == 11:
#         print(string)
    # elif len(string) ==3:
    #     print('this is alb')
    # else:
    #     print('not eleven or three')


# opening files
#
# f = open('testfile.csv', 'r+')
# content = f.readlines()
# for line in content:
#     print(line)
# f.close()
#
#
#
# # .map method for accessing external
# key value for determining password.
#     finding valid passwords in string
# from itertools import product
# from string import ascii_lowercase
# keywords = [''.join(i) for i in product(ascii_lowercase, repeat = 3)]
# print(keywords)
#
# from itertools import product
# from string import ascii_lowercase
# keywords = map(''.join, product(ascii_lowercase, repeat=3))
# print(keywords)


# contexts:
# this opens the documentation and then closes automatically with new indent. You can also create new contexts
#
#
# with open('testfile.csv', 'r+') as f:
#     content = f.readlines()
#     for line in content:
#         print(line)
#         #do thing 2 all based on indent
#         #do thing 3 still based on indent
#     print(f.readlines()) #
#print(f.readlines()) #closed

#new indent closes the context

# #cursor for adding info into file
# reference .seek documentation
# or write.

#sets are like arrays but

#searching for dup numbers problem
# numArray = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10]
#
# for startNumber in numArray:
#     for duplicateCheckNumber in numArray:
#         if startNumber == duplicateCheckNumber:
#             print(startNumber)
#     numArray.pop(startNumber)

# numArray = [14, 52, 22, 9, 44, 45, 21, 45]
#
# print(numArray.index(min(numArray)))

#
# x = [55, 2, 98, 34, 22]
#
# print(x.index(min(x)))

# numArray = [91, 94, 88, 37, 84, 22, 34, 1, 4]
#
# print(numArray.index(min(numArray)))
#
# #7
#
# numArray = [68, 97, 28]
#
# x=100
# for i in numArray:
#     if i < x:
#         x = i
# print(x)
#
# #286

# name = ('gnirtS')

# for i in reversed(name):
#     print(i)
# S
# t
# r
# i
# n
# g


# [33, 53, 98, 22, 41]
# 41
# 22
# 98
# 53
# 33




# functions: define function with def


#
# def functionName(arguments):
#     return arguments + 5
#
# def functionWithFunc(function):
#     return function(4) + 6
#
# print(functionName(4))
#
# print(functionWithFunc(functionName))

#functions can be passed to other things

# def revString(string):
#     negLen = len(string) * -1
#     position = -1
#     newString = ''
#
#     for i in range(len(string)):
#         newString += string[position]
#         position -= 1
#         if position < negLen:
#             break
#
#     return newString
#
# print(revString('String'))
#
# for i in range(1, 101):
#     if i % 7 == 0:
#         print('wolf')
#     elif i % 5 == 0:
#         print('fizz')
#     elif i % 3 == 0:
#         print('buzz')
#     else:
#         print(i)
#
# name = "John"
# age = 23
# if name == "John" and age == 23:
#     print("Your name is John, and you are also 23 years old.")
#
# if name == "John" or name == "Rick":
#     print("Your name is either John or Rick.")
#
#
# class A:
#     def __init__(self):
#         print("A.__init__")
#
#
# class B(A):
#     def __init__(self):
#         print("B.__init__")
#         super().__init__()
#
#
# class C(A):
#     def __init__(self):
#         print("C.__init__")
#         super().__init__()
#
#
# class D(B, C):
#     def __init__(self):
#         print("D.__init__")
#         super().__init__()


