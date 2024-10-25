#feladat 1
def atlag(jegyek):
    total=0
    i=0
    while(i<len(jegyek)):
        total+=jegyek[i]
        i+=1

    eredmeny=total/len(jegyek)
    
    return eredmeny

#2
def otosok_szama(jegyek):
    i=0
    otos=0
    while(i<len(jegyek)):
        if(jegyek[i]==5):
            otos+=1
        i+=1
    return otos
#3
def egyesek_szama(jegyek):
    i=0
    egyes=0
    while(i<len(jegyek)):
        if(jegyek[i]==1):
            egyes+=1
        i+=1
    return egyes

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
    szamok = [0] * 5 
    i = 0

    while i < len(jegyek):
        jegy = jegyek[i]
        if 1 <= jegy <= 5:
            szamok[jegy - 1] += 1
        i += 1

    print("Sávdiagram:")
    i = 0
    while i < 5:
        print(f"{i + 1}| {'*' * szamok[i]}")
        i += 1

#6
def diak_jegyek(jegyek, diak_nevek):
    """Megjeleníti a diákok jegyeit látványos formában."""
    i = 0
    print("Diákok jegyei:")
    while i < len(jegyek):
        print(f"{i + 1}. diák: {diak_nevek[i]}: {jegyek[i]}")
        i += 1

#7
import random
def diak_jegyek_generalasa(szam):
    """Véletlen diák jegyek generálása."""
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

