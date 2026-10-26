def miesiac(numer):
    if numer == 1:
        print(f"The name of Month {numer} is Jan")
    elif numer == 2:
        print(f"The name of Month {numer} is Feb")
    elif numer == 3:
        print(f"The name of Month {numer} is Mar")
    elif numer == 4:
        print(f"The name of Month {numer} is Apr")
    elif numer == 5:
        print(f"The name of Month {numer} is May")
    elif numer == 6:
        print(f"The name of Month {numer} is Jun")
    elif numer == 7:
        print(f"The name of Month {numer} is Jul")
    elif numer == 8:
        print(f"The name of Month {numer} is Aug")
    elif numer == 9:
        print(f"The name of Month {numer} is Sep")
    elif numer == 10:
        print(f"The name of Month {numer} is Oct")
    elif numer == 11:
        print(f"The name of Month {numer} is Nov")
    elif numer == 12:
        print(f"The name of Month {numer} is Dec")
    elif numer > 12 or numer < 1:
        print(f"The name of Month {numer} doesn't exist")

numer = int(input("Podaj numer: "))
miesiac(numer)