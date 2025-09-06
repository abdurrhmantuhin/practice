##Creating Variables
# y = "tuhin"
# x = 18

# print(f"my name is : {y} and my age : {x} ")



##Casting
# x = str(2)
# y = int(762)
# z = float(82)

# print(x,y,z)



## Get the Type
# x = "string"
# y = '8'
# z = 423
# a = 54.54

# print(type(x))
# print(type(y))
# print(type(z))
# print(type(a))



## Many Values to Multiple Variables
# x,y,z = 12, "tuhin" , 6734.83

# print (x,y,z)
# print (type(x))
# print (type(y))
# print (type(z))



## One Value to Multiple Variables
# x = y = z = 9000
# print(y)



# Unpack a Collection
# variable = ("tuhin","amrito","samrat")

# x , y , z = variable
# v = t = c = variable
# print(x)
# print(v)



## Global Variables
# x = "arny"
# def variable ():
#     print("my ex name " , x )

# variable()



## glabal function 
# x = 100 
# def variable ():
#     global x 
#     x = 190

# variable()
# print (" what if ",x)



## Built-in Data Types

# # str
# a = "tuhin"
# print(a)
# print(type(a))

# #int
# b = 90
# print (b)
# print(type(b))

# # complex
# c = 282j
# print(c)
# print(type(c))

# # list 
# d = ["apple","orange","banana"]
# print(d)
# print(type(d))

# # tuple
# e = ("apple","banana","orange",)
# print(e)
# print(type(e))

# # range
# f = range(100)

# print(f)
# print (type(f))

# # set
# g = {'aple', "banana"}
# print (g)
# print(type(g))

# # bool
# h = True
# H = False

# print (h)
# print (H)
# print(type(h))
# print(type(H))

# # bytes
# i = b"hello"
# print (i)
# print(type(i))

# # bytearray
# j = bytearray (2)
# print (j)
# print(type(j))

# # none type
# k = None
# print (k)
# print(type(k))




# String Format
# l = str(input("enter your name:" ))
# L = int(input("enter your age :"))
# name = l
# age = L

# print(f"my name is {name} and my age is {age}")



# Boolean Values
# a = int(input("enter your fast number: "))
# b = int(input("enter your second number: "))
# x = ( a < b )

# if x is True :
#     print ("your second number is bigger than fast number!")
# elif x is False:
#     print("your fast number is bigger than your second number! ")
# else:
#     print("sorry we cant undastend what your say!")



# Python Operators

# m = 50
# n = 10
# w = m + n
# x = m - n
# y = m * n 
# z = m / n

# a = m % n
# b = m ** n
# c = m // n 
# d = 5

# m += 553
# m -= 5
# m *= 5
# m /= 6
# m %= 8
# m //= 50
# m **= 4

# print(m == n)
# print(m != n) 
# print(m < n)
# print(m > n)
# print(m >= n)
# print(m <= n)


# print(w)
# print(x)
# print(y)
# print(z)
# print(a)
# print(b)
# print(c)
# print(d)
# print(m)



# Python Logical Operators
# x = 5
# y = 7

# print(x < y and x > y )
# print(x < y and x > y )

# print(x > y or x < y )
# print(x > y or x < y )

# print(x < y and not x > y )
# print(x < y or not x > y )

# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is z)     # returns True because z is the same object as x
# print(x is y)      # returns False because x is not the same object as y, even if they have the same content
# print(x == y)       # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y



# Python Lists
# list1 = ["banana","apple","orange","junkfrut","papaya"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]

# print (list1)
# print(len(list1))

# Python - Access List Items
# print(list1[1])
# print(list1[-1])
# print(list1[0:4])
# print(list1[:4])
# print(list1[2:])
# print(list1[-5:-1])

# if "banana" in list1 :             # To determine if a specified item is present in a list use the in keyword
#     print("thats ok")

# list1[0] = "kola"                  # To change the value of a specific item, refer to the index number
# print (list1)

# list1 [0:1] = ["hey","hello","bye","beutty","love you"] 
# print(list1)

# list1.insert(0,"hello wolrd")   #To insert a new list item, without replacing any of the existing values, we can use the insert() method. 
# print (list1)