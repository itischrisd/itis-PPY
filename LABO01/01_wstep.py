# Wprowadzenie

# Instalacja PEP z poziomu terminala
# pip install autopep8

# Język wysokiego poziomu
print('Hello World')

# Silnie typowany
print('1' == 1)

# Dynamicznie typowany
liczba = 5
print(type(liczba))
liczba = 5.0
print(type(liczba))

# Ograniczenie liczby znaków w linii - 79 według PEP8 (PyCharm limituje do 120)
przyklad = 'Litwo! Ojczyzno moja! ty jesteś jak zdrowie. Ile cię trzeba cenić, ten tylko się dowie, Kto cię stracił. ' \
           'Dziś piękność twą w całej ozdobie Widzę i opisuję, bo tęsknię po tobie. Panno Święta, co Jasnej bronisz ' \
           'Częstochowy I w Ostrej świecisz Bramie! Ty, co gród zamkowy Nowogródzki ochraniasz z jego wiernym ludem! '
print(przyklad)


# Komentarze
def multiply(first_num,
             second_num):
    """Komentarze multiline stosuje się w celu
    opisu działania funkcji - zazwyczaj wewnątrz jej"""
    return first_num * second_num

print('po funkcji')
print(multiply(2, 5))


# Indentacja
def summarize(first_num,
              second_num):
    print(first_num, second_num)
    return first_num + second_num


print('Przed')
print(summarize(1, 3))

# Zmienna
liczba = 5
moja_liczba = 5

# Stała
STALA = 3.14
MOJA_STALA = 3.14


# Przykłady poprawnego nazewnictwa obiektów
class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f"Jestem {self.imie} {self.nazwisko}. Mam {self.wiek} lat.")

    def urodziny(self):
        wiek_przed = self.wiek
        self.wiek += 1
        return wiek_przed


# Typy danych
integers = 5
floats_1 = 5.5
floats_2 = 5.
floats_3 = .5
floats_4 = .4e7
floats_5 = 4.2e-4
complex_num = 3 + 4j
complex_real = complex_num.real
complex_imag = complex_num.imag
strings = 'Hello World!'
boolean = True
print(f'integers = {type(integers)}\n',
      f'floats_1 = {type(floats_1)}\n',
      f'floats_2 = {type(floats_2)}\n',
      f'floats_3 = {type(floats_3)}\n',
      f'floats_4 = {type(floats_4)}\n',
      f'floats_5 = {type(floats_5)}\n',
      f'complex_num = {type(complex_num)}\n',
      f'complex_real ({complex_real}) = {type(complex_real)}\n',
      f'complex_imag ({complex_imag}) = {type(complex_imag)}\n',
      f'strings = {type(strings)}\n',
      f'boolean = {type(boolean)}\n', )

# Konwersja typów danych
integers_1_conversion = int(floats_5)
integers_2_conversion = int('2')
integers_3_conversion = int(boolean)

floats_1_conversion = float(integers)
floats_2_conversion = float('2.0')
floats_3_conversion = float(boolean)
floats_4_conversion = float(False)

strings_1_conversion = str(integers)
strings_2_conversion = str(floats_1)
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
      f'boolean_2_conversion ({boolean_2_conversion}) = {type(boolean_2_conversion)}\n', )

# Funkcje vs metody
integers = 5
strings = 'Ala ma kota'
print(pow(integers, 3))
print(strings)
print(strings.upper())

