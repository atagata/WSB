import random
# chicken_leg = 2
# cow_leg = 4
# pig_leg = 4


# def legSumator(chickens, cows, pigs):
#     legSum = chickens*chicken_leg + cows*cow_leg + pigs*pig_leg
#     return legSum

# chickensQty = 3
# cowsQty=4
# pigsQty=5

# print(legSumator(chickensQty, cowsQty, pigsQty))

# defaultList = [22, 23131, 3131, 141415]


# def listReturn(list):
#     return list[0]


def listCreator(start, end, i):
    randomList = []
    for i in range(0,i+1):
        n = random.randint(start, end)
        randomList.append(n)
    print(f"Twoja lista to: {randomList}")
    return randomList

def listCreatorInput():
    parameters = []
    print("Witaj w kreatorze list!")
    start = int(input("Podaj początek zakresu: "))
    end = int(input("Podaj koniec zakresu: "))
    i = int(input("Podaj ile chcesz mieć elementów w liście: "))
    
def findMax(list):
    max = list[0]
    for number in list:
        if number > max:
            max = number
    print (f"Największa liczba w podanym zakresie to {max}")
    return max
    
def findMaxBySort(list):
    list = sorted(list)
    return list[-1]

def findMaxByMethodMax(list):
    maxNum = max(list)
    return maxNum

# defaultList = [22, 47, 12, 55, 3]

# print("Witaj w kreatorze list!")
# start = int(input("Podaj początek zakresu: "))
# end = int(input("Podaj koniec zakresu: "))
# i = int(input("Podaj ile chcesz mieć elementów w liście: "))

listCreatorInput()
randomList = listCreator(start, end, i)
print(f"Największa liczba w wygenerowanym zbiorze to: {findMaxBySort((randomList))}")
print(f"Największa liczba w wygenerowanym zbiorze to: {findMaxByMethodMax((randomList))}")
# findMax((randomList))

