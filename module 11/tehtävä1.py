class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(
            f"Kirja: {self.nimi}, kirjoittaja {self.kirjoittaja}, "
            f"{self.sivumaara} sivua"
        )


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}, päätoimittaja {self.paatoimittaja}")


if __name__ == "__main__":
    kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
    lehti = Lehti("Aku Ankka", "Aki Hyyppä")
    julkaisut = [lehti, kirja]

    for julkaisu in julkaisut:
        julkaisu.tulosta_tiedot()