# Operatory arytmetyczne
dodawanie = 5 + 5
odejmowanie = 5 - 5
mnozenie = 5 * 5
dzielenie = 5 / 5
dzielenie_calkowite = 5 // 3
reszta_z_dzielenia = 5 % 3
potegowanie = 5 ** 5
operacje_laczone = (5 + 3) ** (30 // 10)
operacje_laczone_eval = eval("(5 + 3) ** (30 // 10)")
print(dodawanie,
      odejmowanie,
      mnozenie,
      dzielenie,
      dzielenie_calkowite,
      reszta_z_dzielenia,
      potegowanie,
      operacje_laczone,
      operacje_laczone_eval, )

# Nadpisywanie + szybkie operacje na zmiennych

liczba = 5
liczba = liczba
liczba = 10
print(liczba)
liczba_1 = 10
liczba_2 = liczba_1
print(liczba_1, liczba_2)

# Dodawanie
liczba_1 = liczba_1 + 10
liczba_2 += 10
print(liczba_1, liczba_2, liczba_1 == liczba_2)

# Odejmowanie
liczba_1 = liczba_1 - 10
liczba_2 -= 10
print(liczba_1, liczba_2, liczba_1 == liczba_2)

# Mnożenie
liczba_1 = liczba_1 * 10
liczba_2 *= 10
print(liczba_1, liczba_2, liczba_1 == liczba_2)

# Dzielenie
liczba_1 = liczba_1 / 10
liczba_2 /= 10
print(liczba_1, liczba_2, liczba_1 == liczba_2)

# Potęgowanie
liczba_1 = liczba_1 ** 10
liczba_2 **= 10
print(liczba_1, liczba_2, liczba_1 == liczba_2)

# ZADANIE
"""
1. Zadeklaruj zmienną wzrost równą twojemu wzrostowi w metrach w formacie string
2. Przekonwertuj wzrost na liczbę
3. Zadeklaruj zmienną waga w kg jako mnożenie dwóch liczb w formacie string
4. Przekonwertuj działanie zapisane w wadze na liczbę
5. Zadeklaruj zmienną BMI równą waga / wzrost**2 i ją wypisz
"""

# ROZWIĄZANIE
# 1.
wzrost = '1.84'
# 2.
wzrost = float(wzrost)
# 3.
waga = '2 * 44.5'
# 4.
waga = eval(waga)
# 5.
bmi = waga / (wzrost ** 2)
print(bmi)

# Operatory porównujące
liczba_1 = 5
liczba_2 = 10
liczba_3 = 15
print(f'{liczba_1} == {liczba_2} = {liczba_1 == liczba_2}\n',
      f'{liczba_1} != {liczba_2} = {liczba_1 != liczba_2}\n',
      f'{liczba_1} > {liczba_2} = {liczba_1 > liczba_2}\n',
      f'{liczba_1} < {liczba_2} = {liczba_1 < liczba_2}\n',
      f'{liczba_1} >= {liczba_2} = {liczba_1 >= liczba_2}\n',
      f'{liczba_1} <= {liczba_2} = {liczba_1 <= liczba_2}\n',
      f'{liczba_1} <= {liczba_2} <= {liczba_3} = {liczba_1 <= liczba_2 <= liczba_3}\n',
      f'{liczba_1} <= {liczba_3} <= {liczba_2} = {liczba_1 <= liczba_3 <= liczba_2}\n', )

# Operacje bitowe na liczbach całkowitych
print(f'10 & 7 = {10 & 7}\n\t1010\n\t &\n\t0111\n\t0010 = 2\n',  # operator AND - zwróć 1 gdy oba bity są równe 1
      f'10 | 7 = {10 | 7}\n\t1010\n\t |\n\t0111\n\t1111 = 15\n',
      # operator OR - zwróć 1 gdy chociaż jeden z bitów równy 1
      f'10 ^ 7 = {10 ^ 7}\n\t1010\n\t ^\n\t0111\n\t1101 = 13\n',
      # operator XOR - zwróć 1 gdy jeden z bitów jest równy 1, a drugi 0
      f'~10 = {~10}\n\t~1010\n\t-(1010+1)\n\t-1011 = -11\n',
      # operator dopełnienia jednostkowego - liczba przeciwna wartości bitowej + 1
      f'10 << 2 = {10 << 2}\n\t1010<<2\n\t101000 = 40\n',
      # operator przesunięcia w lewo - dodaj N zer do wartości bazowej
      f'10 >> 2 = {10 >> 2}\n\t1010>>2\n\t10 = 2\n',  # operator przesunięcia w prawo - zabierz N bitów od prawej
      )

# Operatory logiczne
true_and_true = True and True
true_and_false = True and False
true_or_false = True or False
false_or_false = False or False
not_false = not False
print(f'True and True = {true_and_true}\n',
      f'True and False = {true_and_false}\n',
      f'True or False = {true_or_false}\n',
      f'False or False = {false_or_false}\n',
      f'not False = {not_false}\n',
      )

# Operatory specjalne - sprawdzają konkretną alokacje w pamięci
integers = 5
floats = 5.0
list_1 = [1, 2, 3]
list_2 = list_1
list_3 = list_1[:]
strings = 'True'

int_is_int = integers is integers
int_is_float = integers is floats
string_is_string = strings is strings
list_1_is_list_2 = list_1 is list_2
list_1_is_list_3 = list_1 is list_3
int_is_not_int = integers is not integers
int_is_not_float = integers is not floats
string_is_not_string = strings is not strings
list_1_is_not_list_2 = list_1 is not list_2
list_1_is_not_list_3 = list_1 is not list_3

print(f'5 is 5 = {int_is_int}\n',
      f'5 is 5.0 = {int_is_float}\n',
      f'\'True\' is \'True\' = {string_is_string}\n',
      f'list_1({list_1}) is list_2({list_2}) = {list_1_is_list_2}\n',
      f'list_1({list_1}) is list_3({list_3}) = {list_1_is_list_3}\n',
      f'5 is not 5 = {int_is_not_int}\n',
      f'5 is not 5.0 = {int_is_not_float}\n',
      f'\'True\' is not \'True\' = {string_is_not_string}\n',
      f'list_1({list_1}) is not list_2({list_2}) = {list_1_is_not_list_2}\n',
      f'list_1({list_1}) is not list_3({list_3}) = {list_1_is_not_list_3}\n',
      )

# Definiowanie funkcji

input_data = input()
power_num = pow(int(input_data), 3)
print(input_data, power_num)


def dodawanie_1(pierwsza_liczba, druga_liczba):
    return pierwsza_liczba + druga_liczba


def dodawanie_2(pierwsza_liczba, druga_liczba):
    suma = pierwsza_liczba + druga_liczba
    return suma


print(dodawanie_1(5, 12), dodawanie_2(5, 12))


# Nieokreślona liczba argumentów - *args
def kto_najmlodszy(*dzieci):
    return dzieci[-1]


print(kto_najmlodszy('Patrycja', 'Anna', 'Piotr'))


# Argumenty kluczowe - keyword arguments
def kto_najmlodszy(pierwsze, drugie, ostatnie):
    return ostatnie


print(kto_najmlodszy(pierwsze='Patrycja', drugie='Anna', ostatnie='Piotr'))


# Argumenty kluczowe - **kwargs
def kto_najmlodszy(**dzieci):
    return dzieci['ostatnie']


print(kto_najmlodszy(pierwsze='Patrycja', drugie='Anna', ostatnie='Piotr'))


# Argumenty domyślne funkcji
def dodawanie_1(pierwsza_liczba=5, druga_liczba=10):
    return pierwsza_liczba + druga_liczba


def dodawanie_2(pierwsza_liczba, druga_liczba=10):
    return pierwsza_liczba + druga_liczba


print(dodawanie_1(),
      dodawanie_1(10),
      dodawanie_1(druga_liczba=25),
      dodawanie_2(25))


# Restrykcja argumentów do wyłącznie argumentów pozycyjnych
def dodawanie(pierwsza_liczba, druga_liczba, /):
    return pierwsza_liczba + druga_liczba


# print(dodawanie(pierwsza_liczba=10, druga_liczba=15))     # błąd intencjonalny - nie możemy podawać argumentów kluczowych jeżeli funkcja wymaga wyłącznie pozycyjnych
print(dodawanie(10, 15))


# Restrykcja argumentów do wyłącznie argumentów kluczowych
def dodawanie(*, pierwsza_liczba, druga_liczba):
    return pierwsza_liczba + druga_liczba


print(dodawanie(pierwsza_liczba=10, druga_liczba=15))
# print(dodawanie(10,15))     # błąd intencjonalny - nie możemy podawać argumentów pozycyjych jeżeli funkcja wymaga wyłącznie kluczowych


# Kombinacja restrykcji w definiowaniu funkcji
def dodawanie(pierwsza_liczba, /, *, druga_liczba):
    return pierwsza_liczba + druga_liczba


# print(dodawanie(pierwsza_liczba=10, druga_liczba=15))     # błąd intencjonalny - nie możemy podawać argumentów wyłącznie kluczowych jeżeli funkcja wymaga innych
# print(dodawanie(10,15))     # błąd intencjonalny - nie możemy podawać argumentów pozycyjych jeżeli funkcja wymaga innych
print(dodawanie(10, druga_liczba=15))


# Rekurencja funkcji
def tri_recursion(k):
    if (k > 0):
        print(f'Rozważamy liczbę: {k}')
        result = k + tri_recursion(k - 1)
        print(f'Zakończyliśmy iterację dla liczby: {k}')
        print(result)
    else:
        result = 0
    return result


tri_recursion(6)

# PAUSE
