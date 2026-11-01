import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus = max(0, min(self.nopeus + muutos, self.huippunopeus))
        return self.nopeus

    def kulje(self, tuntimaara):
        self.kuljettu_matka += self.nopeus * tuntimaara
        return self.kuljettu_matka


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\nKilpailu: {self.nimi} ({self.pituus} km)")
        print(f"{'Rekisteritunnus':<18}{'Huippunopeus':>14}{'Nopeus':>10}{'Matka':>14}")
        print("-" * 56)
        for auto in self.autot:
            print(
                f"{auto.rekisteritunnus:<18}{auto.huippunopeus:>11} km/h"
                f"{auto.nopeus:>7} km/h{auto.kuljettu_matka:>10.1f} km"
            )

    def kilpailu_ohi(self):
        return any(auto.kuljettu_matka >= self.pituus for auto in self.autot)


if __name__ == "__main__":
    autot = [
        Auto(f"ABC-{numero}", random.randint(100, 200))
        for numero in range(1, 11)
    ]
    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    tunteja = 0
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunteja += 1
        if tunteja % 10 == 0:
            kilpailu.tulosta_tilanne()

    print(f"\nKilpailu päättyi {tunteja} tunnin jälkeen.")
    kilpailu.tulosta_tilanne()
