"""names = ['ali', 'ayse','suna','melis','kemal']
years= [1998,1987,1994,1995,1999]
#1-cenk ismini listenin sonuna ekleme
names.append('cenk')
#2-sena ismini listenin başına ekle
names.insert(0,'sena')
#Listenin en sonuna bir eleman eklemek istersek names.insert (len(names),'Mehmet')
#3-ayse ismini listeden siliniz
names.remove('ayse')
print(names)
#4-suna isminin indexi nedir
ad=names.index('suna')
print(ad)
#5-ali listenin bir elemanı mıdır
if 'ali' in names:
    print ('Bu listede ali ismi bulunmakta')
else:
    print('Bu listede ali diye bir isim yok.')
#6-liste elemanlarını ters çevirin
names.reverse()
print(names)
#7-liste elemanlarını alfabetik olarak sıralayın
names.reverse()
names.sort()
print(names)
#8-years listesini sayısal büyüklüğe göre sıralayınız
years.sort()
print(years)
#9-str='Chevrolet,Dacia' dizisini listeye çeviriniz.
str="Chevrolet,Dacia"
dizi=str.split(',')
print(dizi)

#10-years dizisinin en büyük ve en küçük elemanları nelerdir
min=min(years)
max=max(years)
print(min, max)
#11-years dizisinde kaç tane 1998 elemanı vardır
sayi =years.count(1998)

#12-years dizisindeki tüm elemanları sil
years.clear()
print(years)
#13-kullanıcıdan aldığımız üç markayı bir listede tut
markalar=[]
marka1=input('Marka: ')
markalar.append(marka1)
marka2=input('Marka: ')
markalar.append(marka2)
marka3 =input('Marka: ')
markalar.append(marka3)
print(markalar)
#Tuple
list=[1,2,3]
tuple=(1,'iki',3)
print(list)
print(tuple)
print(type(list))
print(type(tuple))
print(list[2])
print(tuple[2])
print(len((list)))
print(len(tuple))
list=['Sevim','Münevver','Dilek']
tuple=('Ahmet','Mehmet','Selim')
list[0]='Helin'
tuple[0]=='Ali'
print(list)
print(tuple[0])     #bu şekilde atama yapılarak tuple'ın elemanları değiştirilemez.Yani listedeki gibi elemanları üzerinde herhangi bir değişiklik yapılamaz.
names=['kerem','zilan','naz']
names=names+tuple      #Error alırız.tuple ve liste toplanamaz sadece tuple ve tuple toplanabilir.
list=list+names
print(list)
yeni=('mert','fatma','kardel')
yeni+=tuple
print(yeni)
#Dictionary         :key->value ; key bilgisi bizim kullanacağımız bilgidir.
sehirler=['kocaeli','istanbul']
plakalar=[41,34]
print(plakalar[sehirler.index('istanbul')])
#bunu yapmak yerine tek bir değişkende hem plaka hem de sehir isimlerini tutabiliriz.
# DICTIONARY : plaka={'key':'value'}
plakalar={'kocaeli':41,'istanbul':34}
print(plakalar['kocaeli'])
print(plakalar['istanbul'])
plakalar['ankara']=6
plakalar['kocaeli']='new'
print(plakalar)
users={'sadikturan':{
           'age':36,                          #dictionary de alt bilgiler de tablo gibi tanımlanabilir.
           'email':'sadikturan@gmail.com',
           'address':'Ankara/keçiören',
           'phone':5549876645
                    },
       'cahitturan':{
           'age':2,
           'email':'cahitturan@gmail.com',
           'address':'Ankara/yapracık',
           'phone':5312658475
       }

}
print(users['cahitturan'])
print(users['cahitturan']['age'])
#Uygulama
#1-Bilgileri verilen öğrencileri kullanıcıdan aldığımız bilgilerle bir dictionary içinde saklayalım.
#2-Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterelim.
ogrenciler={
    '120':{
        'Ad': 'Elif',
        'Soyad':'Ters',
        'Tel':5524786632
}
    '121':{
        'Ad':'Reyhan',
        'Soyad':'Yıldırım',
        'Tel':5326214521
    },
    '123':{
        'Ad':'Eda',
        'Soyad':'Ada',
        'Tel':5418597856
    }
}
ogrenciler={}
number=input("öğrenci numarası: ")
name=input("öğrenci adı: ")
surname =input("öğrenci soyadı: ")
phone=input("öğr. numarası: ")
ogrenciler[number]={
    'adı':name,
    'soyadı':surname,
    'telefon':phone
}
print(ogrenciler)
#Aynı şeyleri update() methoduyla yapabiliriz:
ogrenciler.update({
    number:{
        'ad':name,
        'soyad':surname,
        'telefon':phone
    }
})
print(ogrenciler)
ogrNo=input("öğrenci numarası: ")
ogrenci=ogrenciler[ogrNo]
print(ogrenci)
#atama operatörleri
values=1,2,3,4,5
print(type(values))  #tuple tipinde


x, y, *z = values   #1 ve 2 ; x ve y ye gider kalan tüm elemanlar z ye dizi şeklinde atanır.
print(x,y,z)
print(x,y,z[0])
#uygulama
"""
#1-kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?
#2- y'nin x'e kalansız bölümü nedir?
#3-(x,y,z) toplamının mod 3'ü nedir?
#4-y'nin x. kuvvetini hesaplayınız.
#5-x,*y,z=numbers işlemine göre z'nin küpü kaçtır?
#6-x,*y,z=numbers işlemine göre y'nin değerleri toplamı kaçtır?
"""
#1.soru
x,y,z=10,20,3
a=int(input("1.sayı:"))
b=int(input("2.sayı:"))
carpım=a*b
toplam = x + y + z
fark=carpım-toplam
print(fark)

#2.soru
t = y // x
print(t)

#3.soru
toplam = x + y + z
mod=toplam%3
print(mod)

#4.soru
kv=y**x
print(kv)

#5.soru
x,*y,z=1,2,6,5,8,3
kp=z**3
print(kp)

#6.soru
x,*y,z=1,2,6,5,8,3
list=y
toplam=y[0]+y[1]+y[2]+y[3]
for i in list:
   toplam+=i
print(toplam)
#karşılaştırma operatörleri
input("lütfen kullanıcı adı giriniz:")
password=input("lütfen şifre giriniz:")

giris = (username=='edeee') and (password=='rojın32ede')

print(giris)
#uygulama2
#1-girilen 2 sayıdan hangisi büyüktür.

sayi1=int(input("1.sayi:"))
sayi2=int(input("2.sayi:"))
result=sayi1<sayi2
print(f'sayi1:{sayi1} sayi2:{sayi2} den büyüktür:{result}')

#2-kullanıcıdan 2 sınav notu vize(%60) ve final(%40) notu alıp ortalama hesaplayınız?
#eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazınız.
vize=float(input("vize notu:"))
final=float(input("final notu:"))
ort=vize*0.6 + final*0.4
result=ort>50
gecme= (result==True)
print(f'vize:{vize} ve final:{final} ortalaması:{ort} ve ogrencinin gecme durumu:{gecme}')
#girilen bir sayının tek mi çift mi olduğunu yazınız.
sayi=int(input("sayi:"))
durum=(sayi%2==0)
print(f'girilen sayı:{sayi} çift olma durumu:{durum}')

#girilen bir sayının pozitif negatiflik durumunu belirleyip yazdırınız.
sayi=int(input("sayi:"))
durum =(sayi>0)
print(f'sayının pozitif olma durumu :{durum}')
#parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.(parola:abc123 ve email:email@sadikturan.com)
email='email@sadikturan.com'
parola='abc123'
girilenEmail=input("email:")
girilenPassword=input("parola:")
isEmail=(email==girilenEmail.lower().strip())   #lower() metodu kullanılmasının sebebi baş harf büyük yazıldığında bunun otomatik olarak düzeltilmesi
isPassword=(parola==girilenPassword.lower())            #strip() metodunun kullanılmasının sebebi başta ya da sonda bırakılan boşlukları doldurması
print(f'Email bilgisi doğru mu:{isEmail} ve girilen parola doğru mu:{isPassword}')
#mantıksal operatörler- uygulama
#girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz
sayi=int(input("bir sayi giriniz: "))
durum = (sayi >100)
durum2= (sayi<0)
print(f'girilen sayı:{sayi} ve bu sayının 0 dan küçük olma ilişkisi: {durum2} aynı zamanda 100 den büyük olma durumu:{durum} dir ')
#girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz
sayi=int(input("bir sayi giriniz: "))
durum = (sayi >0)
durum2= (sayi%2)
print(f'girilen sayı:{sayi} ve bu sayının pozitif olma durumu: {durum} aynı zamanda sayının çift olma durumu:{durum2==0} dir ')
#email ve parola bilgileri ile giriş kontrolü yapınız
#girilen 3 sayıyı büyüklük olarak karşılaştırınız
sayi1=int(input("bir sayi giriniz: "))
sayi2=int(input("bir sayi giriniz: "))
sayi3=int(input("bir sayi giriniz: "))
durum= (sayi1>sayi2 and sayi1>sayi3 )
print(f'sayi1 en büyük sayıdır:{durum}')
durum=(sayi2>sayi1 and sayi2>sayi3)
print(f'sayi2 en büyük sayıdır:{durum}')
durum=(sayi3>sayi1 and sayi3>sayi2)
print(f'sayi3 en büyük sayıdır:{durum}')
#kullanıcıdan 2 vize %60 ve final %40 alıp ort hesaplayınız
vize1=float(input("vize notu:"))
vize2=float(input("vize notu:"))
final=float(input("final notu:"))
ort=((vize1+vize2)/2)*0.6 + final*0.4
result= ort>=50
print(f'vize1:{vize1} , vize2:{vize2} ve final:{final} notları ve bunların ortalaması:{ort} ve ogrenci geçti mi:{result}')
#eğer ort 50 ve üstüyse geçti değilse kaldı yazın
print(f'geçme durumu:{result==True} öğrenci geçti')

#ort 50 olsa bile final notu en az 50 olmalıdır.
result=ort>=50 and final>=50
print(f'öğrencinin geçme durumu:{result==True}')
#finalden 70 alındığında ort nın önemi olmasın
result=ort>= 50 or final >= 70
#kişinin ad ,boy ve kilo bilgilerini alıp beden kitle indeksini hesaplayınız (formül=kilo/boy uzunluğunun karesi)
ad=input("Adınız:")
boy=float(input("Boyunuz:"))
kilo=float(input("Kilonuz:"))
bki=kilo/(boy**2)
#tabloya göre kişi hangi gruba girmektedir 0-18.4=>zayıf; 18.5-24.9=>normal;25.0- 29.9=>fazla kilolu;30.0-34.9=>şişman(obez)
zayıf=bki>=0 and bki<=18.4
print(f'Kişinin bilgilerine göre kişi:{zayıf} tır.')
normal=bki>18.4 and bki<=24.9
print(f'Kişinin bilgilerine göre kişi:{normal} tır.')
kilolu=bki>24.9 and bki<=29.9
print(f'Kişinin bilgilerine göre kişi:{kilolu} tır.')
obez=bki>29.9 and bki<=34.9
print(f'Kişinin bilgilerine göre kişi:{obez} tır.')
#koşul ifadeleri uygulama
#1-soru:Kullanıcıdan isim ,yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
#Ehliyet alabilme durumu en az 18 yaş ve eğitim lise ya da üniversite olmalıdır.
ad=input("Adınız: ")
yas=int(input("Yaşınız: "))
egitim=input("Eğitim durum bilginizi giriniz: ")
if yas>=18:
    if egitim == ("lise" ).capitalize() or egitim==("üniversite").capitalize():
        print("Ehliyet alabilirsiniz.")
    else:
        print("Eğitim durumunuz ehliyet için yetersizdir.")
else:
    print("Ehliyet için yaş sınırını geçemediniz")
#2-soru:Bir öğrencinin 2 yazılı bir sözlü notu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız.
"""
"""0-24=>0
   25-44=>1
   45-54=>2
   55-69=>3
   70-84=>4
   85-100=>5"""
