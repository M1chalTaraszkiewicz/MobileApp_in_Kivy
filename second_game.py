from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
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

