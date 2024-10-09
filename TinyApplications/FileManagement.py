# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:41:01 2024

@author: Ede Rojin DELİBAŞ
"""

#File Management
#write mode("w"): It is creating the file in givin' path but it is deleting the content of the file then adding the new info. 

file=open("newfile.txt","w",encoding="utf-8") 
print(file)
#closing the file: It is a necessary action otherwise it will use our resources.
file.close()
#We can create a file in any place that we want, we need to give the path
filee= ("C:/users/Ede Rojin DELİBAŞ/.py/BTKAkademiUyg/new.txt","w")
file.write("How do you feel about coding right now?")
#Reading a file
#The method read() also can take a parameter called size which means the character number,It's actually the bit number
#Every character is a bit
#The function readline() shows us just one row on program
#The function readlines() shows the characters inside of an array.
newFile=open("newfile.txt","r",encoding="utf-8")

for i in newFile:
    print(i,end="")
newFile.close()
#using with and closing otomatically(time of the program is up to syntax next to with)
with open("newfile.txt","r",encoding="utf-8") as file:
    content=file.read()
    print(content)
#The method tell() gives the position of the cursor
    print(file.tell())
#Using seek() method we can replace the cursor and go which position we want in the text.
#Updating the read file
#r+ it means reading and writing at the same time.
with open("newfile.txt","r+",encoding="utf-8") as file:
    file.seek(12)
    file.write("deneme")
#updating position=middle of the page

with open("newfile.txt", "r+",encoding="utf-8") as file:
    list=file.readlines()
    list.insert(1,"Selen")
    file.seek(0) #taking the location to the beginning of the page
    file.writelines(list)
    for i in list:
        file.write(i)
with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())    
#Note Example
def calculate_average(rows):
    rows=rows[:-1]#taking the spaces between rows
    liste=rows.split(':')
    SNames=liste[0]
    SNotes=liste[1].split(',')
    not1=int(SNotes[0])
    not2=int(SNotes[1])
    not3=int(SNotes[2])
    avg=(not1+not2+not3)/3
    
    return SNames + ': '+ (str(avg))
    
def readAverage():
    with open ("studentInformations.txt","r",encoding="utf-8") as file:
        for rows in file:
            print(calculate_average(rows))
def enterNotes():
    name=input("Student Name:")
    surname=input("Student Surname:") 
    note1=(input("Note-1:"))
    note2=(input("Note-2:"))
    note3=(input("Note-3:"))
    with open("studentInformations.txt","a",encoding="utf-8") as file:
        file.write(name+' '+surname+':'+note1+','+note2+','+note3+'\n')
    
def saveNotes():
    with open("studentInformations.txt","r",encoding="utf-8") as file:
        liste=[]
        for i in file:
            liste.append(calculate_average(i))
        with open("results.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i+'\n')
while True:
    islem=input("1-Show the Notes\n2-Enter Notes\n3-Save the Notes\n4-Exit\n")
    
    if islem=='1':
        readAverage()
    elif islem=='2':
        enterNotes()
    elif islem=='3':
        saveNotes()
    else:
        break










    