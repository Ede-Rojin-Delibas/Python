# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 07:01:23 2024

@author: Ede Rojin DELİBAŞ
"""
#Pyhton Modules
#1-Math Module
import math
# #First way
value = dir(math)
value1=help(math)
value2=help(math.factorial)
print(value2)

# #Second Way
import math as calc
value3=calc.factorial(5)
print (value3)

# #Third way
from math import * #Getting all
value4=sqrt(64)
print (value4)

# #Forth way:just getting the necessary ones
from math import factorial,sqrt,floor
value5=factorial(4)
print(value5)

# #The Module Random
import random
result=random.random()
print(result) # It's generate a number between 0-1.

# #Get a random number in range using uniform.
res=random.uniform(5, 12)
print(res)
# #randint
ress=random.randint(1,100)
print(ress)
names=['Ali','Ede','Naz','Dilek','Yakup']
index=names[random.randint(0,len(names)-1)]
print(index)

# #We can do the same thing using  choice(choose a random element from a non-empty sequence)
indexx=random.choice(names)
print(indexx)

# #shuffle method: mixing the list
list1=list(range(10))
random.shuffle(list1)
print(list1)
# #sample is used for getting random elements from an array
examples=random.sample(list1,2)
print(examples)

# #Using my module
import MyFirstModule
# #Getting some info about my module
info=help(MyFirstModule)
print(info)
father=MyFirstModule.family_members["father"]
print(father)
func=MyFirstModule.Person()
print(func)
import sys

# #We will use this method for getting the path of the python file and the modules
paths=sys.path
print(paths)

## Datetime Module ##
import datetime
simdi=datetime.datetime.now()
result=simdi.now()
result1=simdi.now().month
print(result1)
t=datetime.datetime.now().ctime()
t1=datetime.datetime.now().strftime('%Y')
t2=datetime.datetime.now().strftime('%d')
ti=datetime.datetime.now().strftime('%Y %X %A')

#for more information go check the datetime python
from datetime import datetime
from datetime import timedelta
t= '23 January 2023 hour 15:41:04'
dt=datetime.strptime(t,'%d %B %Y Hour %H:%M:%S')
saniye=datetime.timestamp(dt)
print(saniye) # It gives the related date in second

#for converting second to datetime again
rst=datetime.fromtimestamp(saniye)
print(rst)
rst=datetime.fromtimestamp(0) #milestone date for computers
print(rst)
#subtraction of two date
newresult=simdi-timedelta(days=10)
print(newresult)

## OS MODULE ##
import os
result=dir(os) # for modules and classes
print(result)
os.chdir('C:\\')#for changing directory
os.chdir('../..') #for changing directory twice - C
os.mkdir("newfile") #creates new folder
result=os.getcwd() #for learning active directory
os.makedirs('newfile/newfl') #another command for creating folder
os.listdir()#for listing
os.stat()#for getting informations about file
path=os.path.abspath('filename') #for finding exact path of files
path1=os.path.join('path1','path2') #join 2 paths
path2=os.path.split('path1','path2') #splitting paths

## Regular Expression Module ##
import re
str="Python programlama kursu BTK"
result=re.findall("Python",str)
r1=re.split(' ',str)
r2=re.sub(' ','-',str)
r3=re.search("Python",str)
# r4=re.match.span() #for location of the pattern
r5=re.findall("[erd]",str)
r6=re.findall('K$',str)
r7=re.findall("p{1}",str)
print(r7)

## JSON MODULE ##
import json
person_string='{"name":"Ali","languages":["python","C#"]}'
result=json.loads(person_string)
# print(type(result)) #class dict
person_dict={
    "name":"Ali",
    "Languages":["Python","C#"]
}
result2=json.dumps(person_dict)
print(type(result2)) #class str

## Example ##
import json
import os
class User:
    def __init__(self,userName,password,email):
        self.userName=userName
        self.password=password
        self.email=email
class UserRepository:
    def __init__(self):
        self.users = []
        self.isloggedIn=False
        self.currentUser={}

        #load users from .json file/method
        self.loadUsers()
    def logout(self):
        self.isloggedIn = False
        self.currentUser = {}
        print('çıkış yapıldı.')
    def identity(self):
        if self.isloggedIn:
            print(f'username:{self.currentUser.userName}')
        else:
            print('giriş yapılmadı')
    def savetoFile(self):
        user_list=[user.__dict__ for user in self.users]
        # determine file path
        file_path = os.path.join(os.path.dirname(__file__), 'users.json')
        # print(file_path)
        #save users to file
        with open(file_path,'w',encoding='utf-8') as file:
            json.dump(user_list,file,ensure_ascii=False,indent=4)
    def loadUsers(self):
        file_path = os.path.join(os.path.dirname(__file__), 'users.json')
        # check if the file exists
        if not os.path.exists(file_path):
            return  # No users to load if file doesn't exist
        # Read and load users from the file
        #json file reading process when userRepository ran
        with open(file_path,'r',encoding='utf-8') as file:
            users=json.load(file)
            for user_data in users:
                user=User(**user_data)
        #         newUser=User(username=user.username,password=user.password,email=user.email)
        #         self.users.append(newUser)
                self.users.append(user)
        # print(self.newUser)
    def register(self,user:User):
        self.users.append(user)
        self .savetoFile()
        print('Kullanıcı oluşturuldu.')
    def login(self,userName,password):
        for user in self.users:
            if user.userName==userName and user.password==password:
                self.isloggedIn=True
                self.currentUser=user
                print('Oturum açıldı')
                break

Repository=UserRepository()
while True:
    print(' Menu '.center(50,'*'))
    secim=input('1-Register\n2-Login\n3-Logout\n4-identity\n5-Exit\nseçiminiz: ')
    if secim=='5':
        break
    else:
        if secim=='1':
            userName=input('username:')
            password=input('password:')
            email=input(('email:'))
            user=User(userName=userName,password=password,email=email)
            Repository.register(user)
            # print(Repository.users)
        elif secim=='2':
            if Repository.isloggedIn:
                print('zaten giriş yaptınız.')
            else:
                userName=input('userName: ')
                password=input('password: ')

            Repository.login(userName,password)
        elif secim=='3':
            Repository.logout()
        elif secim=='4':
            Repository.identity()
        else:
            print('yanlış seçim yaptınız, lütfen tekrar seçiniz.')

## REQUEST MODULE ##
import site
import requests
import json
#it will show the installed packages
print("Kurulu paketlerin yolları:")
for path in site.getsitepackages():
    print(path)
#It prints an obvious package's path
print("\n'requests' paketinin yolu:")
print(requests.__file__)
response = requests.get('https://jsonplaceholder.typicode.com/todos')
result=json.loads(response.text)
print(response) #200
print(result)
response=response.text
print(response)
print(response.json())

### REQUESTS ###
import requests
api_key="cd91dda5d2284eb4cb738a59"
api_url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"
bozulan_doviz=input("Bozulan döviz türü: ") #USD
alinan_doviz=input("Alınan döviz türü: ") #TRY
miktar= int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz?"))
sonuc=requests.get(api_url + bozulan_doviz)
# print(sonuc.text)
sonuc_json=json.loads(sonuc.text)
# print(sonuc_json["conversion_rates"][alinan_doviz])
print("1 {0} = {1} {2}".format(bozulan_doviz,sonuc_json["conversion_rates"][alinan_doviz],alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar,bozulan_doviz,miktar*sonuc_json["conversion_rates"][alinan_doviz],alinan_doviz))

## new example ##
class Github:
    def __init__(self):
        self.api_url='https://api.github.com'
        self.token=''
    def getUser(self,username):
        response=requests.get(self.api_url+'/users/'+username)
        return response.json()
    def getRepositories(self,username):
        response=requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()
    def createRepository(self,name):
        headers = {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json'}
        data = {
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        }
        response = requests.post(f'{self.api_url}/user/repos', headers=headers, json=data)
        return response

github=Github()
while True:
    secim=input("1-Find User\n2-Get Repository\n3-Create Repository\n4-Exit\nSeçim: ")

    if secim == '4':
        break
    else:
        if secim =='1':
            username=input("kullanıcı adınızı giriniz:")
            result=github.getUser(username)
            print(f"name:{result['name']} public repos: {result['public_repos']} followers: {result['followers']}")
        elif secim =='2':
            username=input("kullanıcı adınızı giriniz: ")
            result=github.getRepositories(username)
            for repo in result:
                print(repo['name'])
        elif secim=='3':
            name=input("name: ")
            result=github.createRepository(name)
            print(result)
        else:
            print('yanlış bir seçim yaptınız!')

## new app ## : movies
#themoviedb.org =>film ve dizi arşivi
#themoviedb'nin sunduğu apiyi uygulamamızda kullanalım
#anahtar kelimeye göre arama
#en popüler film listesi
#vizyondaki film listesi

class MovieDB:
    def __init__(self):
        self.api_url="https://api.themoviedb.org/3"
        self.api_key="c25001cfaa78d03a7aa8d9e848239caf"
    def getPopulars(self):
        response=requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()
    def getSearchResults(self,keyword):
        response=requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()

movieApi=MovieDB()
while True:
    secim=input("1-Popular Movies\n2-Search Movies\n3-Exit\nSecim: ")
    if secim=="3":
        break
    else:
        if secim=="1":
            movies=movieApi.getPopulars()
            for movie in movies['results']:
                print(movie['title'])
        if secim=="2":
            keyword=input("keyword: ")
            movies = movieApi.getSearchResults(keyword)
            for movie in movies['results']:
                print(movie['name'])
        else:
            print("lüften tekrar seçim yapınız!!")

