from zwierzeta import *
from rosliny import *
from Organizm import Organizm


class OrganismCreator:
    @staticmethod
    def create_new_organism(typ_organizmu: Organizm.TypOrganizmu, swiat, pozycja):
        if typ_organizmu == Organizm.TypOrganizmu.WILK:
            return Wilk.Wilk(swiat, pozycja, swiat.get_numer_tury())
        if typ_organizmu == Organizm.TypOrganizmu.OWCA:
            return Owca.Owca(swiat, pozycja, swiat.get_numer_tury())
        if typ_organizmu == Organizm.TypOrganizmu.LIS:
            return Lis.Lis(swiat, pozycja, swiat.get_numer_tury())
        if typ_organizmu == Organizm.TypOrganizmu.ZOLW:
            return Zolw.Zolw(swiat, pozycja, swiat.get_numer_tury())
        if typ_organizmu == Organizm.TypOrganizmu.ANTYLOPA:
            return Antylopa.Antylopa(swiat, pozycja, swiat.get_numer_tury())
        if typ_organizmu == Organizm.TypOrganizmu.CZLOWIEK:
            return Czlowiek.Czlowiek(swiat, pozycja, swiat.get_numer_tury())
        if typ_organizmu == Organizm.TypOrganizmu.TRAWA:
            return Trawa.Trawa(swiat, pozycja, swiat.get_numer_tury())
        if typ_organizmu == Organizm.TypOrganizmu.MLECZ:
            return Mlecz.Mlecz(swiat, pozycja, swiat.get_numer_tury())
        if typ_organizmu == Organizm.TypOrganizmu.GUARANA:
            return Guarana.Guarana(swiat, pozycja, swiat.get_numer_tury())
        if typ_organizmu == Organizm.TypOrganizmu.BARSZCZ_SOSNOWSKIEGO:
            return BarszczSosnowskiego.BarszczSosnowskiego(swiat, pozycja, swiat.get_numer_tury())
        if typ_organizmu == Organizm.TypOrganizmu.CYBER_OWCA:
            return CyberOwca.CyberOwca(swiat, pozycja, swiat.get_numer_tury())
        if typ_organizmu == Organizm.TypOrganizmu.WILCZE_JAGODY:
            return WilczeJagody.WilczeJagody(swiat, pozycja, swiat.get_numer_tury())
        return None


