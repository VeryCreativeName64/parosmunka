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

def egyesek_szama(jegyek):
    i=0
    egyes=0
    while(i<len(jegyek)):
        if(jegyek[i]==1):
            egyes+=1
        i+=1
    return egyes


