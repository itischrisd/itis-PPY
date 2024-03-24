# operator przynależności in
x = [1, 2, 3]
y = x
z = x[:]
print(x is y, x is z, y is z)


# określanie typów danych parametrów funkcji i typów zwracanych
# czysto informacyjne, nie wpływa na działanie programu

def add_integers(a: int, b: int) -> int:
    return a + b


print(add_integers(1, 2))
print(add_integers(1.0, 2.0))
print(add_integers('1', '2'))

"""
ZAD1
Bazując na poprzednim zadaniu z BMI utwórz funkcję, która obliczy aktualny wskaźnik BMI bazując na wadze i wzroście użytkownika.
Warunki:
1. Argument wzrost w metrach w formacie string jako parametr wyłącznie kluczowy (wzrost='1.84')
2. Argument waga w kg jako mnożenie dwóch liczb w formacie string wyłącznie jako argument pozycyjny
3. Wzór na BMI to waga / wzrost**2
4. Zwróć wartość True gdy BMI w przedziale 18.5 a 29.9
"""


def bmi_calculator(wzrost: str, /, *, waga: str) -> bool:
    waga = eval(waga)
    wzrost = float(wzrost)
    bmi = waga / (wzrost ** 2)
    return 18.5 < bmi < 29.9


print(bmi_calculator('1.93', waga='4 * 30'))

# dodawanie floatów
print(0.1 + 0.2 == 0.3)
print(0.1 + 0.2)
print(1.40 * 165)

# typy danych sekwencyjnych
example_list1 = [1, 2.0, "kotek", True, 1 + 2j, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3}]
example_list2 = list((1, 2.0, "kotek", True, 1 + 2j, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3}))
first_object = example_list1[0]
last_object = example_list1[-1]
o_1, o_2, o_3, o_4, o_5, o_6, o_7, o_8, o_9 = example_list1
o_10, o_11, *o_rest = example_list2
list_slice = example_list1[1:4]
every_second = example_list1[::2]
list_length = len(example_list1)
list_type = type(example_list1)
new_list = example_list1[:]
new_list[0] = 999

print(f"example_list1 = {example_list1}\n",
      f"example_list2 = {example_list2}\n",
      f"first_object = {first_object}\n",
      f"last_object = {last_object}\n",
      f"o_rest = {o_rest}\n",
      f"list_slice = {list_slice}\n",
      f"every_second = {every_second}\n",
      f"list_length = {list_length}\n",
      f"list_type = {list_type}\n",
      f"new_list = {new_list}\n")

#  operacje na listach
# append, extend, insert, remove, pop, clear, index, count, sort, reverse, copy
example_list1.append(999)
example_list1.insert(0, 999)
joined_list = example_list1 + example_list2

example_list1.remove(999)
example_list1.pop(0)
print(example_list1)
example_list1.clear()
print(example_list1)

num_list = [1, 2.5, 3, 60]
num_list = num_list * 3
list_sum = sum(num_list)
print(num_list, list_sum)

"""
append - dodaje element na końcu listy
extend - rozszerza listę o elementy z innej listy
insert - dodaje element na wskazanej pozycji
remove - usuwa pierwsze wystąpienie elementu
pop - usuwa element z wskazanej pozycji
clear - usuwa wszystkie elementy z listy
index - zwraca indeks pierwszego wystąpienia elementu
count - zwraca liczbę wystąpień elementu
sort - sortuje listę
reverse - odwraca listę
copy - kopiuje listę
"""

"""
ZAD2
1. Utwórz listę zawierającą dwa stringi - twoje imię i nazwisko.
2. Wyprintuj najpierw całą listę, następnie osobno imie i nazwisko (multiassignment lub po indeksie).
3. Dodaj druie imię z użyciem funkcji input() (możliwość wpisywania "z palca"). Następnie wyprintuj listę ponownie.
4. Wyprintuj liczbę obiektów w liście.
5. Wyczyść listę i zwróc ją.
"""

