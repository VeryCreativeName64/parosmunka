
#2
def otosok_szama(jegyek):
    return jegyek.count(5)

#feladat 1
def atlag(jegyek):
    total=0
    i=0
    while(i<len(jegyek)):
        total+=jegyek[i]
        i+=1

    eredmeny=total/len(jegyek)
    
    return eredmeny
