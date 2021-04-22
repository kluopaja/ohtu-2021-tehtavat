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
        self._edellinen_tulos = None

    def suorita(self):
        self._edellinen_tulos = self._sovelluslogiikka.tulos
        arvo = self._arvo_callback()
        if arvo is not None:
            self._sovelluslogiikka.miinus(arvo)

    def kumoa(self):
        if self._edellinen_tulos is not None:
            self._sovelluslogiikka.aseta_arvo(self._edellinen_tulos)

class Pluskomento:
    def __init__(self, sovelluslogiikka, arvo_callback):
        self._sovelluslogiikka = sovelluslogiikka
        self._arvo_callback = arvo_callback
        self._edellinen_tulos = None

    def suorita(self):
        self._edellinen_tulos = self._sovelluslogiikka.tulos
        arvo = self._arvo_callback()
        if arvo is not None:
            self._sovelluslogiikka.plus(arvo)

    def kumoa(self):
        if self._edellinen_tulos is not None:
            self._sovelluslogiikka.aseta_arvo(self._edellinen_tulos)

class Nollauskomento:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka
        self._edellinen_tulos = None

    def suorita(self):
        self._edellinen_tulos = self._sovelluslogiikka.tulos
        self._sovelluslogiikka.nollaa()

    def kumoa(self):
        if self._edellinen_tulos is not None:
            self._sovelluslogiikka.aseta_arvo(self._edellinen_tulos)

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
        self._komentohistoria = []

    def suorita(self, komento):
        uusi_komento = self.komentotehdas.hae(komento)
        if uusi_komento is not None:
            uusi_komento.suorita()
            self._komentohistoria.append(uusi_komento)

    def kumoa(self):
        if self.komentoja_kumoamatta():
            self._komentohistoria.pop().kumoa()

    def komentoja_kumoamatta(self):
        return len(self._komentohistoria) > 0
