# LABO01 - Wprowadzenie

# Instalacja PEP z terminala
# pip install autopep8

# Język wysokiego poziomu
print('Hello World')

# Silnie typowany
print('1' == 1)  # false

# Dynamicznie typowany
number = 5
print(type(number))
number = 5.0
print(type(number))

# Ograniczenie liczby znaków w linii - 79 dla PEP8, 120 dla PyCharma
example = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et '
           'dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip '
           'ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu '
           'fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt '
           'mollit anim id est laborum.')
print(example)


# Komentarze
def multiply(first_num, second_num):
    """To jest komentarz
    wieloliniowy - multiline"""
    return first_num * second_num


print(multiply(2, 5))


# Indentacja - 4 spacje, a nie tab
def summarize(first_num, second_num):
    print(first_num, second_num)
    return first_num + second_num


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

    def greeting(self):
        print(f"Jestem {self.name} {self.surname}. Mam {self.age} lat.")

    def birthday(self):
        age_before = self.age
        self.age += 1
        return age_before


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
print(f"integer = {integer}, {type(integer)}\n", f"float1 = {float1}, {type(float1)}\n",
      f"float2 = {float2}, {type(float2)}\n", f"float3 = {float3}, {type(float3)}\n",
      f"float4 = {float4}, {type(float4)}\n", f"float5 = {float5}, {type(float5)}\n",
      f"complex_num = {complex_num}, {type(complex_num)}\n", f"complex_real = {complex_real}, {type(complex_real)}\n",
      f"complex_imag = {complex_imag}, {type(complex_imag)}\n", f"string = {string}, {type(string)}\n",
      f"boolean = {boolean}, {type(boolean)}\n")

# Konwersja typów danych
# var = typ(var), np
integers_1_conversion = int(float5)
integers_2_conversion = int('2')
integers_3_conversion = int(boolean)

floats_1_conversion = float(integer)
floats_2_conversion = float('2.0')
floats_3_conversion = float(boolean)
floats_4_conversion = float(False)

strings_1_conversion = str(integer)
strings_2_conversion = str(float1)
strings_3_conversion = str(boolean)
strings_4_conversion = str(complex_num)

boolean_1_conversion = bool(0)
boolean_2_conversion = bool(1.0)
print(f'integers_1_conversion ({integers_1_conversion}) = {type(integers_1_conversion)}\n',
      f'integers_2_conversion ({integers_2_conversion}) = {type(integers_2_conversion)}\n',
      f'integers_3_conversion ({integers_3_conversion}) = {type(integers_3_conversion)}\n',
      f'floats_1_conversion ({floats_1_conversion}) = {type(floats_1_conversion)}\n',
      f'floats_2_conversion ({floats_2_conversion}) = {type(floats_2_conversion)}\n',
      f'floats_3_conversion ({floats_3_conversion}) = {type(floats_3_conversion)}\n',
      f'floats_4_conversion ({floats_4_conversion}) = {type(floats_4_conversion)}\n',
      f'strings_1_conversion ({strings_1_conversion}) = {type(strings_1_conversion)}\n',
      f'strings_2_conversion ({strings_2_conversion}) = {type(strings_2_conversion)}\n',
      f'strings_3_conversion ({strings_3_conversion}) = {type(strings_3_conversion)}\n',
      f'strings_4_conversion ({strings_4_conversion}) = {type(strings_4_conversion)}\n',
      f'boolean_1_conversion ({boolean_1_conversion}) = {type(boolean_1_conversion)}\n',
      f'boolean_2_conversion ({boolean_2_conversion}) = {type(boolean_2_conversion)}\n')

# operatory arytmetyczne
# + - * / // % ** () eval("na stringu")

# del a Garbage collector

# operacje z przypisaniem
#  += -= *= /= **=

"""ZAD1"""
"""
1. Zadeklaruj zmienną wzrost równą twojemu wzrostowi w metrach w formacie string
2. Przekonwertuj wzrost na liczbę
3. Zadeklaruj zmienną waga w kg jako mnożenie dwóch liczb w formacie string
4. Przekonwertuj działanie zapisane w wadze na liczbę
5. Zadeklaruj zmienną BMI równą waga / wzrost**2 i ją wypisz
"""
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

# operatory specjalne (równość referencji)
# is, is not

# definiowanie funkcji

input_data = input()
power_num = pow(int(input_data), 3)
print(input_data, power_num)


def nazwa_funkcji(arg1, arg2):
    return arg1 ** arg2


# nieokreślona liczba argumentów
# fun(*args) - args to lista
# np:

def last_element(*lst):
    return lst[-1]


# argumenty kluczowe (keyword arguments)
# np:

def youngest(first, second, last):
    return last


print(youngest(first="Piotr", last="Anna", second="Hania"))


# argumenty kluczowe **kwargs
# def fun(**kwardg) - kwargs to słownik
# i wywołując trzeba nazwać argumenty

def youngest(**children):
    return children['youngest']


# argumenty domyślne
# def fun(arg1, arg2=1):

def increment(base_num, to_add=1):
    return base_num + to_add


# restrykcje
# nie można podać argumentów kluczowych przed /

def fun(first, second, /):
    return first + second


# albo trzeba podać jako kluczowe po *

def fun2(*, first, second):
    return first + second


# można łączyć:

def dodawanie(pierwsza_liczba, /, *, druga_liczba):
    return pierwsza_liczba + druga_liczba


print(dodawanie(10, druga_liczba=15))


# Rekurencja funkcji

def fibonacci(n, memo):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


to_fib = 50
memory = {}
for i in range(1, to_fib + 1):
    print(f"{i}-ta liczba ciągu Fibonacciego to {fibonacci(i, memory)}")
