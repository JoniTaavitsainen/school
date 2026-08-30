from random import randint

x = int(input("monta arpakuutiota heitetään?"))

luvut = []
for i in range(x):
    luvut.append(randint(1, 6))

print("Silmälukujen summa:", sum(luvut))

