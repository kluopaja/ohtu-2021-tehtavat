from enum import Enum
from tkinter import ttk, constants, StringVar

class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3

class Kayttoliittyma:
    def __init__(self, sovellus, komentomanageri, root):
        self._sovellus = sovellus
        self._root = root
        self._komentomanageri = komentomanageri

    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovellus.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)
        komentotehdas = self._komentomanageri.komentotehdas
        komentotehdas.syote_callback = self._lue_kokonaislukusyote

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_kumoa()
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _suorita_komento(self, komento):
        self._komentomanageri.suorita(komento)
        self._paivita_painikkeet()

    def _suorita_kumoa(self):
        self._komentomanageri.kumoa()
        self._paivita_painikkeet()

    def _paivita_painikkeet(self):
        if self._komentomanageri.komentoja_kumoamatta():
            self._kumoa_painike["state"] = constants.NORMAL
        else:
            self._kumoa_painike["state"] = constants.DISABLED

        if self._sovellus.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovellus.tulos)

    def _lue_kokonaislukusyote(self):
        try:
            return int(self._syote_kentta.get())
        except Exception:
            return None
