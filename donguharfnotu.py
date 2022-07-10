"""
KULLANICININ BAŞTA GİRDİĞİ SAYIDA DERSTEN ORTALAMA BULAN PROGRAM
kaç not girileceğini sorup ona göre o kadar giriş alıp 
girilen değerlerin toplamını hafızada tuttuktan sonra notsayisi değişkenine bölerek
ortalama bulan program
ekstra özellik olarak: 1. not gir 2. not gir diye input girişi alındı
"""
notsayisi=int(input("not sayısı gir:"))
notsayisiyedek=notsayisi # notların toplamının bulunduğu döngüde notsayisi sıfırlandığı için yedek alındı.
toplam=0 #ortalama hesaplamak için not toplamı
notsirasi=1 #1. not gir 2. not gir olayı
while notsayisi>0:

    not1=int(input(str(notsirasi)+". not gir:"))
    
    if not1 > 100 or not1 < 0 :
        print("yanlıs not girdiniz (0-100 arasinda olmalı!)")
        not1=int(input(str(notsirasi)+". not gir:"))
    notsirasi+=1
    toplam=toplam+not1
    notsayisi-=1



ortalama= (toplam)/notsayisiyedek

if ortalama >= 80: 
    print("A"+"(ortalamanız="+str(ortalama)+")") 
elif 65 <= ortalama <= 79:
    print("B"+"(ortalamanız="+str(ortalama)+")")
elif 55 <= ortalama <= 64:
    print("C"+"(ortalamanız="+str(ortalama)+")")
elif 50 <= ortalama <= 54:
    print("D"+"(ortalamanız="+str(ortalama)+")")
else:
    print("F(kaldınız yaz okulunda bol şans)")
