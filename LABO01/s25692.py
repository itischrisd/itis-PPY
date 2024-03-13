# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# Instalacja PEP z terminala
# pip install autopep8

# Język wysokiego poziomu
print('Hello World')

# Silnie typowany
print('1' == 1)

# Dynamicznie typowany
number = 5
print(type(number))
number = 5.0
print(type(number))

# Ograniczenie liczby znaków w linii
example = 'Lorem impsum dolor sit amet cośtam dalej szło conseticur abla babla rampampam i coś dalej trza napisać bo brakuje'
print(example)


# Komentarze
def multiply(first_num, second_num):
    """To jest komentarz
    wieloliniowy"""
    return first_num * second_num


print(multiply(2, 5))

# Zmienne
num = 5
my_num = 5

# Stałe
CONST = 5
MY_CONST = 5


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


integer = 5
float1 = 5.5
float2 = 5.
float3 = .5
float4 = .4e5
float5 = 2.3e-4
complex_num = 1 + 2j
complex_real = complex_num.real
complex_imag = complex_num.imag
string = 'Hello World!'
boolean = True

# Konwersja typów danych
# var = typ(var), np
integer = int('555')
boolean = bool(1)

# operatory arytmetyczne
# + - * / // % ** () eval("na stringu")

# del a GC

# operacje z przypisaniem
#  += -= *= /= **=

"""ZAD1"""
height = "1.93"
height = float(height)
weight = "4 * 30"
weight = eval(weight)
bmi = weight / (height ** 2)
print(bmi)

# operatory porównania
# == != > < >= <=, łączenie kilku porównań a < b < c

# operacje bitowe
#  | & ^ >> <<

# operatory ogiczne
# and or not

# operatory specjalne
# is, is not

# definiowanie funkcji

input_data = input()
power_num = pow(int(input_data), 3)
print(input_data, power_num)


def nazwa_funkcji(arg1, arg2):
    return arg1 ** arg2


# nieokreślona liczba argumentów
# fun(*args) - args to lista

# argumenty kluczowe (keyword arguments)


def youngest(first, second, last):
    return last


print(youngest(first="Piotr", last="Anna", second="Hania"))


# argumenty kluczowe **kwargs
# wtedy:
# def fun(**kwards):
# i wywołując trzeba nazwać argumenty

# argumenty domyślne
# def fun(arg1, arg2=1):

# restrykcje

def fun(first, second, /):
    return first + second


# i teraz nie można podać nazw argumentów przy wywołaniu
# w drugą stronę:
# def fun(*, arg1, arg2)
# i teraz trzeba użyć keywordów przy wywołaniu
# można je łączyć:
# def fun(arg1, /, *, arg2):
# pierwszy nie może być nazwany, drugi musi

"""ZAD2"""
