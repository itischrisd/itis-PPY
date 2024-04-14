"""
ZADANIE 1
1. Zadeklaruj zmienną liczby jako range liczb od 1 do 100. (użyj np. range(start,stop,step))
2. Zdefiniuj funkcję print_even i załóż, że przyjmuje ona tylko listy/range jako input.
3. Wewnątrz funkcji Użyj pętli i przeiteruj po całej liście printując tylko parzyste liczby (jedna po drugiej w iteracji).
"""

liczby = range(1, 101)


def print_even(lista):
    for i in lista:
        if i % 2 == 0:
            print(i, end=" ")


print_even(liczby)

# zip() - łączy dwa iteratory w jeden
przykladowa_lista_1 = [1, 2, 3, 4, 5, 6]
przykladowa_lista_2 = ['a', 'b', 'c', 'd', 'e', 'f']
for i, j in zip(przykladowa_lista_1, przykladowa_lista_2):
    match i:
        case 1:
            print(f"i: {i}, j: {j}")
        case 2:
            print(f"i: {i}, j: {j}")
        case 3:
            print(f"i: {i}, j: {j}")
        case 4:
            print(f"i: {i}, j: {j}")
        case 5:
            print(f"i: {i}, j: {j}")
        case 6:
            print(f"i: {i}, j: {j}")

# range
for i in range(1, 10, 2):
    print(i)

# while
i = 10
while i >= 0:
    print(i)
    i -= 1
else:
    print("Koniec pętli")

# while with break
i = 10
while i >= 0:
    if i == 5:
        break
    print(i)
    i -= 1
else:
    print("Koniec pętli")

# while with pass
i = 10
while i >= 0:
    if i == 5:
        pass
    print(i)
    i -= 1
else:
    print("Koniec pętli")

# while with continue
i = 10
while i >= 0:
    if i == 5:
        i -= 1
        continue
    print(i)
    i -= 1

# for with pass
for i in range(10):
    if i == 5:
        pass
    else:
        print(i)

# walrus operator - przypisanie i zwrócenie wartości
numbers = []
inp = input("Enter a number(or 'q' to quit): ")
while inp != 'q':
    numbers.append(int(inp))
    inp = input("Enter a number(or 'q' to quit): ")
print(numbers)
# VS
numbers = []
while (inp := input("Enter a number(or 'q' to quit): ")) != 'q':
    numbers.append(int(inp))
print(numbers)

# lambda
pow = lambda x: x * x
print(pow(5))

print((lambda x, y, z: x + y + z)(1, 2, 3))

print((lambda x, y, z=3: x + y + z)(1, 2))

print((lambda x, y, z=3: x + y + z)(1, y=2))

print((lambda *args: sum(args))(1, 2, 3))

print((lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3))

