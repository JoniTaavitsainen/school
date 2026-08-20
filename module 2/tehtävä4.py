import time

# y on monta lukua käyttäjä syöttää
y = 3
print("Anna" , y , "kokonaislukua")
0
def tulokset(luvut):
    tulo = 1
    for luku in luvut:
        tulo *= luku
    print("Lukujen summa:", sum(luvut), "\nLukujen tulo:", tulo, "\nLukujen keskiarvo:", sum(luvut) / len(luvut))

def lukukysely():
    luvut = []
    for i in range(y):
        luku = int(input(f"Anna luku {i + 1}: "))
        luvut.append(luku)
    return luvut

def mainloop():
    try:
        luvut = lukukysely()
        tulokset(luvut)

    except ValueError:
        print("Virheellinen syöte. Anna vain kokonaislukuja.")
        time.sleep(1)
        mainloop()

mainloop()


