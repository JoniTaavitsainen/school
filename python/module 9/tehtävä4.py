import random


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

    def kulje(self, tuntimaara):
        self.kuljettu_matka += self.nopeus * tuntimaara
        return self.kuljettu_matka

    def __str__(self):
        return (
            f"Rekisteritunnus: {self.rekisteritunnus}, "
            f"Huippunopeus: {self.huippunopeus} km/h, "
            f"Nopeus: {self.nopeus} km/h, "
            f"Kuljettu matka: {self.kuljettu_matka} km"
        )


autot = []
for i in range(1, 11):
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(f"ABC-{i}", huippunopeus))

while not any(auto.kuljettu_matka >= 10000 for auto in autot):
    for auto in autot:
        auto.kiihdyta(random.randint(-10, 15))
        auto.kulje(1)

for auto in autot:
    print(auto)
