from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

# zmienne globalne
color = "blue"
pl = ["Graj", "Ustawienia", "Wyjdź", "Litera po literze", "Druga", "Trzecia", "Wróć", "Różowy", "Biały", "Niebieski", "Zielony", "Polski", "English", "Wielkość czcionki", "Mała", "Średnia", "Duża", "Podaj literę bądź całe hasło!", "Nietrafione litery: ", "Użyte litery: ", "Gratulacje!", "Hasło to: ", "Następne słowo"]
en = ["Play", "Settings", "Quit", "Letter by letter", "Second", "Third", "Back", "Pink", "White", "Blue", "Green", "Polski", "English", "Font size", "Small", "Medium", "Big", "Enter a letter or the entire password!", "Missed letters: ", "Letters used: ", "Congratulations!", "The password is: ", "Next word"]
current_lang = en
font_size = 16
font = "Fonts/RussoOne-Regular.ttf"


# funkcja zwracająca ścieżkę do tła aplikacji o wybranym kolorze
def get_background_path():
    return f"Graphics/Background_{color}.jpg"


# funkcja zwracająca ścieżkę do tła przycisku o wybranym kolorze
def get_button_path():
    return f"Graphics/Button_{color}.png"


class Settings(Screen):
    def __init__(self, **kwargs):
        super(Settings, self).__init__(**kwargs)
        # tworzenie layoutu typu FloatLayout
        layout = FloatLayout()

        # tworzenie przycisku do zmiany języka na angielski
        self.lang_button_en = Button(text=current_lang[12],
                                     font_size=font_size,
                                     font_name=font,
                                     pos_hint={"center_x": 0.3, "y": 0.7},
                                     size_hint=(0.35, 0.1),
                                     background_normal=get_button_path())
        self.lang_button_en.bind(on_release=self.on_language_button_click)
        layout.add_widget(self.lang_button_en)

        # tworzenie przycisku do zmiany języka na polski
        self.lang_button_pl = Button(text=current_lang[11],
                                     font_size=font_size,
                                     font_name=font,
                                     pos_hint={"center_x": 0.7, "y": 0.7},
                                     size_hint=(0.35, 0.1),
                                     background_normal=get_button_path())
        self.lang_button_pl.bind(on_release=self.on_language_button_click)
        layout.add_widget(self.lang_button_pl)

        # tworzenie przycisku do zmiany koloru aplikacji na różowy
        self.color_button_pink = Button(text=current_lang[7],
                                        font_size=font_size,
                                        font_name=font,
                                        pos_hint={"center_x": 0.3, "y": 0.5},
                                        size_hint=(0.35, 0.1),
                                        background_normal="Graphics/Button_pink.png")
        self.color_button_pink.bind(on_release=self.on_color_button_click)
        layout.add_widget(self.color_button_pink)

        # tworzenie przycisku do zmiany koloru aplikacji na biały
        self.color_button_white = Button(text=current_lang[8],
                                         font_size=font_size,
                                         font_name=font,
                                         pos_hint={"center_x": 0.7, "y": 0.5},
                                         size_hint=(0.35, 0.1),
                                         background_normal="Graphics/Button_white.png",
                                         on_release=self.on_color_button_click)
        layout.add_widget(self.color_button_white)

        # tworzenie przycisku do zmiany koloru aplikacji na zielony
        self.color_button_green = Button(text=current_lang[10],
                                         font_size=font_size,
                                         font_name=font,
                                         pos_hint={"center_x": 0.3, "y": 0.38},
                                         size_hint=(0.35, 0.1),
                                         background_normal="Graphics/Button_green.png",
                                         on_release=self.on_color_button_click)
        layout.add_widget(self.color_button_green)

        # tworzenie przycisku do zmiany koloru aplikacji na niebieski
        self.color_button_blue = Button(text=current_lang[9],
                                        font_size=font_size,
                                        font_name=font,
                                        pos_hint={"center_x": 0.7, "y": 0.38},
                                        size_hint=(0.35, 0.1),
                                        background_normal="Graphics/Button_blue.png",
                                        on_release=self.on_color_button_click)
        layout.add_widget(self.color_button_blue)

        # tworzenie przycisków do zmiany wielkości czcionki w aplikacji
        # mała
        self.font_size_button_small = Button(text=current_lang[14],
                                             pos_hint={"center_x": 0.245, "y": 0.25},
                                             size_hint=(0.24, 0.1),
                                             font_size=12,
                                             font_name=font,
                                             background_normal=get_button_path(),
                                             on_release=self.font_size_change)
        layout.add_widget(self.font_size_button_small)

        # średnia
        self.font_size_button_medium = Button(text=current_lang[15],
                                              pos_hint={"center_x": 0.5, "y": 0.25},
                                              size_hint=(0.24, 0.1),
                                              font_size=16,
                                              font_name=font,
                                              background_normal=get_button_path(),
                                              on_release=self.font_size_change)
        layout.add_widget(self.font_size_button_medium)

        # duża
        self.font_size_button_big = Button(text=current_lang[16],
                                           pos_hint={"center_x": 0.755, "y": 0.25},
                                           size_hint=(0.24, 0.1),
                                           font_size=20,
                                           font_name=font,
                                           background_normal=get_button_path(),
                                           on_release=self.font_size_change)
        layout.add_widget(self.font_size_button_big)

        # tworzenie przycisku do powrotu do ekranu głównego
        self.back_button = Button(text=current_lang[6],
                                  pos_hint={"center_x": 0.5, "y": 0.1},
                                  font_size=font_size,
                                  font_name=font,
                                  size_hint=(0.5, 0.1),
                                  background_normal=get_button_path(),
                                  on_release=self.on_back_button_click)
        layout.add_widget(self.back_button)

        # tworzenie tła ekranu
        self.background = Image(source=get_background_path(),
                                keep_ratio=False,
                                allow_stretch=True
                                )
        self.add_widget(self.background)

        self.add_widget(layout)

    # funkcja do zmieny wielkości czcionki w aplikacji
    def font_size_change(self, instance):
        global font_size
        if instance.text == current_lang[14]:
            font_size = 10
        if instance.text == current_lang[15]:
            font_size = 16
        if instance.text == current_lang[16]:
            font_size = 22

        # zmiena wielości tekstów przycisków ekranu "settings"
        self.back_button.font_size = font_size
        self.color_button_pink.font_size = font_size
        self.color_button_white.font_size = font_size
        self.color_button_green.font_size = font_size
        self.color_button_blue.font_size = font_size
        self.lang_button_en.font_size = font_size
        self.lang_button_pl.font_size = font_size

        # zmiana wielkości tekstów przycisków ekranu "main_menu"
        main_menu = self.manager.get_screen('main_menu')
        if main_menu:
            main_menu.play_button.font_size = font_size
            main_menu.settings_button.font_size = font_size
            main_menu.quit_button.font_size = font_size

        # zmiana wielkości tekstów przycisków ekranu "game_menu"
        game_menu = self.manager.get_screen('game_menu')
        if game_menu:
            game_menu.back_button.font_size = font_size
            game_menu.first_button.font_size = font_size
            game_menu.second_button.font_size = font_size
            game_menu.third_button.font_size = font_size

        first_game = self.manager.get_screen('first_game')
        if first_game:
            first_game.back_button.font_size = font_size
            first_game.password_display_label.font_size = font_size*2
            first_game.text_input.font_size = font_size
            first_game.used_letters_title_label.font_size = font_size
            first_game.used_letters_label.font_size = font_size
            first_game.reset_button.font_size = font_size


    # funkcja przycisków "lang_button_pl" i "ang_button_en" zmieniająca język wszystkich ekranów
    def on_language_button_click(self, instance):
        # pobieranie zmiennych globalnych
        global current_lang
        # sprawdzenie, który przycisk został kliknięty
        if instance.text == "Polski":
            current_lang = pl

        if instance.text == "English":
            current_lang = en

        # zmiana tekstów przycisków aktualnego ekranu (settings)
        self.back_button.text = current_lang[6]
        self.color_button_pink.text = current_lang[7]
        self.color_button_white.text = current_lang[8]
        self.color_button_blue.text = current_lang[9]
        self.color_button_green.text = current_lang[10]
        self.font_size_button_small.text = current_lang[14]
        self.font_size_button_medium.text = current_lang[15]
        self.font_size_button_big.text = current_lang[16]

        # zmiana tekstów przycisków ekranu "main_menu"
        main_menu = self.manager.get_screen('main_menu')
        if main_menu:
            main_menu.play_button.text = current_lang[0]
            main_menu.settings_button.text = current_lang[1]
            main_menu.quit_button.text = current_lang[2]

        # zmiana tekstów przycisków ekranu "game_menu"
        game_menu = self.manager.get_screen('game_menu')
        if game_menu:
            game_menu.back_button.text = current_lang[6]
            game_menu.first_button.text = current_lang[3]
            game_menu.second_button.text = current_lang[4]
            game_menu.third_button.text = current_lang[5]

        first_game = self.manager.get_screen('first_game')
        if first_game:
            first_game.back_button.text = current_lang[6]
            first_game.text_input.hint_text = current_lang[17]
            first_game.used_letters_title_label.text = current_lang[19]
            first_game.reset_button.text = current_lang[22]

    # funkcja przycisku "back_button" - przejście do ekranu głównego
    def on_back_button_click(self, instance):
        print(current_lang)
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'main_menu'

    # funkcja przycisków do zmiany kolorów zmieniająca motyw kolorystyczny wszystkich ekranów
    def on_color_button_click(self, instance):
        # pobieranie zmiennych globalnych
        global color, pl, en
        # z racji na sposób odwoływania się do ścieżek plików graficznych w fukcjach "get_background_path" i
        # "get_button_path" potrzebne jest przetłumaczenie kolorów na język angielski i zamaninie pierwszej litery na
        # małą
        if current_lang == pl:
            for index, word in enumerate(pl):
                if instance.text == word:
                    color = en[index].lower()
        else:
            color = instance.text.lower()

        # zmiana koloru przycisków aktualnego ekranu (settings)
        self.background.source = get_background_path()
        self.back_button.background_normal = get_button_path()
        self.lang_button_pl.background_normal = get_button_path()
        self.lang_button_en.background_normal = get_button_path()
        self.font_size_button_small.background_normal = get_button_path()
        self.font_size_button_medium.background_normal = get_button_path()
        self.font_size_button_big.background_normal = get_button_path()

        # zmiana koloru przycisków ekranu "main_menu"
        main_menu = self.manager.get_screen('main_menu')
        if main_menu:
            main_menu.background.source = get_background_path()
            main_menu.play_button.background_normal = get_button_path()
            main_menu.settings_button.background_normal = get_button_path()
            main_menu.quit_button.background_normal = get_button_path()

        # zmiana koloru przycisków ekranu "game_menu"
        game_menu = self.manager.get_screen('game_menu')
        if game_menu:
            game_menu.background.source = get_background_path()
            game_menu.back_button.background_normal = get_button_path()
            game_menu.first_button.background_normal = get_button_path()
            game_menu.second_button.background_normal = get_button_path()
            game_menu.third_button.background_normal = get_button_path()

        first_game = self.manager.get_screen('first_game')
        if first_game:
            first_game.background.source = get_background_path()
            first_game.back_button.background_normal = get_button_path()
            first_game.reset_button.background_normal = get_button_path()
