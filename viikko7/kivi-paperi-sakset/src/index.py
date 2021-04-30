from konsoli_io import KonsoliIo
from sovellus import Sovellustehdas
def main():
    io = KonsoliIo()
    sovellus = Sovellustehdas(io).luo()
    sovellus.suorita()


if __name__ == "__main__":
    main()
