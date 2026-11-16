#from time import sleep
import time
import random

max = 10000

Key = random.randint(0,max)
start = 0

def BF():
    global start, key
    start_tid = time.time()
    for number in range(0,max):
        if number != Key:
            start += 1
            print(start)
        else:
            print(f"\n{start} är lösenordet!")
            break
    tid = time.time() - start_tid
    print(f"Klart på {tid:.6f} sekunder.")

BF()

