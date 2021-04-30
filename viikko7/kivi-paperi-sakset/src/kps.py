from siirto import Siirto
from komentolukija import Kirjainkomentolukija
from pelaajat import Ihmispelaaja, Tekoalypelaaja, ParempiTekoalypelaaja
from pelitiedottaja import Pelitiedottaja
from tuomari import Tuomari

class KPS:
    def __init__(self, pelaaja_1, pelaaja_2, tuomari, pelitiedottaja):
        self._pelaaja_1 = pelaaja_1
        self._pelaaja_2 = pelaaja_2
        self._tuomari = tuomari
        self._pelitiedottaja = pelitiedottaja

    def pelaa(self):
        self._pelitiedottaja.nayta_ohjeet()
        while True:
            pelaajan_1_siirto = self._pelaaja_1.hae_siirto()
            if pelaajan_1_siirto is None:
                break

            pelaajan_2_siirto = self._pelaaja_2.hae_siirto()
            if pelaajan_2_siirto is None:
                break

            self._tuomari.kirjaa_siirto(
                pelaajan_1_siirto,
                pelaajan_2_siirto
            )
            self._pelaaja_1.kerro_toisen_siirto(pelaajan_2_siirto)
            self._pelaaja_2.kerro_toisen_siirto(pelaajan_1_siirto)
            self._pelitiedottaja.paivita_tulostaulu(self._tuomari)

        self._pelitiedottaja.nayta_loppuviesti()
        self._pelitiedottaja.paivita_tulostaulu(self._tuomari)


class KPStehdas:
    def __init__(self, io):
        self._io = io
        siirrot = {
            "k": Siirto.KIVI,
            "p": Siirto.PAPERI,
            "s": Siirto.SAKSET
        }
        siirtolukija_1 = Kirjainkomentolukija(self._io, siirrot,
                                              "Ensimmäisen pelaajan siirto: ")

        siirtolukija_2 = Kirjainkomentolukija(self._io, siirrot,
                                              "Toisen pelaajan siirto: ")
        self._pelaaja_1 = Ihmispelaaja(self._io, siirtolukija_1)
        self._pelaaja_2 = Ihmispelaaja(self._io, siirtolukija_2)
        peliohjeet = (
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )

        pelitilanneviesti = "Pelitilanne"

        self._pelitiedottaja = Pelitiedottaja(self._io, peliohjeet, "Pelitilanne",
                                              "Tasapelit", "Kiitos!")

    def kaksinpeli(self):
        return self._luo_pelaajille(self._pelaaja_1, self._pelaaja_2)
        
    def helppo_yksinpeli(self):
        vastustaja = Tekoalypelaaja(list(Siirto))
        return self._luo_pelaajille(self._pelaaja_1, vastustaja)

    def vaikea_yksinpeli(self):
        vastustaja = ParempiTekoalypelaaja(10)
        return self._luo_pelaajille(self._pelaaja_1, vastustaja)

    def _luo_pelaajille(self, pelaaja_1, pelaaja_2):
        return KPS(pelaaja_1, pelaaja_2, Tuomari(), self._pelitiedottaja)

