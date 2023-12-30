from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

# zmienne globalne
color = "blue"
lang = "en"
pl = ["Graj", "Ustawienia", "Wyjdź", "Wisielec", "Druga", "Trzecia", "Wróć", "Różowy", "Biały", "Niebieski", "Zielony", "Polski", "English", "Wielkość czcionki"]
en = ["Play", "Settings", "Quit", "Hangman", "Second", "Third", "Back", "Pink", "White", "Blue", "Green", "Polski", "English", "Font size"]
current_lang = en
font_size = 15


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
                                     pos_hint={"center_x": 0.3, "y": 0.7},
                                     size_hint=(0.35, 0.1))
        self.lang_button_en.background_normal = get_button_path()
        self.lang_button_en.bind(on_release=self.on_language_button_click)
        layout.add_widget(self.lang_button_en)

        # tworzenie przycisku do zmiany języka na polski
        self.lang_button_pl = Button(text=current_lang[11],
                                     font_size=font_size,
                                     pos_hint={"center_x": 0.7, "y": 0.7},
                                     size_hint=(0.35, 0.1))
        self.lang_button_pl.background_normal = get_button_path()
        self.lang_button_pl.bind(on_release=self.on_language_button_click)
        layout.add_widget(self.lang_button_pl)

        # tworzenie przycisku do zmiany koloru aplikacji na różowy
        self.color_button_pink = Button(text=current_lang[7],
                                        pos_hint={"center_x": 0.3, "y": 0.5},
                                        size_hint=(0.35, 0.1),
                                        background_normal="Graphics/Button_pink.png")
        self.color_button_pink.bind(on_release=self.on_color_button_click)
        layout.add_widget(self.color_button_pink)

        # tworzenie przycisku do zmiany koloru aplikacji na biały
        self.color_button_white = Button(text=current_lang[8],
                                         pos_hint={"center_x": 0.7, "y": 0.5},
                                         size_hint=(0.35, 0.1),
                                         background_normal="Graphics/Button_white.png")
        self.color_button_white.bind(on_release=self.on_color_button_click)
        layout.add_widget(self.color_button_white)

        # tworzenie przycisku do zmiany koloru aplikacji na zielony
        self.color_button_green = Button(text=current_lang[10],
                                        pos_hint={"center_x": 0.3, "y": 0.38},
                                        size_hint=(0.35, 0.1),
                                        background_normal="Graphics/Button_green.png")
        self.color_button_green.bind(on_release=self.on_color_button_click)
        layout.add_widget(self.color_button_green)

        # tworzenie przycisku do zmiany koloru aplikacji na niebieski
        self.color_button_blue = Button(text=current_lang[9],
                                        pos_hint={"center_x": 0.7, "y": 0.38},
                                        size_hint=(0.35, 0.1),
                                        background_normal="Graphics/Button_blue.png")
        self.color_button_blue.bind(on_release=self.on_color_button_click)
        layout.add_widget(self.color_button_blue)

        # tworzenie labelu pokazującego aktualną wielkość czcionki
        self.font_size_label = Label(text=current_lang[13] + ":" + str(font_size),
                                     font_size=font_size,
                                     pos_hint={"center_x": 0.5, "y": 0.29},
                                     size_hint=(0.5, 0.05))
        layout.add_widget(self.font_size_label)

        # tworzenie suwaka do zmiany wielkości czcionki w aplikacji
        self.font_size_slider = Slider(min=12, max=22, value=15, step=1,
                                       pos_hint={"center_x": 0.5, "y": 0.25},
                                       size_hint=(0.8, 0.05))
        self.font_size_slider.bind(value=self.on_slider_change)
        layout.add_widget(self.font_size_slider)

        # tworzenie przycisku do powrotu do ekranu głównego
        self.back_button = Button(pos_hint={"center_x": 0.5, "y": 0.1},
                                  size_hint=(0.5, 0.1))
        self.back_button.text = current_lang[6]
        self.back_button.background_normal = get_button_path()
        self.back_button.bind(on_release=self.on_back_button_click)
        layout.add_widget(self.back_button)

        # tworzenie tła ekranu
        self.background = Image(source=get_background_path())
        self.add_widget(self.background)

        self.add_widget(layout)

    # funkcja suwaka zmieniająca wielkość czcionki we wszystkich ekranach
    def on_slider_change(self, instance, value):
        global font_size
        font_size = value
        self.back_button.font_size = value
        self.color_button_pink.font_size = value
        self.color_button_white.font_size = value
        self.color_button_green.font_size = value
        self.color_button_blue.font_size = value
        self.lang_button_en.font_size = value
        self.lang_button_pl.font_size = value
        self.font_size_label.text = current_lang[13] + ": " + str(value)
        self.font_size_label.font_size = value

        # zmiana wielkości tekstów przycisków ekranu "main_menu"
        main_menu = self.manager.get_screen('main_menu')
        if main_menu:
            main_menu.play_button.font_size = value
            main_menu.settings_button.font_size = value
            main_menu.quit_button.font_size = value

        # zmiana wielkości tekstów przycisków ekranu "game_menu"
        game_menu = self.manager.get_screen('game_menu')
        if game_menu:
            game_menu.back_button.font_size = value
            game_menu.first_button.font_size = value
            game_menu.second_button.font_size = value
            game_menu.third_button.font_size = value

    # funkcja przycisków "lang_button_pl" i "ang_button_en" zmieniająca język wszystkich ekranów
    def on_language_button_click(self, instance):
        # pobieranie zmiennych globalnych
        global current_lang, lang, en, pl, font_size
        # sprawdzenie, który przycisk został kliknięty
        if instance.text == "Polski":
            current_lang = pl
            lang = "pl"

        if instance.text == "English":
            current_lang = en
            lang = "en"

        # zmiana tekstów przycisków aktualnego ekranu (settings)
        self.back_button.text = current_lang[6]
        self.color_button_pink.text = current_lang[7]
        self.color_button_white.text = current_lang[8]
        self.color_button_green.text = current_lang[10]
        self.color_button_blue.text = current_lang[9]
        self.font_size_label.text = current_lang[13] + ": " + str(font_size)

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

    # funkcja przycisku "back_button" - przejście do ekranu głównego
    def on_back_button_click(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'main_menu'

    # funkcja przycisków "color_button_white" i "color_button_pink" zmieniająca motyw kolorystyczny wszystkich ekranów
    def on_color_button_click(self, instance):
        # pobieranie zmiennych globalnych
        global color, pl, en, lang
        # z racji na sposób odwoływania się do ścieżek plików graficznych w fukcjach "get_background_path" i
        # "get_button_path" potrzebne jest przetłumaczenie kolorów na język angielski i zamanię pierwszej litery na małą
        if lang == "pl":
            for index, word in enumerate(pl):
                if instance.text == word:
                    color = en[index].lower()
        else:
            color = instance.text.lower()

        # zmiana tekstów przycisków aktualnego ekranu (settings)
        self.background.source = get_background_path()
        self.back_button.background_normal = get_button_path()
        self.lang_button_pl.background_normal = get_button_path()
        self.lang_button_en.background_normal = get_button_path()

        # zmiana tekstów przycisków ekranu "main_menu"
        main_menu = self.manager.get_screen('main_menu')
        if main_menu:
            main_menu.background.source = get_background_path()
            main_menu.play_button.background_normal = get_button_path()
            main_menu.settings_button.background_normal = get_button_path()
            main_menu.quit_button.background_normal = get_button_path()

        # zmiana tekstów przycisków ekranu "game_menu"
        game_menu = self.manager.get_screen('game_menu')
        if game_menu:
            game_menu.background.source = get_background_path()
            game_menu.back_button.background_normal = get_button_path()
            game_menu.first_button.background_normal = get_button_path()
            game_menu.second_button.background_normal = get_button_path()
            game_menu.third_button.background_normal = get_button_path()

