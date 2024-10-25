
#feladat 1
def atlag(jegyek):
    total=0
    i=0
    while(i<len(jegyek)):
        total+=jegyek[i]
        i+=1

    eredmeny=total/len(jegyek)
    
    return eredmeny
"""
#2
def otosok_szama(jegyek):
    i=0
    otos=0
    egyes=0
    while(i<len(jegyek)):
        if(jegyek[i]==5):
            otos+=1
        elif(jegyek[i]==1):
            egyes+=1
        i+=1
    print(f"Egyesek száma:{egyes}")
    print(f"Ötösök száma:{otos}")

"""
#2-3
def osztalyzatok_szama(jegyek,szam):
    i=0
    db=0
    while(i<len(jegyek)):
        if(jegyek[i]==szam):
            db+=1
        i+=1
    return db

#4
def elegtelen(jegyek):
    diak_szama=0
    i=0
    while (i<len(jegyek)):
        if jegyek[i]==1:
            diak_szama+=1
        i+=1
    return diak_szama

#5
def sávdiagram(jegyek):
    szamok = [0,0,0,0,0] 
    i = 0

    while i < len(jegyek):
        jegy = jegyek[i]
        szamok[jegy - 1] += 1
        i += 1

    print("Sávdiagram:")
    i = 0
    while i < 5:
        print(f"{i + 1}| {'*' * szamok[i]}")
        i += 1

#6
def diak_jegyek(jegyek, diak_nevek):
    i = 0
    print("Diákok jegyei:")
    while i < len(jegyek):
        print(f"{i + 1}. diák: {diak_nevek[i]}: {jegyek[i]}")
        i += 1

#7
import random
def diak_jegyek_generalasa(szam):
    
    diakszamok = []
    i = 0
    while(i < szam):
        generalt_szam=random.randint(1,6)
        if generalt_szam==6:
            diakszamok.append(5)
        else:
            diakszamok.append(generalt_szam)
        i+=1
    return diakszamok

