from math import *

def toplama(x,y):
    toplam = 0
    toplam = x + y
    return toplam

def çıkarma(x,y):
    cikar = 0
    cikar = x - y
    return cikar

def carpma(x,y):
    carp = 1
    carp = x * y
    return carp

def bolme(x,y):
    bol = x
    if(y==0):
        raise Exception("0'a bölünemez!")
    bol = x / y
    return bol

def karekok(sayı1):
    a = pow(sayı1,0.5)
    return a

def karesinial(sayi2):
    b = pow(sayi2,2)
    return b

def factoriyel(sayı3):
     c = factorial(sayı3)
     return c

if __name__=='__main__':

    while True:
        print("-"*60)
        print("Hesap Makinesine Hoşgeldiniz!!!!")
        print("Yapacağınız işlemi seçip işleme göre sayı veriniz.")
        print("1.Topla","2.Çıkar","3.Çarp","4.Böl","5.Karekök al",
              "6.Karesini al","7.Faktöriyel bul","8.Çıkış",sep ='\n')
        print("-"*60)

        işlem=input()

        if (int(işlem) not in range(8) or int(işlem) == 0):
            print("Lütfen geçerli bir sayı giriniz!!")
            continue

        if (int(işlem) == 1):

            sayi1 =int(input("Sayı 1 i gir:"))
            sayi2 =int(input("Sayı 2 yi gir:"))

            print("Sonucunuz: ",toplama(sayi1,sayi2))
        elif (işlem == 2):
            sonuc=çıkarma(int(input("Sayılarınızı giriniz.")))
            print("Sonucunuz: ", sonuc)
        elif (işlem == 3):
            sonuc = çarpma(int(input("Sayılarınızı giriniz.")))
            print("Sonucunuz: ", sonuc)
        elif (işlem == 4):
            sonuc = bölme(int(input("Sayılarınızı giriniz.")))
            print("Sonucunuz: ", sonuc)
        elif (işlem == 5):
            sonuc = karekök(int(input("Sayınızı giriniz.")))
            print("Sonucunuz: ", sonuc)
        elif (işlem == 6):
            a = int(input("Sayınızı giriniz."))
            sonuc = karesinial(a)
            print("Sonucunuz: ", sonuc)
        elif (işlem == 7):
            sonuc = faktöriyel(int(input("Sayınızı giriniz.")))
            print("Sonucunuz: ", sonuc)