from Zwierze import Zwierze


class Wilk(Zwierze):
    __ZASIEG_RUCHU = 1
    __SZANSA_WYKONYWANIA_RUCHU = 1
    __SILA = 9
    __INICJATYWA = 5

    def __init__(self, swiat, pozycja, tura_urodzenia):
        super(Wilk, self).__init__(self.TypOrganizmu.WILK, swiat
                                   , pozycja, tura_urodzenia, self.__SILA, self.__INICJATYWA)
        self.set_zasieg_ruchu(self.__ZASIEG_RUCHU)
        self.set_szansa_wykonywania_ruchu(self.__SZANSA_WYKONYWANIA_RUCHU)
        self.set_kolor("#558bd8")

    def __str__(self):
        return "Wilk"