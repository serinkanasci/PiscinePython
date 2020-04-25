# Réalise un programme en Python qui créé une variable qui soit une collection dans laquelle on trouve 
# des chaînes comme les suivantes :
# \b\t80cm\t60cm\n
# \b\t81cm\t51cm\n
# \b\t105cm\t145cm\n
# On parcourera cette collection, en n'affichant que la première valeur de chaque ligne que si celle ci est plus petite 
# que la deuxième.

myList = ["\b\t80cm\t60cm\n","\b\t81cm\t51cm\n","\b\t105cm\t145cm\n"]

for x in myList:
    myValue = x.split("\t",2)
    myFirstValue = myValue[1]
    mySecndValue = (myValue[2].split("\n",1))[0]

    testFValue = (myFirstValue.split("cm",1))[0]
    testSValue = (mySecndValue.split("cm",1))[0]
    if(testFValue > testSValue):
        print(myFirstValue)
    else:
        pass