# tuple comprehension

tup = tuple(i for i in range(10))


# bo samo (i for i in range(10)) da generator, nie tuple

# filter


def is_even(x):
    return x % 2 == 0


liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parzyste = list(filter(is_even, liczby))
print(parzyste)
print(filter(is_even, liczby))

# generatory i iteratory
# iterator - kiedy dane już mamy
lista = [1, 2, 3, 4, 5]
iter_lista = lista.__iter__()
a = iter_lista.__next__()
b = iter_lista.__next__()
c = iter_lista.__next__()
d = iter_lista.__next__()
e = iter_lista.__next__()
# print(iter_lista.__next__()) # StopIteration
print(a, b, c, d, e)


# generator - kiedy dane są tworzone w locie


def liczby_napotkane(limit):
    obecna = 0
    while obecna < limit:
        obecna += 1
        yield obecna  # return by zakończyło funkcję


generator_liczb = liczby_napotkane(5)

for liczba in generator_liczb:
    print(liczba)

print(list(generator_liczb), generator_liczb)

generator_liczb2 = (num for num in range(1000) if num % 2 == 0)
print(generator_liczb2)
print(list(generator_liczb2))
print(list(generator_liczb2))  # pusty bo generator jest jednorazowy


# iterator enumerate
lista = ['a', 'b', 'c', 'd']
for index, value in enumerate(lista):
    print(index, value)


"""
Zadanie 1
Zdefiniuj generator, który będzie iterował przez kolejne liczby w ciągu Fibonacciego. 
Pamiętaj, że ciąg Fibonacciego zaczyna się od dwóch początkowych liczb: 0 i 1.
Użyj dwóch zmiennych, aby przechowywać dwie ostatnie liczby w ciągu. Na początku ustaw je na 0 i 1.
Wewnątrz generatora użyj pętli while lub for, aby generować kolejne liczby w ciągu Fibonacciego. 
Każda kolejna liczba jest sumą dwóch poprzednich liczb w ciągu.
"""


def generuj_ciag_fibonacciego():
    num1, num2 = 0, 1
    while True:
        yield num1
        num1, num2 = num2, num1 + num2


fib = generuj_ciag_fibonacciego()
for _ in range(11):
    print(next(fib), end=' ')

print()


# Biblioteki = "pip install nazwa_biblioteki"
import os
# os.system('pip install numpy')

# importowanie biblioteki
import numpy

# import numpy as np
#  from numpy import * - archaiczne, nie używać
# from numpy import array, arrange, add - tak lepiej
# from numpy import array as tablica - żeby nie było konfliktu z nazwami

# utworzenie tablicy za pomocą funkcji z biblioteki numpy
tablica = numpy.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
print(tablica, tablica.shape)
print(tablica.reshape(5, 2))

# importowanie z pliku .py
from dodawanie import dodawanie_func  # pliki muszą być w zmiennych środowiskowych (PATH)

print(dodawanie_func(1, 2))

"""
Zadanie 2
Znajdź jakąś bibliotekę.
Zainstaluj ją, a następnie zaimportuj jakieś funkcje z tej biblioteki i zaprezentuj ich działanie.
(Przydatna strona z dokumentacją - https://pypi.org)
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://google.pl')
driver.close()
# otworzy przeglądarkę, przejdzie na google.pl i zamknie przeglądarkę

# moduły wbudowane
# sys
import sys

# argumenty z linii poleceń
arguments = sys.argv
nazwa_skryptu = arguments[0]
dodatkowe_argumenty = arguments[1:]
print(arguments, nazwa_skryptu, dodatkowe_argumenty, type(dodatkowe_argumenty))

# wyjście z programu z kodem błędu
# sys.exit(1)

# sys.stdout, sys.stderr
import sys

# przekierowanie wyjścia do pliku
with open('output.txt', 'w') as f:
    sys.stdout = f
    print('Hello world')

# przywrócenie wyjścia do konsoli
sys.stdout = sys.__stdout__

# wyświetlenie błędu
sys.stderr.write('Błąd został wyświetlony w linii 146\n')

# sys.platfrom - informacje o systemie
print(sys.platform)
if sys.platform == 'linux':
    print('Jestem na Linuksie')
elif sys.platform == 'win32':
    print('Jestem na Windowsie')
elif sys.platform == 'darwin':
    print('Jestem na MacOS')

"""
Zadanie 3
Napisz program, który będzie obliczał BMI użytkownika.
Argumenty takie jak wzrost / waga będą podawane jako argumenty z poziomu konsoli.

