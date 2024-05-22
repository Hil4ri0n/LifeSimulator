class Punkt:
    def __init__(self):
        self.__x = 0
        self.__y = 0

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def __eq__(self, other):
        if isinstance(self, type(other)):
            return self.__x == other.__x and self.__y == other.__y
        else:
            return False

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

    def set_x(self, x: int) -> int:
        self.__x = x

    def set_y(self, y: int) -> int:
        self.__y = y
