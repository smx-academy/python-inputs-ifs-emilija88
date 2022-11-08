#Da se napravi programa vo koja korisnikot ke vnese 2 broevi i da se proveri dali zbirot e pomal od 100

zbir=0
x=int(input("Vnesete prv broj"))
y=int(input("Vnesete vtor broj"))
zbir=x+y
print("{} + {} = {}".format(x, y, zbir))
if zbir < 100:
    print("Zbirot na dvata broja sto gi vnesovte e pomal od 100.")
else:
    print("Zbirot na dvata broja koi gi vnesovte e pogolem od 100 i ne gi ispolnuva uslovite.")
