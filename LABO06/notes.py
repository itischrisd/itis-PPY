def Adding(a):
    def Addition(b):
        return a + b

    return Addition


a = 5  # int(input("Enter first number: "))
b = 4  # int(input("Enter second number: "))

AddVariable = Adding(a)
print(AddVariable)

Result = AddVariable(b)

print(f"Result: {Result}")

# magiczne metody

for method in dir(str):
    print(method, end=", ")


class Car:
    def __init__(self, car_name):
        print(f"Car: {car_name} created!")
        self.car_name = car_name

    def __repr__(self):
        return f"Car: {self.car_name}"

    def __str__(self):
        return f"Car: {self.car_name}"


car = Car("Audi")
print(car)
print(str(car) + " A4")


# print(car + " A4")  # TypeError: unsupported operand type(s) for +: 'Car' and 'str'


class CarWithAddition(Car):
    def __add__(self, other):
        return f"{self.car_name} {other}"


car = CarWithAddition("Audi")
print(car + " A4")


# __new__ - tworzenie nowego obiektu
# __init__ - inicjalizacja obiektu
# __del__ - usuwanie obiektu


class Animal:
    def __new__(cls, *args, **kwargs):
        print("Creating new object")
        return super().__new__(cls)

    def __init__(self, name):
        print("Initializing object")
        self.name = name

    def __del__(self):
        print("Deleting object")


animal = Animal("Dog")
print(animal.name)
del animal


# NUMERIC


class NegativePositiveValue:
    def __init__(self, value):
        self.value = value

    def __pos__(self):
        return self.value

    def __neg__(self):
        return -self.value


value = NegativePositiveValue(5)
print(+value)
print(-value)

# __trunc__ - zwraca część całkowitą
# __ceil__ - zwraca najmniejszą liczbę całkowitą większą od danej
# __floor__ - zwraca największą liczbę całkowitą mniejszą od danej
# __round__ - zaokrągla do danej liczby miejsc po przecinku
# __invert__ - zwraca bitowy negatyw liczby
# __abs__ - zwraca wartość bezwzględną liczby
# __neg__ - zwraca wartość przeciwną liczby
# __pos__ - zwraca wartość liczby

import numpy as np

mat_a = np.mat("1 2; 3 4")
mat_b = np.mat("5 6; 7 8")

arr_a = np.array([[1, 2], [3, 4]])
arr_b = np.array([[5, 6], [7, 8]])

print(mat_a, "\n", mat_b, "\n")
print(arr_a, "\n", arr_b, "\n")

print(mat_a * mat_b, "\n")
print(arr_a * arr_b, "\n")

# ARYTMETYCZNE
# __add__ - dodawanie
# __sub__ - odejmowanie
# __mul__ - mnożenie
# __truediv__ - dzielenie
# __floordiv__ - dzielenie całkowite
# __mod__ - reszta z dzielenia
# __pow__ - potęgowanie
# __lshift__ - przesunięcie bitowe w lewo
# __rshift__ - przesunięcie bitowe w prawo
# __and__ - bitowy AND
# __or__ - bitowy OR
# __xor__ - bitowy XOR


class Greeting:
    def __init__(self, greeting):
        self.greeting = greeting

    def __repr__(self):
        return f"Greeting: {self.greeting}"

    def __add__(self, other):
        print(f"Adding {other.greeting} to {self.greeting} twice")
        return f"{self.greeting} {other.greeting} {other.greeting}"


greeting1 = Greeting("Hello")
greeting2 = Greeting("World")
print(greeting1 + greeting2)

# STRING

# __str__ - zwraca reprezentację obiektu jako string
# __repr__ - zwraca reprezentację obiektu jako string
# __len__ - zwraca długość obiektu
# __unicode__ - zwraca reprezentację obiektu jako string
# __format__ - formatuje obiekt
# __hash__ - zwraca hash obiektu


class String:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"String: {self.string}"

    def __str__(self):
        return f"String: {self.string}"

    def __len__(self):
        return len(self.string)

    def __hash__(self):
        return hash(self.string)

    def __bool__(self):
        return bool(self.string)


string = String("Hello")
print(string)
print(len(string))
print(hash(string))
print(bool(string))


