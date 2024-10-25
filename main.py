import metodus
jegyek=[5,2,3,4,4,5,5,5,1,2,2,3,4,5,5,5,4,3,3]
diak_nevek = ["Anna", "Béla", "Cecil", "Dávid", "Erika", "Ferenc", "Gábor", "Hanna", "Ildikó", "János", "Katalin", "László", "Mária", "Nóra", "Olivér", "Péter", "Rita", "Sándor", "Tímea"]

#1 Bendegúz
e=metodus.atlag(jegyek)
print(f"Az osztályátlag:{e}")


#2-3 Bendegúz-Dominik
db=metodus.osztalyzatok_szama(jegyek,5)
print(f"Az osztályzatok száma: {db}")
"""
#3
e=metodus.egyesek_szama(jegyek)
print(f"{e} darab diák bukott meg.")
"""
#4 Dominik
diak_szama=metodus.elegtelen(jegyek)
print(f"Az elégtelent kapott diákok száma: {diak_szama}")

#5 Bendegúz
metodus.sávdiagram(jegyek)

#6 Dominik
metodus.diak_jegyek(jegyek, diak_nevek)

#7 Bendegúz-Dominik
diakszamok=metodus.diak_jegyek_generalasa(17)
print(f"Diákok véletlen jegyei:{diakszamok}")

