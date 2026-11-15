import random


def heita_noppaa(tahkojen_maara):
    return random.randint(1, tahkojen_maara)


maksimisilmaluku = int(input("Anna nopan tahkojen määrä: "))
silmaluku = 0

while silmaluku != maksimisilmaluku:
    silmaluku = heita_noppaa(maksimisilmaluku)
    print(silmaluku)