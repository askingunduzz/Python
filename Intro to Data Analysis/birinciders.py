# -*- coding: utf-8 -*-
"""birinciDers.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vsamYeqYp8Isch0BjSDkYhqTZE-KyuqP
"""

Learning

"""Learning

Simple data structures: List Dictionary Set tuple, Booleans, Integers,FLoats
"""





"""Booleans

"""

x=True #sdfsdf
y=False
type(x)

"""Integers and Floats"""

x=1
type(x)
y=1.4
type(1.4)

"""Float

"""

2*3

x=3
y=4.3
x*y

x+y

4*5

"""Exponentiation"""

2**3
3**3
3*3

"""Stringas"""

x="Hello everyone whats up"
print(x)

print(x[1])

x[0]

x[-1]

x[-3]

x[0]='Y'  ##we cant do this. strings in python are not mutable. You cant just change them

x=3

x=4

x="hello"
y="everyone"
x+" " +y

"""String Formatting"""

x= 37
print(f"I am {x} years old")

print("I am {} years old".format(x))

x=1.5
y=3.0
##dir(x)
x.is_integer()

str="I am {} years old".format(x)
print(str)

str.split()

"""String Slicing"""

str[2:10]
str[0:12]
str[-10:]

type(str)

"""#Lists"""

x=[] #empty list

#A list is a container of objects

x=[1,2,3,4]
print(x)

x[1]

x[0]=10
print(x)   #we couldnt do this with strings
#lists are mutable!

S=["sad",True,10,[123,234],["aha","haha"]]   #python allows this! wow
print(S)

S[0]

S[-2]

dir(S)

S.append("aaHHHHHaaa")   #vaaaaayy
print(S)

S.pop()
print(S)

#Concatanate Lists
x=[1,2,3,4]
y=["a","b","c"]
x+y   #isnt the same with y+x !!

#How do i check that x contains 1?
1 in x
#çok havalı bu arada
"d" in y
#also
1 not in x   #not contained

5*x == x+x+x+x+x

#For instance you would like to initialize a list of zeros of length 10
x=10*[0]
print(x)
y=10*"y "
print(y)

#Dictionaries
