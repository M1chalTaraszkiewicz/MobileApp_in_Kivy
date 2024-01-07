from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import random
from settings import get_background_path, get_button_path, font, font_size, current_lang





class ThirdGame(Screen):
    def __init__(self, **kwargs):
        super(ThirdGame, self).__init__(**kwargs)

        # tworzenie layoutu typu FloatLayout
        layout = FloatLayout()




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

    def on_back_button_click(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'game_menu'
