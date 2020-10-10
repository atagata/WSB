""" silnia - funkcja przyjmuje liczbę całkowitą i zwraca jej silnię """

def factorial(integer):
    i = 1
    factorial = 1
    if integer <= 0:
        print("Podaj liczbę całkowitą różną od 0!")
    elif integer == 1:
        print("Nie można policzyć silni dla cyfry 1. Podaj liczbę wiekszą od 0 i różną od 1")
    else:
        for i in range (1, integer+1):
           factorial *= i 
    return factorial

def factorialWhile(integer):
    i = 1
    factorial = 1
    if integer <= 0:
        print("Podaj liczbę całkowitą różną od 0!")
    elif integer == 1:
        print("Nie można policzyć silni dla cyfry 1. Podaj liczbę wiekszą od 0 i różną od 1")
    else:
        while i <= integer:
            factorial *= i
            i += 1
    return factorial


integer = int(input("Podaj liczbę całkowitą: "))
print(factorial(integer))
print(factorialWhile(integer))