print((lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)
myquadrupler = myfunc(4)
myquintupler = myfunc(5)

print(mydoubler(10))
print(mytripler(10))
print(myquadrupler(10))
print(myquintupler(10))

"""
ZADANIE 2
1. Analogicznie do powyższego przykładu zdefiniuj funkcję "possess" przyjmującą jako input 
string "animal" odpowiadający zwierzakowi. 
2. Stwórz taką kombinację tej funkcji z funkcją lambda, aby:
móc tworzyć z niej funkcje np. a_dog, a_cat, a_hobbyhorse, które po przyjęciu jako inputu "name" (czyjeś imie) 
zwrócą string np. "Ala ma kota" lub trzymając się angielskiego "Ala has a cat"

Np. 
a_hobbyhorse = possess("hobbyhorse")
a_hobbyhorse("Adam") # Output: "Adam has a hobbyhorse"
"""


def possess(animal):
    return lambda name: f"{name} has a {animal}"


a_cat = possess("cat")
a_dog = possess("dog")
a_hobbyhorse = possess("hobbyhorse")
print(a_cat("Ala"))
print(a_dog("Ala"))
print(a_hobbyhorse("Adam"))

# albo lambda w lambdzie, chociaż PEP8 nie zaleca zagnieżdżania lambd

possess = lambda animal: lambda name: f"{name} has a {animal}"
a_cat = possess("cat")
a_dog = possess("dog")
a_hobbyhorse = possess("hobbyhorse")
print(a_cat("Ala"))
print(a_dog("Ala"))
print(a_hobbyhorse("Adam"))


# Zasięg zmiennych - zakres global, local, nonlocal

# global
def dodawanie(num1, num2):
    global suma
    suma = num1 + num2
    return suma


print(dodawanie(2, 3), suma)


# nonlocal
def dodawanie_i_mnozenie(num1, num2):
    suma_nowa = 0

    def dodawanie_nowe(l1, l2):
        nonlocal suma_nowa
        suma_nowa = l1 + l2
        return suma_nowa

    print(dodawanie_nowe(num1, num2), suma_nowa)
    return dodawanie_nowe(num1, num2) * suma_nowa


# print(dodawanie_nowe(2, 3), suma_nowa) - nie zadziała, bo funkcja jest zagnieżdżona
print(dodawanie_i_mnozenie(2, 3))

# list comprehension
import time

lista = []

start_time = time.time()
for liczba in range(10000000):
    lista.append(liczba)
print("--- %s seconds ---" % (time.time() - start_time))
print(len(lista))
# trochę trwało

# with list comprehension
start_time = time.time()
lista = [liczba for liczba in range(10000000)]
print("--- %s seconds ---" % (time.time() - start_time))
print(len(lista))

# dict comprehension

slownik = {}

start_time = time.time()
for liczba in range(10000000):
    slownik[liczba] = liczba
print("--- %s seconds ---" % (time.time() - start_time))
print(len(slownik), type(slownik))

# with dict comprehension
start_time = time.time()
slownik = {liczba: liczba for liczba in range(10000000)}
print("--- %s seconds ---" % (time.time() - start_time))
print(len(slownik), type(slownik))

# tuple comprehension

krotka = ()

start_time = time.time()
for liczba in range(1000000):
    krotka += (liczba,)
print("--- %s seconds ---" % (time.time() - start_time))
print(len(krotka), type(krotka))

# with tuple comprehension
start_time = time.time()
krotka = tuple(liczba for liczba in range(1000000))
print("--- %s seconds ---" % (time.time() - start_time))
print(len(krotka), type(krotka))

# set comprehension

zbior = set()

start_time = time.time()
for liczba in range(10000000):
    zbior.add(liczba)
print("--- %s seconds ---" % (time.time() - start_time))
print(len(zbior), type(zbior))

# with set comprehension
start_time = time.time()
zbior = {liczba for liczba in range(10000000)}
print("--- %s seconds ---" % (time.time() - start_time))
print(len(zbior), type(zbior))

# map
numbers = range(1, 11)
m = map(lambda x: x * x, numbers)
print(list(m))
# print(m.__geitem__()) - nie zadziała, bo map jest iteratorem
# Dlaczego zwraca tylko raz? Bo map jest iteratorem, który zwraca wartości po kolei, aż do wyczerpania
print([i for i in m])
print(list(m))

# iteratory - przykład
s = "hello"
it = iter(s)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) - wywali błąd, bo wyczerpał już wszystkie wartości

"""
ZADANIE 3
Stwórz listę liczb 1-100 w której będą wyłącznie liczby parzyste. Zmieść się w jednej linijce.
"""

liczby_parzyste = [i for i in range(1, 101) if i % 2 == 0]
print(liczby_parzyste)
# albo z map, bez filter
liczby_parzyste = list(map(lambda x: x * 2, range(1, 51)))
print(liczby_parzyste)

# reduce
iterable = [1, 2, 3, 4, 5]
init = 0
fun = lambda x, y: x + y
acc = init

for i in iterable:
    acc = fun(acc, i)
print(acc)

# with reduce
from functools import reduce

iterable = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x + y, iterable, 0))
print(reduce(lambda x, y: x + y, iterable, 10))
print(reduce(lambda x, y: x + y, iterable, 15))

# accumulate - reduce plus obiekt iteroowalny

from itertools import accumulate

iterable = [1, 2, 3, 4, 5]
print(list(accumulate(iterable)))
print(list(accumulate(iterable, lambda x, y: x + y)))

# sorted
lista = [1, 3, 2, 5, 4]
print(lista)
print(sorted(lista))
print(sorted(lista, reverse=True))
print(id(lista), id(sorted(lista)))

# sort
lista = [1, 3, 2, 5, 4]
print(lista)
lista.sort()
print(lista)


