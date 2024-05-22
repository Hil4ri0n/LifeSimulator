from Organizm import Organizm
import random
from Punkt import Punkt
from Logs import Logs


class Roslina(Organizm):
    def __intit__(self, typ_organizmu, swiat, pozycja, tura_urodzenia, sila, inicjatywa):
        super(Roslina, self).__init__(typ_organizmu, swiat, pozycja, tura_urodzenia, sila, inicjatywa)
        self.set_szansa_rozmnazania(0.3)

    def akcja(self):
        upperbound = 100
        tmp_losowanie = random.randint(0, upperbound)
        if tmp_losowanie < self.get_szansa_rozmnazania() * 100:
            self.rozprzestrzenianie()

    @staticmethod
    def czy_jest_zwierzeciem() -> bool:
        return False

    def rozprzestrzenianie(self):
        tmp_punkt = self.losowe_puste_pole(self.get_pozycja())
        if tmp_punkt == self.get_pozycja():
            return
        else:
            from OrganismCreator import OrganismCreator
            tmp_organizm = OrganismCreator.create_new_organism(self.get_typ_organizmu(), self.get_swiat(), tmp_punkt)
            Logs.dodaj_komentarz("Rosnie nowa roslina " + tmp_organizm.organizm_to_string())
            self.get_swiat().dodaj_organizm(tmp_organizm)

    def kolizja(self, other: Organizm):
        pass
