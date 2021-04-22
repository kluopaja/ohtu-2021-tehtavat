from kayttoliittyma import Komento
class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo

class Miinuskomento:
    def __init__(self, sovelluslogiikka, arvo_callback):
        self._sovelluslogiikka = sovelluslogiikka
        self._arvo_callback = arvo_callback

    def suorita(self):
        arvo = self._arvo_callback()
        if arvo is not None:
            self._sovelluslogiikka.miinus(arvo)

class Pluskomento:
    def __init__(self, sovelluslogiikka, arvo_callback):
        self._sovelluslogiikka = sovelluslogiikka
        self._arvo_callback = arvo_callback

    def suorita(self):
        arvo = self._arvo_callback()
        if arvo is not None:
            self._sovelluslogiikka.plus(arvo)

class Nollauskomento:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self._sovelluslogiikka.nollaa()

class Komentotehdas:
    def __init__(self, sovelluslogiikka):
        self.syote_callback = lambda: None
        self._komennot = {
            Komento.SUMMA: lambda: Pluskomento(sovelluslogiikka,
                                               self.syote_callback),
            Komento.EROTUS: lambda: Miinuskomento(sovelluslogiikka,
                                                  self.syote_callback),
            Komento.NOLLAUS: lambda: Nollauskomento(sovelluslogiikka)
        }

    def hae(self, komento):
        if komento in self._komennot:
            return self._komennot[komento]()
        return None

class Komentomanageri:
    def __init__(self, komentotehdas):
        self.komentotehdas = komentotehdas

    def suorita(self, komento):
        uusi_komento = self.komentotehdas.hae(komento)
        if uusi_komento is not None:
            uusi_komento.suorita()
