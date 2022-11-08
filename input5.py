# Da se napravi programa vo koja korisnikot ke vnese nekoe ime i 
# da se proveri sekoja samoglaska kolku pati se pojavuva vo imeto
# i od kolku karakteri e sostaveno toa ime

vowels = 'aeiou'
x = input("Vnesete go vasheto ime")
count = {}.fromkeys(vowels, 0)
	
for character in x:
	if character in count:
		count[character] += 1
character = (len(x))
print(count)
print("Vasheto ime e sostaveno od {} karakteri.".format(character))
