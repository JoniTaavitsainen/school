luvut = []

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")

    if syote == "":
        break

    try:
        luku = float(syote)
    except ValueError:
        print("Virheellinen syöte. Anna numero tai tyhjä merkkijono lopettaaksesi.")
        continue

    luvut.append(luku)


viisi_suurinta = sorted(luvut, reverse=True)[:5]

for luku in viisi_suurinta:
    print(luku)

