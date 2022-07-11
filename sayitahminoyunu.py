import random 

kullanicirandom=int(input("0-3 arasında sayı gir!:"))

def tahmin():
    while True:
        
        bilgisayartahmin=random.randint(0,3)
        if bilgisayartahmin==kullanicirandom:
            print("bilgisayar girdiğiniz {} sayısını bildi".format(kullanicirandom))
            break
        else:
            print("bilgisayarın tahmini:"+str(bilgisayartahmin))
            onay=input("bilgisayar seçtiğiniz sayıyı bilemedi tekrar denesin mi ?[(e)vet, (h)ayır]:")
            if onay== "e":
                continue
            else:
                break

tahmin()

while True:
    tekraroynama=input("tekrar oynamak ister misin[(e)vet, (h)ayır]:")
    if tekraroynama=="e":
        kullanicirandom=int(input("0-3 arasında sayı gir!:"))
        tahmin()
        continue
    else:
        print("oyun bitti")
        break
        