# obsługa błędów
def adder(x, y):
    type_1, type_2 = type(x), type(y)
    if type_1 != int or type_2 != int:
        raise TypeError("Both arguments must be integers")
    elif y == 42:
        raise ValueError("You cannot add 42")
    return int(x + y)


print(adder(2, 3))
# print(adder(2, "3")) - TypeError
# print(adder(2, 42)) - ValueError

try:
    adder(2, "3")
    # adder(2, 42)
    # adder(2, 3)
except TypeError:
    print("Caught TypeError")
except ValueError:
    print("Caught ValueError")
#     except: - złapie wszystkie błędy, ale nie jest zalecane
finally:
    adder(2, 3)
    print("Finally block")

"""
ZADANIE 4
1. Stwórz zmienną uzytkownicy jako słownik (dictionary), w którym kluczami są trzy imiona osób. 
2. Wartościami tych imion są również słowniki stworzone z kluczów waga (i wartością float) 
oraz wzrost (i wartością w m jako float).
3. Zdefiniuj funkcję BMI przyjmującą zgodnie z założeniem słownik jako argument.
4. Dokonaj walidacji danych wejściowych i zwróć odpowiedni komunikat w wypadku błędu/błędów.
5. Niech funkcja BMI przeiteruje po wszystkich użytkownikach i:
    - sprawdzi poprawność danych (zakładamy że jeżeli wzrost > 3.5 m lub waga większa niż 500 kg to przejdź do następnej iteracji)
    - obliczy ich BMI i zapisze je do słownika pierwotnego jako parę 'BMI' : wartość_BMI
    - określi czy uzytkownik ma nadwagę/niedowagę/prawidłową wagę 
    (BMI < 18.5 to niedowaga, BMI > 29.9 to nadwaga, a pomiędzy to waga prawidłowa).
    Zapisz ten string jako wartość klucza 'stan':string_stanu. 
 .
6.Dodatkowo na koniec przeiteruj po słowniku (poza funkcją) i wyprintuj w formacie fstring
f'Użytkownik {uzytkownik} - {waga}kg, {wzrost}m. BMI = {BMI} - {string_stanu}'

Przykłądowy słownik początkowy:
uzytkownicy = {'adam' : {'wzrost':1.84, 'waga':88.4},
                'piotr' : {'wzrost':1.92, 'waga':100.1}} 

uzytkownicy_po_funkcji = {'adam' : {'wzrost':1.84, 'waga':88.4, 'BMI': wartość_bmi, 'stan':string_stanu },
                'piotr' : {'wzrost':1.92, 'waga':100.1, 'BMI': wartość_bmi, 'stan':string_stanu}} 

f'Użytkownik adam - 88.4kg, 1.84m. BMI = wartość_bmi - string_stanu'
"""

uzytkownicy = {'adam': {'waga': 88.4, 'wzrost': 1.84},
               'piotr': {'waga': 100.1, 'wzrost': 1.92},
               'kamil': {'waga': 120, 'wzrost': 1.75}}


def bmi(uzytkownicy):
    if not isinstance(uzytkownicy, dict):
        raise TypeError("Input data must be a dictionary")
    for uzytkownik, dane in uzytkownicy.items():
        if not isinstance(uzytkownik, str):
            raise TypeError("Keys must be strings")
        if not isinstance(dane, dict):
            raise TypeError("Values must be dictionaries")
        if 'waga' not in dane or 'wzrost' not in dane:
            raise KeyError("Both 'waga' and 'wzrost' keys must be present")
        if not isinstance(dane['waga'], (int, float)) or not isinstance(dane['wzrost'], (int, float)):
            raise TypeError("Both 'waga' and 'wzrost' values must be numbers")
        if dane['wzrost'] > 3.5 or dane['waga'] > 500:
            continue
        bmi = dane['waga'] / dane['wzrost'] ** 2
        if bmi < 18.5:
            stan = 'niedowaga'
        elif bmi > 29.9:
            stan = 'nadwaga'
        else:
            stan = 'waga prawidłowa'
        dane['BMI'] = bmi
        dane['stan'] = stan
    return uzytkownicy


uzytkownicy_po_funkcji = bmi(uzytkownicy)

for uzytkownik, dane in uzytkownicy_po_funkcji.items():
    print(f"Użytkownik {uzytkownik} - {dane['waga']}kg, {dane['wzrost']}m. BMI = {dane['BMI']} - {dane['stan']}")

