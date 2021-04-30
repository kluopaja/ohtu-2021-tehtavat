from abc import ABC, abstractmethod
from siirto import Siirto
class Pelaaja(ABC):
    @abstractmethod
    def hae_siirto(self):
        """Hakee Pelaajan siirron.

        Palauttaa:
            Mikäli siirron hakeminen onnistui:
                Siirto-enum
            muuten:
                None
        """
        pass

    @abstractmethod
    def kerro_toisen_siirto(self, toisen_siirto):
        """Kertoo Pelaajalle toisen pelaajan viimeisimmän siirron

        Argumentit:
            `siirto` Siirto-enum
                Vastustajan viimeisin siirto
        """
        pass

class Ihmispelaaja(Pelaaja):
    """Luokka ihmispelaajalle"""
    def __init__(self, io, siirtolukija):
        self._io = io
        self._siirtolukija = siirtolukija

    def hae_siirto(self):
        return self._siirtolukija.lue(tiukka=True)

    def kerro_toisen_siirto(self, toisen_siirto):
        pass

class Tekoalypelaaja(Pelaaja):
    """Luokka heikolle tekoälypelaajaalle"""
    def __init__(self, siirtolista):
        self._siirto = 0
        self._siirtolista = siirtolista

    def hae_siirto(self):
        self._siirto = self._siirto + 1
        self._siirto = self._siirto % len(self._siirtolista)

        return self._siirtolista[self._siirto]

    def kerro_toisen_siirto(self, toisen_siirto):
        pass


class ParempiTekoalypelaaja(Pelaaja):
    """Luokka vahvalle tekoälypelaajaalle"""
    def __init__(self, muistin_koko):
        self._muisti = [None] * muistin_koko
        self._vapaa_muisti_indeksi = 0

    def hae_siirto(self):
        if self._vapaa_muisti_indeksi == 0 or self._vapaa_muisti_indeksi == 1:
            return Siirto.KIVI

        viimeisin_siirto = self._muisti[self._vapaa_muisti_indeksi - 1]

        k = 0
        p = 0
        s = 0

        for i in range(0, self._vapaa_muisti_indeksi - 1):
            if viimeisin_siirto == self._muisti[i]:
                seuraava = self._muisti[i + 1]

                if seuraava == Siirto.KIVI:
                    k = k + 1
                elif seuraava == Siirto.PAPERI:
                    p = p + 1
                else:
                    s = s + 1

        # Tehdään siirron valinta esimerkiksi seuraavasti;
        # - jos kiviä eniten, annetaan aina paperi
        # - jos papereita eniten, annetaan aina sakset
        # muulloin annetaan aina kivi
        if k > p or k > s:
            return Siirto.PAPERI
        elif p > k or p > s:
            return Siirto.SAKSET
        else:
            return Siirto.KIVI

        # Tehokkaampiakin tapoja löytyy, mutta niistä lisää
        # Johdatus Tekoälyyn kurssilla!

    def kerro_toisen_siirto(self, toisen_siirto):
        # jos muisti täyttyy, unohdetaan viimeinen alkio
        if self._vapaa_muisti_indeksi == len(self._muisti):
            for i in range(1, len(self._muisti)):
                self._muisti[i - 1] = self._muisti[i]

            self._vapaa_muisti_indeksi = self._vapaa_muisti_indeksi - 1

        self._muisti[self._vapaa_muisti_indeksi] = toisen_siirto
        self._vapaa_muisti_indeksi = self._vapaa_muisti_indeksi + 1