"""
yazili1= int(input("1.yazılı notunuz: "))
yazili2=int(input("2.yazili notunuz: "))
sozlu=int(input("Sözlü notunuz: "))
ortalama=(yazili1+yazili2+sozlu)/3
if ortalama>=0 and ortalama<25:
    print("Not bilginiz 0'dır.")
elif ortalama>=25 and ortalama<45:
    print("Not bilginiz 1'dir. ")
elif ortalama>=45 and ortalama<55:
    print("Not bilginiz 2'dir.")
elif ortalama>=55 and ortalama<70:
    print("Not bilginiz 3'dür.")
elif ortalama>=70 and ortalama<85:
    print("Not bilginiz 4'dür.")
elif ortalama>=85 and ortalama<=100:
    print("Not bilginiz 5'dir.")
else:
    print("Yanlış not bilgisi girdiniz.")

#3-soru: Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.//Bu uygulamada sıkıntı var.
#1.bakım=>1.yıl
#2.bakım=>2.yıl
#3.bakım=>3.yıl
#**Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
#**datetime modülünü kullanmanız gerekiyor.
import datetime
tarih= input("Trafiğe çıkıs tarihinizi giriniz(2015/05/09): ")
tarih=tarih.split('/')
trafigeCikis=datetime.datetime(int(tarih[0],int(tarih[1]),int(tarih[2])))
suan=datetime.datetime.now()
fark=suan-trafigeCikis
days=fark.days
if days<=365:
    print("1.Bakım yılınız gelmiştir.")
elif days<=365*2:
    print("2.Bakım yılınız gelmiştir.")
elif days<=365*3:
    print("3.Bakım yılınız gelmiştir.")
else:
    print("yanlış veri girişi yapıldı.")
#Koşul blokları kullanarak daha önce yapılan kodları tekrar oluştur.
#1-girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz
sayi=int(input("bir sayi giriniz: "))
if sayi >=0 and sayi<=100:
    print(f"Girilen sayi 0 ve 100 arasındadır.Sayi:{sayi}")
else:
    print(f"Girilen sayi belirlenen sınırın dışındadır.Sayi:{sayi}")
#2-email ve parola bilgileri ile giriş kontrolü yapınız
email="edero@gmail.com"
password="fghjk123"
girilenEmail=input("Emailinizi giriniz: ")
girilenPassword=input("Şifrenizi giriniz: ")
if girilenEmail==email:
   if girilenPassword==password:
       print("Giriş başarılı")
   else:
       print("Şifreyi yanlış girdiniz, tekrar deneyiniz.")
else:
    print("Hatalı mail girişi, lütfen tekrar giriniz.")
#girilen 3 sayıyı büyüklük olarak karşılaştırınız
sayi1=int(input("bir sayi giriniz: "))
sayi2=int(input("bir sayi giriniz: "))
sayi3=int(input("bir sayi giriniz: "))
if sayi1>sayi2 and sayi1>sayi3:
    print(f"En büyük sayi: {sayi1}")
    if sayi2>sayi3:
        print(f"En küçük sayi:{sayi3} ve sayıların sıralaması:{sayi1} >{sayi2} >{sayi3}")
    else:
        print(f"En küçük sayi:{sayi2} ve sayıların sıralaması:{sayi1} >{sayi3} >{sayi2}")
elif sayi2>sayi1 and sayi2>sayi3:
    print(f"En büyük sayi: {sayi2}")
    if sayi1>sayi3:
        print(f"En küçük sayi:{sayi3} ve sayıların sıralaması:{sayi2} >{sayi1} >{sayi3}")
    else:
        print(f"En küçük sayi:{sayi1} ve sayıların sıralaması:{sayi2} >{sayi3} >{sayi1}")
elif sayi3>sayi1 and sayi3>sayi2:
    print(f"En büyük sayi: {sayi3}")
    if sayi1>sayi2:
        print(f"En küçük sayi:{sayi2} ve sayıların sıralaması:{sayi3} >{sayi1} >{sayi2}")
    else:
        print(f"En küçük sayi:{sayi1} ve sayıların sıralaması:{sayi3} >{sayi2} >{sayi1}")
#kullanıcıdan 2 vize %60 ve final %40 alıp ort hesaplayınız
vize1=float(input("vize1 notu:"))
vize2=float(input("vize2 notu:"))
final=float(input("final notu:"))
ort=((vize1+vize2)/2)*0.6 + final*0.4
###ortalamanın 50 ve üstü olması durumunda

if ort>=50 :
    print(f"Geçtiniz, ortalamanız:{ort}")
else:
    print(f"Kaldınız, ortalamanız:{ort}")
###ort 50 olsa bile final notu en az 50 olmalıdır.
if final>=50 :
    if ort>=50:
        print(f"Geçtiniz, ortalamanız:{ort}")
    else:
        print(f"Kaldınız, ortalamanız:{ort}")
else:
    print("Final notunuz 50'nin altında olduğu için kaldınız.")

#finalden 70 alındığında ort nın önemi olmasın
if final>=70 :
    print("Tebrikler finalden 70 ya da üstü aldığınız için geçtiniz.")
else:
    if final >= 50:
        if ort >= 50:
            print(f"Geçtiniz, ortalamanız:{ort}")
        else:
            print(f"Kaldınız, ortalamanız:{ort}")
    else:
        print("Final notunuz 50'nin altında olduğu için kaldınız.")

#kişinin ad ,boy ve kilo bilgilerini alıp beden kitle indeksini hesaplayınız (formül=kilo/boy uzunluğunun karesi)
ad=input("Adınız:")
boy=float(input("Boyunuz:"))
kilo=float(input("Kilonuz:"))
bki=kilo/(boy**2)

#tabloya göre kişi hangi gruba girmektedir """
"""0-18.4=>zayıf
   18.5-24.9=>normal
   25.0- 29.9=>fazla kilolu
   30.0-34.9=>şişman(obez)
   
if bki>=0 and bki<=18.4:
    print(f'Kişinin bilgilerine göre kişinin bki:{bki} dir ve kişi zayıftır.')
elif bki>18.4 and bki<=24.9:
    print(f'Kişinin bilgilerine göre kişinin bki:{bki} dir ve kişi normaldir.')
elif bki>24.9 and bki<=29.9:
    print(f'Kişinin bilgilerine göre kişinin bki:{bki} dir ve kişi kiloludur.')
elif bki>29.9 and bki<=34.9:
    print(f'Kişinin bilgilerine göre kişinin bki {bki} dir ve kişi obezdir.')
else:
    print("Hatalı beden kitle indeksi")
#for döngüleri
d={'k1':1,'k2':2,'k3':3}
for item in d:  // k değerlerini item ile ekrana yazar.
for item in d.items():    #dictionarydeki key+value lara erişim sağlarız.
    print(item)
for key, value in d.items():    #dictionarydeki key+value lara erişim sağlarız.
    print(value)
#for döngüsü uygulama
#1-sayilar dizindeki hangi sayılar 3'ün katıdır.
sayilar=[1,3,5,7,9,12,19,21]
ucun_katları=[]
for i in sayilar:
    if i%3==0:
        ucun_katları.append(i)   #print(i)
    else:
        i=i+1
print(f"Üçün katı olan sayılar:{ucun_katları}")
#2-sayilar dizindeki sayiların toplamı kaçtır?
toplam=0
for i in sayilar:
    toplam+=i
print(f"Sayilar dizisindeki sayıların toplamı:{toplam}")
#3-sayilar dizisindeki tek sayıların karesini alınız
tekSayilar=[]
teKare=[]
for i in sayilar:
    if i%2==1:
        tekSayilar.append(i)
print(tekSayilar)
a=[]
for tsk in tekSayilar:
    a.append(tsk**2)
print(a)
#4-şehirlerden hangileri en fazla 5 karakterlidir.
sehirler=['izmir','ankara','rize','van','muğla','kocaeli','konya']
bes=[]
for se in sehirler:
    if len(se)<=5:
        bes.append(se)   #print(se)

print(bes)
#5-Ürünlerin toplamı nedir?

urunler=[{'name':'samsung S6','price':'3000'},
         {'name':'samsung S7','price':'4000'},
         {'name':'samsung S8','price':'5000'},
         {'name':'samsung S9','price':'6000'},
         {'name':'samsung S10','price':'7000'}
]
toplam=0
for urun in urunler:
    fiyat=int(urun['price'])
    toplam+=fiyat
print(toplam)

#6-Ürünlerin fiyatı en fazla 5000 olan ürünleri gösteriniz.
urunler=[{'name':'samsung S6','price':'3000'},
         {'name':'samsung S7','price':'4000'},
         {'name':'samsung S8','price':'5000'},
         {'name':'samsung S9','price':'6000'},
         {'name':'samsung S10','price':'7000'}
]
for urun in urunler:
    if (int(urun['price'])) <= 5000:
        print(urun['name'])
#while döngüleri
x=0
while x<=100:
    print(x)
    x+=1
print("bitti...")
#cift sayıların ekrana yazdırılması
x=0
while x<=100:
    if x%2==0:
        print(x)
    x+=1
print("bitti...")
#kullanıcıdan adını alana kadar sürekli sorma
name='' #False
while not name.strip() :    #True ; strip() metodu ile kullanıcı boşluk karakteri girerse bunun boş string olarak algılanmaması ve
    name=input("Lütfen adınızı giriniz: ")          #isim bilgisinin sürekli istenmesi için yazıldı.

print(f'Merhaba, {name}')
#uygulama while döngüleriyle ilgili

#1-sayilar dizisini while ile ekrana yazdırınız
x=0
while x < len(sayilar):
     print(sayilar[x])
     x+=1
print("bitti...")
#2-Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek syıları ekrana yazdırın
baslangıc=int(input("Başlangıç değerini giriniz: "))
bitis=int(input("Bitiş değerini giriniz: "))

while baslangıc<=bitis:
    if baslangıc%2==1:
        print(baslangıc)
    baslangıc+=1
print("bütün sayıları yazdırdım.")
#3-1-100 arasındaki sayıları azalan şekilde ekrana yazdırın.
x=100
while 0<=x:
    print(x)
    x-=1
print("bitti...")
#4-Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.

x=1
while x<=5:
    sayi=int(input("sayi: "))
    print(sayi)
    x+=1
#2.yöntem :
numbers=[]
i=0
while i<5:
    sayi =int(input("sayi: "))
    numbers.append(sayi)
    i+=1
numbers.sort()
print(numbers)
#5-Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde saklayınız
  **ürün sayısını kullanıcıya sorun 
  **dictionary liste yapısı (name,price şeklinde olsun)
  **ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin
urunler=[]
urunS=int(input("Ürün sayısı:"))
x=0
while x<=urunS:
    name= input("Ürün adını giriniz:")
    price = int(input("Ürün fiyatını giriniz:"))
    urunler.append({
        'name':name ,
         'price':price,
    })
    x+=1
for urun in urunler:
    print(f'Ürün adı:{urun['name']} ve ürün fiyatı:{urun['price']} dır.' )
#break ve continue terimleri
#break döngüden tamamen çıkış yapıyor ancak continue sadece o anki döngü turunu iptal ediyor ve tekrar kaldığı yerden devam eder.
name ='Ede Rojin Delibaş'
for letter in name:
    if letter == 'o':
        continue    #break de yazabilirsin
    print(letter)
#x+=1 i döngü başında kullanmalısın eğer döngü içerisinde continue kullanacaksan.
#1 den 100 e kadar olan sayıların toplamını ekrana yazdırma while ile
result=0
x=0
while x<=100:
    x+=1
    if x%2==1:
        continue
    result+=x
print(f'toplam :{result}')
#Döngü methodları :
#range(bitis) baslangıc=0(default) ve bitisi de kullanıcı girer  for döngüsü içerisinde işimizi kolaylaştırmak için kullanılır.
#range bir liste oluşturur. Eğer başlangıç değerini de vermek istersek range(2,100) şeklinde yazabiliriz.
#Aynı zamanda range içerisindeki aralığı da girebiliriz örneğin; range((2,100,5)) gibi range(start, stop, step)
#range() içerisinden gelen bilgileri bir listeye çevirebiliriz örneğin; list(range(2,100,5))
li=[1,2,3,4,5,6] #'list is not callable or not an object' hatasının sebebi: Bir liste nesnesini bir fonksiyonmuş gibi çağırmaya çalıştığınızda oluşur.
for item in range(50,100,2):
    print(item)
m=list(range(50,100,2))
print(m)
#enumerate() index numarası ve indexe karşılık gelen değerleri bir liste şeklinde tek tek oluşturur.
index=0
greeting='Hello sweety'
for letter in greeting:
    print(f'index:{index} letter:{greeting[index]}')
    index+=1
#2.yöntem
index = 0
greeting = 'Hello'
for item in enumerate(greeting):
        print(item)
#zip() metodu listeleri birleştirmek için kullanılır bu listelerin index ve değerlerini bir nevi eşleştirir .
#dictionary gibi çalışır da denebilir, bir tuple oluşturur.

list1=[1,2,3,4,5]       #ad
list2=['a','b','c','d','e'] #telefon numaraları
l=[]
l.append(zip(list1,list2))
print(l)
for x in range(10):
    print(x)
#ya da
#python da list comprehensions kavramı ve ilgili örnekler
numbers=[x for x in range(10)]
#ya da
numbers=[x*x for x in range(10) if x%3==0]
print(numbers) 
#örnek:
years=[1988,1980,1999,1992,2002]
ages=[2024-year for year in years]
print(ages)
#örnek:#in  range(1,10)]   #eğer sayi çiftse result listesine yazar değilse ekrana tek yazar
print(result)
#örnek:
result=[]
for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)
#yukarıdaki örneğe eşdeğerdir
numbers=[(x,y) for x in range(3) for y in range(3)]
print(numbers)
#Uygulama-Sayı Tahmini
#1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.
#random modülü için python random şeklinde arama yapın
#100 üzerinden puanlama yapın, her soru 20 puan
#hak bilgisini kullanıcıdan alın ve her soru ,belirtilen can sayısı üzerinden hesaplansın .
import random
sayi=random.randint(1,10)
can=int(input("Sayıyı kaç kez tahmin etmek istiyorsunuz:"))
hak=can
sayac=0

while hak>0:
    hak-=1
    sayac+=1
    tahmin = int(input("Sayıyı tahmin ediniz:"))
    if tahmin==sayi:
        print(f"Tebrikler {sayac}. defada bildiniz :),puanınız : {100-((100/can) * (sayac-1))}")
        break
    elif tahmin < sayi:
        print("Biraz daha yüksek bir tahminde bulununuz")

    else:
        print("Biraz daha düşük bir tahminde bulununuz")

    if hak==0:
        print(f"Hakkınız kalmadı:( ")
#uygulama : Asal sayı
#Girilen bir sayının asal olup olmadığını bulun.Asal sayı 1 ve kendisi hariç tam böleni olmayan sayıdır.
#asal sayılar tektir (2 hariç),
sayi=int(input("Sayı giriniz:"))
asalMi=True
if  sayi==1:
    asalMi=False
for i in range(2,sayi):
    if sayi%i==0:
        asalMi=False
        break
if asalMi:
    print("Girilen sayı asaldır.")
else:
    print("Girilen sayı asal değildir.")

#fonksiyon kullanımı
def sayHello(name='user'):
    print("Hello "+name)
sayHello('Rojin')

--def yasKac(dogumYili):
    return 2024 - dogumYili

selinYas =yasKac(2000)

#print(selinYas)
--def EmekliligeKacYasKaldı(dogumYili,isim):
      '''
      DOCSTRING:DogumYiliniza gore emekliliginize kac yıl kaldı.
      INPUT: Dogum Yili 
      OUTPUT: Hesaplanan Yil Bilgisi
      '''

    yas=yasKac(dogumYili)
    emeklilik= 65 - yas
    if emeklilik > 0:
        print(f"Emekliliğinize {emeklilik} yıl kaldı.")
    else:
        print("Zaten emeklisiniz.")
EmekliligeKacYasKaldı(1979,'Yakup')
print(help(EmekliligeKacYilKaldi))

list=[1,2,3,4]
#print(help(list.append))  OUTPUT of this code block is down below
#Help on built-in function append:

#append(object, /) method of builtins.list instance
 #   Append object to the end of the list.

#None

#Fonksiyon Parametreleri
def changeName(n):
    n='Ada'

name='Gediz'
changeName(name)
print(name)     #name değiştirilemedi çünkü value type'tır.

def change(n):
    n[0]='İstanbul'

sehirler=['Ankara','İzmir']
change(sehirler)    #adres kopyalaması yapıldı
print(sehirler)     #sehirler listesinin ilk elemanı değiştirildi çünkü burada referans type kullanıldı ve adreste kayıtlı olan değer değiştirildi.
#adres kopyalaması değilde slicing yapılsaydı şu şekilde olurdu.

n=sehirler[:]       #orijinal listeye hiç dokunmadan liste elemanlarını kopyalama
print(n)
#sum pythonda gömülü bir fonksiyon , herhangi bir nesne üzerinden ulaşılmıyor.Python kütüphanesiyle birlikte geliyor.
def add(*params):       #tuple() tek yıldız
    sum=0
    #return sum((params))    #gönderilen sayıları bir tuple listesi şeklinde gönderir.
    #eğer sum fonksiyonunu kullanmak istemiyorsak;
    for i in params:
        sum+=i
    return sum
#dictionary ** 
print(add(10,25,58))
def displayUser(**args):
    print(type(args))
    for key, value in args.items():
        print('{} is {}'.format(key, value))


displayUser(name='Ede', age='22', city='Ankara',mail='deyenaz@gmail.com')
displayUser(name='Eye', age='21', city='Ankara',phone='12578445')
displayUser(name='Dilek', age='43', city='Ankara')
#Uygulama Fonksiyonlar
#gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.
def tekrarla():
    sayi=int(input("Kelimeyi kaç kez ekrana yazmak istiyorsunuz:"))
    kelime=input("yazdırmak istediğiniz kelimeyi yazınız:")
    while sayi>0:
        print(kelime)
        sayi-=1
    if sayi==0:
        print("END...")
kel=tekrarla()
print(kel)
#başka bir çözüm
def yazdir(kelime,adet):
    print(kelime*adet)
yazdir('Hellö\n',2)
#kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonsiyonu yazınız.
def listeCevir(*params):
    liste=[]
    for i in params:
        liste.append(i)
    return liste

sayilarListesi=listeCevir(10,20,0,55,'m')
print(sayilarListesi)

#gönderilen iki sayı arasındaki tüm asal sayıları bulun
def asalSayiBul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi > 1:
            for i in range(2,sayi):
                if sayi%i==0:
                    break
            else:
                print(sayi)

sayi1=int(input("Hangi sayıdan başlamak istersiniz:"))
sayi2=int(input("Hangi sayı ile bitirmek istersiniz:"))
asalSayiBul(sayi1,sayi2)
#kendine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürün
def tamBolenleriBul(sayi):
    tamBolenler=[]
    for i in range(2,sayi):
        if sayi%i==0:
            tamBolenler.append(i)
    return tamBolenler
sayi=tamBolenleriBul(100)
print(sayi)
#lamda expression , map ve filter fonksiyonları
def square(num): return num ** 2

number=[1,3,5,4]

#print(list(map(square, number)))    #'list is not an object' erro
for i in (map(square, number)):
    print(i)
#lambda expression
number=[1,3,5,4]
#print(list(map(lambda num:num ** 2, number)))
for i in (map(lambda num: num ** 2, number)):
    print(i)
#filter fonksiyonu
def check_even(num): return num %2==0
number=[1,3,5,4]
for i in (filter(check_even, number)):
    print(i)
#yukarıdaki fonksiyonun lambda kullanılarak oluşturulması

number=[1,3,5,4]
for num in (filter(lambda num: num%2==0 , number)):
     print(num)
#Bankamatik Uygulaması

sadikHesap={
    'ad':'Sadik Turan',
    'hesapNo':'1234567',
    'bakiye':3000,            #tanımlanan objeler ram içinde referans olarak alınıyor.
    'ekBakiye':2000           #Ayrı objeler/değişkenler tanımlansaydı gerekli güncellemeler yapılmazdı
}
aliHesap={
    'ad':'Ali Turan',
    'hesapNo':'1278938',
    'bakiye':2000,
    'ekBakiye':1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye']>=miktar):
        hesap['bakiye'] -= miktar
        print("Paranızı alabilirsiniz.")
    else:
        toplam= hesap['bakiye'] + hesap['ekBakiye']

        if toplam>=miktar:
            ekHesapKullanilsinMi= input("Ek hesap kullanılsın mı? (e/h)")
            if ekHesapKullanilsinMi=='e':
                ekHesapKullanilacakMiktar= miktar - hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekBakiye'] -= ekHesapKullanilacakMiktar
                print("Paranızı alabilirsiniz.")
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır.")
        else:
            print("Yetersiz bakiye ")


def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır.Ek hesabınızda ise {hesap['ekBakiye']} TL bulunmaktadır.")

paraCek(sadikHesap,1000)
bakiyeSorgula(sadikHesap)

print("**********************")
paraCek(sadikHesap,2000)
bakiyeSorgula(sadikHesap)
#UYGULAMALAR
#Uygulama 1:İkinci dereceden ax^2 + bx + c =0 denkleminin diskriminant çözümünü yapınız.
#kullanıcıdan a, b ve c değerlerini alarak deltayı hesaplayınız.
import math
a=int(input("1.sayiyi giriniz:"))
b=int(input("2.sayiyi giriniz:"))
c=int(input("3.sayiyi giriniz:"))
delta = (b**2) - 4*a*c
if delta>0:
    print("Denklemin iki tane kökü vardır.")
    rootDelta=math.sqrt(delta)
    print("Delta",rootDelta)
    kok1=float((-b + rootDelta)/2*a)
    kok2=float((-b - rootDelta)/2*a)
    print("Denklemin kökleri:",(kok1),kok2)
elif delta==0:
    print("Denklemin kökleri çakışıktır.")
    x3=(-b)/(2*a)
    print("Denklemin kökü:", x3)
else:
    print("Denklemin kökü yoktur.")
#---Bir sayının tamsayı bölenlerini bulma

def tam_bolen(sayi):
    liste=[]
    for i in range(1,sayi+1):
        if sayi%i==0:       #tam bölünenler
            liste.append(i)
    return liste
result=tam_bolen(200)
print(result)
#---Bir sayının asal olup olmadığının kontrol edilmesi

def asal_mi(sayi):
    if sayi==1:
        return False
    for i in range(2,sayi):
        if sayi%i==0:
            return False
        else:
            return True
        
a=int(input("asallığı kontrol edilecek sayi:"))
print(asal_mi(a))
#İki sayının ortak tam bolenleri
def ortak_tam_bolenler(a,b):
    kucuk=min(a,b)
    ortak_bolenler=[]
    for i in range(1,kucuk+1):
        if (a%i==0) and (b%i==0):
            ortak_bolenler.append(i)
        
    return ortak_bolenler
    
sayi1=int(input("1.sayı:"))
sayi2=int(input("2.sayı:"))
result=ortak_tam_bolenler(sayi1, sayi2)
print(result)
#about dictionary
kullanici1={'ad':'Ferhat','soyad':'Aydın','uzmanlik':['Front-End']}
kullanici2={'ad':'Gökçe','soyad':'Gün','uzmanlik':['Tasarım']}
kullanici3={'ad':'Mesut','soyad':'Gün','uzmanlik':['Front-End']}
#Ferhat isimli kullanıcının uzmanlık alanını döndür
a=kullanici1['uzmanlik']
print(a)
#Front-End alanına uzman olanların isimlerini getir
kullanici_listesi=[kullanici1,kullanici2,kullanici3]
for kullanici in kullanici_listesi:
    if kullanici.get('uzmanlik')=='Front-End':
        print(kullanici.get('ad'))
    else:
        print(kullanici.get('uzmanlik'))

#Mesut isimli kullanıcının uzmanlık alanına yazılımı ekle ve yeni uzmanlık sütununu güncelle
kullanici3['uzmanlik'].append('Yazilim')
print(kullanici3)
#1'den fazla uzmanlık alanı olan kullanıcıları döndür
kullanici1={'ad':'Ferhat','soyad':'Aydın','uzmanlik':['Front-End']}
kullanici2={'ad':'Gökçe','soyad':'Gün','uzmanlik':['Tasarım']}
kullanici3={'ad':'Mesut','soyad':'Gün','uzmanlik':['Front-End']}
kullanici_listesi=[kullanici1,kullanici2,kullanici3]
for kullanici in kullanici_listesi:
    if len(kullanici
           ['uzmanlik'])>1:
        print(kullanici)

#kullanicilistesi ile kullanıcı yaşları listelerini zip kullanarak bu 2 listeyi birleştirip yaşı 30 dan az 
#olan kullanıcıları bastır.
kullanici_yaslari=[22,64,18]
for kullanici,yas in zip(kullanici_listesi,kullanici_yaslari):
    if yas > 30:
        print(kullanici)
        
#filter fonksiyonu örneği
def carp (sayi1,sayi2):
    return sayi1*sayi2
def tek_sayi(number):
    return number%2==1
    
liste1=range(1,10)
liste2=range(11,20)
liste3=map(carp,liste1,liste2)
print(filter(tek_sayi(liste3)))
#1 parametre alacak liste tipinde ve map/lambda ifadelerini kullanarak  6 sıfır atacak biçimde oluşturun.
def paradan_sifir_at(liste):
    sonuc=[]
    for x  in liste:
        sonuc.append(x/1000000)
    return sonuc

result=paradan_sifir_at([1,8,79,66,34,50])
print(result)

#input komutu ile kullanıcıdan saat ve dakika alacak biçimde saat verisini oluşturun
def zaman_verisi_al():
    saat=int(input("Saat giriniz:"))
    if ((saat>0) and (saat<24)):
        dakika=int(input("dakika giriniz:"))
        if ((dakika>=0) and (dakika<60)):
            return 'Giriş yapılan zaman {}:{}'.format(saat, dakika)
        else:
            return 'Girilen dakika aralığı yanlış!'
    else:
        return 'Girilen saat aralığı yanlış!'
    
zaman=zaman_verisi_al()
print(zaman)
#Fibonacci dizisine göre 1000 den küçük olan sayıların yazılması
#fibonacci 1-1-2-3-5-8-13
a=1
b=1
c=0
while c<1000:
    print(b)
    c=a+b
    a=b
    b=c
    
#kullanicinin girdiği sayı adedi kadar sayıyı bir diziye atan ve elde edilen
#dizinin toplamını ve ortalamasını bulan algoritma
adet=int(input("Kaç adet sayı girmek istiyorsunuz:"))
dizi=[]
toplam=0
for i in range(adet):
    dizi.append(int(input("sayı giriniz: ")))
    toplam+=dizi[i]
print(dizi)
print(toplam)
print("Ortalama:",toplam/adet)
#3X3 rastgele sayılardan oluşan 2 matris oluşturun.Bu matrislerin toplamını hesaplatın.
import random

m1=[[0 for x in range(3)] for y in range(3)]
m2=[[0 for x in range(3)] for y in range(3)]
mt=[[0 for x in range(3)] for y in range(3)]  
for i in range(3):
    for j in range(3):
        m1[i][j]=random.randint(0,10)
        m2[i][j]=random.randint(0,10)
        mt=m1[i][j] + m2[i][j]
print(m1)
print(m2)
print(mt)

#matris transpozu bulma 
import random

satir=int(input("satır sayısı:"))
sutun=int(input("sutun sayısı:"))
 
m=[[0 for x in range(sutun) ]for y in range(satir)]#3x5
mt=[[0 for x in range(satir) ]for y in range(sutun)]#5x3
for i in range(satir):
    for j in range(sutun):
        m[i][j]=random.randint(0,9)
        mt[j][i]=m[i][j]
    
print(m)
print(mt)
#Palindrom sayılar;tersten yazıldığında da aynı değeri olan sayılardır.Örneğin;1991,1001 gibi
#1000-10000 arasındaki palindrom sayıları yazınız.
for i in range(1000,10000):
    s=str(i)
    t=s[::-1]
    if s==t:
        print(s)
#kullanıcıdan alınan bir cümlede kaç adet kelime olduğunu ve kaç adet harf olduğunu bulan program
s=input("Bir metin giriniz:")
bosluk_sayaci=0
for k in s:
    if k == " ":
        bosluk_sayaci+=1
print("Metindeki boşluk sayısı:",bosluk_sayaci)
print("Metindeki kelime sayısı:",bosluk_sayaci+1)
print("Harf sayısı:",len(s))
#Nested Functions(Encapsulation)
def outer(num1):
    print('outer')
    def inner_increament(num1):
        print('inner')
        return num1 + 1
    num2=inner_increament(num1)
    print(num1,num2)
outer(10)
#factorial example with nested functions
def factorial(number):
    if not isinstance(number, int): #isinstance:controls object is in the class 
        raise TypeError("number must be an integer")
    if not number>=0:
        raise ValueError("number must be zero or positive")
        
    def inner_factorial(number):
        if number <=1:
            return 1
        return number * inner_factorial(number-1)
    return inner_factorial(number)

try:
    print(factorial(3))
except Exception as ex:
    print(ex)
#authentication
def yetki_sorgulama(page):
    def inner(role):
        if role=="Admin":
            return "{0} rolü {1} sayfasına ulaşabilir.".format(role,page)
        else:
            "{0} rolü {1} sayfasına ulaşamaz.".format(role,page)
    return inner
user1=yetki_sorgulama("Product Edit")
print(user1("Admin"))
#Example
def islem(islem_adi):
    def toplama(*args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam
    def carpma(*args):
        carpim=1
        for i in args:
            carpim*=i
        return carpim
    if islem_adi=="toplama":
        return toplam
    else:
        return carpim
toplama=islem("toplama")
print(toplama(1,3,5,23,44))
carpma=islem("carpma")
print(carpma(1,2,1))
#Givin functions as a parameter
def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b
def islem(f1,f2,f3,f4,islem_adi):
    if islem_adi=="toplama":
        print(f1(2,3))
    elif islem_adi=="cikarma":
        print(f2(3,8))
    elif islem_adi=="carpma":
        print(f3(4,9))
    elif islem_adi=="bolme":
        print(f4(8,6))
    else:
        print("geçersiz işlem")
islem(toplama,cikarma,carpma,bolme, "bolme")
#Decorators
def my_decorator(func):
    def wrapper(name):
        print("fonksiyondan önceki işlemler")
        func(name)
        print("fonksiyondan sonraki işlemler")
    return wrapper()
@my_decorator()
def sayHello(name):
    print("Hello",name)
#we can use @decorator_name instead of this usage
# sayHello=my_decorator(sayHello)
# sayHello()
import math 
import time
def usalma(a,b):
    start = time.time()
    time.sleep(1)
    print(math.pow(a, b))
    finish=time.time()
    print("Fonksiyon"+ str(finish-start) + "saniye sürdü.")
def faktoriyel(num):
    start = time.time()
    time.sleep(1)
    print(math.factorial(num))
    finish=time.time()
    print("Fonksiyon"+ str(finish-start) + "saniye sürdü.")
usalma(4,3)
#creating a decorator for this example
#A decorator takes in a function, adds some functionality and returns it.
def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        func(*args, **kwargs)
        finish=time.time()
        print("Fonksiyon"+ fun.__name__ + str(finish-start) + "saniye sürdü.")
    return inner
@calculate_time    
def usalma(a,b):
     print(math.pow(a, b))
@calculate_time
def faktoriyel(num):       
    print(math.factorial(num)) 
faktoriyel(7)
#Example-1 (This examples from programiz.com)
def smart_divide(func):
    def inner(a,b):
        print("I am going to divide",a,"and", b)
        if b==0:
            print("Whoops! Cannot divide")
            return
        return func(a,b)
    return inner
@smart_divide
def divide(a,b):
    return a/b
divide(200,5)
#Example-2 
def star(func):
    def inner(*args,**kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner 
def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner
@star
@percent
def printer(msg):
    print(msg)
printer("EDE")
#The above syntax of is equaivalent to 
def printer(msg):
    print(msg)
printer=star(percent(printer))"""
#Iterators(scenerio behind the loop for)
liste_iter=[88,52,75,96]
iterator=iter(liste_iter)
print(next(iterator))
while True:
    try:
        elemet=iter(liste_iter)
        print(elemet)
    except StopIteration:
        break
#List comprehension

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

