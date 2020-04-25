#  15
    # définir la liste : liste =[17, 38, 10, 25, 72], puis effectuez les actions suivantes :
    # – triez et affichez la liste ;
    # – ajoutez l’élément 12 à la liste et affichez la liste ;
    # – renversez et affichez la liste ;
    # – affichez l’indice de l’élément 17 ;
    # – enlevez l’élément 38 et affichez la liste ;
    # – affichez la sous-liste du 2e au 3e élément ;
    # – affichez la sous-liste du début au 2e élément ;
    # – affichez la sous-liste du 3e élément à la fin de la liste ;
    # – affichez la sous-liste complète de la liste ;
maListe =[17, 38, 10, 25, 72]
maListe.sort(reverse=True)
print(maListe)
maListe.append(12)
print(maListe)
maListe.sort(reverse=False)
print(maListe)
print("INDEX de 17=" + str(maListe.index(17))) 
maListe.remove(38)
print(maListe)
print(maListe[2:3])
print(maListe[3:])
print(maListe)

#  16
    # Ecrire l’inverse d’une chaine.
wrd = "Hello World"
listWrd = []
tailleWrd = len(wrd)
newWrd = ""
for i in wrd:
    listWrd.append(i)
for x in range(1,tailleWrd + 1):
    newWrd += listWrd[tailleWrd-x]
print(newWrd)

easyWay = "Hello World"[::-1]
print(easyWay)

#  17
    # Verifier si une chaine est un palindrome.
myWord = input("Entrer un mot pour voir si c'est un palindrome : ")
myWordReversed = myWord[::-1]
if(myWord == myWordReversed):
    print("C'est un palindrome")
else:
    print("Ce n'est pas un palindrome")

#  18
    # Verifier si une chaine est un email en regardant la présence de @ et de . puis de max 3 caractères
    # après le .
mailAddr = input("Quelle est votre addresse mail ? : ")
myLen = len(mailAddr)
myDot = mailAddr.rfind('.') + 1
# mailAddr.index(lastDot) + 1 -- Mais peut pas mettre plus d'un point
ending = myLen - myDot
if("@" in mailAddr and "." in mailAddr and ending <= 3):
    print("Votre mail est valide.")
elif(ending > 3):
    print("La fin du mail est plus grand que 3.(ex: .fr .com .de ...)")
elif("@" not in mailAddr):
    print("Pas de @ dans votre mail.")
else:
    print("Pas de . dans votre mail.")

#  19
    # Initialisez truc comme une liste vide, et machin comme une liste de cinq flottants nuls. Affichez ces listes.
truc = []
machin = [i+0.0 for i in range(0,5)]
print(machin + truc)

#  20
    # Utilisez la fonction range() pour afficher :
    # – les entiers de 0 à 3 ;
    # – les entiers de 4 à 7 ;
    # – les entiers de 2 à 8 par pas de 2.
    # Définir chose comme une liste des entiers de 0 à 5 et testez l’appartenance des éléments 3 et 6 à chose.

for i in range(0,4):
    print(i)
for i in range(4,8):
    print(i)
for i in range(2,9,2):
    print(i)

chose = [i+0 for i in range(0,6)]

if(3 in chose):
    print("3 Appatient à chose")
else:
    print("3 N'appatient pas à chose")

if(6 in chose):
    print("6 Appatient à chose")
else:
    print("6 N'appatient pas à chose")