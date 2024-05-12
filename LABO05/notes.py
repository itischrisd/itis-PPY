# Class
import asyncio
import json
import time

import requests
from bs4 import BeautifulSoup


class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def display(self):
        print(self.model, self.year)


print(Car)

# Object

car1 = Car("Toyota", 2019)
car1.display()
print(car1)
print(car1.model)
print(car1.year)
print(car1.display())


# Inheritance


class Vehicle:
    def __init__(self, type_of_vehicle: str, no_of_wheels: int):
        self.type_of_vehicle = type_of_vehicle
        self.no_of_wheels = no_of_wheels

    @staticmethod
    def honk():
        print("Honk Honk")


class Car(Vehicle):
    def __init__(self, model_name: str, year: int):
        super().__init__(type_of_vehicle="Car", no_of_wheels=4)
        self.model_name = model_name
        self.year = year

    def __repr__(self):
        return (
            f"It is a {self.type_of_vehicle} with {self.no_of_wheels} wheels."
            f" The model is {self.model_name} and it was made in {self.year}."
        )


car1 = Car("Toyota", 2019)
print(car1.model_name, car1.no_of_wheels)
print(car1.honk())
print(car1)

car2 = Car("Honda", 2020)
print(car2)
car2.honk()
car2.year = 2021
print(car2)


class Animal:
    def __init__(self, animal_name: str, number_of_legs: int):
        self.animal_name = animal_name
        self.number_of_legs = number_of_legs

    def fly(self):
        print("I can fly")


class Bird(Animal):
    def __init__(self, name: str, species: str):
        super().__init__(animal_name=name, number_of_legs=2)
        self.species = species

    def __repr__(self):
        return f"{self.animal_name} is a {self.species} and has {self.number_of_legs} legs."


class Human(Animal):
    def __init__(self, name: str, surname: str):
        super().__init__(animal_name=name, number_of_legs=2)
        self.surname = surname

    def __repr__(self):
        return f"My name is {self.animal_name} {self.surname}."

    def fly(self):
        print("I cannot fly")


bird1 = Bird("Bombel", "Parrot")
print(bird1)
bird1.fly()

human1 = Human("John", "Doe")
print(human1)
human1.fly()


# Data abstraction and encapsulation


class Animal:
    defualt_legs = 4
    _default_legs = 4
    __default_legs = 4

    def __init__(self, animal_name: str, number_of_legs: int):
        self.animal_name = animal_name
        self.number_of_legs = number_of_legs


class Bird(Animal):
    def __init__(self, name: str, specie: str):
        super().__init__(animal_name=name, number_of_legs=2)
        self.species = specie

    def __repr__(self):
        return f"{self.animal_name} is a {self.species} and has {self.number_of_legs} legs."


bird1 = Bird("Bombel", "Parrot")
print(bird1)
print(bird1.number_of_legs)
print(bird1.defualt_legs)
print(bird1._default_legs)
# print(bird1.__default_legs)
# nie tak, tylko tak
print(bird1._Animal__default_legs)

"""
Zadanie 1
Stwórz funkcjonalny i podstawowy system bankowy, w którym klienci mogą robić podstawowe operacje takie jak depozyt, withdrawal, transfer.
1. Stwórz klasę Person która przyjmuje dwa parametry (name, surname)
2. Stwórz klasę BankCustomer, która dziedziczy po Person. Zawiera dodatkowo informację o Account.
3. Stwórz klasę Account, jako konto klienta która zawiera informacje o obecnym stanie konta.
4. Dodaj metody deposit/withdraw/transfer w odpowiedniej klasie.

Przykładowa operacja:
bank_customer_1 = BankCustomer(...)
bank_customer_2 = BankCustomer(...)

print(bank_customer_1.balance)      # Output: 50

bank_customer_1.deposit(50)
print(bank_customer_1.balance)      # Output: 100

bank_customer_1.withdraw(50)
print(bank_customer_1.balance)      # Output: 50

print(bank_customer_2.balance)      # Output: 50
bank_customer_1.transfer(bank_customer_2, 50)
print(bank_customer_1.balance)      # Output: 0
print(bank_customer_2.balance)      # Output: 100
"""


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname


class Account:
    def __init__(self, balance: int):
        self.balance = balance


class BankCustomer(Person):
    def __init__(self, name: str, surname: str, balance: int):
        super().__init__(name, surname)
        self.account = Account(balance)

    @property
    def balance(self):
        return self.account.balance

    def deposit(self, amount: int):
        self.account.balance += amount

    def withdraw(self, amount: int):
        if amount > self.account.balance:
            print("Insufficient balance")
        else:
            self.account.balance -= amount

    def transfer(self, other, amount: int):
        if amount > self.account.balance:
            print("Insufficient balance")
        else:
            self.account.balance -= amount
            other.account.balance += amount


