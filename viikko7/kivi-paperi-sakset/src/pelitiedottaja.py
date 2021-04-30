class Pelitiedottaja:
    """Luokka peliin liittyvien tietojen näyttämiseen"""
    def __init__(self, io, peliohjeet, pelitilanneviesti,
                 tasapeliviesti, loppuviesti):
        self._io = io
        self._peliohjeet = peliohjeet
        self._pelitilanneviesti = pelitilanneviesti
        self._tasapeliviesti = tasapeliviesti
        self._loppuviesti = loppuviesti

    def nayta_ohjeet(self):
        self._io.kirjoita(self._peliohjeet)

    def paivita_tulostaulu(self, tuomari):
        """Tulostaa tulostaulun tekstimuotoisena.

        Argumentit:
            `tuomari`: Tuomari-olio
        """


        self._io.kirjoita(
            f"{self._pelitilanneviesti}: {tuomari.ekan_pisteet} - {tuomari.tokan_pisteet}"
        )
        self._io.kirjoita(f"{self._tasapeliviesti}: {tuomari.tasapelit}")

    def nayta_loppuviesti(self):
        self._io.kirjoita(self._loppuviesti)
