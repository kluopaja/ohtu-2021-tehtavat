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
        elif not isinstance(kasvatuskoko, int) or kasvatuskoko <= 0:
            raise Exception("Oletuskasvatuksen tulee olla positiivinen kokonaisluku")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.alkiot = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.alkiot[0:self.alkioiden_lkm]

    def lisaa(self, n):
        if not self.kuuluu(n):
            self._kasvata_tarvittaessa()
            self.alkiot[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1
            return True

        return False

    def _kasvata_tarvittaessa(self):
        if self.alkioiden_lkm == len(self.alkiot):
            taulukko_old = self.alkiot
            self.alkiot = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
            self.kopioi_taulukko(taulukko_old, self.alkiot)

    def poista(self, n):
        if not self.kuuluu(n):
            return False

        self._poista_kohdasta(self.alkiot.index(n))
        return True

    def _poista_kohdasta(self, kohta):
        for j in range(kohta, self.alkioiden_lkm - 1):
            self.alkiot[j] = self.alkiot[j + 1]

        self.alkioiden_lkm -= 1

    def kopioi_taulukko(self, a, b):
        for i in range(len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.alkiot[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        tulos = IntJoukko()
        for luku in a.to_int_list():
            tulos.lisaa(luku)

        for luku in b.to_int_list():
            tulos.lisaa(luku)

        return tulos

    @staticmethod
    def leikkaus(a, b):
        tulos = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for luku in a_taulu:
            if luku in b_taulu:
                tulos.lisaa(luku)

        return tulos

    @staticmethod
    def erotus(a, b):
        tulos = IntJoukko()
        for luku in a.to_int_list():
            tulos.lisaa(luku)

        for luku in b.to_int_list():
            tulos.poista(luku)

        return tulos

    def __str__(self):
        return "{" + ", ".join([str(x) for x in self.alkiot[:self.alkioiden_lkm]]) + "}"
