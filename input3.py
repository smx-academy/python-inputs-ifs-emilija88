# Da se napravi programa vo koja korisnikot ke vnese strani na dva pravoagolnici, 
# da se presmeta plostinata i 
# da se proveri koj pravoagolnik e pogolem


x = int(input("Vnesete ja prvata strana na pravoagolnikot"))
y = int(input("vnesete ja vtorata strana na pravoagolnikot"))
plostina1=x*y
print("Plostinata na dadenite strani za prviot pravoagolnik e {}cm".format(plostina1))
c = int(input("Vnesete ja prvata strana na pravoagolnikot"))
d = int(input("vnesete ja vtorata strana na pravoagolnikot"))
plostina2=c*d
print("Plostinata na dadenite strani za vtoriot pravoagolnik e {}cm.".format(plostina2))
if plostina1 < plostina2:
    print("Plostinata na prviot pravoagolnik e {}cm i e pomala od plostinata na vtoriot pravoagolnik koja e {}cm.".format(plostina1, plostina2))
else:
    print("Plostinata na prviot pravoagolnik e {}cm i e pogolema od plostinata na vtoriot pravagolnik koja e {}cm.".format(plostina2, plostina1))