class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        if alin_kerros > ylin_kerros:
            raise ValueError("Alimman kerroksen täytyy olla ylimmän kerroksen alapuolella.")

        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def siirry_kerrokseen(self, kohdekerros):
        if not self.alin_kerros <= kohdekerros <= self.ylin_kerros:
            raise ValueError("Kohdekerros ei ole hissin kerrosalueella.")

        while self.kerros < kohdekerros:
            self.kerros_ylös()
        while self.kerros > kohdekerros:
            self.kerros_alas()

        return self.kerros

    def kerros_ylös(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
        print(f"Hissi on kerroksessa {self.kerros}.")
        return self.kerros

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
        print(f"Hissi on kerroksessa {self.kerros}.")
        return self.kerros


if __name__ == "__main__":
    hissi = Hissi(-1, 5)
    hissi.siirry_kerrokseen(3)
    hissi.siirry_kerrokseen(-1)
    hissi.kerros_alas()
    hissi.siirry_kerrokseen(5)
    hissi.kerros_ylös()