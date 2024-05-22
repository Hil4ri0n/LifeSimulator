import random
from zwierzeta.Czlowiek import Czlowiek
from Roslina import Roslina
from Logs import Logs


class WilczeJagody(Roslina):
    __SILA = 99
    __INICJATYWA = 0

    def __init__(self, swiat, pozycja, tura_urodzenia):
        super(WilczeJagody, self).__init__(self.TypOrganizmu.WILCZE_JAGODY,
                                    swiat, pozycja, tura_urodzenia, self.__SILA, self.__INICJATYWA)
        self.set_kolor("#670680")
        self.set_szansa_rozmnazania(0.05)

    def akcja(self):
        tmp_losowanie = random.randint(0, 100)
        if tmp_losowanie < self.get_szansa_rozmnazania() * 100:
            self.rozprzestrzenianie()

    def __str__(self):
        return "Wilcze Jagody"

    def zdolnosckolizji(self, atakujacy, ofiara) -> bool:
        if isinstance(atakujacy, Czlowiek) and atakujacy.get_umiejetnosc().get_active():
            atakujacy.uciekaj(self)
            return True
        else:
            Logs.dodaj_komentarz(atakujacy.organizm_to_string() + " zjada " + self.organizm_to_string())
            if atakujacy.get_sila() >= 99:
                self.get_swiat().usun_organizm(self)
                Logs.dodaj_komentarz(atakujacy.organizm_to_string() + " niszczy krzak wilczej jagody")
            if atakujacy.czy_jest_zwierzeciem():
                self.get_swiat().usun_organizm(atakujacy)
                Logs.dodaj_komentarz(atakujacy.organizm_to_string() + " ginie od wilczej jagody")
            return True
