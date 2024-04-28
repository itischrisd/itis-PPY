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
