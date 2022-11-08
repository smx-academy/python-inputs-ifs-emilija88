# Da se napravi programa vo koja korisnikot ke vnese godina na ragjanje, 
# ke se presmeta kolku godini e i 
# da se odredi dali e maloleten ili polnoleten

x=0
x=int(input("Vnesete godina na ragjanje"))
y=2022-x
print("Korisnikot ima {} godini.".format(y))
if y >= 18:
    print("Korisnikot e polnoleten.")
else:
    print("Korisnikot e maloleten i ne gi ispolnuva uslovite.")