import random
import os
from os import system

försök = 3
tal = random.randint(1,10)
system("clear")

for i in range(1,4):
    gissa = int(input("\nGissa ett heltal mellan 1-10 >> "))
    if gissa < tal:
        försök -= 1
        print(f"Du gissade för lågt! Du har {försök} antal försök kvar.\n")
        if försök == 0:
            print("Du förlorade\n")
            break
    elif gissa > tal:
        försök -= 1
        print(f"Du gissade för högt! Du har {försök} antal försök kvar.\n")
        if försök == 0:
            print("Du förlorade\n")
            break
    elif gissa > 10:
        print("över 10?.. Du kasta bort en av dina gissningar. Idiot.")
    else:
        print("Du gissade rätt!\n")
        break



