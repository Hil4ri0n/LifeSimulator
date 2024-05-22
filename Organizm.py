from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum
from Punkt import Punkt
import random


class Organizm(ABC):

    LICZBA_GATUNKOW = 12

    class TypOrganizmu(Enum):
        CZLOWIEK = 1
        WILK = 2
        OWCA = 3
        LIS = 4
        ZOLW = 5
        ANTYLOPA = 6
        CYBER_OWCA = 7
        TRAWA = 8
        MLECZ = 9
        GUARANA = 10
        WILCZE_JAGODY = 11
        BARSZCZ_SOSNOWSKIEGO = 12

    class Kierunek(Enum):
        LEWO = 0
        PRAWO = 1
        GORA = 2
        DOL = 3
        BRAK_KIERUNKU = 4

        def __init__(self, value: int):
            self.__value = value

        def getValue(self) -> int:
            return self.__value

    @abstractmethod
    def akcja(self):
        pass

    @abstractmethod
    def kolizja(self, other: Organizm):
        pass

    @staticmethod
    def czy_jest_zwierzeciem() -> bool:
        pass

    def __init__(self, typOrganizmu: TypOrganizmu, swiat, pozycja: Punkt, turaNarodzin: int, sila: int, inicjatywa: int):
        self.__typOrganizmu = typOrganizmu
        self.__swiat = swiat
        self.__pozycja = pozycja
        self.__turaNarodzin = turaNarodzin
        self.__sila = sila
        self.__inicjatywa = inicjatywa
        self.__isDead = False
        self.__kierunek = [True, True, True, True]
        self.__czy_sie_rozmnazal = None
        self.__kolor = None
        self.__szansa_rozmnazania = 1

    def zdolnosckolizji(self, atakujacy, ofiara) -> bool:
        return False

    def __str__(self):
        return "Organizm"

    def organizm_to_string(self) -> str:
        return (str(self) + " x[" + str(self.__pozycja.get_x()) + "] y["
                + str(self.__pozycja.get_y()) + "] sila[" + str(self.__sila) + "]")

    def ruch(self, przyszlapozycja: Punkt):
        x = przyszlapozycja.get_x()
        y = przyszlapozycja.get_y()
        self.__swiat.get_plansza()[self.__pozycja.get_y()][self.__pozycja.get_x()] = None
        self.__swiat.get_plansza()[y][x] = self
        self.__pozycja.set_x(x)
        self.__pozycja.set_y(y)

    @classmethod
    def losuj_typ(cls):
        tmp = random.randint(0, cls.LICZBA_GATUNKOW - 1)
        if tmp == 0:
            return cls.TypOrganizmu.ANTYLOPA
        if tmp == 1:
            return cls.TypOrganizmu.BARSZCZ_SOSNOWSKIEGO
        if tmp == 2:
            return cls.TypOrganizmu.GUARANA
        if tmp == 3:
            return cls.TypOrganizmu.LIS
        if tmp == 4:
            return cls.TypOrganizmu.MLECZ
        if tmp == 5:
            return cls.TypOrganizmu.OWCA
        if tmp == 6:
            return cls.TypOrganizmu.TRAWA
        if tmp == 7:
            return cls.TypOrganizmu.WILCZE_JAGODY
        if tmp == 8:
            return cls.TypOrganizmu.WILK
        if tmp == 9:
            return cls.TypOrganizmu.CYBER_OWCA
        else:
            return cls.TypOrganizmu.ZOLW

    def losowe_pole(self, pozycja: Punkt) -> Punkt:
        self.allow_all_dirs()
        poz_x = pozycja.get_x()
        poz_y = pozycja.get_y()
        size_x = self.__swiat.get_size_x()
        size_y = self.__swiat.get_size_y()
        ile_kierunkow_mozliwych = 0

        if poz_x == 0:
            self.delete_direction(self.Kierunek.LEWO)
        else:
            ile_kierunkow_mozliwych += 1
        if poz_x == size_x - 1:
            self.delete_direction(self.Kierunek.PRAWO)
        else:
            ile_kierunkow_mozliwych += 1
        if poz_y == 0:
            self.delete_direction(self.Kierunek.GORA)
        else:
            ile_kierunkow_mozliwych += 1
        if poz_y == size_y - 1:
            self.delete_direction(self.Kierunek.DOL)
        else:
            ile_kierunkow_mozliwych += 1

        if ile_kierunkow_mozliwych == 0:
            return pozycja

        while True:
            upperbound = 100
            tmp_losowanie = random.randint(0,100)
            if tmp_losowanie < 25 and not self.czy_kierunek_zablokowany(self.Kierunek.LEWO):
                return Punkt(poz_x - 1, poz_y)
            elif tmp_losowanie < 50 and not self.czy_kierunek_zablokowany(self.Kierunek.PRAWO):
                return Punkt(poz_x + 1, poz_y)
            elif tmp_losowanie < 75 and not self.czy_kierunek_zablokowany(self.Kierunek.GORA):
                return Punkt(poz_x, poz_y - 1)
            elif not self.czy_kierunek_zablokowany(self.Kierunek.DOL):
                return Punkt(poz_x, poz_y + 1)

    def losowe_puste_pole(self, pozycja: Punkt) -> Punkt:
        self.allow_all_dirs()
        poz_x = pozycja.get_x()
        poz_y = pozycja.get_y()
        size_x = self.__swiat.get_size_x()
        size_y = self.__swiat.get_size_y()
        ile_kierunkow_mozliwych = 0

        if poz_x == 0 or self.__swiat.czy_pole_jest_zajete(Punkt(poz_x - 1, poz_y)):
            self.delete_direction(self.Kierunek.LEWO)
        else:
            ile_kierunkow_mozliwych += 1

        if poz_x == size_x - 1 or self.__swiat.czy_pole_jest_zajete(Punkt(poz_x + 1, poz_y)):
            self.delete_direction(self.Kierunek.PRAWO)
        else:
            ile_kierunkow_mozliwych += 1

        if poz_y == 0 or self.__swiat.czy_pole_jest_zajete(Punkt(poz_x, poz_y - 1)):
            self.delete_direction(self.Kierunek.GORA)
        else:
            ile_kierunkow_mozliwych += 1

        if poz_y == size_y - 1 or self.__swiat.czy_pole_jest_zajete(Punkt(poz_x, poz_y + 1)):
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

    def delete_direction(self, kierunek: Kierunek):
        self.__kierunek[kierunek.getValue()] = False

    def allow_direction(self, kierunek: Kierunek):
        self.__kierunek[kierunek.getValue()] = True

    def allow_all_dirs(self):
        self.allow_direction(self.Kierunek.LEWO)
        self.allow_direction(self.Kierunek.PRAWO)
        self.allow_direction(self.Kierunek.GORA)
        self.allow_direction(self.Kierunek.DOL)

    def czy_kierunek_zablokowany(self, kierunek: Kierunek) -> bool:
        return not self.__kierunek[kierunek.getValue()]

    def get_sila(self):
        return self.__sila

    def get_inicjatywa(self):
        return self.__inicjatywa

    def get_tura_narodzin(self):
        return self.__turaNarodzin

    def get_dead(self):
        return self.__isDead

    def get_czy_sie_rozmnazal(self):
        return self.__czy_sie_rozmnazal

    def get_swiat(self):
        return self.__swiat

    def get_pozycja(self):
        return self.__pozycja

    def get_typ_organizmu(self):
        return self.__typOrganizmu

    def get_kolor(self):
        return self.__kolor

    def set_sila(self, sila):
        self.__sila = sila

    def set_inicjatywa(self, inicjatywa):
        self.__inicjatywa = inicjatywa

    def set_tura_narodzin(self, tura_narodzin):
        self.__turaNarodzin = tura_narodzin

    def set_dead(self, is_dead):
        self.__isDead = is_dead

    def set_czy_sie_rozmnazal(self, czy_sie_rozmnazal):
        self.__czy_sie_rozmnazal = czy_sie_rozmnazal

    def set_swiat(self, swiat):
        self.__swiat = swiat

    def set_pozycja(self, pozycja):
        self.__pozycja = pozycja

    def set_typ_organizmu(self, typ_organizmu):
        self.__typOrganizmu = typ_organizmu

    def set_kolor(self, kolor):
        self.__kolor = kolor

    def get_szansa_rozmnazania(self):
        return self.__szansa_rozmnazania

    def set_szansa_rozmnazania(self, szansa_rozmnazania):
        self.__szansa_rozmnazania = szansa_rozmnazania





