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


auto = Auto("ABC-123", 142)
auto.nopeus = 60
auto.kuljettu_matka = 2000

print(f"Ennen kulkemista: {auto.kuljettu_matka} km")
auto.kulje(1.5)
print(f"Kuljettu matka: {auto.kuljettu_matka} km")