bank_customer_1 = BankCustomer("John", "Doe", 50)
bank_customer_2 = BankCustomer("Jane", "Doe", 50)

print(bank_customer_1.balance)  # Output: 50

bank_customer_1.deposit(50)
print(bank_customer_1.balance)  # Output: 100

bank_customer_1.withdraw(50)
print(bank_customer_1.balance)  # Output: 50

print(bank_customer_2.balance)  # Output: 50
bank_customer_1.transfer(bank_customer_2, 50)
print(bank_customer_1.balance)  # Output: 0
print(bank_customer_2.balance)  # Output: 100

# Magiczna metoda pythona
if __name__ == "__main__":
    print("Hello")

# obsługa plików / praca z kontekstowym menadżerem plików
file_path = "test.txt"

# czytanie pliku z użyciem open
file = open(file_path, "r")
print(file.read())
file.close()

# czytanie pliku z użyciem with (automatyczne zamykanie pliku)

with open(file_path, "r") as file:
    print(type(file))
    print(file.readline(100))
    print(file.read())

# pisanie do pliku
with open(file_path, "w") as file:
    file.write("Hello World")
    file.write("\n")

with open(file_path, "r") as file:
    print(file.read())

# czytanie pliku wiersz po wierszu
with open(file_path, "r") as file:
    for tr in file:
        print(tr)

"""
Zadanie 2
Zdefiniuj funkcję, przyjmującą jako argumenty: ścieżkę absolutną (jako string) oraz liczbę znaków (jako integer).
Niech funkcja wypisze do pliku reverse_pyramid.txt odwróconą piramidę stworzoną ze znaków X, o podstawie równej drugiemu argumentowi.

Przykład:
make_pyramid('/Users/grzegorz/Downloads/Zajęcia/Python 101/', 11)

po wyprintowaniu pliku /Users/grzegorz/Downloads/Zajęcia/Python 101/reverse_pyramid.txt:
# Output:
XXXXXXXXXXX
 XXXXXXXXX
  XXXXXXX
   XXXXX
    XXX
     X
"""


def make_pyramid(path: str, base: int):
    if base % 2 == 0:
        print("Baza piramidy musi być nieparzysta!")
        return

    levels = (base // 2) + 1

    with open(path + "reverse_pyramid.txt", "w") as file:
        for i in range(levels):
            num_x = base - 2 * i
            num_spaces = i
            line = " " * num_spaces + "X" * num_x + "\n"
            file.write(line)


make_pyramid("", 11)


# programowanie asynchroniczne


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"Started at {time.strftime('%X')}")
    await say_after(1, "Hello")
    print(f"Finished at {time.strftime('%X')}")
    await say_after(2, "World")
    print(f"Finished at {time.strftime('%X')}")


# asyncio.run(main())

# praca z requestami

response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response)
print(response.headers)
print(response.encoding)
print(response.text)
print(response.json())
print(response.status_code)

# pretty print json
print(json.dumps(response.json(), indent=4))

# web scraping

response = requests.get("https://www.gpw.pl/spolka?isin=PLNFI0600010")
print("Object type:", type(response))

soup = BeautifulSoup(response.text, "html5lib")
print("Object type:", type(soup))

print(soup.prettify())

with open("gpw.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())

print(soup.title)
print(soup.a)
for tr in soup.find_all("tr"):
    try:
        if tr.th.string == "Nazwa pełna:":
            print(tr)
            print(tr.td.string)
    except AttributeError:
        pass

"""
Zadanie 3
Stwórz funkcję, która przyjmuje jako argument link do konkretnej spółki w formacie:
https://www.gpw.pl/spolka?isin=PLNFI0600010.
Niech funkcja ta zescrapuje ostatnią cenę akcji i wyprintuje ją.
"""


def get_stock_price(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html5lib")
    stock_prices = soup.find_all("span", class_="summary")
    for stock_price in stock_prices:
        print(stock_price.string)


get_stock_price("https://www.gpw.pl/spolka?isin=PLNFI0600010")

# High Order Functions
# 1. Funkcja jako odnośnik do innej funkcji (nadrzędnej)


def spell(text: str):
    return text.upper()


print(spell("hello"))
scream = spell
print(scream("hello"))

# 2. Funkcja jako argument innej funkcji


def scream(text: str):
    return text.upper()


def whisper(text: str):
    return text.lower()


def speak(func: callable):
    speaking = func("Lorem Ipsum Dolor Sit Amet")
    print(speaking)


speak(scream)
speak(whisper)
