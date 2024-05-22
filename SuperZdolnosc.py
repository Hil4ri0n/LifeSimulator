class SuperZdolnosc:
    __CZAS_TRWANIA_ZDOLNOSCI = 5
    __COOLDOWN_ZDOLNOSCI = 10

    def __init__(self):
        self.__coldown = 0
        self.__czas_trwania = 0
        self.__is_active = False
        self.__is_available = True

    def zmiana(self):
        if self.__coldown > 0:
            self.__coldown -= 1
        if self.__czas_trwania > 0:
            self.__czas_trwania -= 1
        if self.__czas_trwania == 0:
            self.dezaktywuj()
        if self.__coldown == 0:
            self.__is_available = True

    def aktywuj(self):
        if self.__coldown == 0:
            self.__is_active = True
            self.__is_available = False
            self.__coldown = self.__COOLDOWN_ZDOLNOSCI
            self.__czas_trwania = self.__CZAS_TRWANIA_ZDOLNOSCI

    def dezaktywuj(self):
        self.__is_active = False

    def get_available(self) -> bool:
        return self.__is_available

    def set_available(self, available: bool):
        self.__is_available = available

    def get_active(self) -> bool:
        return self.__is_active

    def set_active(self, active: bool):
        self.__is_active = active

    def get_czas_trwania(self) -> int:
        return self.__czas_trwania

    def set_czas_trwania(self, czas_trwania: int):
        self.__czas_trwania = czas_trwania

    def get_cooldown(self) -> int:
        return self.__coldown

    def set_cooldown(self, cooldown: int):
        self.__coldown = cooldown
