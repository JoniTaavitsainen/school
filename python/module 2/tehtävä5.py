import time


def muunna_grammoiksi(leiviskat, naulat, luodit):
    grammoja = leiviskat * 20 * 32 * 13.3 + naulat * 32 * 13.3 + luodit * 13.3
    return grammoja


def mainloop():
    try:
        leiviskat = float(input("Anna leiviskät.\n"))
        naulat = float(input("Anna naulat.\n"))
        luodit = float(input("Anna luodit.\n"))

        grammoja = muunna_grammoiksi(leiviskat, naulat, luodit)
        kilogrammat = int(grammoja // 1000)
        gramman_jaljella = grammoja - kilogrammat * 1000

        print(f"\nMassa nykymittojen mukaan:\n{kilogrammat} kilogrammaa ja {gramman_jaljella:.2f} grammaa.")

    except ValueError:
        print("Virheellinen syöte. Anna vain numeroita.")
        time.sleep(1)
        mainloop()


mainloop()
