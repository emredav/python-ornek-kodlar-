id=input("id gir:")

"""
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