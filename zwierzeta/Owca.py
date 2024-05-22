
from Zwierze import Zwierze


class Owca(Zwierze):
    __ZASIEG_RUCHU = 1
    __SZANSA_WYKONYWANIA_RUCHU = 1
    __SILA = 4
    __INICJATYWA = 4

    def __init__(self, swiat, pozycja, tura_urodzenia):
        super(Owca, self).__init__(self.TypOrganizmu.OWCA, swiat, pozycja, tura_urodzenia, self.__SILA, self.__INICJATYWA)
        self.set_zasieg_ruchu(self.__ZASIEG_RUCHU)
        self.set_szansa_wykonywania_ruchu(self.__SZANSA_WYKONYWANIA_RUCHU)
        self.set_kolor("#ff99cc")

    def __str__(self):
        return "Owca"
