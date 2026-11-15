while True:
    tuumat = float(input("Anna tuumamäärä (negatiivinen luku lopettaa): "))

    if tuumat < 0:
        print("Ohjelma lopetetaan.")
        break

    senttimetrit = tuumat * 2.54
    print(f"{tuumat} tuumaa = {senttimetrit:.2f} cm")