Z poziomu konsoli uruchomienie skryptu np. "python zadanie3.py  84.5 1.84" powinno zwrócić poprawne BMI jako print oraz
wyjść z programu.
Dodatkowo jeżeli użytkownik poda argumenty niekonwertowalne na float, zwróć błąd (z użyciem sys.stderr.write) oraz zapisz 
te argumenty do pliku faulty_input.txt.
Zakładamy, że użytkownik zawsze będzie podawał tylko dwa dodatkowe argumenty i że pierwsza podana jest zawsze waga, następnie wzrost
"""

# BEGIN zadanie3.py
import sys
waga = sys.argv[1]
wzrost = sys.argv[2]
try:
    waga = float(waga)
    wzrost = float(wzrost)
except ValueError:
    sys.stderr.write('Podano nieprawidłowe argumenty')
    with open('faulty_input.txt', 'w') as f:
        f.write(f'Waga: {waga}, Wzrost: {wzrost}')
    sys.exit(1)

bmi = waga / wzrost ** 2
print(bmi)
# END zadanie3.py

# moduł random
import random

# random.random - losowa liczba z zakresu 0-1
print(a := random.random())
print(a)

# random.randint - losowa liczba całkowita z zakresu
print(random.randint(1, 200))

# random.choice - losowy element z listy
lista = [1, 2, 3, 4, 5]
string = 'abcdef'
print(random.choice(lista))
print(random.choice(string))

# random.shuffle - przetasowanie listy
random.shuffle(lista)
print(lista)

# random.sample - losowe elementy z listy, k - ilość elementów
print(random.sample(lista, 2))

# random.seed - ustawienie ziarna
random.seed(42)

lista = [1, 2, 3, 4, 5]
sample = random.sample(lista, 2)
print(sample)
# zawsze wylosuje te same liczby

"""
Zadanie 4
Stwórz prostą grę w zgadywanie liczb.
Włączenie gry następuje z konsoli i przyjmuje jeden argument dodatkowy, którym jest poziom trudności (liczba całkowita)
Gra ma polegać na wybraniu liczby przez program, a uzytkownik musi ją zgadnąć (while loop + input).
Dopóki nie zgadnie, gra się nie kończy.
Losowo wybrana liczba przez program to liczba z przedziału 0 do poziom_trudnosci.
Nie trzeba robić walidacji poprawności danych itd.

Działanie:
komenda "python game.py 10" zwróci komunikat, że liczba została wylosowana i poprosi gracza o input.
Jeżeli input == liczba_wylosowana wyprintuj gratulacje i zakończ działanie pętli
"""

# BEGIN zadanie4.py
import sys
import random
difficulty = int(sys.argv[1])
number = random.randint(0, difficulty)
print('Liczba została wylosowana')
while True:
    guess = int(input('Zgadnij liczbę: '))
    if guess == number:
        print('Gratulacje!')
        break
# END zadanie4.py
# Uprzejmie proszę, żeby nie spędził Pan całego wieczora na graniu w grę, którą napisałem. Dziękuję. ;P

# takewhile, dropwhile
from itertools import takewhile, dropwhile

# dropwhile
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
drop = dropwhile(lambda x: x < 5, lista)
print(lista)
print(drop)
print(list(drop))
print(list(drop))  # pusty bo generator jest jednorazowy

# takewhile
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
take = takewhile(lambda x: x < 5, lista)
print(lista)
print(take)
print(list(take))
print(list(take))  # pusty bo generator jest jednorazowy

# moduł re i regex
import re

string = 'Ala ma kota, kot ma Alę'
pattern = r'Al[aę]'

print(re.findall(pattern, string))

# search
search = re.search(pattern, string)
print('Pierwsze wystąpienie na pozycji:', search.start(), ' o zawartości:', search.group())

# split
nonletters = r'[\W\d_]+'
lst = re.split(nonletters, string)
print(lst)

ls = [x for x in re.split(nonletters, string) if x]
print(ls)

# sub
print(re.sub(nonletters, '-', string))

"""
Zadanie 5
Zadeklaruj funkcję get_all_cities, która jako argument przyjmuje string.
W fukncji zastosuj wyrażenie regularne, która zwróci do listy wszystkie nazwy miast (wszystkie nazwy własne).
Następnie przejdź pętlą po tej liście i wyprintuj wszystkie miasta jedno po drugim.

Założenia:
String zawiera wszystkie możliwe znaki pomiędzy miastami. 
Miasta mogą składać się z dwóch członów np. Nowy Jork pomiędzy którymi wystąpi zawsze jedna spacja.
Przykładowy string testowy: r'iwuagdua,.,./;';[][][-==Nowy Jork=-./,/,/,/ ===..,.=Tokio=.;==[==-' 
    powinien zwrócić print 'Nowy Jork', 'Tokio'.
"""

string = r"iwuagdua,.,./;';[][][-==Nowy Jork=-./,/,/,/ ===..,.=Tokio=.;==[==-"


def get_all_cities(string: str):
    pattern = r'[A-Z][a-z]+\s?[A-Z]?[a-z]*'
    return re.findall(pattern, string)


cities_list = get_all_cities(string)

for city in cities_list:
    print(city)

# moduł datetime
import datetime

teraz = datetime.datetime.now()
print(teraz, type(teraz))
print(teraz.time(), type(teraz.time()))
print(teraz.date(), type(teraz.date()))
print(teraz.year, type(teraz.year))
print(teraz.month, type(teraz.month))
print(teraz.day, type(teraz.day))
print(teraz.hour, type(teraz.hour))
print(teraz.minute, type(teraz.minute))
print(teraz.second, type(teraz.second))
print(teraz.strftime('%Y-%m-%d %H:%M:%S'), type(teraz.strftime('%Y-%m-%d %H:%M:%S')))

# moduł time
import time

start = time.time()
some_list = [x for x in range(1000000)]
end = time.time()
print(f'Upłynęło {end - start} sekund')

start = time.time()
time.sleep(2)
end = time.time()
print(f'Upłynęło {end - start} sekund')

now_tuple = time.localtime()
print(now_tuple)
now_formatted = time.strftime('%Y-%m-%d %H:%M:%S', now_tuple)
print(now_formatted)

"""
Zaadanie 6
"""

# czytanie plików - stara fomra

file = open('output.txt', 'r')
print(file.read())
file.close()

# czytanie plików - nowa forma

with open('output.txt', 'r') as file:
    print(type(file))
    print(file.readline(100))  # czyta 100 znaków
    print(file.read())

    for line in file:
        print(line)
