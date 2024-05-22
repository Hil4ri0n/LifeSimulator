import random

from Zwierze import Zwierze
from Punkt import Punkt

class Lis(Zwierze):
    __ZASIEG_RUCHU = 1
    __SZANSA_WYKONYWANIA_RUCHU = 1
    __SILA = 3
    __INICJATYWA = 7

    def __init__(self, swiat, pozycja, tura_urodzenia):
        super(Lis, self).__init__(self.TypOrganizmu.LIS, swiat, pozycja, tura_urodzenia, self.__SILA, self.__INICJATYWA)
        self.set_zasieg_ruchu(self.__ZASIEG_RUCHU)
        self.set_szansa_wykonywania_ruchu(self.__SZANSA_WYKONYWANIA_RUCHU)
        self.set_kolor("#ff8000")

    def __str__(self):
        return "Lis"

    def losowe_pole(self, pozycja: Punkt) -> Punkt:
        self.allow_all_dirs()
        poz_x = pozycja.get_x()
        poz_y = pozycja.get_y()
        size_x = self.get_swiat().get_size_x()
        size_y = self.get_swiat().get_size_y()
        ile_kierunkow_mozliwych = 0

        if poz_x == 0:
            self.delete_direction(self.Kierunek.LEWO)
        else:
            tmp_organizm = self.get_swiat().get_plansza()[poz_y][poz_x - 1]
            if tmp_organizm is not None and tmp_organizm.get_sila() > self.get_sila():
                self.delete_direction(self.Kierunek.LEWO)
            else:
                ile_kierunkow_mozliwych += 1

        if poz_x == size_x - 1:
            self.delete_direction(self.Kierunek.PRAWO)
        else:
            tmp_organizm = self.get_swiat().get_plansza()[poz_y][poz_x + 1]
            if tmp_organizm is not None and tmp_organizm.get_sila() > self.get_sila():
                self.delete_direction(self.Kierunek.PRAWO)
            else:
                ile_kierunkow_mozliwych += 1

        if poz_y == 0:
            self.delete_direction(self.Kierunek.GORA)
        else:
            tmp_organizm = self.get_swiat().get_plansza()[poz_y - 1][poz_x]
            if tmp_organizm is not None and tmp_organizm.get_sila() > self.get_sila():
                self.delete_direction(self.Kierunek.GORA)
            else:
                ile_kierunkow_mozliwych += 1

        if poz_y == size_y - 1:
            self.delete_direction(self.Kierunek.DOL)
        else:
            tmp_organizm = self.get_swiat().get_plansza()[poz_y + 1][poz_x]
            if tmp_organizm is not None and tmp_organizm.get_sila() > self.get_sila():
                self.delete_direction(self.Kierunek.DOL)
            else:
                ile_kierunkow_mozliwych += 1

        if ile_kierunkow_mozliwych == 0:
            return Punkt(poz_x, poz_y)

        while True:
            tmp_losowanie = random.randint(0, 100)
            if tmp_losowanie < 25 and not self.czy_kierunek_zablokowany(self.Kierunek.LEWO):
                return Punkt(poz_x - 1, poz_y)
            elif tmp_losowanie < 50 and not self.czy_kierunek_zablokowany(self.Kierunek.PRAWO):
                return Punkt(poz_x + 1, poz_y)
            elif tmp_losowanie < 75 and not self.czy_kierunek_zablokowany(self.Kierunek.GORA):
                return Punkt(poz_x, poz_y - 1)
            elif not self.czy_kierunek_zablokowany(self.Kierunek.DOL):
                return Punkt(poz_x, poz_y + 1)
