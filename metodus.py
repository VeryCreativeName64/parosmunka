

#feladat 1
def atlag(jegyek):
    total=0
    i=0
    while(i<len(jegyek)):
        total+=jegyek[i]
        i+=1

    eredmeny=total/len(jegyek)
    
    return eredmeny
