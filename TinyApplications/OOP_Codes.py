# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 15:31:36 2024

@author: Ede Rojin DELİBAŞ
"""
#OOP-Object Oriented Programmming Codes
class Person:
    pass    #yer tutucu
    #attributes
        #-class seviyesinde attribute (class attributes)tanımlama ve object seviyesinde attributes(object attributes) tanımlama
    #methods
    #object attributes tanımı
    def __init__(self,name,year):
        self.name=name
        self.year=year
        #print("self methodu çalıştırıldı.")
        
        #instance method
    def intro(self):
        print("Hello There.I am " + self.name)
        
    def calculateAge(self):
        return 2024 - self.year
#class attributes, constructor ya da methodların aynı hizada olması gerekiyor.
#instance methodun ilk parametresi selftir.
    

#init methodunun oluşturulmasındaki sebep her obje için mutlaka çalıştırılıyor olması
#obje tanımı ; obje tanımlandıktan sonra o sınıfın method ve attribute'larını kullanabilir.
p1=Person('Bay Darcy',1974)
p1.intro()
print(p1.calculateAge())
print(f"name:{p1.name}, year:{p1.year}")

class Circle:
    #class object attribute
    pi=3.14
    
    def __init__(self,yaricap=1):
        self.yaricap=yaricap

    #Methods
    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap
        
    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)
c1=Circle(3)
print(f'c1 nesnesinin alanı:{c1.alan_hesapla()} ve c1 nesnesinin çevresi:{c1.cevre_hesapla()}')
#Inheritance(Kalıtım) kavramı
#Person=>name,lastname, age, eat(),drink(),breathe()
#student(person),teacher(person)
#animal=> dog(animal),fish(animal)

class Person():
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        print('Person created')
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        print('Student created')
class Teacher(Person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)
        self.branch=branch
    def who_am_i(self):
        print(f'I am a {self.branch} teacher')
p1=Person('Ali','Aydın')
s1=Student('Çınar','Turan')
t1=Teacher('Semra', 'Kara', 'literaty')
t1.who_am_i()
print(p1.firstname +' '+p1.lastname)
print(s1.firstname +' '+s1.lastname)
#objeler üzerinde kullandığımız bazı özel methodlar
#len methodu class üzerinde direkt olarak kullanılmaz (liste ya da dictionary de  bir classtır 
#ve onlar üzerinde len methodunu kullanabiliriz. )
class Movie():
    def __init__(self,title, director,duration):
        self.title=title            #self ile point etme, gösterme işlemi(this()) attributes gösterme 
        self.director=director
        self.duration=duration
        print("Movie objesi oluşturuldu.")
    def __str__(self):
        return f'{self.title} by {self.director}'
    def __len__(self):
        return self.duration

m=Movie('The Irishman', 'Martin Scorsese', 185)
print(str(m))
print(len(m))
#objeleri del methoduyla siliyoruz.syntax:del obje adı
#Diğer methodlara bakmak için python special methods list web sitesine bakabilirsin
#constructor methodlar __init__  initial func
#örnek
class Animal(object):
    #constructor
    def __init__(self,animal_type):
        self.animal_type=animal_type
        print('The type of animal is :',animal_type)
    
class Mammal(Animal):
    def __init__(self):
        super().__init__('Mammal')   
        print('Mammals can give birth directly')
      
snowdog=Mammal()
#animal sınıfındaki __init__ methodunu kullanmak için super() methodunu kullanabiliriz.106.satır
#Örnekler
#1.Örnek:
class Person:
    company="ucd"
    #construtor
    def __init__(self):
        self.age=23
        
p1=Person()
print(p1.age)
#Örnek2:
class Person2:
    company="ucd"
    def __init__(self,age,salary):
        self.age=age
        self.salary=salary
    
p2=Person2(12,0)
p3=Person2(20,19000)
print(f"Kişilerin gelirleri:{p2.salary} ve {p3.salary} dir.")
#Örnek3:
class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
d1=Dog('Ruby',2)        
print(d1.name)
#Örnek4:
class Dog:
    species='Canis Familiaris'
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
        #Instance Method
    def description(self):
        return f"{self.name} is {self.age} years old."
        #Another Instance Method
        
    def speak(self,sound):
        return f"{self.name} says {sound}"
    
miles=Dog('Miles', 4)
print(miles.description())
print(miles.speak("hhawww"))
#Örnek5:
class Parrot: 
        #class attributes
        name=""
        age=0
#create parrot1 object
parrot1=Parrot()
parrot1.name="Ivy"
parrot1.age=2
#access attributes
print(f"My little parrot {parrot1.name} is {parrot1.age} years old.")
#22.07.2024 / örnek6:Kapsülleme(encapsulation)
class Computer():
    
    def __init__(self):
        self._maxprice=900
        
    def sell(self):
        print("Selling price: {}".format(self._maxprice))
        
    def setMaxPrice(self,price):
        self._maxprice=price
            
c=Computer()
print(c.sell())
#change the price
c._maxprice=1200  #fiyat neden değişti değişmemesi gerekiyordu?
print(c.sell())
c.setMaxPrice(200)
print(c.sell())
#örnek7:
class Polygon:
    #method to render a shape
    def render(self):
        print("Rendering Poylgon...")
        
class Square(Polygon):
    #renders square
    def render(self):
        print("Rendering Square...")
class Circle(Polygon):
    #renders circle
    def render(self):
        print("Rendering Circle...")
#create an object of Square
s1=Square()
s1.render()
#create an object of Circle
c1=Circle()
c1.render()
#Örnek8:general
class Animal:
    #attribute and method of the parent class
    name=""
    def eat(self):
        print("I can eat")
    #inherit from Animal
class Dog(Animal):
    #new method in subclass
    def display(self):
    #access name attribute of superclass using self
        print("My name is ",self.name)
    #create an object of the subclass
labrador=Dog()
#access superclass attribute and method     
labrador.name="Rohan"
labrador.eat()
#call subclass method 
labrador.display()
#örnek9:
class Polygon:
    #Initializing the number of sides
    def __init__(self,no_of_sides):
        self.n=no_of_sides
        self.sides=[0 for i in range(no_of_sides)]
        
    def inputSides(self):
        self.sides=[float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
    #method to display the lenght of each side of the polygon
    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
class Triangle(Polygon):
    #Initializing the number of sides of the triangle to 3 by
    #calling the __init__ method of the Polygon class
    def __init__(self):
        Polygon.__init__(self,3)
        
    def findArea(self):
        a,b,c=self.sides
        #calculate the semi-perimeter
        s=(a+b+c)/2  
        #Using the Heron's formula to calculate the area of the triangle
        area=(s*(s-a)*(s-b)*(s-c))**0.5
        print("The area of the triangle is %0.2f"%area)
#creating an instance  of the triangle class
t=Triangle()
#Prompting the user to enter the sides of the triangle 
t.inputSides()
#displaying the sides of the triangle 
t.dispSides()
#Calculating and printing the area of the triangle
t.findArea()
#Ödev:Üniversitedeki çalışanları tanımlayan bir class sistemi oluştur.you failed from homework and you need to try it again
class UCalisan:
    #methods for this superclass
    #constructor
    def __init__(self,alan,ofisNumber):
        self.alan=alan
        self.ofisNumber=ofisNumber
        print("The workers of our university...")
        
class OgretimElemani(UCalisan):
    #constructor
    def __init__(self,ogrAlan):
        print(ogrAlan,"alanında çalışmaktadır.")
        super().__init__(ogrAlan)
  
    def departman(self,ogrAlan):
        self.ogrAlan=ogrAlan
        ogrAlan=input("Alan:",ogrAlan)
        return ogrAlan
    #Another sublass
    
class Docent(OgretimElemani):
    def __init__(self,docAlan):
        print(docAlan,"alanında çalışmaktadır.")
        super().__init__(docAlan)
        
ogr1=OgretimElemani()
print(ogr1.__init__("Math"))
#Ödevin farklı bir versiyonu ama aynı işlevi yapıyor.
class Personel:
    def __init__(kisi,ad,soyad,gorev,calismaSuresi):
        #constructor method(first things first you need to define this method)
        kisi.ad=ad
        kisi.soyad=soyad
        kisi.gorev=gorev
        kisi.calismaSuresi=calismaSuresi
        #superclass
        def maasHesapla(kisi):
        #Maaş kıdemKatsayısı ile asgari ücretin çarpılarak toplanması ile elde edilir.
            asgariUcret=8500
            kidemKatsayisi=kisi.calismaSuresi*0.01
            maas=asgariUcret+(asgariUcret*kidemKatsayisi)
            return maas
        def veriYazdir(kisi):
            #bilgi yazdırma
            print("Personalin Adı-Soyadı:",kisi.ad,kisi.soyad)
            print("Görevi:",kisi.gorev)
            print("Kurumda çalışma süresi:",kisi.calismaSuresi)
            print("Aldığı ücret:")
class Calisan(Personel):
    pass
class Yonetici(Personel):
    #subclass
    def maasHesapla(kisi):
        #super().maasHesapla
        asgariUcret=8500
        kıdemKatsayısı=kisi.calismaSuresi*0.01
        print("Kıdem katsayısı:",kisi.kidemKatsayisi)
        if kisi.gorev=="Mühendis":
            unvanKatsayisi=0.25
        elif kisi.gorev=="Üretim Müdürü":
            unvanKatsayisi=1.25
        maas=(3*asgariUcret)+(asgariUcret*kıdemKatsayısı)+(asgariUcret*unvanKatsayisi)
        return maas
#Calisan sınıfından nesneler oluşturma 
personel1=Calisan("Ede Rojin", "Delibaş", "Mühendis", 5)
personel2=Calisan("Eye Nazdar", "Delibaş", "Üretim Müdürü", 5)
personel3=Calisan("Ahmet", "Aydın", "İşçi", 8)
personel1.veriYazdir()  #error
print(personel1.maasHesapla)
print()
print()
#örnek
class India():#super class
    def printfile(self):
        print("")
        
    def capital(self):
        print("New Delhi is the capital city of India.")
    def language(self):
        print("The most widely spoken language is Hindi in India.")
    def develop(self):
        print("India is a developing country.And they have a lot of engineer.")
        
class USA():    #super class
    def capital(self):
        print("Washington D.C. is the capital city of USA")
    def language(self):
        print("English is the primary language in USA.")
    def develop(self):
        print("USA is developed country.")
    def printfile(self):
        print("")
        
hindu=India()
usa=USA()   
#for i in list
for country in (hindu,usa):
    country.capital()
    country.language()
    country.develop()
    country.printfile()
#26.07.2024
#setter function ile kapsüllenmiş olan değişkenlerin değerlerini değiştirebiliriz    
#getter ve setter methodları ile dışardan değerleri değiştirebiliriz
#object has no attribute hatası class içerisinde class çağırma yapmamız gerekiyor.

    
    
    
    

        
        












        
        
            
        






