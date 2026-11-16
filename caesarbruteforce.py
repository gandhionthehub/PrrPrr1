from os import system 

alfabet = "abcdefghijklmnopqrstuvwxyzåäö"
meddelande = "khm"

system("clear")


def dekryptera(meddelande):
    for nyckel in range(0,len(alfabet)+1):
        print("\n")
        for bokstav in meddelande:
            if bokstav in alfabet:
                position = alfabet.index(bokstav)
                ny_position = (position - nyckel) % len(alfabet)
                ny_bokstav = alfabet[ny_position]
                print(ny_bokstav, end ="")
                print(f" {nyckel}")

dekryptera(meddelande)

    

