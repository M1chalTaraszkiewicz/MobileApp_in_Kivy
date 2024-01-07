from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import random
from settings import get_background_path, get_button_path, font, font_size, current_lang


def password_generator():
    from settings import current_lang
    if current_lang[0] == "Graj":
        with open('words_pl.txt', 'r', encoding='utf-8') as file:
            words = file.read().split()
    else:
        with open('words_en.txt', 'r', encoding='utf-8') as file:
            words = file.read().split()
    word = random.choice(words)
    print(word)
    password = ["_" for _ in range(len(word))]
    usedLetters = []
    return word, password, usedLetters


word, password, usedLetters = password_generator()


class FirstGame(Screen):
    def __init__(self, **kwargs):
        super(FirstGame, self).__init__(**kwargs)

        # tworzenie layoutu typu FloatLayout
        layout = FloatLayout()

        self.password_display_label = Label(text=" ".join(password),
                                            font_size=font_size*2,
                                            font_name=font,
                                            pos_hint={"center_x": 0.5, "center_y": 0.6},
                                            size_hint=(1, 0.2))
        layout.add_widget(self.password_display_label)

        self.text_input = TextInput(hint_text=current_lang[17],
                                    font_size=font_size,
                                    font_name=font,
                                    foreground_color=(1, 1, 1),
                                    hint_text_color=(0.7, 0.7, 0.7),
                                    halign='center',
                                    background_color=(0.2, 0.2, 0.2),
                                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                                    size_hint=(0.8, 0.05),
                                    on_text_validate=self.on_text_input,
                                    multiline=False,
                                    text_validate_unfocus=False)
        layout.add_widget(self.text_input)

        self.used_letters_title_label = Label(text=current_lang[19],
                                              font_size=font_size,
                                              font_name=font,
                                              pos_hint={"center_x": 0.5, "center_y": 0.43},
                                              size_hint=(0.8, 0.2))
        layout.add_widget(self.used_letters_title_label)

        self.used_letters_label = Label(text=" ".join(usedLetters),
                                        font_size=font_size,
                                        font_name=font,
                                        pos_hint={"center_x": 0.5, "center_y": 0.38},
                                        size_hint=(0.8, 0.2),
                                        halign='center')
        layout.add_widget(self.used_letters_label)

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
        self.game_reset(self)
        pass

    def on_text_input(self, instance):
        global usedLetters, password, word
        from settings import current_lang

        if len(instance.text) > 0 and instance.text.isalpha():
            if len(instance.text) == 1 and instance.text.lower() not in usedLetters:
                letter = instance.text.lower()
                if letter in word:
                    for i, x in enumerate(word):
                        if letter == x:
                            password[i] = letter

                usedLetters.append(letter)
                instance.hint_text_color = (0.7, 0.7, 0.7)
                if "_" not in password:
                    self.text_input.readonly = True
                    self.password_display_label.color = (0, 1, 0)
                    self.reset_button.opacity = 1
                    self.reset_button.size_hint = (0.5, 0.1)
                    self.reset_button.text = current_lang[22]

            if len(instance.text) > 1:
                if instance.text.lower() == word:
                    password = word
                    self.text_input.readonly = True
                    self.password_display_label.color = (0, 1, 0)
                    self.reset_button.opacity = 1
                    self.reset_button.size_hint = (0.5, 0.1)
                    self.reset_button.text = current_lang[22]

            instance.hint_text_color = (0.7, 0.7, 0.7)
        else:
            instance.hint_text_color = (1, 0, 0)

        self.password_display_label.text = " ".join(password)
        self.used_letters_label.text = " ".join(usedLetters)
        instance.text = ""

    def on_back_button_click(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'game_menu'

    def game_reset(self, instance):
        global word, password, usedLetters
        word, password, usedLetters = password_generator()
        self.used_letters_label.text = " ".join(usedLetters)
        self.password_display_label.text = " ".join(password)
        self.password_display_label.color = (1, 1, 1)
        self.reset_button.text = ""
        self.reset_button.opacity = 0
        self.reset_button.size_hint = (0, 0)
        self.text_input.readonly = False
