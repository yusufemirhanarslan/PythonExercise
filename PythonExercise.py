isim = "Joseph" #String
fiyat = 13.95 #float
aldiMi = False #boolean
x = 3 #integer

bookName = "Moby Dick"
weight = 13.45
pageCount = 195
isNew = True

print(bookName)

print(type(weight)) #weight in tipini bize döndürür.

#isim = input("İsminizi giriniz? ")
#print("Merhaba " + isim)

#userName = input("İsminizi giriniz ")
#loveFood = input("Lütfen sevdiğiniz yemeği giriniz ")
#print(userName + " " +loveFood + " sever")

isim = "Joseph"
yas = 23

print(isim + " " + str(yas) + " " + "Yaşında")

print(3 ** 5) #Anlamı 3 üzeri 5 tir.

print(round(9.8)) #yuvarlama işlemi yapar.
print(abs(-9)) #mutlak değer alır.

import math #böylece paket ekleyebiliriz.
print(math.sqrt(9)) #karekök bulmaya yarar.

print(min(9, 10, 56)) #minimum değer bulmaya yarar.
print(max(9, 10, 56)) #maksimum değer bulmaya yarar.


isim = 'Yusuf işe gidiyor'
print(isim[0]) #stringin kaçıncı elamanı alacağını yazıyoruz.
print(isim[0:3]) # stringi 0. elemandan başlayarak 3. elemana kadar olan değerleri alıyoruz.

print(isim[-4:-1]) #sondan başlayarak gerekli yere kadar değerleri yazdırır.

print(len(isim)) #stringin uzunluğunu öğrenebiliriz.
print(isim.title) #metnin ilk harfi büyür.
print(isim.upper) #değişkenin bütün harfleri büyür.
print(isim.lower) #tüm harfler küçük yazılır.
print(isim.find("u")) #değerdeki u harfini içeren indexi döndürür.
print(isim.replace("gidiyor","gitmiyor")) #gidiyor ifadesini gitmiyor olarak değiştiriyoruz.

mektup = """merhaba ahmet umarım iyisindir"""
print(mektup)

isRain = False
isSun = False

if isRain:
    print("Paltonu giy")

elif isSun:
    print("Güneş gözlüğü tak.")

else:
    print("Normal şekilde dışarı çık.")


ehliyet = False
araba = True

if ehliyet and araba:
    print("Araba kullanabilirsin")
elif ehliyet or araba:
    print("Araba kullanmana çok az kaldı.")
elif araba and not ehliyet:
    print("Sürücü kursumuzla hemen ehliyet alıp araba kullanabilirsiniz.")
else:
    print("Araba kullanmak için çok zamanın var") 

temperature = 35

if temperature > 30:
    print("Hava çok sıcak")
elif temperature < 0:
    print("Hava çok soğuk")
elif temperature >= 35:
    print("Hava sıcak ve 35 dereceye eşit veya daha büyük")
elif temperature == 35:
    print("Hava 35 derece")
elif temperature != 35:
    print("Hava 35 derece değil")

isciler = ["Mehmet", "Ali", "Veli", "Deli"]
print(isciler)
isciler.append("Leo")
print(isciler)
print(isciler[0:3]) #sondaki 3 dahil değil


from urllib.request import urlopen
from urllib.request import urlopen
import json
url = "https://jsonplaceholder.typicode.com/todos/1"
with urlopen(url) as response:
   body = response.read()
todo_item = json.loads(body)
print(todo_item)

#python functionlar
def yasHesapla(age1, age2):
    return int(age1) + int(age2)

yasTop = yasHesapla(10, 15)
print(yasTop)
