class KonsoliIo:
    def lue_syote(self, teksti):
        if teksti is None:
            return input()

        return input(teksti)

    def kirjoita(self, teksti):
        print(teksti)
