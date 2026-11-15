from tehtävä1 import Hissi


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        if hissien_lukumaara < 1:
            raise ValueError("Talossa täytyy olla vähintään yksi hissi.")

        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = [
            Hissi(alin_kerros, ylin_kerros)
            for _ in range(hissien_lukumaara)
        ]

    def aja_hissia(self, hissin_numero, kohdekerros):
        if not 1 <= hissin_numero <= len(self.hissit):
            raise IndexError("Annettua hissin numeroa ei ole talossa.")

        return self.hissit[hissin_numero - 1].siirry_kerrokseen(kohdekerros)


if __name__ == "__main__":
    talo = Talo(-1, 5, 3)
    talo.aja_hissia(1, 4)
    talo.aja_hissia(2, 2)
    talo.aja_hissia(3, -1)
