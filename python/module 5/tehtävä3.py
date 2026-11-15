x = int(input("Anna kokonaisluku: "))
z = []

for i in range(1, x + 1):
    if x % i == 0:
        z.append(i)

if len(z) == 2:
    print(f"Luku {x} on alkuluku.")
else:
    print(f"Luku {x} ei ole alkuluku.")