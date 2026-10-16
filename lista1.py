import math
#zadanie 1
print("Zadanie 1:\n")

for i in range(1, 6):
    spacje = 5 - i
    gwiazdki = 2 * i - 1
    print(" " * spacje + "*" * gwiazdki)

print("")
#zadanie 2
print("Zadanie 2:\n")

pi = math.pi
print(round(pi, 5))

print("")
#zadanie 3
print("Zadanie 3:\n")

imie = input("Podaj swoje imię: ")
print(f"\033[32mCześć! {imie}\033[0m")

print("")
#zadanie 4
print("Zadanie 4:\n")

imie = "Jan"
nazwisko = "Kowalski"
srednia_ocen = 4.75
wiek = 21

print(f"Imię: {imie} (typ: {type(imie).__name__})")
print(f"Nazwisko: {nazwisko} (typ: {type(nazwisko).__name__})")
print(f"Średnia ocen: {srednia_ocen} (typ: {type(srednia_ocen).__name__})")
print(f"Wiek: {wiek} (typ: {type(wiek).__name__})")

input()