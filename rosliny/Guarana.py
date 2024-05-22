from Roslina import Roslina
from Organizm import Organizm
from Logs import Logs


class Guarana(Roslina):
    __SILA = 0
    __INICJATYWA = 0
    __ZWIEKSZENIE_SILY = 3

    def __init__(self, swiat, pozycja, tura_urodzenia):
        super(Guarana, self).__init__(self.TypOrganizmu.GUARANA,
                                    swiat, pozycja, tura_urodzenia, self.__SILA, self.__INICJATYWA)
        self.set_kolor("#dc143c")

    def __str__(self):
        return "Guarana"

    def zdolnosckolizji(self, atakujacy, ofiara) -> bool:
        tmp_pozycja = self.get_pozycja()
        self.get_swiat().usun_organizm(self)
        atakujacy.ruch(tmp_pozycja)
        Logs.dodaj_komentarz(atakujacy.organizm_to_string() + " zjada " + self.organizm_to_string()
                             + " i zwieksza swoja sile na " + str(self.__ZWIEKSZENIE_SILY))
        atakujacy.set_sila(atakujacy.get_sila() + self.__ZWIEKSZENIE_SILY)
        return True

