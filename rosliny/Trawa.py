from Roslina import Roslina


class Trawa(Roslina):
    __SILA = 0
    __INICJATYWA = 0

    def __init__(self, swiat, pozycja, tura_urodzenia):
        super(Trawa, self).__init__(self.TypOrganizmu.TRAWA,
                                    swiat, pozycja, tura_urodzenia, self.__SILA, self.__INICJATYWA)
        self.set_kolor("green")

    def __str__(self):
        return "Trawa"
