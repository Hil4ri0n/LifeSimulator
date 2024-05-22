from Organizm import Organizm
import random
from Punkt import Punkt
from Logs import Logs


class Zwierze(Organizm):

    def __init__(self, typ_organizmu, swiat, pozycja, tura_urodzenia, sila, inicjatywa):
        super(Zwierze, self).__init__(typ_organizmu, swiat, pozycja, tura_urodzenia, sila, inicjatywa)
        self.set_czy_sie_rozmnazal(False)
        self.set_szansa_rozmnazania(0.5)
        self.__zasieg_ruchu = None
        self.__szansa_wykonywania_ruchu = None

    def akcja(self):
        for i in range(0, self.__zasieg_ruchu):
            przyszla_pozycja = self.nowa_pozycja()
            if self.get_swiat().czy_pole_jest_zajete(przyszla_pozycja) \
                    and self.get_swiat().get_field(przyszla_pozycja) != self:
                self.kolizja(self.get_swiat().get_field(przyszla_pozycja))
                break
            elif self.get_swiat().get_field(przyszla_pozycja) != self:
                self.ruch(przyszla_pozycja)

    def kolizja(self, other: Organizm):
        if self.get_typ_organizmu() == other.get_typ_organizmu():
            if random.randint(0, 100) < self.get_szansa_rozmnazania() * 100:
                self.rozmnazanie(other)
        else:
            if other.zdolnosckolizji(self,other) or self.zdolnosckolizji(self, other):
                return

            from zwierzeta.Czlowiek import Czlowiek
            if self.get_sila() >= other.get_sila():
                if isinstance(other, Czlowiek) and other.get_umiejetnosc().get_active():
                    other.uciekaj(self)
                else:
                    self.get_swiat().usun_organizm(other)
                    self.ruch(other.get_pozycja())
                    Logs.dodaj_komentarz(self.organizm_to_string() + " zabija " + other.organizm_to_string())
            else:
                if isinstance(self, Czlowiek) and self.get_umiejetnosc().get_active():
                    self.uciekaj(other)
                else:
                    self.get_swiat().usun_organizm(self)
                    Logs.dodaj_komentarz(other.organizm_to_string() + " zabija " + self.organizm_to_string())

    @staticmethod
    def czy_jest_zwierzeciem() -> bool:
        return True

    def nowa_pozycja(self) -> Punkt:
        tmp_losowanie = random.randint(0, 100)

        if tmp_losowanie >= self.__szansa_wykonywania_ruchu * 100:
            return self.get_pozycja()
        else:
            return self.losowe_pole(self.get_pozycja())

    def rozmnazanie(self, other: Organizm):
        if self.get_czy_sie_rozmnazal() or other.get_czy_sie_rozmnazal():
            return

        tmp_punkt = self.losowe_puste_pole(self.get_pozycja())
        if tmp_punkt == self.get_pozycja():
            tmp_punkt = other.losowe_puste_pole(other.get_pozycja())
            if tmp_punkt == other.get_pozycja():
                return

        from OrganismCreator import OrganismCreator
        tmp_organizm = OrganismCreator.create_new_organism(self.get_typ_organizmu(), self.get_swiat(), tmp_punkt)
        Logs.dodaj_komentarz("Urodzil sie " + tmp_organizm.organizm_to_string())
        self.get_swiat().dodaj_organizm(tmp_organizm)
        self.set_czy_sie_rozmnazal(True)
        other.set_czy_sie_rozmnazal(True)

    def get_zasieg_ruchu(self) -> int:
        return self.__zasieg_ruchu

    def set_zasieg_ruchu(self, zasieg_ruchu: int):
        self.__zasieg_ruchu = zasieg_ruchu

    def get_szansa_wykonywania_ruchu(self) -> float:
        return self.__szansa_wykonywania_ruchu

    def set_szansa_wykonywania_ruchu(self, szansa_wykonywania_ruchu: float):
        self.__szansa_wykonywania_ruchu = szansa_wykonywania_ruchu


