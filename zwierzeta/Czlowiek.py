import random
from Logs import Logs
from Zwierze import Zwierze
from SuperZdolnosc import SuperZdolnosc
from Punkt import Punkt

class Czlowiek(Zwierze):
    __ZASIEG_RUCHU = 1
    __SZANSA_WYKONYWANIA_RUCHU = 1
    __SILA_CZLOWIEKA = 5
    __INICJATYWA_CZLOWIEKA = 4

    def __init__(self, swiat, pozycja, tura_urodzenia):
        super(Czlowiek, self).__init__(self.TypOrganizmu.CZLOWIEK, swiat, pozycja, tura_urodzenia, self.__SILA_CZLOWIEKA, self.__INICJATYWA_CZLOWIEKA)
        self.set_zasieg_ruchu(self.__ZASIEG_RUCHU)
        self.set_szansa_wykonywania_ruchu(self.__SZANSA_WYKONYWANIA_RUCHU)
        self.__kierunek = self.Kierunek.BRAK_KIERUNKU
        self.set_kolor(kolor="blue")
        self.__super_zdolnosc = SuperZdolnosc()

    def uciekaj(self, other):
        zaatakowany = self.get_swiat().get_field(self.get_pozycja())
        if isinstance(zaatakowany, Czlowiek):
            self.get_swiat().clear_field(self.get_pozycja())
        punkty = []
        x = self.get_pozycja().get_x()
        y = self.get_pozycja().get_y()

        if y - 1 >= 0:
            org = self.get_swiat().get_field(Punkt(x, y - 1))
            if org is None or org.get_sila() <= self.get_sila():
                punkty.append(Punkt(x, y - 1))
        if x - 1 >= 0:
            org = self.get_swiat().get_field(Punkt(x - 1, y))
            if org is None or org.get_sila() <= self.get_sila():
                punkty.append(Punkt(x - 1, y))
        if x + 1 < self.get_swiat().get_size_x():
            org = self.get_swiat().get_field(Punkt(x + 1, y))
            if org is None or org.get_sila() <= self.get_sila():
                punkty.append(Punkt(x + 1, y))
        if y + 1 < self.get_swiat().get_size_y():
            org = self.get_swiat().get_field(Punkt(x, y + 1))
            if org is None or org.get_sila() <= self.get_sila():
                punkty.append(Punkt(x, y + 1))

        if len(punkty) != 0:
            los = random.randint(0, len(punkty)-1)
            self.set_pozycja(punkty[los])
            if self.get_swiat().get_field(self.get_pozycja()) is not None:
                self.get_swiat().usun_organizm(self.get_swiat().get_field(self.get_pozycja()))
                self.get_swiat().clear_field(self.get_pozycja())
            self.get_swiat().set_field(self.get_pozycja(), self)
            Logs.dodaj_komentarz("Czlowiek uciekl z pola.")
        else:
            self.get_swiat().usun_organizm(self)
            Logs.dodaj_komentarz(other.organizm_to_string() + " zabija " + self.organizm_to_string())

        self.get_swiat().get_swiat_gui().odswiez_swiat()

    def nowa_pozycja(self) -> Punkt:
        x = self.get_pozycja().get_x()
        y = self.get_pozycja().get_y()
        self.losowe_pole(self.get_pozycja())  # BLOKUJE KIERUNKI NIEDOZWOLONE PRZY GRANICY SWIATA
        if self.__kierunek == self.Kierunek.BRAK_KIERUNKU or self.czy_kierunek_zablokowany(self.__kierunek):
            return self.get_pozycja()
        else:
            if self.__kierunek == self.Kierunek.DOL:
                return Punkt(x, y + 1)
            if self.__kierunek == self.Kierunek.GORA:
                return Punkt(x, y - 1)
            if self.__kierunek == self.Kierunek.LEWO:
                return Punkt(x - 1, y)
            if self.__kierunek == self.Kierunek.PRAWO:
                return Punkt(x + 1, y)
            return Punkt(x, y)

    def akcja(self):
        for i in range(self.get_zasieg_ruchu()):
            przyszla_pozycja = self.nowa_pozycja()

            if self.get_swiat().czy_pole_jest_zajete(przyszla_pozycja):
                organizm_na_polu = self.get_swiat().get_field(przyszla_pozycja)
                if organizm_na_polu != self:
                    self.kolizja(organizm_na_polu)
                    break
            else:
                self.ruch(przyszla_pozycja)

        self.__kierunek = self.Kierunek.BRAK_KIERUNKU
        self.__super_zdolnosc.zmiana()

    def __str__(self):
        return "Czlowiek"

    def get_umiejetnosc(self):
        return self.__super_zdolnosc

    def set_kierunek_ruchu(self, kierunek_ruchu):
        self.__kierunek = kierunek_ruchu