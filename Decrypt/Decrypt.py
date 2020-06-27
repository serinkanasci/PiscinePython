import hashlib
import xlrd
import string
import random
import itertools

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

def permute_single_index(word, index):
    permutations = []
    word_left = word[0:index]
    word_right = word[index+1:]
    for i in reversed(range(10)):
        permutations.append(f"{word_left}{i}{word_right}")
    return permutations


def permuteVoyellePrenomUp(pre):
    voyelle = ["A", "E", "I", "O", "U", "Y"]
    upper_pre = pre.upper()
    replace_indexes = [i for i, x in enumerate(upper_pre) if x in voyelle]

    permutations = [upper_pre]

    for ri in replace_indexes:
        new_permutations = []
        for word in permutations:
            new_permutations += permute_single_index(word, ri)
        permutations += new_permutations

    return permutations

def permuteVoyellePrenomLow(pre):
    voyelle = ["a", "e", "i", "o", "u", "y"]
    upper_pre = pre.lower()
    replace_indexes = [i for i, x in enumerate(upper_pre) if x in voyelle]

    permutations = [upper_pre]

    for ri in replace_indexes:
        new_permutations = []
        for word in permutations:
            new_permutations += permute_single_index(word, ri)
        permutations += new_permutations

    return permutations

def testVoyellePrenomUp(myPrenoms,myNames,myCryptedPasswords):
    answers = open("Decrypt/passwords.txt", mode="a",encoding="utf-8")
    decryptedPasswords = []
    for ps in myCryptedPasswords:
        inPass = myCryptedPasswords.index(ps)
        for pre in myPrenoms:
            pre = permuteVoyellePrenomUp(pre)
            for testing in pre:        
                result = hashlib.md5(testing.encode())
                if(ps == result.hexdigest()):
                    finalRes = myNames[inPass] + " : " + testing + " password=" + ps
                    decryptedPasswords.append(finalRes)
                    answers.write(finalRes + "\n")
                            
    answers.close()
    return decryptedPasswords

def testVoyellePrenomLow(myPrenoms,myNames,myCryptedPasswords):
    answers = open("Decrypt/passwords.txt", mode="a",encoding="utf-8")
    decryptedPasswords = []
    for ps in myCryptedPasswords:
        inPass = myCryptedPasswords.index(ps)
        for pre in myPrenoms:
            pre = permuteVoyellePrenomLow(pre)
            for testing in pre:        
                result = hashlib.md5(testing.encode())
                if(ps == result.hexdigest()):
                    finalRes = myNames[inPass] + " : " + testing + " password=" + ps
                    decryptedPasswords.append(finalRes)
                    answers.write(finalRes + "\n")
                            
    answers.close()
    return decryptedPasswords

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
# print(testVoyellePrenomUp(prenoms,noms,cryptedPasswords))
# print(testVoyellePrenomLow(prenoms,noms,cryptedPasswords))

# Sans resultat :
# print(testDate(cryptedPasswords))