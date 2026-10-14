from math import*
# x = input("ismingizni kiriting")
# print("salom", x)

# a = int(input("son kiriting"))
# b = int(input("son kiriting")) 
# print("ko'paytma", a * b, "yig'indi", a + b)

# a = float(input("son kiriting"))
# if a > 0:
#     print("son musbat")
# elif a < 0:
#     print("son manfiy")
# else:
#     print("nol")

# from math import*
# x = int(input("son kiriting"))
# y = pi * x ** 2
# if x > 50:
#     print("katta doira")
# else:
#     print("kichik doira")
# print(x, y)

# a = int(input("son kiriting"))
# print("ildizi:", sqrt(a))

# a = int(input("son kiriting"))
# if a % 2 == 0:
#     print("juft son")
# else:
#     print("toq son")
# print(a)

# a = int(input("yosh kirting"))
# if a > 18:
#     print("ruxsat")
# else:
#     print("ruxsat yo'q")


# a = int(input("1- son kiriting"))
# b = int(input("2- son kiriting"))
# c = int(input("3- son kiriting"))
# print("maksimal daraja", max(a, b, c))

# a = int(input("son kiriting"))
# print("sinus:", sin(a))

# a = int(input("son kiriting"))
# if a > 100:
#     print("Katta faktorial")
# else :
#     print("kichik faktorial")
# print("faktorial", factorial(a))

# a = float(input("1-son"))
# b = float(input("2-son"))

# if b != 0 and a % b == 0:
#     print("birinchi ikkichiga qoldiqsiz bo'linadi")
# else:
#     print("qoldiqsiz bo'linmaydi")

# a = int(input("butun son kirting:"))
# if a >= 0:
#     print("faktorial", factorial(a))
# else:
#     print("musbat emas")

# baho = int(input("Bahoni kiriting (1 dan 5 gacha): "))

# if baho == 5:
#   print("A’lo")
# elif baho == 4:
#   print("Yaxshi")
# elif baho == 3:
#   print("Qoniqarli")
# elif baho == 2:
#   print("Qoniqarsiz")
# elif baho == 1:
#   print("Yomon")
# else:
#   print("Iltimos, 1 dan 5 gacha bo'lgan son kiriting")

# a = float(input("Son kiriting asosiy:"))
# b = float(input("daraja kiriting:"))
# c = a ** b
# print("natija", c)

#ai yordamida
# yil = int(input("Yilni kiriting: "))

# if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
#   print("Kabisa yili")
# else:
#   print("Kabisa yili emas")



# son = float(input("Musbat son kiriting: "))

# if son > 0:
#   yaxlit = int(ceil(sqrt(son)))
#   print("Yaxlit son:", yaxlit)

#   if yaxlit % 2 == 0:
#     print("Juft")
#   else:
#     print("Toq")
# else:
#   print("Musbat son kiriting")

# son = float(input("O'nli kasr son kiriting:"))
# yaxlit = ceil(son)
# print("katta butun son", yaxlit)

# a = float(input("1-sonni kiriting: "))
# b = float(input("2-sonni kiriting: "))
# if a >= b:
#   natija = a - b
# else:
#   natija = b - a
# print("Ayirma natijasi:", natija)

# yil = 2026
# tugilgan_yil = int(input("yilingizni kiriting"))
# yosh = yil - tugilgan_yil
# if yosh < 0 or yosh > 120:
#     print("Bunday yosh bo'lishi mumkin emas")
# else:
#     print(f"Sizning yoshingiz: {yosh} yosh.")

# son = float(input("Son kiriting"))
# modul = fabs(son)
# print("Absolyut qiymat", modul)

# son = int(input("Sonni kiriting: "))

# if son % 3 == 0 and son % 5 == 0:
#   print("Bu son 3 ga ham, 5 ga ham bir vaqtning o'zida bo'linadi.")
# else:
#   print("Bu son 3 ga va 5 ga bir vaqtning o'zida bo'linmaydi.")

# son = float(input("kasr son kiriting"))
# yaxlit = floor(son)
# print("kichik butun son", yaxlit)

# harorat = float(input("Haroratni kiriting: "))

# if harorat < 0:
#   print("Muz")
# elif 0 <= harorat <= 100:
#   print("Suv")
# else:
#   print("Bug")

# a = float(input("a tomonni kiriting: "))
# b = float(input("b tomonni kiriting: "))
# c = float(input("c tomonni kiriting (gipotenuza): "))

# if pow(a, 2) + pow(b, 2) == pow(c, 2):
#   print("To'g'ri burchakli")
# else:
#   print("To'g'ri burchakli emas")

# son1 = int(input("1-son"))
# son2 = int(input("2-son"))
# e = gcd(son1, son2)
# print("Ekub", e)

# p = "pul"
# parol = input("parol kiriting")
# if parol == p:
#     print("pulingizni olishungiz mumkin")
# else:
#     print("pulga kuydingiz")


# a = float(input("1-katetni kiriting: "))
# b = float(input("2-katetni kiriting: "))

# gipotenuza = hypot(a, b)

# print("Gipotenuza:", gipotenuza)
#_________________________________________________________________________________________________________________________
# bu tomoni kserakopiya
#_____________________________________________________________________________________________________________________

# g = float(input("Gradus: "))
# print("Radian:", math.radians(g))

# a = float(input("1-son: "))
# b = float(input("2-son: "))
# m = input("Amal (+, -, *, /): ")

# if m == "+":
#   print(a + b)
# elif m == "-":
#   print(a - b)
# elif m == "*":
#   print(a * b)
# elif m == "/":
#   print(a / b if b != 0 else "Nolga bo'lmaydi")

# k = float(input("Kasr: "))
# y = math.floor(k)
# print("Bo'linadi" if y % 5 == 0 else "Bo'linmaydi")

# s = float(input("Son: "))
# print("Log:", math.log(s) if s > 0 else "Xato")

# n = int(input("Son: "))
# print(n / 2 if n % 2 == 0 else n * 3 + 1)

# r = float(input("Radian: "))
# print("Gradus:", math.degrees(r))

# h = input("Harf: ").lower()
# print("Unli" if h in "aeiou" else "Undosh")

# t = input("4 xonali son: ")
# print("Yigindi:", sum(int(x) for x in t))

# bl = float(input("Ball: "))
# print(
#     "A"
#     if bl >= 90
#     else "B" if bl >= 80 else "C" if bl >= 70 else "D" if bl >= 60 else "F"
# )

# as_s = float(input("Asos: "))
# dj = float(input("Daraja: "))
# p = math.pow(as_s, dj)
# print("Katta" if p > 100 else "Teng" if p == 100 else "Kichik")

# ik = input("2 xonali son: ")
# print("Teng" if ik[0] == ik[1] else "Teng emas")

# or_s = float(input("Son: "))
# print("Oraliqda" if 10 <= or_s <= 50 else "Oraliqda emas")

# blv = float(input("Bo'luvchi: "))
# print("Mumkin" if blv != 0 else "Xato")

# x1 = float(input("1-son: "))
# x2 = float(input("2-son: "))
# x3 = float(input("3-son: "))
# print("Tartibli:", sorted([x1, x2, x3]))

# st = float(input("Staj: "))
# print("10%" if st < 5 else "20%" if st <= 10 else "30%")

# kn = int(input("Hafta kuni (1-7): "))
# print("Ish kuni" if 1 <= kn <= 5 else "Dam olish" if 6 <= kn <= 7 else "Xato")