KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetin tulee olla epänegatiivinen kokonaisluku")
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kasvatuskoko, int) or  kasvatuskoko <= 0:
            raise Exception("Oletuskasvatuksen tulee olla positiivinen kokonaisluku")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.ljono[0:self.alkioiden_lkm]

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm == len(self.ljono):
                taulukko_old = self.ljono
                self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.ljono)

            return True

        return False

    def poista(self, n):
        kohta = -1

        for i in range(self.alkioiden_lkm):
            if n == self.ljono[i]:
                kohta = i  # haluttu luku löytyy tuosta kohdasta
                break

        if kohta != -1:
            for j in range(kohta, self.alkioiden_lkm - 1):
                self.ljono[j] = self.ljono[j + 1]

            self.alkioiden_lkm -= 1
            return True

        return False

    def kopioi_taulukko(self, a, b):
        for i in range(len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(len(a_taulu)):
            for j in range(len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        return "{" + ", ".join([str(x) for x in self.ljono[:self.alkioiden_lkm]]) + "}"
