from tkinter import Tk
from kayttoliittyma import Kayttoliittyma
from sovelluslogiikka import Sovelluslogiikka, Komentomanageri, Komentotehdas


def main():
    sovellus = Sovelluslogiikka()

    window = Tk()
    window.title("Laskin")
    komentomanageri = Komentomanageri(Komentotehdas(sovellus))

    kayttoliittyma = Kayttoliittyma(sovellus, komentomanageri, window)
    kayttoliittyma.kaynnista()

    window.mainloop()

if __name__ == "__main__":
    main()
