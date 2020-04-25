Euros = 0
AryAry = 0

def myFunc(myString):
    myValue = 0
    if("AE " in myString):
        Euros = 0.00024
        split_string = myString.split(" ", 1)
        myValue = float(split_string[1])
        myValue = str(myValue) + " AryAry = " + str(myValue * Euros) + " €"
    elif("EA " in myString):
        AryAry = 4114.54
        split_string = myString.split(" ", 1)
        myValue = float(split_string[1])
        myValue = str(myValue) + " € = " + str(myValue * AryAry) + " AryAry"
    else:
        print("Conversion impossible entrez une valeur valide : \nsens de conversion AE/EA + espace + la valeur a convertir")
    return(myValue)


print(myFunc("AE 15111431"))
print(myFunc("AE 15111.431"))
print(myFunc("EA 15111431"))
print(myFunc("EA 15111.431"))