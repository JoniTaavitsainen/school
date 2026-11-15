from random import randint

arvottu = randint(1, 10)

while True:
    arvaus = int(input("Arvaa luku väliltä 1..10: "))

    if arvaus > arvottu:
        print("Liian suuri arvaus")
    elif arvaus < arvottu:
        print("Liian pieni arvaus")
    else:
        print("Oikein")
        break
