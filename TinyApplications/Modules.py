# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 07:01:23 2024

@author: Ede Rojin DELİBAŞ
"""
#Pyhton Modules
#1-Math Module
#import math
#First way
"""value = dir(math)
value1=help(math)
value2=help(math.factorial)
print(value2)"""
#Second Way
import math as calc
value3=calc.factorial(5)
#print (value3)
#Third way 
from math import * #Getting all
value4=sqrt(64)
#print (value4)
#Forth way:just getting the necessary ones
from math import factorial,sqrt,floor
value5=factorial(4)
print(value5)
#Random Modülü
import random
result=random.random()
#print(result) # It's generate a number between 0-1.
#Get a random number in range using uniform. 
res=random.uniform(5, 12)
#print(res)
#randint
ress=random.randint(1,100)
#print(ress)
names=['Ali','Ede','Naz','Dilek','Yakup']
index=names[random.randint(0,len(names)-1)]
#print(index)
#We can do the same thing using  choice(choose a random element from a non-empty sequence)
indexx=random.choice(names)
print(indexx)
#shuffle method: mixing the list
list1=list(range(10))
random.shuffle(list1)
#print(list1)
#sample is used for getting random elements from an array
examples=random.sample(list1,2)
#print(examples)
#Using my module
import MyFirstModule
#Getting some info about my module
info=help(MyFirstModule)
#print(info)
father=MyFirstModule.family_members["father"]
print(father)
func=MyFirstModule.Person()
#print(func)
import sys
#We will use this method for getting the path of the python file and the modules

paths=sys.path
print(paths)
















