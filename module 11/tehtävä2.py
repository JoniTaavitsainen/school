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


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko


if __name__ == "__main__":
    sahkoauto = Sähköauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

    sahkoauto.kiihdyta(120)
    polttomoottoriauto.kiihdyta(100)
    sahkoauto.kulje(3)
    polttomoottoriauto.kulje(3)

    print(
        f"{sahkoauto.rekisteritunnus}: "
        f"{sahkoauto.kuljettu_matka} km"
    )
    print(
        f"{polttomoottoriauto.rekisteritunnus}: "
        f"{polttomoottoriauto.kuljettu_matka} km"
    )
