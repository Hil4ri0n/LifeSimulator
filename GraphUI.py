import tkinter as tk
from Logs import Logs
from OrganismCreator import OrganismCreator
from Organizm import Organizm
from Punkt import Punkt
from Swiat import Swiat


class GUI:
    class KomentarzeLayout(tk.Frame):
        def __init__(self, main_panel, grafika_planszy, width, height):
            super().__init__(main_panel, bg="gray", width=width,
                             height=height)
            self.__grafika_planszy = grafika_planszy

            self.__tekst = ""
            self.__instruction = "Autor: Piotr Kolasinski 193275\nStrzałki - ruch człowieka\nP - aktywacja umiejętności\nEnter - przejście do następnej tury\n"
            self.__text_area = tk.Text(self, bg="gray", fg="white")
            self.__text_area.configure(state='disabled')
            self.__text_area.tag_configure("center", justify='center')
            self.pack(pady=10)
            self.__text_area.pack()

        def odswiez_komentarze(self):
            self.__tekst = self.__instruction + Logs.get_content()
            self.__text_area.configure(state='normal')
            self.__text_area.delete("1.0", tk.END)
            self.__text_area.insert(tk.END, self.__tekst)
            self.__text_area.tag_add("center", "1.0", "end")
            self.__text_area.configure(state='disabled')

    def __init__(self, title):
        self.__root = tk.Tk()
        self.__root.title(title)
        self.__root.geometry("800x600")

        screen_width = 800
        screen_height = 600

        menu_bar = tk.Menu(self.__root)
        menu = tk.Menu(menu_bar, tearoff=0)
        menu.add_command(label="Nowa gra", command=self.show_dimensions_window)
        menu.add_command(label="Wczytaj", command=self.load)
        menu.add_command(label="Zapisz", command=self.save)
        menu.add_separator()
        menu.add_command(label="Wyjscie", command=self.exit)
        menu_bar.add_cascade(label="Menu", menu=menu)
        self.__root.config(menu=menu_bar)

        self.__map_height = screen_height
        self.__map_width = screen_width // 3 * 2
        self.__left_bar_width = screen_width // 3
        self.__left_bar_height = screen_height

        self.__left_bar = tk.Frame(self.__root, bg="light yellow", width=self.__left_bar_width, height=self.__left_bar_height)
        self.__left_bar.pack(side=tk.LEFT)
        self.__komentarze_layout = self.KomentarzeLayout(self.__left_bar, self, self.__left_bar_width, self.__left_bar_height // 5 * 3)
        # self.komentarze_layout.pack(pady=10)

        self.__map_section = tk.Frame(self.__root, bg="light blue", width=self.__map_width, height=self.__map_height)
        self.__map_section.pack(side=tk.LEFT)

        self.__legend_section = tk.Frame(self.__left_bar, bg="white", width=self.__left_bar_width, height=self.__left_bar_height // 5 * 2)
        self.__legend_section.pack(pady=10)
        legend_button_width = self.__left_bar_width // 3
        legend_button_height = self.__left_bar_height // 10
        pixel = tk.PhotoImage(width=1, height=1)
        button = tk.Button(self.__legend_section, bg="#a27c36", image=pixel, text="Antylopa", width=legend_button_width, height=legend_button_height, compound="center")
        button.grid(row=0, column=0, padx=1, pady=1)
        button = tk.Button(self.__legend_section, bg="black", image=pixel, fg="white", text="CyberOwca", width=legend_button_width, height=legend_button_height, compound="center")
        button.grid(row=0, column=1, padx=1, pady=1)
        button = tk.Button(self.__legend_section, bg="blue", image=pixel, text="Czlowiek", width=legend_button_width, height=legend_button_height, compound="center")
        button.grid(row=0, column=2, padx=1, pady=1)
        button = tk.Button(self.__legend_section, bg="#ff8000", image=pixel, text="Lis", width=legend_button_width, height=legend_button_height, compound="center")
        button.grid(row=0, column=3, padx=1, pady=1)
        button = tk.Button(self.__legend_section, bg="#ff99cc", image=pixel, text="Owca", width=legend_button_width, height=legend_button_height, compound="center")
        button.grid(row=0, column=4, padx=1, pady=1)
        button = tk.Button(self.__legend_section, bg="#558bd8", image=pixel, text="Wilk", width=legend_button_width, height=legend_button_height, compound="center")
        button.grid(row=0, column=5, padx=1, pady=1)
        button = tk.Button(self.__legend_section, bg="#2cfec5", image=pixel, text="Zolw", width=legend_button_width, height=legend_button_height, compound="center")
        button.grid(row=1, column=0, padx=1, pady=1)
        button = tk.Button(self.__legend_section, bg="#cc00cc", image=pixel, text="Barszcz\nSosnowskiego", width=legend_button_width, height=legend_button_height, compound="center")
        button.grid(row=1, column=1, padx=1, pady=1)
        button = tk.Button(self.__legend_section, bg="#dc143c", image=pixel, text="Guarana", width=legend_button_width, height=legend_button_height, compound="center")
        button.grid(row=1, column=2, padx=1, pady=1)
        button = tk.Button(self.__legend_section, bg="yellow", image=pixel, text="Mlecz", width=legend_button_width, height=legend_button_height, compound="center")
        button.grid(row=1, column=3, padx=1, pady=1)
        button = tk.Button(self.__legend_section, bg="green", image=pixel, text="Trawa", width=legend_button_width, height=legend_button_height, compound="center")
        button.grid(row=1, column=4, padx=1, pady=1)
        button = tk.Button(self.__legend_section, bg="#670680", image=pixel, text="WilczeJagody", width=legend_button_width, height=legend_button_height, compound="center")
        button.grid(row=1, column=5, padx=1, pady=1)

        self.__root.bind("<Key>", self.key_pressed)
        self.__pixel = tk.PhotoImage(width=1, height=1)
        self.__swiat = None
        self.__size_y = 0
        self.__size_x = 0
        self.__pola_planszy = None
        self.wygeneruj_domyslny_swiat()
        self.__root.mainloop()

    def wygeneruj_domyslny_swiat(self):
        self.nowy_swiat(10, 10, 0.5)
        self.odswiez_swiat()


    def show_dimensions_window(self):
        self.dim_window = tk.Toplevel(self.__root)
        self.dim_window.title("Wymiary planszy")

        width_label = tk.Label(self.dim_window, text="Szerokość:")
        width_label.pack()
        width_entry = tk.Entry(self.dim_window)
        width_entry.pack()

        height_label = tk.Label(self.dim_window, text="Wysokość:")
        height_label.pack()
        height_entry = tk.Entry(self.dim_window)
        height_entry.pack()

        zapelnienie_swiata_label = tk.Label(self.dim_window, text="Zapełnienie świata:")
        zapelnienie_swiata_label.pack()
        zapelnienie_swiata = tk.Entry(self.dim_window)
        zapelnienie_swiata.pack()

        ok_button = tk.Button(self.dim_window, text="OK", command=lambda: [self.generate_world(width_entry, height_entry, zapelnienie_swiata), self.dim_window.destroy()])
        ok_button.pack()

    def wyczysc_plansze(self):
        for widget in self.__map_section.winfo_children():
            widget.destroy()

    def generate_world(self, szerokosc_entry, wysokosc_entry, zapelnienie_entry):
        szerokosc = int(szerokosc_entry.get())
        wysokosc = int(wysokosc_entry.get())
        zapelnienie = float(zapelnienie_entry.get())
        self.nowy_swiat(szerokosc, wysokosc, zapelnienie)

    def nowy_swiat(self, szerokosc, wysokosc, zapelnienie):
        self.wyczysc_plansze()
        self.__swiat = Swiat(szerokosc, wysokosc, self)
        self.__swiat.create_world(zapelnienie)
        self.__size_x = self.__swiat.get_size_x()
        self.__size_y = self.__swiat.get_size_y()
        self.zbuduj_plansze()

    def zbuduj_plansze(self):
        self.__size_y = self.__swiat.get_size_y()
        self.__size_x = self.__swiat.get_size_x()
        button_height = self.__map_height // self.__size_y
        button_width = self.__map_width // self.__size_x
        button_pad_y = button_height // 3
        button_height = button_height // 3 * 2
        button_pad_x = button_width // 3
        button_width = button_width // 3 * 2

        self.__pola_planszy = []
        for i in range(self.__size_y):
            wiersz = []
            for j in range(self.__size_x):
                if self.__swiat.get_plansza()[i][j] is not None:
                    color = self.__swiat.get_plansza()[i][j].get_kolor()
                    button = tk.Button(self.__map_section, bg=color, image=self.__pixel, width=button_width,
                                       height=button_height, state='disabled',
                                       command=lambda x=j, y=i: self.create_popup_list(x, y))
                else:
                    color = "white"
                    button = tk.Button(self.__map_section, bg=color, image=self.__pixel, width=button_width,
                                       height=button_height, state='normal',
                                       command=lambda x=j, y=i: self.create_popup_list(x, y))
                button.grid(row=i, column=j, padx=2, pady=2)
                wiersz.append(button)
            self.__pola_planszy.append(wiersz)

    def load(self):
        dim_window = tk.Toplevel(self.__root)
        dim_window.title("Wczytaj swiat")
        load_label = tk.Label(dim_window, text="Nazwa pliku:")
        load_label.pack()
        load_entry = tk.Entry(dim_window)
        load_entry.pack()
        ok_button = tk.Button(dim_window, text="OK", command=lambda: [self.przygotuj_plansze(load_entry), dim_window.destroy()])
        ok_button.pack()

    def przygotuj_plansze(self, load_entry):
        file_name = load_entry.get()
        Logs.wyczysc_komentarze()
        tmp_swiat = self.__swiat.odtworz_swiat(file_name)
        if tmp_swiat is not None:
            self.__swiat = tmp_swiat
            self.__swiat.set_swiat_gui(self)
            self.wyczysc_plansze()
            self.zbuduj_plansze()
            self.odswiez_swiat()

    def save(self):
        dim_window = tk.Toplevel(self.__root)
        dim_window.title("Zapisz swiat")
        save_label = tk.Label(dim_window, text="Nazwa pliku:")
        save_label.pack()
        save_entry = tk.Entry(dim_window)
        save_entry.pack()
        ok_button = tk.Button(dim_window, text="OK", command=lambda: [self.__swiat.zapisz_swiat(save_entry.get()), dim_window.destroy()])
        ok_button.pack()

    def exit(self):
        self.__root.quit()

    def key_pressed(self, event):
        if self.__swiat is not None and self.__swiat.is_pauza():
            if event.keycode == 13:
                pass
            elif self.__swiat.get_czy_czlowiek_zyje():
                if event.keysym == "Up":
                    self.__swiat.get_czlowiek().set_kierunek_ruchu(Organizm.Kierunek.GORA)
                elif event.keysym == "Down":
                    self.__swiat.get_czlowiek().set_kierunek_ruchu(Organizm.Kierunek.DOL)
                elif event.keysym == "Left":
                    self.__swiat.get_czlowiek().set_kierunek_ruchu(Organizm.Kierunek.LEWO)
                elif event.keysym == "Right":
                    self.__swiat.get_czlowiek().set_kierunek_ruchu(Organizm.Kierunek.PRAWO)
                elif event.keycode == 80:
                    tmp_superzdolnosc = self.__swiat.get_czlowiek().get_umiejetnosc()
                    if tmp_superzdolnosc.get_available():
                        tmp_superzdolnosc.aktywuj()
                        Logs.dodaj_komentarz(f"Umiejetnosc \"Niesmiertelnosc\" zostala " +
                                             f"wlaczona (Pozostaly czas trwania wynosi " +
                                             f"{tmp_superzdolnosc.get_czas_trwania()} tur")
                    elif tmp_superzdolnosc.get_active():
                        Logs.dodaj_komentarz("Umiejetnosc juz zostala aktywowana " +
                                             f"Pozostaly czas trwania wynosi " +
                                             f"{tmp_superzdolnosc.get_czas_trwania()} tur")
                        self.__komentarze_layout.odswiez_komentarze()
                        return
                    else:
                        Logs.dodaj_komentarz("Umiejetnosc mozna wlaczyc tylko po " +
                                             f"{tmp_superzdolnosc.get_cooldown()} turach")
                        self.__komentarze_layout.odswiez_komentarze()
                        return
                else:
                    Logs.dodaj_komentarz("\nNieoznaczony symbol, sprobuj ponownie")
                    self.__komentarze_layout.odswiez_komentarze()
                    return
            elif event.keysym == "UP" or event.keysym == "Down" or event.keysym == "Left" or event.keysym == "Right":
                Logs.dodaj_komentarz("Czlowiek umarl, nie mozesz nim wiecej sterowac")
                self.__komentarze_layout.odswiez_komentarze()
                return
            else:
                Logs.dodaj_komentarz("\nNieoznaczony symbol, sprobuj ponownie")
                self.__komentarze_layout.odswiez_komentarze()
                return
            Logs.wyczysc_komentarze()
            self.__swiat.set_pauza(False)
            self.__swiat.wykonaj_ture()
            self.odswiez_swiat()
            self.__swiat.set_pauza(True)

    def odswiez_swiat(self):
        self.odswiez_plansze()
        self.__komentarze_layout.odswiez_komentarze()
        self.__root.update()
        self.__root.focus_force()

    def odswiez_plansze(self):
        for i in range(self.__size_y):
            for j in range(self.__size_x):
                tmp_organizm = self.__swiat.get_plansza()[i][j]
                if tmp_organizm is not None:
                    color = tmp_organizm.get_kolor()
                    self.__pola_planszy[i][j].configure(bg=str(color), image=self.__pixel, state='disabled')
                else:
                    color = "white"
                    self.__pola_planszy[i][j].configure(bg=str(color), image=self.__pixel, state='normal')

    def create_popup_list(self, x, y):

        popup = tk.Tk()
        popup.title("Pop-up List")
        popup.geometry("300x300")

        scrollbar = tk.Scrollbar(popup)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        listbox = tk.Listbox(popup, yscrollcommand=scrollbar.set)
        lista = ["Antylopa", "CyberOwca","Lis", "Owca", "Wilk", "Zolw", "BarszSosnowskiego", "Guarana",
                 "Mlecz", "Trawa", "WilczeJagody"]
        for i in lista:
            listbox.insert(tk.END, i)
        listbox.grid(row=0, column=0, sticky=tk.NSEW)

        scrollbar.config(command=listbox.yview)

        ok_button = tk.Button(popup, text="OK", command=lambda:[self.dodaj_organizm(x,y,self.choice(listbox)),
                                                                popup.destroy()], width=10)
        ok_button.grid(row=1, column=0, pady=10)

        popup.grid_rowconfigure(0, weight=1)
        popup.grid_columnconfigure(0, weight=1)

        popup.mainloop()

    @staticmethod
    def choice(listbox):
        try:
            selected_item = listbox.get(listbox.curselection())
        except tk.TclError:
            return None

        if selected_item == "Wilk":
            return Organizm.TypOrganizmu.WILK
        elif selected_item == "Owca":
            return Organizm.TypOrganizmu.OWCA
        elif selected_item == "CyberOwca":
            return Organizm.TypOrganizmu.CYBER_OWCA
        elif selected_item == "Antylopa":
            return Organizm.TypOrganizmu.ANTYLOPA
        elif selected_item == "Lis":
            return Organizm.TypOrganizmu.LIS
        elif selected_item == "Zolw":
            return Organizm.TypOrganizmu.ZOLW
        elif selected_item == "BarszSosnowskiego":
            return Organizm.TypOrganizmu.BARSZCZ_SOSNOWSKIEGO
        elif selected_item == "Guarana":
            return Organizm.TypOrganizmu.GUARANA
        elif selected_item == "Mlecz":
            return Organizm.TypOrganizmu.MLECZ
        elif selected_item == "Trawa":
            return Organizm.TypOrganizmu.TRAWA
        elif selected_item == "WilczeJagody":
            return Organizm.TypOrganizmu.WILCZE_JAGODY
        else:
            return None

    def dodaj_organizm(self, x, y, typ_organizmu):
        if typ_organizmu is not None:
            tmp_organizm = OrganismCreator.create_new_organism(typ_organizmu, self.__swiat, Punkt(x, y))
            self.__swiat.dodaj_organizm(tmp_organizm)
            Logs.dodaj_komentarz("Stworzono nowy organizm " + tmp_organizm.organizm_to_string())
            self.odswiez_swiat()
