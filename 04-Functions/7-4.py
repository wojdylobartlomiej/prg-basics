def licznik(a,b):
    liczba=0
    for char in a:
        if char == b:
        liczba = liczba +1
    print(f"Ta litera{b} pojawila sie {liczba} razy")

abe=str(input("napisz zdanie"))
lit=input("wybierz litere")
licznik(abe,lit)