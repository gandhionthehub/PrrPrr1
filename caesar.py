from os import system 

alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
meddelande = input("Skriv det som du vill kryptera: ")
nyckel = 1

system("clear")

def kryptera(text):
    for bokstav in text:
        if bokstav in alfabet:
            position = alfabet.index(bokstav)
            ny_position = (position + nyckel) % len(alfabet)
            ny_bokstav = alfabet[ny_position]
            print(ny_bokstav, end ="")

kryptera(meddelande)
