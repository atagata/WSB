import random

# """ Napisz funkcję która zamienia liczbzę lat na dni. Założenie: brak lat przestępnych """

# years = int(input("Podaj liczbę lat: ))

# def yearsToDays(years):
#     days = years*365
#     return days

# if years == 1:
#     print(f"{years} rok zawiera w sobie {yearsToDays(years)} dni.")
# else:
#     print(f"{years} lat zawiera w sobie {yearsToDays(years)} dni.")

# def listCreator(start, end, i):
#     randomList = []
#     for i in range(0,i+1):
#         n = random.randint(start, end)
#         randomList.append(n)
#     print(f"Twoja lista to: {randomList}")
#     return randomList

# def MaxMin(list):
#     list = sorted(list)
#     print(f"Lista po posortowaniu wygląda tak: {list}")
#     return list[-1] - list[0]

# randomList = listCreator(41, 100, 4)
# print(f"Największa liczba to {sorted(randomList)[-1]}, a najmniejsza to {sorted(randomList)[0]}. Różnica między nimi wynosi {MaxMin(randomList)}")

