#  6
    # Demandez à l'utilisateur de saisir une chaine de caractères à l'écran, puis vous vérifierez si cette
    # chaine possède un @ et si cette chaine termine par .com, si c'est le cas, vous indiquerez que c'est
    # un email valide
mailAddr = input("Quelle est votre addresse mail ? : ")
if("@" in mailAddr and ".com" in mailAddr):
    print("Votre mail est valide.")
else:
    print("Erreur de mail")

#  7
    # Faire une boucle pour faire afficher 10 fois un message à l'écran
for i in range(1,11):
    print("Hello " + str(i))

#  8
    # Faire une boucle pour afficher les lettres d'un mot lettre par lettre.
wrd = input("Entrer un mot : ")
for i in wrd:
    print(i)

#  9
    # Initialisez deux entiers : a = 0 et b = 10.
    # Écrire une boucle affichant et incrémentant la valeur de a tant qu’elle reste inférieure
    # à celle de b.
a = 0
b = 10
while a < b:
    a += 1
print("a=" + str(a) + " , b=" + str(b))

#  10
    # Écrire une autre boucle décrémentant la valeur de b et affichant sa valeur si elle est
    # impaire. Boucler tant que b n’est pas nul.
b = 10
while b != 0:
    if(b%2 == 1):
        print(str(b))
    b -= 1
print("END, b=" + str(b))

#  11
    # Écrire une saisie filtrée d’un entier dans l’intervalle 1 à 10, bornes comprises. Affichez la saisie.
x = int(input("Entrer un entier entre 1 et 10: "))
while(x > 10 or x < 1):
    x = int(input("Refaite, ENTRE 1 ET 10: "))
print("Saisie accepte : " + str(x))

#  12
    # Affichez chaque caractère d’une chaîne en utilisant une boucle for.
    # Affichez chaque élément d’une liste en utilisant une boucle for.
myString = "Hello World"
myList = ["Hello World 1", "Hello World 2", "Hello World 3", "Hello World 4", "Hello World 5"]
for x in myString:
    print(x)
for i in myList:
    print(i)

#  13
    # Affichez les entiers de 0 à 15 non compris, de trois en trois, en utilisant une boucle for et
    # l’instruction range()
for i in range(0, 15, 3):
    print(i)

#  14
    # Utiliser une boucle while puis une boucle for pour afficher les n premiers nombres pairs.
x = 0
while(x < 20):
    for n in range(x,x+1):
        if(n%2 == 0):
            print(x)
    x+=1
