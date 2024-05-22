import random
from Organizm import Organizm
from Roslina import Roslina
from Punkt import Punkt
from zwierzeta.Czlowiek import Czlowiek
from Logs import Logs


class BarszczSosnowskiego(Roslina):
    __SILA = 10
    __INICJATYWA = 0

    def __init__(self, swiat, pozycja, tura_urodzenia):
        super(BarszczSosnowskiego, self).__init__(self.TypOrganizmu.BARSZCZ_SOSNOWSKIEGO,
                                                  swiat, pozycja, tura_urodzenia, self.__SILA, self.__INICJATYWA)
        self.set_kolor("#cc00cc")
        self.set_szansa_rozmnazania(0.05)

    def akcja(self):
        poz_x = self.get_pozycja().get_x()
        poz_y = self.get_pozycja().get_y()
        self.losowe_pole(self.get_pozycja())
        for i in range(4):
            tmp_organizm = None
            if i == 0 and not self.czy_kierunek_zablokowany(self.Kierunek.DOL):
                tmp_organizm = self.get_swiat().get_field(Punkt(poz_x, poz_y + 1))
            elif i == 1 and not self.czy_kierunek_zablokowany(self.Kierunek.GORA):
                tmp_organizm = self.get_swiat().get_field(Punkt(poz_x, poz_y - 1))
            elif i == 2 and not self.czy_kierunek_zablokowany(self.Kierunek.LEWO):
                tmp_organizm = self.get_swiat().get_field(Punkt(poz_x - 1, poz_y))
            elif i == 3 and not self.czy_kierunek_zablokowany(self.Kierunek.PRAWO):
                tmp_organizm = self.get_swiat().get_field(Punkt(poz_x + 1, poz_y))

            if tmp_organizm is not None and tmp_organizm.czy_jest_zwierzeciem() \
                    and tmp_organizm.get_typ_organizmu() != Organizm.TypOrganizmu.CYBER_OWCA:
                if isinstance(tmp_organizm, Czlowiek) and tmp_organizm.get_umiejetnosc().get_active():
                    tmp_organizm.uciekaj(self)
                else:
                    self.get_swiat().usun_organizm(tmp_organizm)
                    Logs.dodaj_komentarz(self.organizm_to_string() + " zabija " + tmp_organizm.organizm_to_string())
        tmp_losowanie = random.randint(0, 100)
        if tmp_losowanie < self.get_szansa_rozmnazania() * 100:
            self.rozprzestrzenianie()

    def __str__(self):
        return "Barszcz Sosnowskiego"

    def zdolnosckolizji(self, atakujacy, ofiara) -> bool:
        if atakujacy.get_sila() >= 10:
            self.get_swiat().usun_organizm(self)
            Logs.dodaj_komentarz(atakujacy.organizm_to_string() + " zjada " + self.organizm_to_string())
            atakujacy.ruch(ofiara.get_pozycja())
        if (atakujacy.czy_jest_zwierzeciem() and atakujacy.get_typ_organizmu() != Organizm.TypOrganizmu.CYBER_OWCA) \
                or atakujacy.get_sila() < 10:
            self.get_swiat().usun_organizm(atakujacy)
            Logs.dodaj_komentarz(self.organizm_to_string() + " zabija " + atakujacy.organizm_to_string())
        return True
