#Ders bilgisi
dersAdi = input("Dersin adını giriniz: ")

#Birinci öğrenci bilgileri
birinciOgrenci = input("Birinci öğrencinin adını ve soyadını giriniz: ")
while True:
    try:
        birinciOgrenciNot1 = int(input(f"{dersAdi} dersinin 1.sınav notu:  "))
        birinciOgrenciNot2 = int(input(f"{dersAdi} dersinin 2.sınav notu:  "))
        birinciOgrenciNot3 = int(input(f"{dersAdi} dersinin 3.sınav notu:  "))
        if 0 <= birinciOgrenciNot1 <= 100 and 0 <= birinciOgrenciNot2 <= 100 and 0 <= birinciOgrenciNot3 <= 100:
            break
        print("Notlar 0 ile 100 arasında olmalı.")
    except:
        print("Lütfen sayısal bir değer giriniz.")
birinciOgrenciNotlar = [birinciOgrenciNot1,birinciOgrenciNot2,birinciOgrenciNot3]
  
#İkinci öğrenci bilgileri 
ikinciOgrenci = input("İkinci öğrencinin adını ve soyadını giriniz: ")
while True:
    try:
        ikinciOgrenciNot1 = int(input(f"{dersAdi} dersinin 1.sınav notu:  "))
        ikinciOgrenciNot2 = int(input(f"{dersAdi} dersinin 2.sınav notu:  "))
        ikinciOgrenciNot3 = int(input(f"{dersAdi} dersinin 3.sınav notu:  "))
        if 0 <= ikinciOgrenciNot1 <= 100 and 0 <= ikinciOgrenciNot2 <= 100 and 0 <= ikinciOgrenciNot3 <= 100:
            break
        print("Notlar 0 ile 100 arasında olmalı.")
    except:
        print("Lütfen sayısal bir değer giriniz.")
ikinciOgrenciNotlar = [ikinciOgrenciNot1,ikinciOgrenciNot2,ikinciOgrenciNot3]

#Üçüncü öğrenci bilgileri
ucuncuOgrenci = input("Üçüncü öğrencinin adını ve soyadını giriniz: ")
while True:
    try:
        ucuncuOgrenciNot1 = int(input(f"{dersAdi} dersinin 1.sınav notu:  "))
        ucuncuOgrenciNot2 = int(input(f"{dersAdi} dersinin 2.sınav notu:  "))
        ucuncuOgrenciNot3 = int(input(f"{dersAdi} dersinin 3.sınav notu:  "))
        if 0 <= ucuncuOgrenciNot1 <= 100 and 0 <= ucuncuOgrenciNot2 <= 100 and 0 <= ucuncuOgrenciNot3 <= 100:
            break
        print("Notlar 0 ile 100 arasında olmalı.")
    except:
        print("Lütfen sayısal bir değer giriniz.")
ucuncuOgrenciNotlar = [ucuncuOgrenciNot1,ucuncuOgrenciNot2,ucuncuOgrenciNot3]

#Öğrenci Ortalaması Ataması ve Hesaplaması
birinciOgrenciOrtalama = sum(birinciOgrenciNotlar) / len(birinciOgrenciNotlar)
ikinciOgrenciOrtalama = sum(ikinciOgrenciNotlar) / len(ikinciOgrenciNotlar)
ucuncuOgrenciOrtalama = sum(ucuncuOgrenciNotlar) / len(ucuncuOgrenciNotlar)

def birinciOgrenciHesapla(birinciOgrenciOrtalama):
    return birinciOgrenciOrtalama
def ikinciOgrenciHesapla(ikinciOgrenciOrtalama):
    return ikinciOgrenciOrtalama
def ucuncuOgrenciHesapla(ucuncuOgrenciOrtalama):
    return ucuncuOgrenciOrtalama

print(f"Öğrencilerin {dersAdi} dersinin ortalamaları şu şekildedir: ")
print(f" {birinciOgrenci}: {birinciOgrenciOrtalama:.2f}")
print(f" {ikinciOgrenci}: {ikinciOgrenciOrtalama:.2f}")
print(f" {ucuncuOgrenci}: {ucuncuOgrenciOrtalama:.2f}")

#Başarılı olan öğrenciyi tespit etme
if birinciOgrenciOrtalama > ikinciOgrenciOrtalama and birinciOgrenciOrtalama > ucuncuOgrenciOrtalama:
    print(f"{dersAdi} dersinin en başarılı öğrencisi: {birinciOgrenci}")
elif ikinciOgrenciOrtalama > birinciOgrenciOrtalama and ikinciOgrenciOrtalama > ucuncuOgrenciOrtalama:
    print(f"{dersAdi} dersinin en başarılı öğrencisi: {ikinciOgrenci}")
elif ucuncuOgrenciOrtalama > birinciOgrenciOrtalama and ucuncuOgrenciOrtalama > ikinciOgrenciOrtalama:
    print(f"{dersAdi} dersinin en başarılı öğrencisi: {ucuncuOgrenci}")
else:
    if birinciOgrenciOrtalama == ikinciOgrenciOrtalama == ucuncuOgrenciOrtalama:
        print(f"Tüm öğrenciler aynı ve en yüksek ortalamaya sahip: {birinciOgrenci}, {ikinciOgrenci}, {ucuncuOgrenci}")
    elif birinciOgrenciOrtalama == ikinciOgrenciOrtalama:
        print(f"{birinciOgrenci} ve {ikinciOgrenci} aynı ve en yüksek ortalamaya sahip.")
    elif birinciOgrenciOrtalama == ucuncuOgrenciOrtalama:
        print(f"{birinciOgrenci} ve {ucuncuOgrenci} aynı ve en yüksek ortalamaya sahip.")
    elif ikinciOgrenciOrtalama == ucuncuOgrenciOrtalama:
        print(f"{ikinciOgrenci} ve {ucuncuOgrenci} aynı ve en yüksek ortalamaya sahip.")

#Ortalamalara göre başarı sırası
ogrenciler = [(birinciOgrenci,birinciOgrenciOrtalama),(ikinciOgrenci,ikinciOgrenciOrtalama),(ucuncuOgrenci,ucuncuOgrenciOrtalama)]

siralama = sorted(ogrenciler,key=lambda x:x[1],reverse=True)
print(f"{dersAdi} dersinde öğrencilerin başarı sıralaması: ")
for i,(isim,ortalama) in enumerate(siralama,start=1):
    print(f"{i}. {isim}: {ortalama:.2f}")

#Dersten geçti-kaldı analizi
print(f"{dersAdi} dersinden geçen ve kalan öğrencilerin sıralaması: ")

for isim,ortalama in ogrenciler:
    if ortalama >= 50:
        print(f"{isim} {dersAdi} dersinden geçti.")
    else:
        print(f"{isim} {dersAdi} dersinden kaldı.")