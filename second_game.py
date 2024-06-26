from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.clock import Clock
import random
import json
from settings import get_background_path, get_button_path, font, font_size, current_lang


with open('questions_en.json', 'r', encoding='utf-8') as file:
    questions_en = json.load(file)
with open('questions_pl.json', 'r', encoding='utf-8') as file:
    questions_pl = json.load(file)


def generate_question():
    from settings import current_lang
    if current_lang[0] == "Graj":
        question = random.choice(questions_pl)
    else:
        question = random.choice(questions_en)
    q = question['question']
    answers = question['answers']
    random.shuffle(answers)
    correct_answer = question['correct_answer']
    return q, answers, correct_answer


class SecondGame(Screen):
    def __init__(self, **kwargs):
        super(SecondGame, self).__init__(**kwargs)

        # tworzenie layoutu typu FloatLayout
        layout = FloatLayout()

        q, answers, correct_answer = generate_question()
        self.correct_answer = correct_answer
        self.answers = answers

        self.info_button = Button(text="i",
                                  pos_hint={"x": 0.01, "y": 0.91},
                                  font_size=font_size,
                                  font_name=font,
                                  size_hint=(0.20, 0.08),
                                  background_normal=get_button_path(),
                                  on_release=self.on_info_button)
        layout.add_widget(self.info_button)

        self.question_label = Label(text=q,
                                    text_size=(self.width*4, None),
                                    font_size=font_size,
                                    font_name=font,
                                    halign='center',
                                    pos_hint={"center_x": 0.5, "center_y": 0.7},
                                    size_hint=(1, 0.2))
        layout.add_widget(self.question_label)

        self.a_answer_label = Label(text="A. " + answers[0],
                                    font_size=font_size,
                                    font_name=font,
                                    halign='left',
                                    pos_hint={"center_x": 0.5, "center_y": 0.65},
                                    size_hint=(1, 0.2))
        layout.add_widget(self.a_answer_label)

        self.b_answer_label = Label(text="B. " + answers[1],
                                    font_size=font_size,
                                    font_name=font,
                                    halign='left',
                                    pos_hint={"center_x": 0.5, "center_y": 0.6},
                                    size_hint=(1, 0.2))
        layout.add_widget(self.b_answer_label)

        self.c_answer_label = Label(text="C. " + answers[2],
                                    font_size=font_size,
                                    font_name=font,
                                    halign='left',
                                    pos_hint={"center_x": 0.5, "center_y": 0.55},
                                    size_hint=(1, 0.2))
        layout.add_widget(self.c_answer_label)

        self.d_answer_label = Label(text="D. " + answers[3],
                                    font_size=font_size,
                                    font_name=font,
                                    halign='left',
                                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                                    size_hint=(1, 0.2))
        layout.add_widget(self.d_answer_label)

        self.a_button = Button(text="A",
                               font_size=font_size,
                               font_name=font,
                               pos_hint={"center_x": 0.3, "center_y": 0.4},
                               size_hint=(0.35, 0.1),
                               background_normal=get_button_path(),
                               on_release=self.on_button_click)
        layout.add_widget(self.a_button)

        self.b_button = Button(text="B",
                               font_size=font_size,
                               font_name=font,
                               pos_hint={"center_x": 0.7, "center_y": 0.4},
                               size_hint=(0.35, 0.1),
                               background_normal=get_button_path(),
                               on_release=self.on_button_click)
        layout.add_widget(self.b_button)

        self.c_button = Button(text="C",
                               font_size=font_size,
                               font_name=font,
                               pos_hint={"center_x": 0.3, "center_y": 0.28},
                               size_hint=(0.35, 0.1),
                               background_normal=get_button_path(),
                               on_release=self.on_button_click)
        layout.add_widget(self.c_button)

        self.d_button = Button(text="D",
                               font_size=font_size,
                               font_name=font,
                               pos_hint={"center_x": 0.7, "center_y": 0.28},
                               size_hint=(0.35, 0.1),
                               background_normal=get_button_path(),
                               on_release=self.on_button_click)
        layout.add_widget(self.d_button)

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

    def on_info_button(self, instance):
        from settings import current_lang
        text_pl = (f'Twój cel to udzielenie poprawnych odpowiedzi na pytania. Poniżej znajdziesz 4 przyciski z literami'
                   f' (A, B, C, D). Wybierz przycisk z literą, która Twoim zdaniem jest poprawną odpowiedzią. Jeśli'
                   f' udzielisz poprawnej odpowiedzi, przycisk zmieni kolor na zielony, a po chwili pojawi się kolejne'
                   f' pytanie. W przypadku błędnej odpowiedzi, przycisk z odpowiedzią zmieni kolor na czerwony, ale'
                   f' masz szansę na ponowny wybór.\nPowodzenia!')
        text_en = (f'Your goal is to answer the questions correctly. Below you will find 4 buttons with letters'
                   f' (A, B, C, D). Select the button with the letter you think is the correct answer. If you answer'
                   f' correctly, the button will turn green and after a while another question will appear. If you'
                   f' answer incorrectly, the answer button will turn red, but you have a chance to choose again.'
                   f'\nGood luck!')

        title_pl = f'Witaj w grze "Pytania"!'
        title_en = f'Welcome to the game "Qestions"'

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
                      pos_hint={"center_x": 0.5, "y": 0.13})
        layout.add_widget(label)

        back_button = Button(text=current_lang[6],
                             pos_hint={"center_x": 0.5, "y": 0.05},
                             font_size=font_size,
                             font_name=font,
                             size_hint=(0.5, 0.15),
                             background_normal=get_button_path(),
                             on_release=lambda x: popup.dismiss())
        layout.add_widget(back_button)

        popup = Popup(title=title,
                      title_align='center',
                      title_font=font,
                      title_size=font_size,
                      content=layout,
                      size_hint=(0.8, 0.65),
                      separator_color=(0, 0, 0, 0))
        popup.open()

    def on_back_button_click(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'game_menu'

    def on_button_click(self, instance):
        if instance.text == 'A':
            if self.correct_answer == self.answers[0]:
                self.a_answer_label.color = (0, 1, 0)
                Clock.schedule_once(self.game_reset, 2)
            else:
                self.a_answer_label.color = (1, 0, 0)
        if instance.text == 'B':
            if self.correct_answer == self.answers[1]:
                self.b_answer_label.color = (0, 1, 0)
                Clock.schedule_once(self.game_reset, 2)
            else:
                self.b_answer_label.color = (1, 0, 0)
        if instance.text == 'C':
            if self.correct_answer == self.answers[2]:
                self.c_answer_label.color = (0, 1, 0)
                Clock.schedule_once(self.game_reset, 2)
            else:
                self.c_answer_label.color = (1, 0, 0)
        if instance.text == 'D':
            if self.correct_answer == self.answers[3]:
                self.d_answer_label.color = (0, 1, 0)
                Clock.schedule_once(self.game_reset, 2)
            else:
                self.d_answer_label.color = (1, 0, 0)

    def game_reset(self, instance):
        q, answers, correct_answer = generate_question()
        self.correct_answer = correct_answer
        self.answers = answers

        # Tutaj ustaw nowe pytanie i odpowiedzi na ekranie
        self.question_label.text = q
        self.a_answer_label.text = "A. " + answers[0]
        self.b_answer_label.text = "B. " + answers[1]
        self.c_answer_label.text = "C. " + answers[2]
        self.d_answer_label.text = "D. " + answers[3]

        # Tutaj przywróć kolor labeli z odpowiedziami do stanu pierwotnego
        self.a_answer_label.color = (1, 1, 1)
        self.b_answer_label.color = (1, 1, 1)
        self.c_answer_label.color = (1, 1, 1)
        self.d_answer_label.color = (1, 1, 1)

