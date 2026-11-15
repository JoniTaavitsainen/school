from tehtävä2 import Talo as TalonRunko


class Talo(TalonRunko):
    def palohalytys(self):
        pohjakerros = 0 if self.alin_kerros <= 0 <= self.ylin_kerros else self.alin_kerros
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(pohjakerros)


if __name__ == "__main__":
    talo = Talo(-1, 5, 3)
    talo.aja_hissia(1, 4)
    talo.aja_hissia(2, 2)
    talo.aja_hissia(3, -1)
    print("Palohälytys!")
    talo.palohalytys()
