import random

from Roslina import Roslina

class Mlecz(Roslina):
    __SILA = 0
    __INICJATYWA = 0
    __ILE_PROB = 3
    
    def __init__(self, swiat, pozycja, tura_urodzenia):
        super(Mlecz, self).__init__(self.TypOrganizmu.MLECZ,
                                    swiat, pozycja, tura_urodzenia, self.__SILA, self.__INICJATYWA)
        self.set_kolor("yellow")

    def akcja(self):
        for i in range(self.__ILE_PROB):
            tmp_losowanie = random.randint(0, 100)
            if tmp_losowanie < self.get_szansa_rozmnazania():
                self.rozprzestrzenianie()

    def __str__(self):
        return "Mlecz"