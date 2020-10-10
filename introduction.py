# import random

# x = random.randrange(1, 100)
# print(x)

# if 0 < x <= 25 or 60 <= x < 80:
#     print("Twoja liczba jest z zakresu")
# else:
#     print("Twoja liczba nie jest z zakresu")

# LIST

# myList = ["W", "S", "B"]
# print(myList)

# print(myList[0])
# print(myList[1])
# print(myList[2])

NameList = ["Joanna", "Michał", "Krzysztof"]

# name = "Marcin"

# if name in NameList:
#     print(f"\nImię '{name}' jest na liście!")
# else:
#     print(f"\nImienia '{name}' nie ma na liście, ale je dodamy!\n...")
#     NameList.append(name)
#     print(f"Teraz {name} jest na liście: {NameList}\n")

# myTupleList = ()
# print(myTupleList)

# i = 0
# while i <= 10:
#     print(i)
#     i += 1
# else:
#     print("To już jest koniec")


sampleList = ["Warszawa", "Kraków", "Gdańsk"]

# myCity = "Gdynia"     
 
# for city in sampleList:
#     if myCity in sampleList:
#         com = myCity + " jest na liście"
#         break
#     else:
#         com = myCity + " nie ma na liście"
#         # addCity = input("Chcesz je dodać? Y/N: ")
#         # addCity = addCity.upper()
#         # if addCity == "Y":
#         #     sampleList.append(myCity)
#         #     print(f"Teraz '{myCity}' jest na liście : {sampleList}")
#         # else:
#         #         print("XD")
#         # break


# print(com)
# addCity = input("Chcesz je dodać? Y/N: ")
# addCity = addCity.upper()
# if addCity == "Y":
#     sampleList.append(myCity)
#     print(f"Teraz '{myCity}' jest na liście : {sampleList}")
# else:
#     print("XD")

# myName = "Agata"
# mySurname = "Wiśniewska"
# myAge = 27
# def greetings(name, surname, age):
#     print(f"Nazywam się {name} {surname}.")
#     print(f"Mam {age} lat.")

# greetings(myName, mySurname, myAge)

# def example01(city="Gdynia"):
#     print(f"Miasto {city}")

# example01()

# def example02(*arg):
#     print(arg)
#     print(type(arg))

# example02("a", "b", "c")

# def example04():
#     return 1

numbersList = [1, 6, -2, 4.3]
start = -2

def sumFunction(numbers, suma=0):
    for number in numbers:
        suma += number
    summary = suma
    return summary

sumFunction(numbersList)
print(f"Suma to {summary}")
# def sumFunction():
    
# print(sum(numbersList, start))
