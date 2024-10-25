import metodus
jegyek=[5,2,3,4,4,5,5,5,1,2,2,3,4,5,5,5,4,3,3]
diak_nevek = ["Anna", "Béla", "Cecil", "Dávid", "Erika", "Ferenc", "Gábor", "Hanna", "Ildikó", "János", "Katalin", "László", "Mária", "Nóra", "Olivér", "Péter", "Rita", "Sándor", "Tímea"]

#1
e=metodus.atlag(jegyek)
print(f"Az osztályátlag:{e}")


#2
e=metodus.otosok_szama(jegyek)
print(f"Az ötösök száma: {e}")

#3
e=metodus.egyesek_szama(jegyek)
print(f"{e} darab diák bukott meg.")

#4
diak_szama=metodus.elegtelen(jegyek)
print(f"Az elégtelent kapott diákok száma: {diak_szama}")

#5
metodus.sávdiagram(jegyek)

#6
metodus.diak_jegyek(jegyek, diak_nevek)

#7
diakszamok=metodus.diak_jegyek_generalasa(17,tobb_5_os=False)
print(f"Diákok véletlen jegyei:{diakszamok}")
