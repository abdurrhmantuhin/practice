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




# #String Format
# l = str(input("enter your name:" ))
# L = int(input("enter your age :"))
# name = l
# age = L

# print(f"my name is {name} and my age is {age}")



# #Boolean Values
# a = int(input("enter your fast number: "))
# b = int(input("enter your second number: "))
# x = ( a < b )

# if x is True :
#     print ("your second number is bigger than fast number!")
# elif x is False:
#     print("your fast number is bigger than your second number! ")
# else:
#     print("sorry we cant undastend what your say!")



# #Python Operators

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



# #Python Logical Operators
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



# #Python Lists
# list1 = ["banana","apple","orange","junkfrut","papaya"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]

# print (list1)
# print(len(list1))

# #Python - Access List Items
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

# #add list items
# list1.append("juice")
# list1.insert(0, "yello")
# list1.extend(list2)         #The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

# print(list1)


# #remove items 
# list1.remove("banana")
# list1.pop(1)
# del list1 [3]
# del list1             #this will cause an error because you have succsesfully deleted "thislist".
# list1.clear()         #The list still remains, but it has no content.

# print(list1)



# #Loop Through a List
# thislist = ["apple", "banana", "cherry"]
# x = 0
# for x in thislist:
#     print (thislist)
#     print (x)

# for x in range(len(thislist)):
#     print (thislist[x])

# while x < len(thislist):
#     print (thislist[x])
#     x += 1 

# [print (x) for x in thislist]



# #List Comprehension
# number = [1,2,3,4,5,]
# double = [i**3 for i in number]
# print (double)



# #Sort Lists
# num1 = [3,65,8,32,54,21,5,4,6,531,745]
# num2 = ["c","s","f","e","q","t","i","o","p","m","j","h","g","w"]

# num2.sort()
# print (num2)

# num1.sort()
# print (num1)


# #reverse
# num = [1,2,3,4,5,6,7,8]
# num.sort(reverse = True)
# print (num) 



# #Copy Lists
# num = [1,2,3,4,5,6,7,8,9,10]
# num2 = num.copy()
# print (num2)



# # Join Two Lists
# num1 = [1,2,3,4,5,]
# num = [6,7,8,9,10]
# num1.extend(num)
# print (num1)


# # #matrix
# num = [
#     [1,2,3,4,5,6],
#     [7,8,9,10,11],
#     1233 ,
#     ["banana","apple","juice","mango"]
# ]

# print(num[3][3])



# #Tuples
# num = (1,2,3,4,5,6,7,8,9,10)

# num[2] = 23                    # A tuple is a collection which is ordered and unchangeable.
# print(num)
# print(num[2])                  # Negative Indexing

# print(num[2:3])                  # Range of Indexes



# # Python - Update Tuples
# eng = ("apple","banana","papaya")

# x = list(eng)                              # there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
# x.append("orange")
# eng = tuple(x)
# print (eng)

# x = ("cherry",)
# eng += x                    # allowed to add tuples to tuples
# print (eng)

# #Unpack Tuples
# fruits = ("apple", "banana", "cherry","papaya","oange")
# (*x,y,z) = fruits
# print(x)                                #  we are also allowed to extract the values back into variables. This is called "unpacking"
# (x,*z) = fruits
# print (z)
# (x,*y,z)= fruits
# print (y)



# # Loop Tuples
# fruits = ("apple", "banana", "cherry","papaya","oange")


# for x in fruits :
#     print(x)


# for i in range(len(fruits)):
#     print (fruits[i])

# x = 0 

# while x < len(fruits):
#     print(fruits[x])
#     x += 1



# # Join Tuples
# num = (1,2,3,4,5,67,8)
# # num1 = (1,2,3,4,5,67,8)
# num2 = num * 2
# print (num2)
# print(num+num1)



# Tuple Methods
# fruits = ("apple", "banana", "cherry","papaya","orange", "banana")

# x = fruits.index("orange")                                              # Returns the number of times a specified value occurs in a tuple
# print(x)

# y = fruits.count("banana")                                             # Searches the tuple for a specified value and returns the position of where it was found

# print (y)



# #set type 
# fruits = {1,2,3,4,5,6,7,8,26,"apple","banana","cherry","orange","papapya","papapya","orange",False}
# print(len(fruits))

# for x in fruits:
#     print (x)

# print(1 in fruits)              # and only True and False 



# #Add Set Items
# set1 = {1,2,3,4,5,10}
# set2 = [6,7,8,9,10]

# set1.add(6)
# print(set1)

# set1.update(set2)
# print (set1)

# set1.remove(3)
# set1.discard(10)                           # If the item to remove does not exist, discard() will NOT raise an error.
# set1.pop()
# set1.clear()

# print (set1)