# PORÓWNANIA
# __eq__ - równość
# __ne__ - nierówność
# __lt__ - mniejsze niż
# __le__ - mniejsze lub równe
# __gt__ - większe niż
# __ge__ - większe lub równe


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book: {self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.title < other.title

    def __le__(self, other):
        return self.title <= other.title

    def __gt__(self, other):
        return self.title > other.title

    def __ge__(self, other):
        return self.title >= other.title


book1 = Book("Python", "Guido van Rossum")
book2 = Book("Java", "James Gosling")
book3 = Book("Python", "Guido van Rossum")

print(book1 == book2)
print(book1 == book3)
print(book1 < book2)
print(book1 <= book2)
print(book1 > book2)
print(book1 >= book2)


# OTHER
# __call__ - wywołanie obiektu
# __getitem__ - pobranie elementu
# __setitem__ - ustawienie elementu
# __delitem__ - usunięcie elementu
# __iter__ - iteracja
# __next__ - kolejny element
# __contains__ - sprawdzenie czy element jest w obiekcie
# __setslice__ - ustawienie wycinka


class OtherExample:
    def __init__(self, data):
        self.data = data

    def __call__(self):
        return self.data

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __contains__(self, item):
        return item in self.data

    def __setslice__(self, start, stop, step):
        return self.data[start:stop:step]


other = OtherExample([1, 2, 3, 4, 5])
print(other())
print(other[0])
other[0] = 0
print(other[0])
del other[0]
print(other[0])
for item in other:
    print(item)
print(3 in other)
print(6 in other)
print(other[1:3:1])

# ITERATORY


class IteratorSkonczony:
    def __init__(self, value):
        self.limit = value

    def __iter__(self):
        return self

    def __next__(self):
        self.limit *= 2
        if self.limit > 50:
            raise StopIteration
        else:
            return self.limit


iterator = IteratorSkonczony(3)
for i in iterator:
    print(i)


class IteratorNieskonczony:
    def __init__(self, value):
        self.limit = value

    def __iter__(self):
        return self

    def __next__(self):
        self.limit *= 2
        return self.limit


iterator = IteratorNieskonczony(3)
for i in iterator:
    if i > 50:
        break
    print(i)


"""
ZADANIE 1
Stwórz iterator printujący kolejne liczby ciągu Fibonacciego podobnie to iteratora NieskonczonyIterator opisanego powyżej..
Wykorzystaj metody __iter__ oraz __next__.
"""


class FibonacciIterator:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result


fibonacci = FibonacciIterator()
for _ in range(10):
    print(next(fibonacci), end=" ")

print()

# gettery, settery, property


class Person:
    def __init__(self):
        self.__name = "John"
        self.__age = 30

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        self.__age = age


person = Person()
print(person.name)
print(person.age)
person.name = "Alice"
person.age = 25
print(person.name)
print(person.age)

# dekoratory


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def say_hello():
    print("Hello!")


say_hello()


def say_hello2():
    print("Hello!")


say_hello2 = do_twice(say_hello2)
say_hello2()

# Inne dekoratory oraz referencje
# classmethod


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split()
        return cls(name, age)


person = Person.from_string("Alice 25")
print(person.name)

# staticmethod


class Math:
    @staticmethod
    def add(a, b):
        return a + b


print(Math.add(5, 4))


"""
ZADANIE 2
Napisz klasę LibraryBook, która będzie symulować operacje na książkach bibliotecznych.

Wymagania:

Konstruktor:
__init__(self, title, author, isbn, copies=1): Konstruktor powinien przyjmować tytuł książki (title), autora (author),
numer ISBN (isbn) oraz opcjonalnie liczbę kopii (copies), która domyślnie wynosi 1.

Metody instancji:
borrow_book(self): Ta metoda powinna zmniejszać liczbę dostępnych kopii o 1, jeśli są dostępne kopie. Jeśli nie ma
dostępnych kopii, metoda powinna wyświetlać komunikat o braku dostępnych egzemplarzy.
return_book(self): Ta metoda powinna zwiększać liczbę dostępnych kopii o 1.
get_info(self): Ta metoda powinna zwracać informację o książce (tytuł, autor, ISBN, dostępne kopie).
reserve_book(self): Ta metoda rezerwuje książkę, zmniejszając liczbę dostępnych kopii o 1, ale tylko wtedy, gdy jest
przynajmniej jedna dostępna kopia. Rezerwacja powinna być wyświetlana jako komunikat: "Książka została zarezerwowana".

Metoda klasowa:
get_library_name(cls): Ta metoda powinna zwracać nazwę biblioteki. Nazwa biblioteki powinna być przechowywana jako
atrybut klasy (np. library_name).

Metoda statyczna:
is_valid_isbn(isbn): Ta metoda powinna sprawdzać, czy numer ISBN jest poprawny. Dla uproszczenia załóżmy, że poprawny
numer ISBN to taki, który składa się z 13 cyfr.

Właściwość:
copies: Zdefiniuj właściwość, która pozwala na pobieranie i ustawianie liczby kopii. Przy ustawianiu liczby kopii, jeśli
nowa wartość jest mniejsza niż 0, powinna być wyświetlana odpowiednia wiadomość o błędzie.
"""


class LibraryBook:
    library_name = "Library"

    def __init__(self, title, author, isbn, copies=1):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__copies = copies

    def borrow_book(self):
        if self.__copies > 0:
            self.__copies -= 1
        else:
            print("No copies available")

    def return_book(self):
        self.__copies += 1

    def get_info(self):
        return f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.__isbn}, Copies: {self.__copies}"

    def reserve_book(self):
        if self.__copies > 0:
            self.__copies -= 1
            print("Book has been reserved")

    @classmethod
    def get_library_name(cls):
        return cls.library_name

    @staticmethod
    def is_valid_isbn(isbn):
        return len(isbn) == 13 and isbn.isdigit() and isbn[0:3] in ["978", "979"]

    @property
    def copies(self):
        return self.__copies

    @copies.setter
    def copies(self, copies):
        if copies < 0:
            print("Invalid number of copies")
        else:
            self.__copies = copies


