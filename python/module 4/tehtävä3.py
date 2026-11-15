pienin = None
suurin = None

while True:
    syote = input("Anna luku (tyhjä merkkijono lopettaa): ")

    if syote == "":
        break

    luku = float(syote)

    if pienin is None or luku < pienin:
        pienin = luku
    if suurin is None or luku > suurin:
        suurin = luku

if pienin is None or suurin is None:
    print("Et antanut yhtään lukua.")
else:
    print(f"Pienin luku: {pienin}")
    print(f"Suurin luku: {suurin}")