full_name = ["Krzysztof", "Dudek"]
print(full_name)
# by index
print(full_name[0])
print(full_name[1])
# by multiassignment
name, surname = full_name
print(name)
print(surname)
full_name.insert(1, input("Podaj drugie imię: "))
print(full_name)
print(len(full_name))
full_name.clear()
print(full_name)

# Tuple - krotki - niezmienne, indeksowane, hashowalne, sortowalne, pozwalające na duplikaty
example_tuple = (1, 2.0, "kotek", True, 1 + 2j, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3})
first_object = example_tuple[0]
last_object = example_tuple[-1]
o_1, o_2, o_3, o_4, o_5, o_6, o_7, o_8, o_9 = example_tuple
o_10, o_11, *o_rest = example_tuple
tuple_slice = example_tuple[1:4]
every_second = example_tuple[::2]
tuple_length = len(example_tuple)
tuple_type = type(example_tuple)
new_tuple = example_tuple[:]
# new_tuple[0] = 999 # TypeError: 'tuple' object does not support item assignment
print(f"example_tuple = {example_tuple}\n",
      f"first_object = {first_object}\n",
      f"last_object = {last_object}\n",
      f"o_rest = {o_rest}\n",
      f"tuple_slice = {tuple_slice}\n",
      f"every_second = {every_second}\n",
      f"tuple_length = {tuple_length}\n",
      f"tuple_type = {tuple_type}\n",
      f"new_tuple = {new_tuple}\n")

# dodawanie tupli
tuple_1 = (1, 2, 3)
tuple_2 = ("a", "b", "c")
joined_tuple = tuple_1 + tuple_2
print(joined_tuple)

# operacje na tuplach - matematyczne oparacje
math_tuple = (1, 2, 3)
multiplied_tuple = math_tuple * 3
print(f"math_tuple = {multiplied_tuple}\n",
      f"multiplied_tuple = {multiplied_tuple}\n")

# jak zmieniać tuple
example_tuple = (1, 2, 3, "a", "b", "c")
example_list = list(example_tuple)
# zmiana na listę, operacje na liście, zmiana na tuple

# tuple - metody
# count, index
print(example_tuple.count(1))
print(example_tuple.index(1))

# Set - zbiory - niezmienne, nieindeksowane, niehaszowalne, niesortowalne, niepozwalające na duplikaty
example_set = {1, 2.0, "kotek", True, 1 + 2j}
example_set = set((1, 2.0, "kotek", True, 1 + 2j))
# first_object = set[0]  # TypeError: 'set' object is not subscriptable
set_length = len(example_set)
set_type = type(example_set)
new_set1 = set((1, 2, 3))
new_set2 = set(example_tuple)
new_set3 = set(example_list)
print(f"example_set = {example_set}\n",
      f"set_length = {set_length}\n",
      f"set_type = {set_type}\n",
      f"new_set1 = {new_set1}\n",
      f"new_set2 = {new_set2}\n",
      f"new_set3 = {new_set3}\n")

# dostęp do elementów
for element in example_set:
    print(element)

# dodawanie elementów do set
example_set.add("pies")
print(example_set)
example_set.update(example_list, example_tuple)
print(example_set)
final_set = example_set.union(new_set1, new_set2, new_set3)
print(final_set)

# usuwanie elementów ze zbioru
example_set.remove(1)
print(example_set)
example_set.discard(1)
print(example_set)
example_set.pop()
print(example_set)

"""
add - dodaje element
update - dodaje elementy z innej sekwencji
remove - usuwa element, KeyError gdy nie ma
discard - usuwa element, brak KeyError
pop - usuwa losowy element
"""

