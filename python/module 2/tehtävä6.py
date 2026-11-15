import random


def arvo_koodi3():
    koodi3 = ""
    for i in range(3):
        koodi3 += str(random.randint(0, 9))
    return koodi3


def arvo_koodi4():
    koodi4 = ""
    for i in range(4):
        koodi4 += str(random.randint(1, 6))
    return koodi4


def mainloop():
    try:
        print("Kolmenumeroisen lukon koodi:", arvo_koodi3())
        print("Nelinumeroisen lukon koodi:", arvo_koodi4())

    except ValueError:
        print(ValueError)


mainloop()
