import time


def tarkista_hemoglobiini(sukupuoli, arvo):
    sukupuoli = sukupuoli.lower().strip()

    if sukupuoli == "nainen":
        if 117 <= arvo <= 175:
            return "normaali"
        elif arvo < 117:
            return "alhainen"
        else:
            return "korkea"

    elif sukupuoli == "mies":
        if 134 <= arvo <= 195:
            return "normaali"
        elif arvo < 134:
            return "alhainen"
        else:
            return "korkea"

    else:
        raise ValueError("Sukupuoli tulee olla nainen tai mies.")


def mainloop():
    try:
        sukupuoli = input("Anna biologinen sukupuoli (nainen/mies): ")
        arvo = float(input("Anna hemoglobiiniarvo g/l: "))

        tulos = tarkista_hemoglobiini(sukupuoli, arvo)
        print(f"Hemoglobiiniarvo on {tulos}.")

    except ValueError:
        print("Virheellinen syöte. Anna sukupuoli nainen/mies ja hemoglobiiniarvo numerona.")
        time.sleep(1)
        mainloop()


mainloop()
