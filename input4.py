# Da se napravi programa vo koja korisnikot ke vnese goleminite na aglite na triagolnici, 
# i da se proveri dali so tie golemini moze da se kreira triagolnik(zbirot treba da bide 180)

zbir=0
for i in range(3):
    x = int(input("Vnesete eden agol na triagolnikot"))
    zbir+=x
if zbir==180:
    print("Zbirot na dadenite agli e {} i moze da se kreira triagolnik.".format(zbir))
else:
    print("Zbirot na dadenite agli e {} i ne gi ispolnuva uslovite da kreirate triagolnik.".format(zbir))
