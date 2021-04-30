from siirto import Siirto
# Luokka pitää kirjaa ensimmäisen ja toisen pelaajan pisteistä sekä tasapelien määrästä.
class Tuomari:
    def __init__(self):
        self.ekan_pisteet = 0
        self.tokan_pisteet = 0
        self.tasapelit = 0

    def kirjaa_siirto(self, ekan_siirto, tokan_siirto):
        if self._ensimmainen_siirto_voittaa(ekan_siirto, tokan_siirto):
            self.ekan_pisteet = self.ekan_pisteet + 1
        elif self._ensimmainen_siirto_voittaa(tokan_siirto, ekan_siirto):
            self.tokan_pisteet = self.tokan_pisteet + 1
        else:
            self.tasapelit = self.tasapelit + 1

    def __str__(self):
        return f"Pelitilanne: {self.ekan_pisteet} - {self.tokan_pisteet}\nTasapelit: {self.tasapelit}"

    # sisäinen metodi joka tarkastaa voittaako siirto `eka` siirron `toka`
    def _ensimmainen_siirto_voittaa(self, eka, toka):
        if eka == Siirto.KIVI and toka == Siirto.SAKSET:
            return True
        if eka == Siirto.SAKSET and toka == Siirto.PAPERI:
            return True
        if eka == Siirto.PAPERI and toka == Siirto.KIVI:
            return True

        return False
