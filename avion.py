from os import system

# lista = ['placeholder_0_position']

# lista.append(input())
# lista.append(input())
# lista.append(input())
# lista.append(input())
# lista.append(input())

system("clear")

stuff = """N-FBI1
9A-USKOK
I-NTERPOL
G-MI6
RF-KGB1
N321-CIA
F3-B12I
F-BI-12
OVO-JE-CIA
KRIJUMCAR1"""

lista = stuff.split()

for index, value in enumerate(lista):
    if 'FBI' in value:
        print(index + 1)

lista = stuff.split()

for value in lista:
    if 'CIA' not in lista:
        print("HE GOT AWAY!")
