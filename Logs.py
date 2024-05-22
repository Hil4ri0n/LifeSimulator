class Logs:
    __content = ""

    @classmethod
    def dodaj_komentarz(cls, log):
        cls.__content += log + "\n"

    @classmethod
    def get_content(cls):
        return cls.__content

    @classmethod
    def wyczysc_komentarze(cls):
        cls.__content = ""
