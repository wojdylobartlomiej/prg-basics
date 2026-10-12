kwota=float(input("Podaj kwote"))
znizka=float(input("Podaj znizka"))
znizka= znizka*0.01
znizka_c=kwota*znizka
nowa_cena=kwota-znizka_c
print("nowa cena", nowa_cena)
print("znizka", znizka_c)
# no i tu round