# strings
example_string = "Hello World!"
first_char = example_string[0]
last_char = example_string[-1]
# o_1, o_2, o_3, o_4, o_5, o_6, o_7, o_8, o_9 = example_string
o_10, o_11, *o_rest = example_string
char_slice = example_string[1:4]
every_second = example_string[::2]
string_length = len(example_string)
string_type = type(example_string)
new_string_1 = example_string[:]
new_string_2 = str(123)
new_string_3 = str([1, 2, 3])
# new_string[0] = "h"  # TypeError: 'str' object does not support item assignment
print(f"example_string = {example_string}\n",
      f"first_char = {first_char}\n",
      f"last_char = {last_char}\n",
      f"o_rest = {o_rest}\n",
      f"char_slice = {char_slice}\n",
      f"every_second = {every_second}\n",
      f"string_length = {string_length}\n",
      f"string_type = {string_type}\n",
      f"new_string = {new_string_1}\n"
      f"new_string_2 = {new_string_2}\n"
      f"new_string_3 = {new_string_3}\n")

# dodawanie stringów
string_1 = "Hello"
string_2 = "World"
joined_string = string_1 + string_2
print(joined_string)

# formatowanie stringów
example_string = "Hello {}!"
print(example_string.format("World"))
example_string = "{} ma {}"
print(example_string.format("Ala", "kota"))
example_string = "{1} ma {0}"
print(example_string.format("kota", "Ala"))

# escape characters
print("Hello\nWorld!")
print("Hello\\World!")
print("Hello\tWorld!")
print("Hello\"World!\"")
print("Hello\bWorld!")
print("Hello\fWorld!")

# string - metody
example_list = ["Hello", "World!"]
list_to_string = " ".join(example_list)
print(list_to_string)

# dictionaries - słowniki
example_dict = {1: "Hello", 2: "World!", (1, 2): "Hello World!", "key": [1, 2, 3]}
# first_object = example_dict[0]  # KeyError: 0
dict_length = len(example_dict)
print(dict_length)
dict_type = type(example_dict)
print(dict_type)
object_key = example_dict["key"]
print(object_key)
dict_keys = example_dict.keys()
print(dict_keys)
dict_values = example_dict.values()
print(dict_values)
dict_items = example_dict.items()
print(dict_items)
example_dict[2] = "Hello"
print(example_dict)
example_dict.update({1: "Goodbye"})
print(example_dict)
example_dict.pop(1)
print(example_dict)
example_dict.popitem()
print(example_dict)
del example_dict[2]
print(example_dict)
example_dict.clear()
print(example_dict)

"""
ZAD3
Zdefiniuj funkcję, która zamieni wartości Bool na 'Tak' lub 'Nie' (True='Tak', False='Nie').
Wykorzystaj w tym zadaniu własności słowników.
"""


def bool_to_string(boolean: bool) -> str:
    bool_dict = {True: "Tak", False: "Nie"}
    return bool_dict[boolean]


print(bool_to_string(True))
print(bool_to_string(False))

# operatory przynależności
example_list = [1, 2, 3]
example_set = {1, 2, 3}
example_tuple = (1, 2, 3)
example_string = "Hello World!"
example_dict = {1: 1, 2: 2, 3: 3}
print(1 in example_list)
print(1 in example_set)
print(1 in example_tuple)
print("Hello" in example_string)
print(1 in example_dict)

#  if else elif
age = 18
if age < 18:
    print("Niepełnoletni")
elif age == 18:
    print("Pełnoletni")
else:
    print("Dorosły")

#  match case
example_int = 1
match example_int:
    case 1:
        print("Jeden")
    case 2:
        print("Dwa")
    case _:
        print("Inna wartość")

"""
ZAD4
Zdefiniuj funkcję printującą informacje czy podany 
integer jest parzysty czy nieparzysty
"""


def even_odd(integer: int) -> None:
    match integer % 2:
        case 0:
            print("Parzysty")
        case 1:
            print("Nieparzysty")


# pętla for
example_list = [1, 2, 3]
for element in example_list:
    print(element)

example_tuple = (1, 2, 3)
for element in example_tuple:
    print(element)

example_dict = {1: 1, 2: 2, 3: 3}
for pair in example_dict:
    print(object)

# enumerate for

example_list = ['a', 'b', 'c']
for index, element in enumerate(example_list):
    print(index, element)
