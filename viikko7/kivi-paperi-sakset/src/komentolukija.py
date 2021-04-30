class Kirjainkomentolukija:
    """Luokka, joka lukee komennon ja palauttaa komentoa vastaavan arvon

    Huomaa, että palautettava arvo voi olla myös funktio.

    """
    def __init__(self, io, komennot, kyselyviesti = None):
        """Alustaa Komentolukijan.

        Argumentit:
            `io`: Io-olio
            `komennot`: Sanakirja (avain, arvo) -pareja
                `avain`: pituuden 1 merkkijono
        """
        self._io = io
        self._komennot = komennot
        self._kyselyviesti = kyselyviesti

    def lue(self, tiukka=True):
        """Lukee syotteen ja palauttaa sitä vastaavan arvon.

        Argumentit:
            `tiukka`: totuusarvo
                Jos True, niin hyväksyy vain täysin oikean syötteen.
                muuten hyväksyy, kunhan viimeinen kirjain vastaa
                jotakin komentoa.

        Palauttaa
            Syötettä vastaavan arvon (tai funktion)
            None, jos syötettä vastaavaa arvoa ei löydy"""
        syote = self._io.lue_syote(self._kyselyviesti)
        if len(syote) == 0:
            return None

        if tiukka and len(syote) != 1:
            return None

        komentokirjain = syote[-1]
        if not komentokirjain in self._komennot:
            return None

        return self._komennot[komentokirjain]
