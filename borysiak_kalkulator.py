#czesc to moj program z kalkulatorem

print("Witam Cię w moim pierwszym kalkulatorze w języku Python")

a = float(input("Podaj pierwszą literę: "))
b = float(input("Podaj drugą literę: "))

print(
"""Wybierz operację na wskazanych liczbach:
d - dodawanie;
o - odejmowanie;
m - mnożenie;
d - dzielenie"""
)

c = str(input("Wybrana operacja: "))

if c == 'd':
    print(a+b)
elif c == 'o':
    print(a-b)
elif c =='m':
    print(a*b)
elif c =='d':
    print(a/b)
else:
    print("Wprowadź poprawną operację!")

#sprawdzam git