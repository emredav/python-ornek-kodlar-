# id doğru ise şifre soran giriş ekranı
id=input("id gir:")

"""
# versiyon 2: id ve şifre girildikten sonra kontrol eden kısım
if id=="aliye" and password=="123":
    print("giriş başarılı")
elif id=="aliye":
    print("şifre yanlış")
else: 
    print("kullanıcı adı yanlış")
"""
if id != "aliye":
  print("kullanıcı adı yanlış")
else: 
    password=input("şifre gir:")

if  password=="123":
    print("giriş başarılı")
else:
    print("şifre yanlış")
