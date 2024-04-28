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
