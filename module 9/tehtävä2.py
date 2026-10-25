class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

        return self.nopeus


auto = Auto("ABC-123", 142)

for muutos in (30, 70, 50):
    auto.kiihdyta(muutos)
    print(f"Nopeus muutoksen {muutos} km/h jälkeen: {auto.nopeus} km/h")

auto.kiihdyta(-200)
print(f"Nopeus kun muutos on -200 km/h: {auto.nopeus} km/h")
