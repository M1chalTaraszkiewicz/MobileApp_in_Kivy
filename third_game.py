from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import random
from settings import get_background_path, get_button_path, font, font_size, current_lang


def number_generator():
    number = random.randint(100, 999)
    print(number)
    return number


number = None
chances = 10


class ThirdGame(Screen):
    def __init__(self, **kwargs):
        super(ThirdGame, self).__init__(**kwargs)

        # tworzenie layoutu typu FloatLayout
        layout = FloatLayout()

        self.info_button = Button(text="i",
                                  pos_hint={"x": 0.01, "y": 0.91},
                                  font_size=font_size,
                                  font_name=font,
                                  size_hint=(0.20, 0.08),
                                  background_normal=get_button_path(),
                                  on_release=self.on_info_button)
        layout.add_widget(self.info_button)

        self.number_label = Label(text="X",
                                  font_size=font_size*3,
                                  font_name=font,
                                  pos_hint={"center_x": 0.5, "center_y": 0.62},
                                  size_hint=(1, 0.2))
        layout.add_widget(self.number_label)

        self.text_input = TextInput(hint_text=current_lang[23],
                                    font_size=font_size*0.8,
                                    font_name=font,
                                    foreground_color=(1, 1, 1),
                                    hint_text_color=(0.7, 0.7, 0.7),
                                    halign='center',
                                    background_color=(0.2, 0.2, 0.2),
                                    pos_hint={"center_x": 0.5, "center_y": 0.52},
                                    size_hint=(0.8, 0.05),
                                    on_text_validate=self.on_text_input,
                                    multiline=False,
                                    text_validate_unfocus=False)
        layout.add_widget(self.text_input)

        self.chances_label = Label(text=current_lang[28] + str(chances),
                                   color=(1, 1, 1, 1),
                                   outline_color=(0, 0, 0, 1),
                                   outline_width=1,
                                   font_size=font_size,
                                   font_name=font,
                                   halign='center',
                                   valign='middle',
                                   pos_hint={"center_x": 0.5, "y": 0.44},
                                   size_hint=(0.75, 0.07))
        layout.add_widget(self.chances_label)

        self.first_hint_button = Button(text=":",
                                        pos_hint={"center_x": 0.245, "y": 0.35},
                                        font_size=font_size,
                                        font_name=font,
                                        size_hint=(0.24, 0.1),
                                        background_normal=get_button_path(),
                                        background_disabled_normal=get_button_path(),
                                        on_release=self.on_hint_button)
        layout.add_widget(self.first_hint_button)

        self.second_hint_button = Button(text="+",
                                         pos_hint={"center_x": 0.5, "y": 0.35},
                                         font_size=font_size,
                                         font_name=font,
                                         size_hint=(0.24, 0.1),
                                         background_normal=get_button_path(),
                                         background_disabled_normal=get_button_path(),
                                         on_release=self.on_hint_button)
        layout.add_widget(self.second_hint_button)

        self.third_hint_button = Button(text="?",
                                         pos_hint={"center_x": 0.755, "y": 0.35},
                                         font_size=font_size,
                                         font_name=font,
                                         size_hint=(0.24, 0.1),
                                         background_normal=get_button_path(),
                                         background_disabled_normal=get_button_path(),
                                         on_release=self.on_hint_button)
        layout.add_widget(self.third_hint_button)

        self.reset_button = Button(text="",
                                   pos_hint={"center_x": 0.5, "y": 0.22},
                                   font_size=font_size,
                                   font_name=font,
                                   size_hint=(0, 0),
                                   opacity=0,
                                   background_normal=get_button_path(),
                                   on_release=self.game_reset)
        layout.add_widget(self.reset_button)

        # tworzenie przycisku do powrotu do ekranu game_menu
        self.back_button = Button(text=current_lang[6],
                                  pos_hint={"center_x": 0.5, "y": 0.1},
                                  font_size=font_size,
                                  font_name=font,
                                  size_hint=(0.5, 0.1),
                                  background_normal=get_button_path(),
                                  on_release=self.on_back_button_click)
        layout.add_widget(self.back_button)

        self.background = Image(source=get_background_path(),
                                keep_ratio=False,
                                allow_stretch=True)
        self.add_widget(self.background)
        self.add_widget(layout)

    def on_pre_enter(self):
        from settings import font_size
        self.chances_label.font_size = font_size
        self.game_reset(self)
        pass

    def on_info_button(self, instance):
        from settings import current_lang
        text_pl = (f'Twoim zadaniem jest odgadnięcie liczby z przedziału 100-999. Wpisz swoją propozycję liczby. Po'
                   f' każdym wpisaniu liczby otrzymasz wskazówkę czy szukana liczba jest większa czy mniejsza od'
                   f' wpisanej. Masz również do dyspozycji trzy rodzaje podpowiedzi:\n":": podaje losowy dzielnik'
                   f' szukanej liczby,\n"+": podaje sumę cyfr szukanej liczby,\n"?": podaje jedną cyfrę znajdującą się'
                   f' w szukanej liczbie.\nUżyj mądrze podpowiedzi, ale pamiętaj, że każde użycie kosztuje jedną '
                   f'szansę. Gra kończy się, gdy odgadniesz liczbę lub skończą ci się szanse.\nPowodzenia!')
        text_en = (f'Your task is to guess a number from 100-999. Enter your proposed number. Each time you enter a'
                   f' number, you will receive an indication whether the number you are looking for is greater or less'
                   f' than the entered number. You also have three types of hints:\n":": gives a random divisor of the'
                   f' number you are looking for,\n"+": gives you the sum of the digits of the number you are looking'
                   f' for,\n"?": gives you one digit in the number you are looking for.\nUse wisely hints, but remember'
                   f' that each use costs one chance. The game ends when you guess the number or run out of chances.\n'
                   f'Good luck!')

        title_pl = f'Witaj w grze "Liczby"!'
        title_en = f'Welcome to the game "Numbers"'

        if current_lang[0] == "Graj":
            text = text_pl
            title = title_pl
        else:
            text = text_en
            title = title_en

        layout = FloatLayout()

        label = Label(text=text,
                      text_size=(self.width*0.7, None),
                      font_size=font_size,
                      font_name=font,
                      halign='center',
                      valign='middle',
                      pos_hint={"center_x": 0.5, "y": 0.11})
        layout.add_widget(label)

        back_button = Button(text=current_lang[6],
                             pos_hint={"center_x": 0.5, "y": 0.05},
                             font_size=font_size,
                             font_name=font,
                             size_hint=(0.5, 0.11),
                             background_normal=get_button_path(),
                             on_release=lambda x: popup.dismiss())
        layout.add_widget(back_button)

        popup = Popup(title=title,
                      title_align='center',
                      title_font=font,
                      title_size=font_size,
                      content=layout,
                      size_hint=(0.8, 0.85),
                      separator_color=(0, 0, 0, 0))
        popup.open()

    def game_reset(self, instance):
        global number, chances
        number = number_generator()
        chances = 10
        self.chances_label.text = current_lang[28] + str(chances)
        self.number_label.text = "X"
        self.number_label.color = (1, 1, 1)
        self.text_input.readonly = False
        self.text_input.hint_text_color = (0.7, 0.7, 0.7)
        self.reset_button.opacity = 0
        self.reset_button.size_hint = (0, 0)
        self.reset_button.text = ""
        self.first_hint_button.text = ":"
        self.first_hint_button.color = (1, 1, 1)
        self.first_hint_button.disabled = False
        self.second_hint_button.text = "+"
        self.second_hint_button.color = (1, 1, 1)
        self.second_hint_button.disabled = False
        self.third_hint_button.text = "?"
        self.third_hint_button.color = (1, 1, 1)
        self.third_hint_button.disabled = False

    def on_back_button_click(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'game_menu'

    def on_text_input(self, instance):
        if len(instance.text) == 3 and instance.text.isnumeric() and int(instance.text) >= 100:
            global chances
            chances -= 1
            self.chances_label.text = current_lang[28] + str(chances)
            instance.hint_text_color = (0.7, 0.7, 0.7)
            num = int(instance.text)
            instance.text = ""
            if num == number:
                self.end(True)
            elif chances == 0:
                self.end(False)
            elif num > number:
                self.number_label.text = f"{num} > X"
            else:
                self.number_label.text = f"{num} < X"
        else:
            instance.hint_text_color = (1, 0, 0)
            instance.text = ""

    def on_hint_button(self, instance):
        global chances
        chances -= 1
        self.chances_label.text = current_lang[28] + str(chances)
        if instance.text == ":":
            dividers = []
            for i in range(2, number):
                if number % i == 0:
                    dividers.append(i)
            if dividers:
                instance.text = str(random.choice(dividers))
            else:
                instance.text = "1"
        elif instance.text == "+":
            sum = 0
            num = number
            for _ in range(3):
                sum += num % 10
                num //= 10
            instance.text = str(sum)
        else:
            rand_digit = random.choice(str(number))
            instance.text = rand_digit
        if chances == 0:
            self.end(False)
        instance.disabled = True
        instance.color = (1, 0.65, 0, 1)

    def end(self, isWin):
        self.number_label.text = str(number)
        self.text_input.readonly = True
        self.reset_button.opacity = 1
        self.reset_button.size_hint = (0.5, 0.1)
        self.reset_button.text = current_lang[24]
        self.first_hint_button.disabled = True
        self.second_hint_button.disabled = True
        self.third_hint_button.disabled = True
        if isWin:
            self.number_label.color = (0, 1, 0)
        else:
            self.number_label.color = (1, 0, 0)

