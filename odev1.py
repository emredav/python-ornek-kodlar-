not1=int(input("not 1 gir:"))

if not1 > 100 or not1 < 0 :
    print("yanlıs not girdiniz (0-100 arasinda olmalı!)")
    not1=int(input("not 1 gir:"))

not2=int(input("not 2 gir:"))

if not2 > 100 or not1 < 0 :
    print("yanlıs not girdiniz (0-100 arasinda olmalı!)")
    not2=int(input("not 2 gir:"))

ortalama= (not1+not2)/2

if ortalama >= 80: 
    print("A")
elif 65 <= ortalama <= 79:
    print("B")
elif 55 <= ortalama <= 64:
    print("C")
elif 50 <= ortalama <= 54:
    print("D")
else:
    print("F(kaldınız yaz okulunda bol şans)")
