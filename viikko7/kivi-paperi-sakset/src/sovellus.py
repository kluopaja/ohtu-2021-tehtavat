from komentolukija import Kirjainkomentolukija
from kps import KPStehdas
class Sovellus:
    def __init__(self, io, komentolukija, paavalikkokuvaus):
        """Luo Sovelluksen.

        Argumentit:
            `io`: Io olio
            `pelivalitsija`: Komentolukija-luokan olio
                Lukee sovelluksen toiminnon ja palauttaa toiminnon
                suorittavan funktion.
            `paavalikkokuvaus`: merkkijono
                Kuvaus päävalikon toiminnasta
        """
        self._io = io
        self._komentolukija = komentolukija
        self._paavalikkokuvaus = paavalikkokuvaus

    def suorita(self):
        while True:
            self._io.kirjoita(self._paavalikkokuvaus)
            komento = self._komentolukija.lue()
            if komento is None:
                break
            komento()

class Sovellustehdas:
    def __init__(self, io):
        self._io = io
        kpstehdas = KPStehdas(self._io)
        komennot = {
            "a": lambda : kpstehdas.kaksinpeli().pelaa(),
            "b": lambda : kpstehdas.helppo_yksinpeli().pelaa(),
            "c": lambda : kpstehdas.vaikea_yksinpeli().pelaa()
        }
        self._komentolukija = Kirjainkomentolukija(self._io, komennot)
        self._paavalikkokuvaus = (
            "Valitse pelataanko"
            "\n (a) Ihmistä vastaan"
            "\n (b) Tekoälyä vastaan"
            "\n (c) Parannettua tekoälyä vastaan"
            "\nMuilla valinnoilla lopetetaan"
        )

    def luo(self):
        return Sovellus(self._io, self._komentolukija, self._paavalikkokuvaus)
