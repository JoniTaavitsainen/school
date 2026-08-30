import random

N = int(input("Anna arvottavien pisteiden määrä: "))

sisalla = 0

for i in range(N):
    x = random.randint(-1000, 1000) / 1000
    y = random.randint(-1000, 1000) / 1000

    if x ** 2 + y ** 2 < 1:
        sisalla += 1

pi = 4 * sisalla / N
print(f"Piin likiarvo on: {pi}")
