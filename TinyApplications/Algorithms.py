# # -*- coding: utf-8 -*-
# """
# Created on Fri Sep 27 18:15:27 2024
#
# @author: Ede Rojin DELİBAŞ
# """
# """Programming Algorithms and Data Structures-Examples By Joe Marini"""
# #Finding the GCD(Greatest Common Denominator) of two integers using Euclid's algorithm
def gcd(a,b):
    while(b != 0):
        t=a
        a=b
        b=t%b
    return a

print(gcd(20, 8))

# #Linked Lists
#The node class
class Node(object):
    def __init__(self,val): #constructor method,initialize a new node
        self.val=val
        self.next=None #it doesn't point to any other node(yet)
    def getData(self):
        return self.val
    def setData(self,val):#This method sets or updates the value of the node
        self.val=val
    def getNext(self):#This method returns the next node that the current node is pointing to
        return self.next
    def setNext(self,next):#This method sets the next attribute to point to another node,
    #effectively linking two nodes together in a sequence
       self.next=next

# #The linked list class
class LinkedList(object):
    def __init__(self, head=None):#meaning the list starts empty.
        self.head=head
        self.count=0 #How many nodes in the list
    def getCount(self):
        return self.count
    def insert(self,data):#This method adds a new node to the beginning of the linked list
        #TODO:insert a new node
        newNode=Node(data)
        newNode.setNext(self.head)
        self.head=newNode
        self.count+=1
    def find(self, val):
        #TODO:find the first item with a given value
        item=self.head
        while (item!=None):
            if item.getData()== val:
                return item
            else:
                item=item.getNext()
        return None
    def deleteAt(self,idx): #idx is the node that we will delete
        #TODO:delete an item at given index
        if idx > self.count-1:#controlling the total node number
            return
        if idx==0:#If we want to delete the head node
            self.head=self.head.getNext()#The head will changed by the next node
        else:
            tempIdx=0
            node=self.head
            while tempIdx < idx-1:
                node=node.getNext()
                tempIdx+=1
            node.setNext(node.getNext())
            self.count-=1

    def dumpList(self):#showing the nodes on the screen
        tempNode=self.head
        while (tempNode!=None):
            print("Node:",tempNode.getData())
            tempNode=tempNode.getNext()

# #create a linkedList and insert some items
itemList=LinkedList()
itemList.insert(12)
itemList.insert(13)
itemList.insert(45)
itemList.dumpList() #prints out the list
#exercise the list
print("Item count: ",itemList.getCount())
print("Finding item: ",itemList.find(13))
print("Finding item: ", itemList.find(33))
itemList.deleteAt(0)
print("Item count: ",itemList.getCount())
print("Finding item: ",itemList.find(12))
itemList.dumpList()

# #Stacks and Queues
stack=[]
stack.append(1) #push items onto stack
stack.append(22)
stack.append(23)
stack.append(45)
x=stack.pop() #pop an item off the stack
print(x)
print(stack)

from collections import deque
queue=deque() #create a new deque object that will function as a queue
queue.append(1) #add some item to the queue
queue.append(22)
queue.append(23)
queue.append(45)
print(queue)
#pop an item off the front of the queue
y=queue.popleft()
print(y)
print(queue)

# #Hash Tables
items1=dict({"key1":1,"key2":2,"key3":"three"})
print(items1)
items2={} #creating progressively
items2["key1"]=1
items2["key2"]=25
items2["key3"]=13
print(items2)
#try to access nonexistent key
print(items1["key5"])#error occurs

#iterate the keys and values in the dictionary
for key, value in items2.items():
    print("Key:", key, " value: ",value)
#use recursion to implement a countdown counter
def countdown(x):
    if x==0:
        print("Done")
        return
    else:
        print(x, "...")
        countdown(x-1)
countdown(5)

#Using recursion to implement power and factorial functions
def power(num,pwr):
    if pwr==0:
        return 1
    else:
        return num * power(num,pwr-1)

def factorial(num):
    if num==0:
        return 1
    else:
        return num * factorial(num - 1)
print("{} to the power of {} is {}".format(5,3,power(5,3)))
print("{} to the power of {} is {}".format(1,5,power(1,5)))
print("{}! is {}".format(4,factorial(4)))
print("{}! is {}".format(0,factorial(0)))

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

# MERGE SORT #
#Implement a merge sort with recursion
items=[6,20,8,19,56,23]
def merge_sort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr=dataset[:mid]
        rightarr=dataset[mid:]
        
        #TODO:recursively break down the array
        merge_sort(leftarr)
        merge_sort(rightarr)

        #TODO:now perform the merging
        i=0 #index into the left array
        j=0 #index into the right array
        k=0 #index into the merged array

        #TODO:while both arrays have content 
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1
        
        #TODO:if the left array still has values, add them
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1

        #TODO:if the right array still has values, add them
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1
print("Unsorted list:", items)
merge_sort(items)
print("Sorted list:", items)

