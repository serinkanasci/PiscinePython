from pathlib import Path

myPath = input("Where is your file ? ")
my_file = Path(myPath)

if my_file.is_file():
    myList = []
    f = open(myPath,'r')
    for line in f:
        myList.append(line.strip())

    for x in myList:
        myValue = x.split("\\t",2)
        myFirstValue = myValue[1]
        mySecndValue = (myValue[2].split("\\n",1))[0]
        testFValue = (myFirstValue.split("cm",1))[0]
        testSValue = (mySecndValue.split("cm",1))[0]
        if(testFValue > testSValue):
            print( x + "  -  OUI")
        else:
            print( x + "  -  NON")
else:
    print("fichier non trouvé")

# Episode 6/myFile.txt