book = LibraryBook("Python", "Guido van Rossum", "9780134444321", 5)
print(book.get_info())
book.borrow_book()
print(book.get_info())
book.return_book()
print(book.get_info())
book.reserve_book()
print(book.get_info())
print(LibraryBook.get_library_name())
print(LibraryBook.is_valid_isbn("9780134444321"))
print(LibraryBook.is_valid_isbn("978013444432"))
book.copies = -1
print(book.get_info())
book.copies = 10
print(book.get_info())

"""
Zadanie 3
1. Stwórz funkcję wyliczającą liczby z zakresu od 0 do n (argumentu funkcji).
2. Utwórz funkcję w formie dekoratora tej funkcji, która będzie podwajała print każdej liczby.
"""


def double_print(func):
    def wrapper(n):
        for i in func(n):
            print(i * 2)

    return wrapper


@double_print
def numbers(n):
    return range(n)


numbers(5)


# list vs queue

lst = [1, 2, 3, 4, 5]
print(lst)
lst.pop()
print(lst)
lst.append(6)
print(lst)

import queue

q = queue.Queue()
q.put("a")
q.put("b")
q.put("c")
print(q)
print(q.get())
print(q.get())
print(q.get())

# multiprocessing

import multiprocessing

print(multiprocessing.cpu_count())


def cube(number):
    print(f"Cube: {number ** 3}")


def square(number):
    print(f"Square: {number ** 2}")


# process1 = multiprocessing.Process(target=cube, args=(5,))
# process2 = multiprocessing.Process(target=square, args=(5,))
#
# process1.start()
# process2.start()
#
# process1.join()
# process2.join()

# json

import requests, json

response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = json.loads(response.text)

# os


import os

print(os.getcwd())
print(os.listdir())
print(os.path.exists("notes.py"))
print(os.path.isfile("notes.py"))
print(os.access("notes.py", os.F_OK))
print(os.access("notes.py", os.R_OK))
print(os.access("notes.py", os.W_OK))
print(os.access("notes.py", os.X_OK))
print(os.path.getsize("notes.py"))
print(os.path.getmtime("notes.py"))
print(os.path.getctime("notes.py"))
print(os.path.getatime("notes.py"))
print(os.path.abspath("notes.py"))
print(os.path.dirname("notes.py"))
print(os.path.basename("notes.py"))
