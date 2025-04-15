# # -*- coding: utf-8 -*-
# """
# Created on Fri Sep 27 18:15:27 2024
#
# @author: Ede Rojin DELİBAŞ
# """
# """Programming Algorithms and Data Structures-Examples By Joe Marini"""
# #Finding the GCD(Greatest Common Denominator) of two integers using Euclid's algorithm
# def gcd(a,b):
#     while(b != 0):
#         t=a
#         a=b
#         b=t%b
#     return a
#
# print(gcd(20, 8))
# #Linked Lists
# #The node class
# class Node(object):
#     def __init__(self,val): #constructor method,initialize a new node
#         self.val=val
#         self.next=None #it doesn't point to any other node(yet)
#     def getData(self):
#         return self.val
#     def setData(self,val):#This method sets or updates the value of the node
#         self.val=val
#     def getNext(self):#This method returns the next node that the current node is pointing to
#         return self.next
#     def setNext(self,next):#This method sets the next attribute to point to another node,
# #effectively linking two nodes together in a sequence
#         self.next=next
#
# # #The linked list class
# class LinkedList(object):
#     def __init__(self, head=None):#meaning the list starts empty.
#         self.head=head
#         self.count=0 #How many nodes in the list
#     def getCount(self):
#         return self.count
#     def insert(self,data):#This method adds a new node to the beginning of the linked list
#         #TODO:insert a new node
#         newNode=Node(data)
#         newNode.setNext(self.head)
#         self.head=newNode
#         self.count+=1
#     def find(self, val):
# #TODO:find the first item with a given value
#         item=self.head
#         while (item!=None):
#             if item.getData()== val:
#                 return item
#             else:
#                 item=item.getNext()
#         return None
#     def deleteAt(self,idx): #idx is the node that we will delete
#         #TODO:delete an item at given index
#         if idx > self.count-1:#controlling the total node number
#             return
#         if idx==0:#If we want to delete the head node
#             self.head=self.head.getNext()#The head will changed by the next node
#         else:
#             tempIdx=0
#             node=self.head
#             while tempIdx < idx-1:
#                 node=node.getNext()
#                 tempIdx+=1
#             node.setNext(node.getNext())
#             self.count-=1
#
#     def dumpList(self):#showing the nodes on the screen
#         tempNode=self.head
#         while (tempNode!=None):
#             print("Node:",tempNode.getData())
#             tempNode=tempNode.getNext()
#
# #create a linkedList and insert some items
# itemList=LinkedList()
# itemList.insert(12)
# itemList.insert(13)
# itemList.insert(45)
# itemList.dumpList() #prints out the list
# #exercise the list
# print("Item count: ",itemList.getCount())
# print("Finding item: ",itemList.find(13))
# print("Finding item: ", itemList.find(33))
# itemList.deleteAt(0)
# print("Item count: ",itemList.getCount())
# print("Finding item: ",itemList.find(12))
# itemList.dumpList()
# #06.10.24
# #Stacks and Queues
# stack=[]
# stack.append(1) #push items onto stack
# stack.append(22)
# stack.append(23)
# stack.append(45)
# x=stack.pop() #pop an item off the stack
# print(x)
# print(stack)
# from collections import deque
# queue=deque() #create a new deque object that will function as a queue
# queue.append(1) #add some item to the queue
# queue.append(22)
# queue.append(23)
# queue.append(45)
# print(queue)
# #pop an item off the front of the queue
# y=queue.popleft()
# print(y)
# print(queue)
# #Hash Tables
# items1=dict({"key1":1,"key2":2,"key3":"three"})
# print(items1)
# items2={} #creating progressively
# items2["key1"]=1
# items2["key2"]=25
# items2["key3"]=13
# print(items2)
# #try to access nonexistent key
# # print(items1["key5"])#error occurs
# #iterate the keys and values in the dictionary
# for key, value in items2.items():
#     print("Key:", key, " value: ",value)
# #use recursion to implement a countdown counter
# def countdown(x):
#     if x==0:
#         print("Done")
#         return
#     else:
#         print(x, "...")
#         countdown(x-1)
# countdown(5)
#03.02.2025
#Using recursion to implement power and factorial functions
# def power(num,pwr):
#     if pwr==0:
#         return 1
#     else:
#         return num * power(num,pwr-1)
#
# def factorial(num):
#     if num==0:
#         return 1
#     else:
#         return num * factorial(num - 1)
# print("{} to the power of {} is {}".format(5,3,power(5,3)))
# print("{} to the power of {} is {}".format(1,5,power(1,5)))
# print("{}! is {}".format(4,factorial(4)))
# print("{}! is {}".format(0,factorial(0)))
## SORTING ALGORITHMS ##
# BUBBLE SORT #
def bubble_sort(dataset):
    #TODO:start with the array lenght and decrement each time
    for i in range(len(dataset)-1,0,-1): #it's starts from end of the array.
        for j in range(i):
            if dataset[j] > dataset[j+1]:
                temp=dataset[j]
                dataset[j]=dataset[j+1]
                dataset[j+1]=temp
        print("current state:",dataset)
def main():
    list1=[6,20,8,19,56,23]
    bubble_sort(list1)
    print("result",list1)
if __name__=="__main__":
    main()