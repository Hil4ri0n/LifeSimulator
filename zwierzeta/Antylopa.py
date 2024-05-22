import random
from Zwierze import Zwierze
from Logs import Logs


class Antylopa(Zwierze):

    __ZASIEG_RUCHU = 2
    __SZANSA_WYKONYWANIA_RUCHU = 1
    __SILA = 4
    __INICJATYWA = 4

    def __init__(self, swiat, pozycja, tura_urodzenia):
        super(Antylopa, self).__init__(self.TypOrganizmu.ANTYLOPA, swiat, pozycja, tura_urodzenia, self.__SILA, self.__INICJATYWA)
        self.set_zasieg_ruchu(self.__ZASIEG_RUCHU)
        self.set_szansa_wykonywania_ruchu(self.__SZANSA_WYKONYWANIA_RUCHU)
        self.set_kolor("#a27c36")

    def __str__(self):
        return "Antylopa"

    def zdolnosckolizji(self, atakujacy, ofiara) -> bool:
        tmp_losowanie = random.randint(0, 100)
        if tmp_losowanie < 50:
            if self == atakujacy:
                Logs.dodaj_komentarz(self.organizm_to_string() + " ucieka od " + ofiara.organizm_to_string())
                tmp_pozycja = self.losowe_puste_pole(ofiara.get_pozycja())
                if tmp_pozycja != ofiara.get_pozycja():
                    self.ruch(tmp_pozycja)
            elif self == ofiara:
                Logs.dodaj_komentarz(self.organizm_to_string() + " ucieka od " + atakujacy.organizm_to_string())
                tmp_pozycja = self.losowe_puste_pole(self.get_pozycja())
                self.ruch(tmp_pozycja)
                if self.get_pozycja() == tmp_pozycja:
                    self.get_swiat().usun_organizm(self)
                    Logs.dodaj_komentarz(atakujacy.organizm_to_string() + " zabija " + self.organizm_to_string())
                atakujacy.ruch(tmp_pozycja)
            return True
        else:
            return False
