#  21
    # Ecrire du code qui demande à l'utilisateur un nombre appelé x, le programme demandera alors x
    # chaines de caractères que le programme enregistrera dans un fichier de nom data.txt (une chaine
    # par ligne)
# x = int(input("Entrer x: "))
# l = []
# for i in range(0,x):
#     l.append(input("Entrer chaine de charactere " + str(i) + " :"))

# f = open("data.txt", mode="a")

# for y in l:
#     f.write(y + '\n')

# f.close()

#  22
    # Ecrire du code qui lit le contenu du fichier data.txt et vérifie pour chaque ligne si c'est un email
    # (présence de @ et de .com à la fin)
# f = open("data.txt", mode="r")

# for i in f:
#     if("@" in i and ".com" in i):
#         print("C'est un mail : " + i)

# f.close()

#  23
    # Ecrire une fonction compterMots ayant un argument (une chaîne de caractères) et qui renvoie un
    # dictionnaire qui contient la fréquence de tous les mots de la chaîne entrée.
def compterMots(myChar):
    
#  24
    # Écrire une fonction volumeSphere qui calcule le volume d’une sphère de rayon r fourni en
    # argument et qui utilise la fonction cube.
    # Tester la fonction volumeSphere par un appel dans le programme principal.
#  25
    # Écrire une autre fonction somme avec trois arguments, et qui renvoie leur somme.
    # Dans le programme principal, définir un tuple de trois nombres, puis utilisez la syntaxe d’appel à la
    # fonction qui décompresse le tuple. Affichez le résultat.