## Quick Sort ##
items=[6,20,8,19,56,23]
def quick_sort(dataset,first,last):
    if first < last:
        #calculate the split point
        pivotIdx=partition(dataset,first,last)

        #now sort the two partitions
        quick_sort(dataset,first,pivotIdx-1)
        quick_sort(dataset,pivotIdx+1,last)

def partition(datavalues,first,last):
    #choose the first item as the pivot
    pivotvalue=datavalues[first]
    #establish the upper and lower indexes
    lower=first + 1
    upper=last

    #start searching for the crossing point 
    done=False

    while not done:
        #TODO:advance the lower index 
        while lower <= upper and datavalues[lower] <= pivotvalue:
            lower += 1
        #TODO:advance the upper index
        while lower <= upper and datavalues[upper] >= pivotvalue:
            upper -= 1

        #TODO:if the indexes cross, we have found the split point
        if lower > upper:
            done = True
        else:
            temp=datavalues[lower]
            datavalues[lower]=datavalues[upper]
            datavalues[upper]=temp

    #when the split point is found,exchange the pivot value
    temp=datavalues[first]
    datavalues[first]=datavalues[upper]
    datavalues[upper]=temp

    #return the split point index
    return upper

#test the merge sort with data
print("Unsorted list:", items)
quick_sort(items, 0, len(items) - 1)
print("Sorted list:", items)

#searching for an item in an unordered list
#sometimes called linear search
items=[6,20,8,19,56,23,87,41,49,53]
def find_item(item,itemlist):
    for i in range(0,len(itemlist)):
        if item == itemlist[i]:
            return i
        
    return None

print(find_item(19,items))  #should return 3
print(find_item(100,items)) #should return None

#searching for an item in an ordered list
#this technique uses a binary search algorithm
items=[6,8,19,20,23,41,49,53,56,87]
def binary_search(item, itemlist):
    #get the list size
    listsize=len(itemlist)-1

    #start at the two ends of the list
    lowerIdx=0
    upperIdx=listsize
    while lowerIdx <= upperIdx:
        #find the midpoint
        midIdx=(lowerIdx + upperIdx) // 2

        #check if the item is at the midpoint
        if itemlist[midIdx] == item:
            return midIdx
        elif itemlist[midIdx] < item:
            #item is in the upper half of the list
            lowerIdx=midIdx + 1
        else:
            #item is in the lower half of the list
            upperIdx=midIdx - 1
    #if we get here, the item was not found
    if lowerIdx > upperIdx:
        return None
    
print(binary_search(19, items))  #should return 3
print(binary_search(100, items)) #should return None

#determine if a list is sorted
items1=[6,8,19,20,23,41,49,53,56,87]
items2=[6,80,9,2,3,40,53,5,7,23]

def is_sorted(itemlist):
    #TODO:using the brute force method
    for i in range(0, len(itemlist) - 1):
        if itemlist[i] > itemlist[i + 1]:
            return False 
    
print(is_sorted(items1))  #should return True
print(is_sorted(items2))  #should return False

# #pythonic way of doing that(py comprehension)
def is_sorted_pythonic(itemlist):
    return all(itemlist[i] <= itemlist[i + 1] for i in range(len(itemlist) - 1))

## HASH TABLES ##
#use a hash table to filter out duplicate items

#define a set of items that we want to reduce duplicate items
items=["apple", "banana", "orange", "apple", "kiwi", "banana",
        "kiwi", "orange", "pomegranate", "strawberry", "kiwi",
        "apple", "banana", "orange", "kiwi", "pomegranate"]
#TODO:create a hashtable to perform a filter
filter = dict()

# TODO:loop over each item and add to the hashtable
for item in items:
    filter[item]=0
# TODO:create a set from the resulting keys in the hashtable
result =set(filter.keys())
print(result)

## Value Counter 
#use a hashtable to count individual items in a list
items=["apple", "banana", "orange", "apple", "kiwi", "banana",
        "kiwi", "orange", "pomegranate", "strawberry", "kiwi",
        "apple", "banana", "orange", "kiwi", "pomegranate"]

#TODO:Create a hashtable object to hold the items and counts
counter=dict()
#TODO:iterate over each item and increament the count for each one
for item in items:
    if(item in counter.keys()):
        counter[item]+=1
    else:
        counter[item]=1 

## find maksimum value with recursion
items=[6,20,8,19,56,23]

def find_max(items):
    if len(items) == 1:
        return items[0]
    opt1=items[0]
    print("Current item:", opt1)
    opt2=find_max(items[1:])
    print(opt2)
    if opt1 > opt2:
        return opt1
    else:
        return opt2
    
print("Maximum value in the list is:", find_max(items))  #should return 56

### Try to understand this code in up 

## maze gui game

