#  1 
    # Affectez les variables temps et distance par les valeurs 6.892 et 19.7.
    # Calculez et affichez la valeur de la vitesse.
    # Améliorez l’affichage en imposant un chiffre après le point décimal.
temps = 6.892
distance = 19.7
vitesse = distance / temps
print("Votre vitesse est de : " + str(round(vitesse,1)))

#  2
    # Saisir un nom et un âge en utilisant l’instruction input(). Les afficher.
    # Enfin, utilisez la « bonne pratique » : recommencez l’exercice en transtypant les saisies effectuées
    # pour les forcer à être du bon type (nom sera un str et age un entier)
nom = input("Quel est votre nom ? : ")
age = int(input("Quel est votre age ? : "))
print(nom + " , " + str(age))

#  3
    # Saisissez un flottant. S’il est positif ou nul, affichez sa racine, sinon affichez un message d’erreur.
from math import sqrt
myFloat = float(input("Entrez un float : "))
if(myFloat >= 0 ):
    print("OK, " + str(sqrt(myFloat)))
else:
    print("ERROR")

#  4 
    # L’ordre lexicographique est celui du dictionnaire.
    # Saisir deux mots, comparez-les pour trouver le « plus petit » et affichez le résultat
frstWord = input("Premier mot : ")
scndWord = input("Second mot : ")
if(frstWord < scndWord):
    print(frstWord)
else:
    print(scndWord)

#  5 
    # On désire sécuriser une enceinte pressurisée.
    # On se fixe une pression seuil et un volume seuil : pSeuil = 2.3, vSeuil = 7.41.
    # On demande de saisir la pression et le volume courant de l’enceinte et d’écrire un script qui simule
    # le comportement suivant :
    # – si le volume et la pression sont supérieurs aux seuils : arrêt immédiat ;
    # – si seule la pression est supérieure à la pression seuil : demander d’augmenter le volume de
    # l’enceinte ;
    # – si seul le volume est supérieur au volume seuil : demander de diminuer le volume
    # de l’enceinte ;
    # – sinon déclarer que « tout va bien ».
    # Ce comportement sera implémenté par une alternative multiple.
pSeuil = 2.3
vSeuil = 7.41
pression = int(input("Entrer pression : "))
volume = int(input("Entrer volume : "))

if(volume > vSeuil and pression > pSeuil):
    print("arrêt immédiat")
elif(pression > pSeuil):
    print("Augmenter le volume de l’enceinte")
elif(volume > vSeuil):
    print("Diminuer le volume de l’enceinte")
else:
    print("Tout va bien")