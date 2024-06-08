print("Hello World")  # :)

x = 3
print(x)

# --------------------------------------------------------------
#  Değişkenler

isim = "Muti"  # string
fiyat = 13.95  # float
yaptinmi = False  # boolean
x = 3

isim2 = "Moby Dick"
sayfa = 195
agirlik = 13.45
Yenimi = True

print(isim)
print(type(sayfa))  # sayfanın hangi tipde olduğunu gösterir(str, int..)

# --------------------------------------------------------------
# Kullanıcı Girişi

ad = input("İsminiz Nedir? ")  # input kullanıcıdan girdi almak için kullanılır.
yemek = input("En sevdiğiniz Yemek? ")
yas = input("Yaşınız kaç? ")
print(str(yas) + " Yaşındaki " + ad + " " + yemek + " Sever")  # str() integer'ı stringe çevirdi - int(), bool()...

# --------------------------------------------------------------
# Matematik İşlemleri

z = 9
y = 5
print(z + y)
# print(z - y)
# print(z * y)
# print(z / y)

print(z // y)  # tam böler virgül bırakmaz
print(z % y)  # kalan bulma
print(z ** y)  # üst alma

a = input("İlk Sayıy Giriniz. ")
b = input("İkinci Sayıy Giriniz. ")
print(a + b)  # yan yana ekler ör: 5+7=57
print(int(a) + int(b))  # şimdi toplama yapar.

# --------------------------------------------------------------
# Matematik Fonksiyonları

print(round(9.8))  # yuvarlar.
print(abs(-9))  # mutlak değerini alır.
import math

print(math.sqrt(9))  # karekök alma işlemi için önce library den import math çektik.

print(min(9, 10, 3))  # yazılan sayılar arasından en küçüğünü alır.
print(max(9, 10, 3))  # yazılan sayılar arasından en büyüğünü alır.

# --------------------------------------------------------------
# String

adi = "Muttlip"
mektup = """merhaba muttalip 
umarım iyisindir"""  # 3 tırnak gözükdüğü gibi çıkarır.

print(mektup)  # yani merhaba muutalip den sonra yan yana yazmaz gözükdüğü gibi alta yazar.

print(adi[0])  # adi'n 1.harfini alıyor.
print(adi[0:3])  # adi'n ilk harfinden başlatıp 3.harfe gidiyor ama 3.harfi almaz.
print(adi[-4:-1])  # bunun çıktısı "tli" olur sondan 4.harfden başlyıp son harfi almayacak.

# --------------------------------------------------------------
# String Fonksiyonları

d = "Ahmet eve gidiyor"

print(len(adi))  # kaç harf veya uzunluğunu öğrenme
print(adi.title())  # metnin ilk harfi büyütür
print(adi.upper())  # metnin bütün harflerini büyütür
print(adi.lower())  # metnin bütün harflerini küçültür
print(adi.find("a"))  # e harfinin kaçıncı satırda olduğunu gösteriri olmayan bir harf koyarsanız -1 çıktısı alırsın
print(d.replace("gidiyor", "gitmiyor"))  # gidiyor u gitmiyor ile değiştiriyorum

# --------------------------------------------------------------
# String Fonksiyonları

yolcuadi = "Muttalip"
yolcusoyadi = "Önalan"
print("Yolcunun adı {} {}".format(yolcuadi, yolcusoyadi))  # Muttalip Önalan
# print("Yolcunun adı {0} {1}".format(yolcuadi, yolcusoyadi)) Muttalip Önalan
# print("Yolcunun adı {1} {0}".format(yolcuadi, yolcusoyadi)) Önalan Muttalip
# print("Yolcunun adı {x} {y}".format(x = yolcuadi, y = yolcusoyadi)) Muttalip Önalan

name, surname = "ali", "kaya"
print(f"benim adım {name} {surname}")

hesapla = 2000 / 300
print(f"hesaplamanın sonucu : {hesapla}")
# --------------------------------------------------------------
# Koşullu İfadeler

yagmurlu = False
gunseli = False

if yagmurlu:
    print("Şemsiyeni al")  # True is yazdırır değilse aşağı geçer
elif gunseli:
    print("Güneş Gözlüğünü al")  # True is yazdırır değilse aşağı geçer
else:
    print("Normal bir şekilde dışarı çık")  # Bütün olasıklıkların False olama durumu

kullaniciadi = "Muttalips"
sifre = "12345"
username = input("Kullanıcı Adı Girin: ")
password = input("Parolanızı Girin: ")

if username == kullaniciadi:
    if password == sifre:
        print("Başaralı Giriş Yaptınız..")
    else:
        print("Şifre Ynalış, Lütfen Tekrar Deneyin..")

else:
    print("Kullanıcı Adı Hatalı Lütfen Tekrar Deneyiniz")

# --------------------------------------------------------------
# Mantıksal Operatörler

ehliyet = True
araba = False
if ehliyet and araba:
    print("Araba Kullanabilirsnin")  # Her iki değişkende de True ise yazdır değilse aşağı geç
elif ehliyet and not araba:
    print("Araba Almalısın")
elif ehliyet or araba:
    print("Araba Kullanmana Çok Az Kaldı")  # Or değişkeni olduğu için ikisinden biri varsa durumu, yoksa aşağı geç
else:
    print("Araba Kullanmana çok zaman var")

# --------------------------------------------------------------
# Karşılaştırma Operatörleri(<,>,>=,<=,==,=!)

sicaklik = 10

if sicaklik > 30:
    print("Hava Çok Sıcak")
elif sicaklik < 0:
    print("Hava Çok Soğuk")
else:
    print("Hava Normal")

# --------------------------------------------------------------
# Askerlik Projesi

yasi = 20
okul = False  # okula gidiyor mu

if yasi > 18 and not okul:
    print("Askere Gelme Yaşınız Geldi")
elif yasi > 18 and okul:
    print("Okulunuz Bittiğinde Askere Geleceksiniz")
else:
    print("Askerlik Yaşınız Daha gelmedi")

# --------------------------------------------------------------
# Hesap Makinesi Yapımı

s1 = int(input("1.Sayıyı Giriniz: "))
s2 = int(input("2.Sayıyı Giriniz: "))

islem = int(input("""Hangi İşlemi Yapmak İstiyorsunuz
(Toplama : 1)
(Çıkarma : 2)
(Çarpma  : 3)
(Bölme   : 4) : """))

if islem == 1:
    print(s1 + s2)
elif islem == 2:
    print(s1 - s2)
elif islem == 3:
    print(s1 * s2)
elif islem == 4:
    print(s1 / s2)
else:
    print("Lütfen İşlemlerden Birini Seçin")

# --------------------------------------------------------------
# Listeler

# *************** LİSTE METODLARI ************************
#   len()         = karakter sayısı
#   max()         = En büyük eleman
#   min()         = En küçük eleman
#   append()      = son eleman ekleme
#   insert()      = isteniilen yere eleman ekleme
#   pop()         = sondaki elemanı silme
#   remove()      = istenilen indexteki elemanı silme
#   sort()        = elemanları sıralam
#   reverse()     = tersten yazdırma
#   count()       = elemandan kaç adet var
#   clear()       = eleamn silme
# *********************************************************

# 1) Normal Liste
mesj = "Merhaba* *benim *adım *M.Ö".split("*")  # split ayırma komutudur, yıldızları çıkartıp mesajı tek tek ayırır.
print(mesj)

my_list = [1, 2, 3, 4, 5]
print(my_list)
print(my_list[0])
my_list[3] = 6
sonc = 8 in my_list  # in metodu herhangi bir şeyin "içinde mi?" olduuğunu kontrol eder True or False.
ekleme = my_list + [7, 9]
del my_list[-1]  # del = silmek - listenin son elemanın siler
print(my_list[::-1])  # :Listenin tamamını yazdır ve :sonuna git -1 tersten yazdır.

my_list1 = ["bir", 2, True, 5.6]
print(my_list1)
print(my_list1[2])

list1 = ["bir", "iki", "üç"]
list2 = ["dört", "beş", "altı"]
# total = list1 + list2
# print(total)
print(list1 + list2)
print(len(list2))  # list2 nin boyutunu gösterir.

kullanici1 = ["Muti", 23]
kullanici2 = ["Batu", 22]
kullaciliar = [kullanici1, kullanici2]  # (liste içi liste)
print(kullaciliar)
print(kullaciliar[0])
print(kullaciliar[1])
print(kullaciliar[0][0])

# 2) Tuple Liste

tuplelist = (23, 342, 545, 423)
print(tuplelist)
print(tuplelist.count(23))  # listede kaç tane olduğunu gösterir
print(tuplelist.index("Muti"))
names = ("Hakan", "Doğan", "Sıla") + tuplelist
print(names)

# 3) Dictionary Liste

# key = value
# "ankara" = 06

plakalar = {"İstanbul": 34, "Ankara": 6}
print(plakalar)
print(plakalar["Ankara"])
plakalar["Ordu"] = 52
print(plakalar)

kullanicilar = {
    "Muttalip": {
        "ePosta": "muttaliponl@gmail.com",
        "iş": ["ogrenci", "yazılımcı"],
        "adres": {
            "il": "İstanbul",
            "ilçe": "Çekmeköy",
            "Mahalle": "Çatalmeşe"
        }
    },
    "Simge": {
        "ePosta": "smgklc@gmail.com",
        "iş": ["ogrenci", "avukat"],
        "adres": {
            "il": "İstanbul",
            "ilçe": "Çekmeköy",
            "Mahalle": "Mehmet Akif"
        }
    }
}
print(kullanicilar)
print(kullanicilar["Muttalip"])
print(kullanicilar["Muttalip"]["iş"][1])
print(kullanicilar["Simge"]["adres"][2])

# 4) Sets Liste

meyve = {"elma", "muz", "portakal"}

# print(meyve[1])  indexlenemez ve sıralınamaz
meyve.add("erik")  # tek değer eklenir
meyve.update(["şeftali", "karpuz"])  # birden çok değer eklenebilir
meyve.remove("elma")  # silme komutu
meyve.discard("muz")  # silme komutu
meyve.pop()  # normalde son değeri siler ama sets listede rastgele siler
meyve.clear()  # bütün listeyi siler

number = [1, 2, 2, 3, 4, 4, 4, 5]
print(set(number))  # listede aynı sayılar siler

# --------------------------------------------------------------
# Mantıksal Operatörleri

# 1) AND

say1 = 4
result = (say1 > 3) and (say1 < 5)
result = (say1 % 2 == 0) and (say1 > 3)

animals = "dog"
result = animals[0] == "d" and len(animals) == 3

# 2) OR

say2 = 5
result = (say2 == 5) or (7 < say2)
result = (say2 % 2 == 0) or (7 < say2)

# 3) NOT

isims = "ahmet"
result = not (len(isims) == 5)

metin = input("İsminizi girin: ")
result = (len(metin) <= 10) and (type(metin) == str)

n1 = input("sayı 1: ")
n2 = input("sayı 2: ")
result = ((n1 > 0) and (n2 > 0) and (n1 % 2 == 0))

print(result)

vize1 = float(input("1.Vize Notunuz: "))
vize2 = float(input("2.Vize Notunuz: "))
final = float(input("Final Notunuz: "))

ortalama = (((vize1 + vize2) / 2) * 0.4) + (final * 0.6)
kaldi_gecti = (ortalama >= 40) and (final >= 40)

print(f"Oralama Notunuz: {ortalama}, ve sınıfı geçme durumunuz: {kaldi_gecti}")

# --------------------------------------------------------------
# İN & İS Operatörleri

q = w = [1, 2, 3]
e = [1, 2, 3]
print(q == w)
print(w == e)
print("****************")
print(q is w)
print(w is e)
# *************************
print("****************")

hayvans = ["dog", "cat"]
print("dog" in hayvans)
print("fish" in hayvans)
hay = "wolf"
print("w" in hay)
print("a" in hay)
print("w" not in hay)

# --------------------------------------------------------------
# For Döngüsü

liste2 = [1, 2, 3, 4]

for sayi in liste2:
    print(sayi)
    s5 = 0

ilce = ["kadıköy", "beykoz", "ümraniye", "avcılar", "fatih", "bakırköy"]
for i in ilce:
    s5 += 1
    print(str(s5) + "." + i)

tuple1 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
for a, b, c in tuple1:
    #   print(a) = 1,4,7
    #    print(b) = 2,5,8
    #    print(c) = 3,6,9
    #    print(a, b) = (1,2) - (4,5) - (7,8)
    #    print(a, c) = (1,3) - (4,6) - (7,9)
    print(b, c)

sozluk = {"k1": 1, "k2": 2, "k3": 3}
for deger in sozluk.items():  # .items() direkt tuple gibi yazdırı normal yazarsak sadce keyleri yazdırır.
    print(deger)

# --------------------------------------------------------------
# While Döngüsü

i = 1
while i <= 5:
    print(i)
    i = i + 1

my_listem = [1, 2, 34, 54, 3, 4, 3, 6, 7]
xs = 0
while xs < len(my_listem):
    print(my_listem[xs])
    xs += 1

ic = 0
kaca = int(input("Hangi Aralıkta olsun : 0-"))
zs = []
yz = []
while ic <= kaca:
    if ic % 2 == 0:
        yz.append(ic)
    else:
        zs.append(ic)
    ic = ic + 1

print("Tek Sayılar:", *zs)
print("Çift Sayılar:", *yz)

import random

x = 1
yk = []
while x <= 5:
    zk = random.randint(1, 99)
    yk.append(zk)
    x += 1
print(yk)

# Zamanlayıcı
import time

while True:
    zaman = time.localtime()
    yil = zaman[0]
    ay = zaman[1]
    gun = zaman[2]
    saat = zaman[3]
    dakika = zaman[4]
    saniye = zaman[5]

    time.sleep(5)

    print("""
        tarih: {}/{}/{}
        saat : {}:{}:{}
        """.format(gun, ay, yil, saat, dakika, saniye))

# --------------------------------------------------------------
# Döngü Metodları

# -------range(): Belirli bir aralıkta sayıları üretir.
lists = [0, 1, 2, 3, 4, 5]
for item in range(6):  # for item in listel:
    print(item)

print(list(range(0, 101, 5)))

# -------enumerate():Bir dizi veya listedeki öğelerin indekslerini ulaşır.-
metins = "merhaba"

# indexx = 0
# for harf in metins:
# print(f"index: {indexx}, harf: {harf}")
# indexx += 1

for index, harf in enumerate(metins):
    print(f"index: {index}, harf: {harf}")

# -------zip(): İki veya daha fazla liste veya diziyi birleştirir. ---
list8 = [1, 2, 3, 4, 5]
list9 = ["a", "b", "c", "d", "e"]

print(list(zip(list8, list9)))

for item in zip(list8, list8):
    print(item)
for x, y in zip(list8, list9):
    print(x)

# --------------------------------------------------------------
# Liste Kavramları

numbers = []
for sayi in range(10):
    numbers.append(sayi)
print(numbers)

numbers = [sayi for sayi in range(10)]
print(numbers)
# ----------------------------------------------------------------------------------#
numbers = []
for sayi in range(10):
    numbers.append(sayi ** 2)
print(numbers)

numbers = [(sayi ** 2) for sayi in range(1, 10)]
print(numbers)
# ----------------------------------------------------------------------------------#
for i in range(10):
    if i % 3 == 0:
        print(i ** 2)

numbers = [(i ** 2) for i in range(10) if (i % 3 == 0)]
print(numbers)

# ----------------------------------------------------------------------------------#
myString = "ATATURK"
my_list = []
for letter in myString:
    my_list.append(letter)
print(my_list)

my_list = [letter for letter in myString]
print(my_list)

# ----------------------------------------------------------------------------------#
listm = []
for x in range(3):
    for y in range(3):
        listm.append((x, y))
print(listm)

listms = [(x, y, x) for x in range(3) for y in range(3) for z in range(3)]
print(listms)

# --------------------------------------------------------------
# Sayı Tahmin Oyunu

import random

rast = random.randint(1, 100)
can = int(input("Kaç Hak İstersiniz: "))
hak = can
sayac = 0
while hak >= 0:
    hak -= 1
    sayac += 1
    sayi_tut = int(input("Bir Sayı Tahmin et: "))

    if sayi_tut == rast:
        print(f"Tebrikler {sayac}. defada Bildiniz. Ve Puanınız {100 - ((100 / can) * (sayac - 1))}")
        break
    elif sayi_tut > rast:
        print("Aşağı")
    else:
        print("Yukarı")

    if hak == 0:
        print(f"Hakkını Bitmiştir Tutulan Sayı {rast}")

# --------------------------------------------------------------
# Döngülerde Asal Sayı Bulma

s_ver = int(input("Sayı Girniz: "))
asalmi = True

if s_ver < 2:
    asalmi = False
else:
    for i in range(2, s_ver):
        if s_ver % i == 0:
            asalmi = False

if asalmi:
    print(f"{s_ver} sayısı asaldır")
else:
    print(f"{s_ver} sayıs asal değildir.")


# --------------------------------------------------------------
#  Fonksiyon Kullanımı
def selamla():
    print("Hello World :)")


selamla()


def selam(kullanicii):
    print(f"merhaba {kullanicii}")


selam("umut")


def sel(kulanici):
    return f"merhaba {kulanici}"  # normal print ile yazsaydık print(mesaj) ın çıktısı none olacaktı.


mesaj = sel("umut")
print(mesaj)


def toplama(sayi1, sayi2):
    return sayi1 + sayi2


print(toplama(15, 45))


def yasHesapla(dogumYili):
    return 2023 - dogumYili


def emeklilik(dogumYili, isims1):
    yass = yasHesapla(dogumYili)
    emeklilikYasi = 65 - yass

    if emeklilikYasi > 0:
        print(f"{isims1} emeklılıgıne {emeklilikYasi} yıl kaldı")
    else:
        print(f"{isims1} Zaten emeklı oldun !")


emeklilik(2013, "umut")


# --------------------------------------------------------------
#  Fonksiyon Parametreleri

def isimdegistir(n):
    n = "sude"  # abd24


yisim = "hakan"  # ksd91
isimdegistir(yisim)
print(yisim)  # hakan yazar çünkü yisim ile n nin adresleri farklı


def meyvedegidistir(p):
    p[0] = "elma"  # aa112


meyvelerr = ["muz", "kiraz"]  # aa112
meyvedegidistir(meyvelerr)
print(meyvelerr)


# def islem(x, y, z=0):
#    return sum((x, y, z))


# print(islem(10, 23))
# print(islem(10, 23, 30))


def islem(*params):
    print(params[0])
    print(params[1])
    return sum(params)


print(islem(10, 23))
print(islem(10, 23, 30))
print(islem(10, 23, 30, 2, 57, 99))


def kullanici(**args):
    for key, value in args.items():
        print(key, value)


kullanici(name="umut", age=21)
kullanici(name="sude", age=23, city="ankara")
kullanici(name="mehmet", age=29, city="londra", phone="1222324")


# --------------------------------------------------------------
#  Fonksiyon Örnekleri

# -Gönderilen bir kelimeyyi belirtilen kez ekranda yazdıran bir fonksiyon

def kelime(keli, kacc):
    return keli * kacc


kac = int(input("Kaç kez ekranda yazsın: "))
kel = input("Ne Yazdırmak İstiyorsun: ")

print(kelime(kel + " ", kac))


# -Kendine Gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren bir fonksiyon


def sinirsiz(*args):
    sinirsizlist = []
    for arg in args:
        sinirsizlist.append(arg)
    return sinirsizlist


print(sinirsiz(1, 2, 3, 4, "muti", ))


# -Kendisine gönderilen bir sayının tam  bölenleri bir liste şeklinde döndüren fonksiyon

def gonderilen(sayig):
    bolenler = []
    for i in range(2, sayig):
        if sayig % i == 0:
            bolenler.append(i)
    return bolenler


sayigon = int(input("Hangi Sayının Bölenlerini bilmek istiyorsun: "))
print(gonderilen(sayigon))


# -Gönderilen iki sayı arasındaki tüm asal sayıları bulan fonksiyon

def asalbulma(sayibir, sayiiki):
    for sayim in range(sayibir, (sayiiki + 1)):
        if sayim > 1:
            for iii in range(2, sayim):
                if sayim % iii == 0:
                    break
            else:
                print(sayim)


sayibirr = int(input("1.sayı yı giriniz: "))
sayikii = int(input("2.sayı yı giriniz: "))
asalbulma(sayibirr, sayikii)


# --------------------------------------------------------------
#  Lamda Fonksiyonları

# ------------------------------ LAMDA EXPRESSİONS -----------------------------------

def toplama(x1, y1):
    return x1 + y1


print(toplama(2, 5))
toplams = lambda x1, y1: x1 + y1
print(toplams(5, 7))


def kareAl(sayii): return sayii ** 2


kareALL = lambda sayii: sayii ** 2

print(kareAl(5))
print(kareALL(6))


# -------------------------------- MAP & FILTER --------------------------------------
def kupAl(sayii): return sayii ** 3


# result = kupAl(5)
# print(result)


sayilar = [1, 2, 3, 4]
result = list(map(kupAl, sayilar))  # alternatif yöntem=  result = [*map(kupAl, sayılar)]
print(result)

for result in map(kupAl, sayilar):
    print(result)

sayilarr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def sayiKontrol(ksayi):
    return ksayi % 2 == 0  # true&false


kontrol = lambda ksayi: ksayi % 2 == 0
result = list(filter(kontrol, sayilarr))
print(result)

for result in filter(sayiKontrol, sayilarr):
    print(result)

# --------------------------------------------------------------
# Modüller

# --------- Math Modüllü ---------
import math

result = dir(math)  # math modülünde içindeki tüm fonksiyonları gösterir.
print(result)
help(math)  # math modülünde içindeki tüm fonksiyonları nasıl kullanıldığını gösterir.

print(math.factorial(5))  # 5in fonksiyonunu gösterir.
print(math.sqrt(49))  # 49 sayısının  kare kökünü alır.
print(math.floor(54.7))  # 54.7 yi 54 e yuvarlar - floor aşağı yuvalar
print(math.ceil(54.7))  # 54.7 yi 55 e yuvarlar - ceil yukaru yuvarlar
print("\n")

import math as islem  # math modülüne isim verip çağırma

print(islem.factorial(5))
print(islem.sqrt(49))
print(islem.floor(54.7))
print(islem.ceil(54.7))
print("\n")

from math import *  # math modülünden tüm fonksiyonları import ediyoruz yani math yazmadan bütün fonksiyonları çağırır.

print(factorial(5))
print(sqrt(49))
print(floor(54.7))
print(ceil(54.7))
print("\n")


def floor(xx):
    print("x: " + xx)


from math import *

print(floor(54.7))
print("\n")

# --------- Random Modüllü ---------
# -- random.random()  --
# -- random.uniform() --
# -- random.randint() --
# -- random.choice()  --
# -- random.shuffle() --
# -- random.sample()  --

import random

dir(random)  # random modülünde içindeki tüm fonksiyonları gösterir.
help(random)  # random modülünde içindeki tüm fonksiyonları nasıl kullanıldığını gösterir.

print(random.random)  # 0.0 ile 0.9 arasaında random bir sayı verir
print(random.uniform(0, 10))  # 0.0 dan başlayıp - verdiğiniz değere (10.0) kadar sayı verir.
print(random.randint(0, 10))  # 0 dan başlayıp - verdiğiniz değere (10) kadar tam sayı verir.

fruitss = ["elma", "üzüm", "erik"]
res = fruitss[random.randint(0, len(fruitss))]
print(res)
print(random.choice(fruitss))  # listeden herhangi bir indexi getir.

sayilist = [1, 2, 3, 4, 5, 6, 7]
print(random.shuffle(sayilist))  # Listeniin içindekiliri rastgele gösteriri.
print(sayilist)

sayilistt = [13, 24, 32, 44, 57, 69, 71]
print(random.sample(sayilistt, 3))  # Listeniin içinden verdiğiniz değer (3) kadar rastgele sayı alıp gösteriri.

# --------------------------------------------------------------
# Hata ve Hata Yönetimi

#       1- ERROR

# -- ZeroDivisionError (Sıfıra Bölme Hatası)
# x = 5
# y = 0
# print(x / y)

# -- SyntaxError (Sözdizimi Hatası)
# print("merhaba")

# -- IndexError (Dizin Hatası)
# lıste=[1, 2, 3, 4, 5]
# print(lıste[5])


# -- ValueError (Değer Hatası)
# yas = int(input("yasınızı gırınız:"))
# print(yas)


# -- KeyError (Anahtar Hatası)
# my_dıct = {"k1":"umut", "k2":"dogan"}
# print(my_dıct["k3"])


# -- NameError (İsim Hatası)
# x = 5
# print(x)


# -- TypeError (Tür Hatası)
# x = 5     #int
# y = "6"   #strıng
# print(x +y )


#       2 - ERROR HANDLİNG

while True:
    try:
        x = int(input("1.Sayıyı Giriniz: "))
        y = int(input("2.Sayıyı Giriniz: "))
        print(x / y)

    except ZeroDivisionError as ex:  # except ZeroDivisionError, ValueError: şeklinde de yazılabilir.
        print(f"{ex} HATASI VAR !  1. ve 2. Sayı  için sıfır girilemez.")
    except ValueError as ex:
        print(f"{ex} HATASI VAR ! 1. ve 2. Sayı  için harf girilemez.")

    except Exception as ex:
        print(f"Programda {ex} Hatası Bulundu!1")
    else:
        print("Hata Bulunamadı Programa Devam Ediliyor...")
        break
    finally:
        print("Try excep bloklarından çıkıldı...")

#       3 - HATA NESNESİ OLUŞTURMA
age = 23
if age < 18:
    raise Exception("Yaşınız 18 den küçük olamaz")


def check_user(user):
    if len(user) < 7:
        raise Exception("Kullanıcı Adı 7 Karakterden Az Olamaz.")
    elif " " in user:
        raise Exception("Kullanıcı Adı'nın İçinde Boşluk Olamaz.")
    elif "_" not in user:
        raise Exception("Kullanıcı Adınız '_' içermelidir.")
    else:
        print("Kullanıcı Adı Başarılı")


user = "Muttalip_12"
check_user(user)


def check_password(passwrd):
    import re
    if len(passwrd) < 7:
        raise Exception("Şİfre 7 Karakterden Az Olamaz.")
    elif not re.search("[a-z]", passwrd):
        raise Exception("Şİfre Küçük Harf İçermeli.")
    elif not re.search("[A-Z]", passwrd):
        raise Exception("Şİfre Büyük Harf İçermeli.")
    elif not re.search("[0-9]", passwrd):
        raise Exception("Şİfre Rakam İçermeli.")
    else:
        print("Şifre Başarılı...")


password = "Muttalip12"
check_password(password)

my_listt = ["muti", "adana", "2309", "kuş", "1903", "2001"]
# listedeki sayısal değerleri bulma

for i in my_listt:
    try:
        if int(i):
            print(f"sayı: {i}")
    except Exception as ex:
        continue
        print("Listedeki veri int değil: ", ex)

# --------------------------------------------------------------
# Dosya İşlemleri

# Python'da dosyalarla çalışmak için anahttar işlevimiz open()
open("dosya_adı.txt", "dosya_modu")

# "x" - Oluşutur = Belirtilen dosyayı oluşturur, dosya varsa bir hata döndürür
file = open("deneme.txt", "x", encoding="utf-8")  # Türkçe dilini destekleyen bit txt dosyası oluşturduk.
print(file)  # dosyanın verilerini yazdırır.
file.close()  # dosyayı kapatma işlemi.

# "w" - Yaz = Yazmka için bir dosya aça, yoksa dosyayı oluşturur.
file = open("deneme.txt", "w", encoding="utf-8")  # belirlenen dosyanın içine veri yazmak için "w" kullanılır.
file.write("Hello World")  # Dosyanın içinde veri yazma işlemi gerçekleşir.
file.close()

# "a" - Ekle = Eklemek için bir dosya açar, yoksa dosya oluşturur.
file = open("deneme.txt", "a", encoding="utf-8")  # Dosyanın içindeki verileri silmez üzerine ekler.
file.write("Merhaba Dünya")
file.close()

# "r" - Oku = Varsayılandır, okumka için bşr dosya açara, dosya yoksa hata verir.
try:
    file = open("deneme.txt", "r", encoding="utf-8")
    print(file)
except FileNotFoundError:
    print("Dosya okuma Hatası")
finally:
    print("Dosya Kapandı")
    file.close()

# for düngüsü ile okuma
file = open("deneme.txt", "r", encoding="utf-8")
for content in file:
    print(content, end="")

# read() fonksiyonu
file = open("deneme.txt", "r", encoding="utf-8")
contentt = file.read()  # read() metodu bize dosya içeriğinin tamamını veriyor.
print(contentt)

# readline() fonksiyonu
file = open("deneme.txt", "r", encoding="utf-8")
con = file.readline()  # readline() metodu tek bir satır veriyor.
print(con, end="")
# readlines() fonksiyonu
file = open("deneme.txt", "r", encoding="utf-8")
cont = file.readlines()  # Dosyadaki her elemanı bir dizi gibi çıkartır.
print(cont, end="")

# - Dosya Okuma Fonksiyonları

# file = (open("deneme.txt", "r", encoding="utf-8"))
# print(file.read())
# file.close()

with open("deneme.txt", "r", encoding="utf-8") as file:  # close işlemini ortadan kaldırır.
    print(file.read())
    print(file.tell())  # klosürü kaçıncı (en son) index de durduğunu gösterir.
    file.seek(0)  # klasörü hangi konuma gönderirsem o konuma gönderen fonksiyon
    print(file.read())  # 2.sefer okuduğunda veri olmadığından boşluk bırakır o yüzden 10-11 sıradaki işlemleri yaptık

# - Dosya Güncelleme

# Bu kullanım tarzı veri ekler ama diğer verileride bozabilir.
with open("meslekler.txt", "r+", encoding="utf-8") as file:  # '+' yazma, okuma ve güncelleme işlemini yapabilirz.
    file.seek(0)
    file.write("Memur\n")
    file.seek(0)
    print(file.read())

# ********* Sayfa Başında Güncelleme ***********
with open("meslekler.txt", "r+", encoding="utf-8") as file:  # '+' yazma, okuma ve güncelleme işlemini yapabilirz.
    ccontt = file.read()
    new_ccontt = "Memur\n" + ccontt
    file.seek(0)
    file.write(new_ccontt)

# ******* Sayfa Ortasında Güncelleme ***********
with open("meslekler.txt", "r+", encoding="utf-8") as file:
    list = file.readlines()
    print(list)
    list.insert(1, "Beşiktaş")  # 1.indexe ekle
    file.seek(0)
    print(list)
    #     file.writelines(list)  for yerine de yazılabilir.
    for i in list:
        file.write(i)

# ********* Sayfa Sonunda Güncelleme ***********
with open("meslekler.txt", "a", encoding="utf-8") as file:  # 'a' (append) klasörü en sondan başlatıyor.
    file.writelines("\nEklendi")


# --------------------------------------------------------------
# Proje

def ikramiye_gir():
    ad = input("Çalışan ad: ")
    soyad = input("Çalışan soyad: ")
    ikramiye1 = input("Kış ikramı: ")
    ikramiye2 = input("Yaz ikrami: ")
    with open("calısanlar.txt", "a", encoding="utf-8") as file:
        file.write(ad + " " + soyad + ":" + ikramiye1 + "-" + ikramiye2 + "\n")
    menu()


def ort_ikramiye(satir):
    yeni_satir = satir[:-1]
    liste = yeni_satir.split(":")

    calisanlar = liste[0]
    ikramiyeler = liste[1].split("-")

    ikram1 = int(ikramiyeler[0])
    ikram2 = int(ikramiyeler[1])

    ortalama = (ikram1 + ikram2) / 2
    if (ortalama >= 7000) and (ortalama <= 10000):
        duzey = "iyi çalışan"
    elif (ortalama >= 5000) and (ortalama < 7000):
        duzey = "orta çalışan"
    else:
        duzey = "normal çalışan"
    return calisanlar + ": " + duzey + "\n"
    menu()


def ikramiye_oku():
    with open("calısanlar.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(ort_ikramiye(satir))
    menu()


def ikramiye_kaydet():
    with open("calısanlar.txt", "r", encoding="utf-8") as file:
        liste = []
        for i in file:
            liste.append(ort_ikramiye(i))
        with open("ikramdurum.txt", "a", encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)
    menu()


def menu():
    while True:
        print("********MENÜ*********")
        islem = input("1- ikramiye gir\n2- ikramiye oku\n3- ikramiye kaydet\n4- Çık\nİşleminiz : ")

        if islem == "1":
            ikramiye_gir()
        if islem == "2":
            ikramiye_oku()
        if islem == "3":
            ikramiye_kaydet()
        else:
            break


menu()


# --------------------------------------------------------------
# Nesne Tabanlı Programlama

# class
class Car:  # classlar her zaman büyük harf ile başlar
    # class atributes
    production_country = "Türkiye"

    # constructor (yapıcı method)
    def __init__(self, marka, model, renk):
        # objevt atributes
        self.model = model
        self.marka = marka
        self.renk = renk

    # methods
    def uretimyeri(self):
        print("Aracın üretim yeri türkiye")

    def uretimkodu(self, uretimkod):
        return f"{self.model} aracın üretim kodu: {uretimkod}"


# object(instance)
c1 = Car("Bmw", "E30", "Siyah")
c2 = Car("Renault", "Fluence", "Beyaz")
print(c1.production_country)
print(f"Arabanın modeli {c1.marka} markası {c1.model} rengi {c1.renk}")
print(f"Arabanın modeli {c2.marka} markası {c2.model} rengi {c2.renk}")
c1.uretimyeri()
print(c1.uretimkodu("tr12093"))
print(c2.uretimkodu("tr79428"))

class Vergihesap:
    # class atributes
    tr_vergi = 1500

    # constructor (yapıcı method)
    def __init__(self, marka, fiyat, uretimyili):
        self.marka = marka
        self.fiyat = fiyat
        self.uretimyili = uretimyili

    def vergisizArac(self):
        return self.fiyat - self.tr_vergi

    def aracpiyasa(self):
        return 2024 - self.uretimyili


v1 = Vergihesap("Honda", 10000, 2015)
print(f" {v1.marka} marka aracın vergisiz fiyatı : {v1.vergisizArac()}")
print(f" {v1.marka} marka araç {v1.aracpiyasa()} yıldır piyasada")

# iNHERİTANCE (Miras Alma)

# THY = model, kapasite, serino, başlangıç, bitiş
# Pegasus(THY), Anadolujet(THY)

class Thy:
    def __init__(self, model, kapasite, serino):
        self.model = model
        self.kapasite = kapasite
        self.serino = serino

    def start(self):
        print("uçak kalkıyor..")

    def stop(self):
        print("uçak iniyor..")
class Pegasus(Thy):
    def __init__(self, model, kapasite, serino):
        Thy.__init__(self, model, kapasite, serino)


t1 = Thy("ak47", "240", "sad78fa")
print(f"Thy'nın {t1.model} model uçağının kapasitesi {t1.kapasite} ve seri nosu {t1.serino}")
t1.start()
t1.stop()
p1 = Pegasus("pg12", "180", "wqj23hu21")
print(f"Pegasus'un {p1.model} model uçağının kapasitesi {p1.kapasite} ve seri nosu {p1.serino}")
p1.start()
p1.stop()

# --------------------------------------------------------------
# Banka Uygulaması (Hatalı)

import sys
import time


def kart_no_kontrol(kartno):
    with open("Bilgi.txt", "r", encoding="utf-8") as file:
        for satir in file:
            kno, _ = satir.strip().split(":")
            if kno == kartno:
                return True
    return False


def Kayit_ol():
    kartno = int(input("Kart Numarası giriniz: "))
    if kart_no_kontrol(kartno):
        print("Bu kart numarası zaten kayıtlı!")
        time.sleep(2)
        return
    sifre = int(input("Şifrenizi giriniz: "))
    with open("Bilgi.txt", "a", encoding="utf-8") as file:
        file.write(f"{kartno}:{sifre}\n")
    print("Kayıt Başarılı, Menüye Yönlendiriliyorsunuz...")
    time.sleep(2)
    main()


def oku():
    with open("Bilgi.txt", "r", encoding="utf-8") as file:
        return file.readlines()  # Dosyadaki satırları okuyup geri döndürüyor


def giris(kartno, sifre):
    oku()
    with open("Bilgi.txt", "r", encoding="utf-8"):
        bilgiler = oku()  # Dosyadaki bilgileri okuyor
        for satir in bilgiler:  # Her bir satırı kontrol ediyor
            kno, sfr = satir.strip().split(":")  # Satırdaki kart numarası ve şifreyi ayırıyor
            if (kno == kartno) and (sfr == sifre):
                girisbasarili = 1
            else:
                girisbasarili = 0
                print("Kart no veya Şifre hatalı! Menüye dönülüyor...")
        if girisbasarili == 1:
            mains()
        else:
            time.sleep(3)
            main()


def sifre_ogr():
    kogr = int(input("Kart no girin: "))
    bilgiler = oku()
    for satir in bilgiler:
        kno, sfr = satir.strip().split(":")
        if kno == kogr:
            print(f"Şifreiz: {sfr}\n")
            print("Menüye Yönlendiriliyorsunuz...")
            time.sleep(2)
            main()
    print("Kart Numarası Bulunamadı!")
    print(" Menüye Yönlendiriliyorsunuz...")
    time.sleep(2)
    main()


def para_ekle(kno):
    ekle = int(input("Ne kadar para eklemek istiyorsunuz: "))
    with open("Banka.txt", "r+", encoding="utf-8") as file2:
        slistesi = file2.readlines()
        for i, satir in enumerate(slistesi):
            if satir.startswith(kno):  # Kart numarasına ait satırı buluyor
                slistesi[i] = f"{kno}:{int(satir.split(':')[1]) + ekle}\n"  # Satırı güncelliyor
                file2.seek(2)  # Dosyanın başına geri dönüyor
                file2.writelines(slistesi)  # Güncellenmiş satırları dosyaya yazıyor
                print("Paranız Eklendi, Menüye Yönlendiriliyorsunuz...")
                time.sleep(2)
                mains()
            print("Kart numarası bulunamadı!")
            print("Menüye Yönlendiriliyorsunuz...")
            time.sleep(2)
            mains()


def para_cek(kno):
    sil = int(input("Ne kadar para çekmek istiyorsunuz: "))
    with open("Banka.txt", "a", encoding="utf-8") as file2:
        slistesi = file2.readlines()
        for i, satir in enumerate(slistesi):
            if satir.startswith(kno):  # Kart numarasına ait satırı buluyor
                mevcut_para = int(satir.split(':')[1])
                if mevcut_para < sil:
                    print("Bu kadar paranız yok")
                else:
                    slistesi[i] = f"{kno}:{mevcut_para - sil}\n"  # Satırı güncelliyor
                    file2.seek(2)  # Dosyanın başına geri dönüyor
                    file2.writelines(slistesi)  # Güncellenmiş satırları dosyaya yazıyor
                    print("Paranız Çekildi")
                    print(" Menüye Yönlendiriliyorsunuz...")
                    time.sleep(2)
                    mains()
        print("Kart numarası bulunamadı!")
        print(" Menüye Yönlendiriliyorsunuz...")
        time.sleep(2)
        mains()


def para_gor(kno):
    with open("Banka.txt", "r", encoding="utf-8") as file2:
        for satir in file2:
            if satir.startswith(kno):  # Kart numarasına ait satırı buluyor
                print(f"Güncel Paranız: {satir.split(':')[1].strip()}")
                print(" Menüye Yönlendiriliyorsunuz...")
                time.sleep(2)
                mains()
        print("Kart numarası bulunamadı!")
        print(" Menüye Yönlendiriliyorsunuz...")
        time.sleep(2)
        mains()


def mains():
    islem = int(input("1- Para Ekle\n2- Para Çek\n3- Para Gör\n4- Çıkış\nİşleminiz: "))
    if islem == 1:
        para_ekle()
    elif islem == 2:
        para_cek()
    elif islem == 3:
        para_gor()
    elif islem == 4:
        print("Giriş Menüsüne Dönülüyor...")
        time.sleep(3)
        main()
    else:
        print("Lütfen Menüden Bir İşlem Seçin...")
        time.sleep(2)
        mains()


def main():
    isle = int(input("1- Giriş Yap\n2- Kayıt ol\n3- Şifre unuttum\n4- Çıkış\nİşleminiz: "))
    if isle == 1:
        kartno = input("Kart Numarası giriniz: ")
        sifre = input("Şifrenizi giriniz: ")
        if giris(kartno, sifre):
            mains()
    elif isle == 2:
        Kayit_ol()
    elif isle == 3:
        sifre_ogr()
    elif isle == 4:
        sys.exit()
    else:
        print("Lütfen Menüden Bir İşlem Seçin...")
        time.sleep(2)
        main()


main()
