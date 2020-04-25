import hashlib
import xlrd
import string
import random
# from collections import deque


alphabet = list(string.ascii_letters)

loc = ("Decrypt/Liste_Atrouver.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

cryptedPasswords = []
noms = []
prenoms = []

def rotate(l, n):
    return l[n:] + l[:n]

for i in range(sheet.nrows):
    if(sheet.cell_value(i, 2) == ''):
        pass
    else:
        cryptedPasswords.append(sheet.cell_value(i, 2))

for y in range(sheet.nrows):
    if(sheet.cell_value(y, 1) == 'Nom'):
        pass
    else:
        noms.append(sheet.cell_value(y, 1))

for z in range(sheet.nrows):
    if(sheet.cell_value(z, 0) == 'Prénom'):
        pass
    else:
        prenoms.append(sheet.cell_value(z, 0))

f = open("Decrypt/dico_animaux.txt", mode="r",encoding="utf-8")
animals = []
for i in f:
    if("\ufeff" in i):
        an = i.split('\ufeff')
        animal = an[1].split('\n')
    else:
        animal = i.split('\n')
    animals.append(animal[0])

f.close()

def testConcatNumName(myNames,myAnimals,myCryptedPasswords):
    answers = open("Decrypt/passwords.txt", mode="a",encoding="utf-8")
    decryptedPasswords = []
    for ps in myCryptedPasswords:
        inPass = myCryptedPasswords.index(ps)
        for name in myNames:
            for an in myAnimals:
                tot = name + an
                totLen = len(tot)
                cmpt = 0
                cmptName = 0
                cmptAn = 0
                testing = ""
                while cmpt != totLen:
                    if(cmpt%2 == 0):
                        try:
                            testing += name[cmptName]
                            cmptName += 1
                        except IndexError:
                            cmptName += 1
                    else:
                        try:
                            testing += an[cmptAn]
                            cmptAn += 1
                        except IndexError:
                            cmptAn += 1
                    cmpt += 1                
                result = hashlib.md5(testing.encode())
                if(ps == result.hexdigest()):
                    finalRes = myNames[inPass] + " : " + testing + " password=" + ps
                    decryptedPasswords.append(finalRes)
                    answers.write(finalRes + "\n")
    answers.close()
    return decryptedPasswords

# testing = myPrenoms[inName][0].upper(); inName = myNames.index(name)
    
def testConcatAnimals(myNames,myAnimals,myCryptedPasswords):
    answers = open("Decrypt/passwords.txt", mode="a",encoding="utf-8")
    decryptedPasswords = []
    for ps in myCryptedPasswords:
        inPass = myCryptedPasswords.index(ps)
        for an in myAnimals:
            for sec_an in myAnimals:
                testing = an + sec_an
                result = hashlib.md5(testing.encode())
                if(ps == result.hexdigest()):
                    finalRes = myNames[inPass] + " : " + testing + " password=" + ps
                    decryptedPasswords.append(finalRes)
                    answers.write(finalRes + "\n")
    answers.close()
    return decryptedPasswords

def testAnimals(myNames,myAnimals,myCryptedPasswords):
    answers = open("Decrypt/passwords.txt", mode="a",encoding="utf-8")
    decryptedPasswords = []
    for ps in myCryptedPasswords:
        inPass = myCryptedPasswords.index(ps)
        for an in myAnimals:
            testing = an
            result = hashlib.md5(testing.encode())
            if(ps == result.hexdigest()):
                finalRes = myNames[inPass] + " : " + testing + " password=" + ps
                decryptedPasswords.append(finalRes)
                answers.write(finalRes + "\n")
    answers.close()
    return decryptedPasswords

def testAnimalsDouble(myNames,myAnimals,myCryptedPasswords):
    answers = open("Decrypt/passwords.txt", mode="a",encoding="utf-8")
    decryptedPasswords = []
    for ps in myCryptedPasswords:
        inPass = myCryptedPasswords.index(ps)
        for an in myAnimals:
            testing = an[::-1] + an
            result = hashlib.md5(testing.encode())
            if(ps == result.hexdigest()):
                finalRes = myNames[inPass] + " : " + testing + " password=" + ps
                decryptedPasswords.append(finalRes)
                answers.write(finalRes + "\n")
    answers.close()
    return decryptedPasswords

def testChanging(myNames,myAnimals,myCryptedPasswords):
    answers = open("Decrypt/passwords.txt", mode="a",encoding="utf-8")
    decryptedPasswords = []
    for ps in myCryptedPasswords:
        inPass = myCryptedPasswords.index(ps)
        for an in myAnimals:
            testing = an.upper()
            minTest=""
            maxTest=""
            cmpt = 0
            for s in testing:
                if(cmpt%2 == 0):
                    minTest += s.upper()
                    maxTest += s.lower()
                else:
                    minTest += s.lower()
                    maxTest += s.upper()
                cmpt += 1
            result = hashlib.md5(minTest.encode())
            otherResult = hashlib.md5(maxTest.encode())
            if(ps == result.hexdigest()):
                finalRes = myNames[inPass] + " : " + minTest + " password=" + ps
                decryptedPasswords.append(finalRes)
                answers.write(finalRes + "\n")
            if(ps == otherResult.hexdigest()):
                finalRes = myNames[inPass] + " : " + maxTest + " password=" + ps
                decryptedPasswords.append(finalRes)
                answers.write(finalRes + "\n")

    answers.close()
    return decryptedPasswords


def testDate(myNames,myCryptedPasswords):
    answers = open("Decrypt/passwords.txt", mode="a",encoding="utf-8")
    decryptedPasswords = []
    days = [x + 1 for x in range(1,32)]
    months = [x + 1 for x in range(1,13)]
    years = [x + 1 for x in range(1900,2021)]
    for ps in myCryptedPasswords:
        inPass = myCryptedPasswords.index(ps)
        for y in years:
            for m in months:
                for d in days:
                    testing = str(d) +"/"+ str(m) +"/"+ str(y)
                    result = hashlib.md5(testing.encode())
                    if(ps == result.hexdigest()):
                        finalRes = myNames[inPass] + " : " + testing + " password=" + ps
                        decryptedPasswords.append(finalRes)
                        answers.write(finalRes + "\n")
    answers.close()
    return decryptedPasswords

def testBirthday(myNames,myPrenoms,myCryptedPasswords, myAlphabet):
    answers = open("Decrypt/passwords.txt", mode="a",encoding="utf-8")
    birthYears = [x + 1 for x in range(1900,2020)]
    decryptedPasswords = []
    for ps in myCryptedPasswords:
        inPass = myCryptedPasswords.index(ps)
        for let in myAlphabet:
            for yer in birthYears:
                for na in myNames:
                    testing = let + na + str(yer)
                    result = hashlib.md5(testing.encode())
                    if(ps == result.hexdigest()):
                        finalRes = myNames[inPass] + " : " + testing + " password=" + ps
                        decryptedPasswords.append(finalRes)
                        answers.write(finalRes + "\n")
                for pr in myPrenoms:
                    testing = let + pr + str(yer)
                    result = hashlib.md5(testing.encode())
                    if(ps == result.hexdigest()):
                        finalRes = myNames[inPass] + " : " + testing + " password=" + ps
                        decryptedPasswords.append(finalRes)
                        answers.write(finalRes + "\n")
    answers.close()
    return decryptedPasswords


def testMultiple(myNames,myPrenoms,myCryptedPasswords):
    answers = open("Decrypt/passwords.txt", mode="a",encoding="utf-8")
    decryptedPasswords = []
    myNumbers = [a + 1 for a in range(0,3500)]
    for ps in myCryptedPasswords:
        inPass = myCryptedPasswords.index(ps)
        for nb in myNumbers:
            for pr in myPrenoms:
                testing = pr.lower() + str(nb)
                result = hashlib.md5(testing.encode())
                if(ps == result.hexdigest()):
                    finalRes = myNames[inPass] + " : " + testing + " password=" + ps
                    decryptedPasswords.append(finalRes)
                    answers.write(finalRes + "\n")
    answers.close()
    return decryptedPasswords

def testVoyelle(myNames,myPrenoms,myCryptedPasswords):
    answers = open("Decrypt/passwords.txt", mode="a",encoding="utf-8")
    voyelle = ["a", "e", "i", "o", "u", "y"]
    myNumbers = [a + 1 for a in range(0,9)]
    decryptedPasswords = []
    for ps in myCryptedPasswords:
        inPass = myCryptedPasswords.index(ps)
        for name in myPrenoms:
            name = name.lower()
            for y in voyelle:
                for nb in myNumbers:
                    name = name.replace(y, str(nb))
                    testing = name
                    y = str(nb)
                    result = hashlib.md5(testing.encode())
                    if(ps == result.hexdigest()):
                        finalRes = myNames[inPass] + " : " + testing + " password=" + ps
                        decryptedPasswords.append(finalRes)
                        answers.write(finalRes + "\n")      
    answers.close()
    return decryptedPasswords

def testConcatAnimalsName(myAnimals,myNames,myPrenoms,myCryptedPasswords):
    answers = open("Decrypt/passwords.txt", mode="a",encoding="utf-8")
    decryptedPasswords = []
    for ps in myCryptedPasswords:
        inPass = myCryptedPasswords.index(ps)
        for an in myAnimals:
            for nom in myNames:
                testing = nom.lower() + an.upper()
                minTest=""
                cmpt = 0
                for s in testing:
                    if(cmpt%2 == 0):
                        minTest += s.upper()
                    else:
                        minTest += s.lower()
                    cmpt += 1
                result = hashlib.md5(minTest.encode())
                otherResult = hashlib.md5(testing.encode())
                if(ps == result.hexdigest()):
                    finalRes = minTest + " password=" + ps
                    decryptedPasswords.append(finalRes)
                    answers.write(finalRes + "\n")
                elif(ps == otherResult.hexdigest()):
                    finalRes = myNames[inPass] + " : " + testing + " password=" + ps
                    decryptedPasswords.append(finalRes)
                    answers.write(finalRes + "\n")
            for pr in myPrenoms:
                testing = pr.lower() + an.upper()
                minTest=""
                cmpt = 0
                for s in testing:
                    if(cmpt%2 == 0):
                        minTest += s.upper()
                    else:
                        minTest += s.lower()
                    cmpt += 1
                result = hashlib.md5(minTest.encode())
                otherResult = hashlib.md5(testing.encode())
                if(ps == result.hexdigest()):
                    finalRes = minTest + " password=" + ps
                    decryptedPasswords.append(finalRes)
                    answers.write(finalRes + "\n")
                elif(ps == otherResult.hexdigest()):
                    finalRes = myNames[inPass] + " : " + testing + " password=" + ps
                    decryptedPasswords.append(finalRes)
                    answers.write(finalRes + "\n")
    answers.close()
    return decryptedPasswords


def testReverse(myNames,myPrenoms,myCryptedPasswords):
    answers = open("Decrypt/passwords.txt", mode="a",encoding="utf-8")
    decryptedPasswords = []
    for ps in myCryptedPasswords:
        inPass = myCryptedPasswords.index(ps)
        for wrd in myPrenoms:
            testing = wrd[::-1].lower()
            result = hashlib.md5(testing.encode())
            if(ps == result.hexdigest()):
                finalRes = myNames[inPass] + " : " + testing + " password=" + ps
                decryptedPasswords.append(finalRes)
                answers.write(finalRes + "\n")
    answers.close()
    return decryptedPasswords

def testReversePlus(myPrenoms,myNames,myCryptedPasswords):
    answers = open("Decrypt/passwords.txt", mode="a",encoding="utf-8")
    voyelle = ["A", "E", "I", "O", "U", "Y","a", "e", "i", "o", "u", "y"]
    decryptedPasswords = []
    for ps in myCryptedPasswords:
        inPass = myCryptedPasswords.index(ps)
        for wrd in myNames:
            for pre in myPrenoms:
                for voy in voyelle:
                    while(voy in wrd or voy in pre):
                        wrd = wrd.replace(voy,"")
                        pre = pre.replace(voy,"")

                    testing = wrd + pre
                    print(testing)
                    result = hashlib.md5(testing.encode())
                    if(ps == result.hexdigest()):
                        finalRes = myNames[inPass] + " : " + testing + " password=" + ps
                        decryptedPasswords.append(finalRes)
                        answers.write(finalRes + "\n")
                
    answers.close()
    return decryptedPasswords

def testNameDouble(myNames,myAlphabet,myCryptedPasswords):
    answers = open("Decrypt/passwords.txt", mode="a",encoding="utf-8")
    decryptedPasswords = []
    for ps in myCryptedPasswords:
        inPass = myCryptedPasswords.index(ps)
        for let in myAlphabet:
            for let2 in myAlphabet:
                for let3 in myAlphabet:
                    for let4 in myAlphabet:
                        for let5 in myAlphabet:
                            for let6 in myAlphabet:
                                testing = let + let2 + let3 + let4 + let5 + let6
                                # print(testing)
                                result = hashlib.md5(testing.encode())
                                if(ps == result.hexdigest()):
                                    finalRes = myNames[inPass] + " : " + testing + " password=" + ps
                                    decryptedPasswords.append(finalRes)
                                    answers.write(finalRes + "\n")
    answers.close()
    return decryptedPasswords


def testVoyellePrenom(myPrenoms,myNames,myCryptedPasswords):
    answers = open("Decrypt/passwords.txt", mode="a",encoding="utf-8")
    voyelle = ["A", "E", "I", "O", "U", "Y"]
    decryptedPasswords = []
    for ps in myCryptedPasswords:
        inPass = myCryptedPasswords.index(ps)
        myNumbers = [a + 1 for a in range(-1,9)]
        myNumbers.reverse()
        for pre in myPrenoms:
            pre = pre.upper()
            myNumbers = rotate(myNumbers,1)
            for x in pre:
                if(x in voyelle):
                    for nb in myNumbers:
                        pre = pre.replace(x,str(nb))
                        x = str(nb)
                        testing = pre
                        print(testing)
                        result = hashlib.md5(testing.encode())
                        if(ps == result.hexdigest()):
                            finalRes = myNames[inPass] + " : " + testing + " password=" + ps
                            decryptedPasswords.append(finalRes)
                            answers.write(finalRes + "\n")
                        
                
    answers.close()
    return decryptedPasswords

# name = name.lower()
#             cmptVoy = []
#             counter = 0
#             for x in voyelle:
#                 if(x in name):
#                     cmptVoy.append(x)
#                     counter += 1
#                 else:
#                     pass
#             cmp = 0
#             cmpVoyUse = 0
#             cmptVoy = cmptVoy*(counter**9)
#             for y in cmptVoy:
#                 p = y
#                 for nb in myNumbers:
#                     testing = name.replace(str(p), str(nb))
#                     p = str(nb)
#                     print(testing)
#                     result = hashlib.md5(testing.encode())
#                     if(ps == result.hexdigest()):
#                         finalRes = myNames[inPass] + " : " + testing + " password=" + ps
#                         decryptedPasswords.append(finalRes)
#                         answers.write(finalRes + "\n")
#                     cmp += 1
#                     if(cmp % 9 == 0):
#                         name = name.replace(str(p), str(cmpVoyUse))
#                         p = str(cmpVoyUse)
#                         cmpVoyUse += 1
#                         if(cmpVoyUse % counter == 0):
#                             name = name.replace(str(p), str(cmpVoyUse)) 


def testAnimalsCapitalize(myNames,myAnimals,myCryptedPasswords):
    answers = open("Decrypt/passwords.txt", mode="a",encoding="utf-8")
    decryptedPasswords = []
    for ps in myCryptedPasswords:
        inPass = myCryptedPasswords.index(ps)
        for an in myAnimals:
            testing = an.capitalize()
            result = hashlib.md5(testing.encode())
            if(ps == result.hexdigest()):
                finalRes = myNames[inPass] + " : " + testing + " password=" + ps
                decryptedPasswords.append(finalRes)
                answers.write(finalRes + "\n")
    answers.close()
    return decryptedPasswords

def testNames(myNames,myPrenoms,myCryptedPasswords):
    answers = open("Decrypt/passwords.txt", mode="a",encoding="utf-8")
    voyelle = ["A", "E", "I", "O", "U", "Y","a","e","i","o","u","y"]
    decryptedPasswords = []
    for ps in myCryptedPasswords:
        inPass = myCryptedPasswords.index(ps)
        for pre in myPrenoms:
            inPre = myPrenoms.index(pre)
            # pre =  pre.lower() + myNames[inPre].lower()
            # pre =  pre.lower() + myNames[inPre].upper()
            # pre =  pre.upper() + myNames[inPre].lower()
                        
            # pre = myNames[inPre].lower() + pre.lower()
            # pre = myNames[inPre].upper() + pre.lower()
            # pre = myNames[inPre].lower() + pre.upper()
            pre = myNames[inPre].upper() + pre.upper()
            for x in pre:
                if(x in voyelle):
                    pre = pre.replace(x,'')
                else:
                    pass
                testing = pre
                print(testing)
                result = hashlib.md5(testing.encode())
                if(ps == result.hexdigest()):
                    finalRes = myNames[inPass] + " : " + testing + " password=" + ps
                    decryptedPasswords.append(finalRes)
                    answers.write(finalRes + "\n")
                        
                
    answers.close()
    return decryptedPasswords

# Fonctionnel:
# print(testChanging(noms,animals,cryptedPasswords))
# print(testAnimals(noms,animals,cryptedPasswords))
# print(testConcatAnimals(noms,animals,cryptedPasswords))
# print(testAnimalsDouble(noms,animals,cryptedPasswords))
# print(testAnimalsCapitalize(noms,animals,cryptedPasswords))
# print(testMultiple(noms,prenoms,cryptedPasswords))
# print(testBirthday(noms,prenoms,cryptedPasswords,alphabet))
# print(testReverse(noms,prenoms,cryptedPasswords))
# print(testVoyelle(noms,prenoms,cryptedPasswords))


# print(testNames(noms,prenoms,cryptedPasswords))

# print(testReversePlus(prenoms,noms,cryptedPasswords))

# print(testNameDouble(noms,alphabet,cryptedPasswords))

print(testVoyellePrenom(prenoms,noms,cryptedPasswords))

# Non fonctionnel:

# Sans resultat :
# print(testConcatNumName(noms,animals,cryptedPasswords))
# print(testDate(cryptedPasswords))
# print(testConcatAnimalsName(animals,noms,prenoms,cryptedPasswords))

# tigreescargot testConcatAnimals
# porcblaireau testConcatAnimals
# raugajjaguar testAnimalsDouble
# WPoutine1952 testBirthday
# adams3103 testMultiple
# sarah1978 testMultiple
# chacal testAnimals
# chat testAnimals
# ToRtUe testChanging


# Pas fini :
# D'autres aiment les animaux et ont dérivés leurs mots de passe de ceux-ci.
# Certains changent toutes les voyelles par un nombre et mettent le tout en majuscules

# Fini :
# d'autres ont rajoutés des nombres devant ou derrière (max 3), et mis la première lettre ou pas en majuscule.
# prénom ou nom,nombres rajoutés (maximum 4). Par exemple, mettre une lettre devant son nom, avant de rajouter à la fin son année de naissance.
# Certains prennent le nom d'un animal, l'ont mis à l'envers, et l'ont dédoublé.
# Certains seulement concaténent 2 animaux...


