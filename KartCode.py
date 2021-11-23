from getpass import getpass

kullanıci = "xabnzk"
Sifre = "abuzer"

kullanici_giris_isim = input(" Kullanıcı Adı =>")
kullanici_giris_sifre = getpass(" Kullanıcı Şifresi =>")

if (kullanici_giris_isim == kullanıci and kullanici_giris_sifre == Sifre):
    print("Hoşgeldin", kullanici_giris_isim)

else:
    print("Yanlış Giriş Yaptınız")

print(" ")
print(" ")
print(" ")
print(" ")
print("Ana Menuye Hoş Geldinniz")

print("Bilet Fiyatı 100₺")
print("Öğrenciye -15₺ İndirim")

alici_isim = input("İsim ->")
alici_yas = input("Yaş ->")
alici_durumu = input("Öğrencimi? ->")

if alici_durumu == ("Evet"):
    print(alici_isim,",Tutar 85₺")

else:
    print(alici_isim,",Tutar 100₺")

while True:
    pass
