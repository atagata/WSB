integer = int(input("Podaj liczbę: "))

def courzon(integer):
    y = 2**integer + 1
    z = 2*integer +1
    if y % z == 0:
        print(f"Liczba {integer} jest liczbą Courzona!")
    else:
        print(f"Liczba {integer} nie jest liczbą Courzona :( ")

courzon(integer)