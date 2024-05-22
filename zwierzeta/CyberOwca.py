from zwierzeta.Owca import Owca
from Punkt import Punkt
from rosliny.BarszczSosnowskiego import BarszczSosnowskiego


class CyberOwca(Owca):
    __ZASIEG_RUCHU = 1
    __SZANSA_WYKONYWANIA_RUCHU = 1
    __SILA = 11
    __INICJATYWA = 4

    def __init__(self, swiat, pozycja, tura_urodzenia):
        super(CyberOwca, self).__init__(swiat, pozycja, tura_urodzenia)
        self.set_typ_organizmu(self.TypOrganizmu.CYBER_OWCA)
        self.set_sila(self.__SILA)
        self.set_inicjatywa(self.__INICJATYWA)
        self.set_zasieg_ruchu(self.__ZASIEG_RUCHU)
        self.set_szansa_rozmnazania(0.1)
        self.set_szansa_wykonywania_ruchu(self.__SZANSA_WYKONYWANIA_RUCHU)
        self.set_kolor("black")

    def losowe_pole(self, pozycja: Punkt) -> Punkt:
        if self.get_swiat().czy_istnieje_barszcz_sosnowskiego():
            najblizszy_barszcz = self.namierz_barszcz()
            cel = najblizszy_barszcz.get_pozycja()
            dx = abs(pozycja.get_x() - cel.get_x())
            dy = abs(pozycja.get_y() - cel.get_y())
            if dx >= dy:
                if pozycja.get_x() > cel.get_x():
                    return Punkt(pozycja.get_x() - 1, pozycja.get_y())
                else:
                    return Punkt(pozycja.get_x() + 1, pozycja.get_y())
            else:
                if pozycja.get_y() > cel.get_y():
                    return Punkt(pozycja.get_x(), pozycja.get_y() - 1)
                else:
                    return Punkt(pozycja.get_x(), pozycja.get_y() + 1)
        else:
            return super().losowe_pole(pozycja)

    def namierz_barszcz(self):
        tmp_barszcz = None
        najmniesza_odl = self.get_swiat().get_size_x() + self.get_swiat().get_size_y() + 1
        for i in range(self.get_swiat().get_size_y()):
            for j in range(self.get_swiat().get_size_x()):
                tmp_organizm = self.get_swiat().get_plansza()[i][j]
                if tmp_organizm is not None\
                        and tmp_organizm.get_typ_organizmu() == self.TypOrganizmu.BARSZCZ_SOSNOWSKIEGO:
                    dx = abs(self.get_pozycja().get_x() - tmp_organizm.get_pozycja().get_x())
                    dy = abs(self.get_pozycja().get_y() - tmp_organizm.get_pozycja().get_y())
                    tmp_odl = dx + dy
                    if najmniesza_odl > tmp_odl:
                        najmniesza_odl = tmp_odl
                        tmp_barszcz = tmp_organizm

        return tmp_barszcz

    def __str__(self):
        return "Cyber owca"
