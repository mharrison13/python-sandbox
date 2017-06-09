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
#
# strList = ('Alb', 'santa fe', 'mississippi')
#
# for string in strList:
#     if len(string) == 11:
#         print(string)
#     elif len(string) ==3:
#         print('this is alb')
#     else:
#         print('not eleven or three')
#

# opening files
#
# f = open('testfile.csv', 'r+')
# content = f.readlines()
# for line in content:
#     print(line)
# f.close()
#
#

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
numArray = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10]
#
# for startNumber in numArray:
#     for duplicateCheckNumber in numArray:
#         if startNumber == duplicateCheckNumber:
#             print(startNumber)
#     numArray.pop(startNumber)

# functions: define function with def

def functionName(arguments):
    return arguments + 5

def functionWithFunc(function):
    return function(4) + 6

print(functionName(4))

print(functionWithFunc(functionName))

#functions can be passed to other things

