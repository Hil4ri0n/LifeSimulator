import math
import random
from Logs import Logs
from OrganismCreator import OrganismCreator
from Punkt import Punkt
from Organizm import Organizm
from typing import List
from zwierzeta.Czlowiek import Czlowiek


class Swiat:
    def __init__(self, size_x, size_y, graph_ui):
        self.__organizmy = []
        self.__graph_ui = graph_ui
        self.__size_x = size_x
        self.__size_y = size_y
        self.__czy_czlowiek_zyje = True
        self.__czy_jest_koniec_gry = False
        self.__pauza = True
        self.__numer_tury = 0
        self.__plansza = [[None for x in range(self.__size_x)] for y in range(self.__size_y)]
        self.__czlowiek = None

    def zapisz_swiat(self, nazwa_pliku):
        try:
            with open(nazwa_pliku + ".txt", "w") as file:
                file.write(
                    f"{self.__size_x} {self.__size_y} {self.__numer_tury} {self.__czy_czlowiek_zyje} {self.__czy_jest_koniec_gry}\n")
                for organizm in self.__organizmy:
                    line = f"{organizm.get_typ_organizmu()} {organizm.get_pozycja().get_x()} {organizm.get_pozycja().get_y()} {organizm.get_sila()} {organizm.get_tura_narodzin()} {organizm.get_dead()}"
                    if organizm.get_typ_organizmu() == Organizm.TypOrganizmu.CZLOWIEK:
                        czlowiek = organizm
                        line += f" {czlowiek.get_umiejetnosc().get_czas_trwania()} {czlowiek.get_umiejetnosc().get_cooldown()} {czlowiek.get_umiejetnosc().get_active()} {czlowiek.get_umiejetnosc().get_available()}"
                    file.write(line + "\n")
        except IOError as e:
            print("Error:", e)

    @staticmethod
    def odtworz_swiat(name_of_file):
        try:
            name_of_file += ".txt"
            file = open(name_of_file, "r")

            line = file.readline()
            properties = line.rstrip().split(" ")
            size_x = int(properties[0])
            size_y = int(properties[1])
            tmp_swiat = Swiat(size_x, size_y, None)
            numer_tury = int(properties[2])
            tmp_swiat.__numer_tury = numer_tury
            czy_czlowiek_zyje = Swiat.string_to_bool(properties[3])
            tmp_swiat.__czy_czlowiek_zyje = czy_czlowiek_zyje
            czy_jest_koniec_gry = Swiat.string_to_bool(properties[4])
            tmp_swiat.__czy_jest_koniec_gry = czy_jest_koniec_gry
            tmp_swiat.__czlowiek = None

            for line in file.readlines():
                properties = line.rstrip().split(" ")
                typ_organizmu = Organizm.TypOrganizmu[properties[0].split(".")[1]]
                x = int(properties[1])
                y = int(properties[2])

                tmp_organizm = OrganismCreator.create_new_organism(typ_organizmu, tmp_swiat, Punkt(x, y))
                sila = int(properties[3])
                tmp_organizm.set_sila(sila)
                tura_urodzenia = int(properties[4])
                tmp_organizm.set_tura_narodzin(tura_urodzenia)
                czy_umarl = Swiat.string_to_bool(properties[5])
                tmp_organizm.set_dead(czy_umarl)

                if typ_organizmu == Organizm.TypOrganizmu.CZLOWIEK:
                    tmp_swiat.set_czlowiek(tmp_organizm)
                    czas_trwania = int(properties[6])
                    tmp_swiat.get_czlowiek().get_umiejetnosc().set_czas_trwania(czas_trwania)
                    cooldown = int(properties[7])
                    tmp_swiat.get_czlowiek().get_umiejetnosc().set_cooldown(cooldown)
                    czy_jest_aktywna = Swiat.string_to_bool(properties[8])
                    tmp_swiat.get_czlowiek().get_umiejetnosc().set_active(czy_jest_aktywna)
                    czy_mozna_aktywowac = Swiat.string_to_bool(properties[9])
                    tmp_swiat.get_czlowiek().get_umiejetnosc().set_available(czy_mozna_aktywowac)

                tmp_swiat.dodaj_organizm(tmp_organizm)

            file.close()
            return tmp_swiat
        except IOError as e:
            print("Error:", e)
        return None

    @staticmethod
    def string_to_bool(string):
        if string == "True":
            return True
        else:
            return False

    def create_world(self, zapelnienie_swiata: float):
        liczba_organizmow = int(math.floor(self.__size_x * self.__size_y * zapelnienie_swiata))
        pozycja = self.losowe_wolne_pole()
        tmp_organizm = OrganismCreator.create_new_organism(Organizm.TypOrganizmu.CZLOWIEK, self, pozycja)
        self.dodaj_organizm(tmp_organizm)
        self.__czlowiek = tmp_organizm

        for i in range(liczba_organizmow - 1):
            pozycja = self.losowe_wolne_pole()
            if pozycja == Punkt(-1, -1):
                return
            self.dodaj_organizm(OrganismCreator.create_new_organism(Organizm.losuj_typ(), self, pozycja))

    def wykonaj_ture(self):
        if self.__czy_jest_koniec_gry:
            return
        self.__numer_tury += 1
        Logs.dodaj_komentarz(f"\nTURA {self.__numer_tury}")
        print(self.__numer_tury)
        print(str(self.__organizmy.__sizeof__()) + "\n")
        self.sortuj_organizmy()
        for i in range(len(self.__organizmy)):
            if self.__organizmy[i].get_tura_narodzin != self.__numer_tury \
                    and self.__organizmy[i].get_dead() == False:
                self.__organizmy[i].akcja()
        i = 0
        while i < len(self.__organizmy):
            if self.__organizmy[i].get_dead() == True:
                del self.__organizmy[i]
                i -= 1
            i += 1
        for i in range(len(self.__organizmy)):
            self.__organizmy[i].set_czy_sie_rozmnazal(False)

    def sortuj_organizmy(self):
        self.__organizmy.sort(key=lambda o: (o.get_inicjatywa(), o.get_tura_narodzin()), reverse=True)

    def losowe_wolne_pole(self) -> Punkt:
        for i in range(self.__size_y):
            for j in range(self.__size_x):
                if self.__plansza[i][j] is None:
                    while True:
                        x = random.randint(0,self.__size_x-1)
                        y = random.randint(0,self.__size_y-1)
                        if self.__plansza[y][x] is None:
                            return Punkt(x, y)
        return Punkt(-1, -1)

    def czy_pole_jest_zajete(self, pole: Punkt) -> bool:
        if self.__plansza[pole.get_y()][pole.get_x()] is None:
            return False
        else:
            return True

    def get_field(self, pole: Punkt) -> Organizm:
        return self.__plansza[pole.get_y()][pole.get_x()]

    def clear_field(self, pole: Punkt):
        self.__plansza[pole.get_y()][pole.get_x()] = None

    def set_field(self, pole: Punkt, organizm: Organizm):
        self.__plansza[pole.get_y()][pole.get_x()] = organizm

    def dodaj_organizm(self, organizm: Organizm):
        self.__organizmy.append(organizm)
        self.__plansza[organizm.get_pozycja().get_y()][organizm.get_pozycja().get_x()] = organizm

    def usun_organizm(self, organizm: Organizm):
        self.__plansza[organizm.get_pozycja().get_y()][organizm.get_pozycja().get_x()] = None
        organizm.set_dead(True)
        if organizm.get_typ_organizmu() == Organizm.TypOrganizmu.CZLOWIEK:
            self.__czy_czlowiek_zyje = False
            self.__czlowiek = None

    def get_size_x(self) -> int:
        return self.__size_x

    def get_size_y(self) -> int:
        return self.__size_y

    def get_numer_tury(self) -> int:
        return self.__numer_tury

    def get_plansza(self) -> List[List[Organizm]]:
        return self.__plansza

    def get_czy_czlowiek_zyje(self) -> bool:
        return self.__czy_czlowiek_zyje

    def get_czy_jest_koniec_gry(self) -> bool:
        return self.__czy_jest_koniec_gry

    def get_organizmy(self) -> List[Organizm]:
        return self.__organizmy

    def get_czlowiek(self) -> Czlowiek:
        return self.__czlowiek

    def set_czlowiek(self, czlowiek: Czlowiek):
        self.__czlowiek = czlowiek

    def set_czy_czlowiek_zyje(self, czy_czlowiek_zyje: bool):
        self.__czy_czlowiek_zyje = czy_czlowiek_zyje

    def set_czy_jest_koniec_gry(self, czy_jest_koniec_gry: bool):
        self.__czy_jest_koniec_gry = czy_jest_koniec_gry

    def is_pauza(self) -> bool:
        return self.__pauza

    def set_pauza(self, pauza: bool):
        self.__pauza = pauza

    def get_swiat_gui(self):
        return self.__graph_ui

    def set_swiat_gui(self, graph_ui):
        self.__graph_ui = graph_ui

    def czy_istnieje_barszcz_sosnowskiego(self) -> bool:
        for i in range(self.__size_y):
            for j in range(self.__size_x):
                if self.__plansza[i][j] is not None and \
                        self.__plansza[i][j].get_typ_organizmu() == Organizm.TypOrganizmu.BARSZCZ_SOSNOWSKIEGO:
                    return True
        return False
