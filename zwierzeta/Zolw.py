from Zwierze import Zwierze
from Organizm import Organizm
from Logs import Logs


class Zolw(Zwierze):
    __ZASIEG_RUCHU = 1
    __SZANSA_WYKONYWANIA_RUCHU = 0.25
    __SILA = 2
    __INICJATYWA = 1

    def __init__(self, swiat, pozycja, tura_urodzenia):
        super(Zolw, self).__init__(self.TypOrganizmu.ZOLW, swiat
                                   , pozycja, tura_urodzenia, self.__SILA, self.__INICJATYWA)
        self.set_zasieg_ruchu(self.__ZASIEG_RUCHU)
        self.set_szansa_wykonywania_ruchu(self.__SZANSA_WYKONYWANIA_RUCHU)
        self.set_kolor("#2cfec5")

    def __str__(self):
        return "Zolw"

    def zdolnosckolizji(self, atakujacy, ofiara) -> bool:
        if self == ofiara:
            if atakujacy.get_sila() < 5 and atakujacy.czy_jest_zwierzeciem():
                Logs.dodaj_komentarz(self.organizm_to_string() + " odpiera atak " + atakujacy.organizm_to_string())
                return True
            else:
                return False
        else:
            if atakujacy.get_sila() >= ofiara.get_sila():
                return False
            else:
                if ofiara.get_sila() < 5 and ofiara.czy_jest_zwierzeciem():
                    Logs.dodaj_komentarz(self.organizm_to_string() + " odpiera atak " + ofiara.organizm_to_string())
                    return True
                else:
                    return False
