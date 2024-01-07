from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from settings import get_background_path, get_button_path, current_lang, font, font_size


class GameMenu(Screen):
    def __init__(self, **kwargs):
        super(GameMenu, self).__init__(**kwargs)
        layout = FloatLayout()

        self.first_button = Button(text=current_lang[3],
                                   font_size=font_size,
                                   font_name=font,
                                   pos_hint={"center_x": 0.5, "center_y": 0.62},
                                   size_hint=(0.5, 0.1),
                                   background_normal=get_button_path(),
                                   on_release=self.on_first_button_click)
        layout.add_widget(self.first_button)

        self.second_button = Button(text=current_lang[4],
                                    font_size=font_size,
                                    font_name=font,
                                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                                    size_hint=(0.5, 0.1),
                                    background_normal=get_button_path(),
                                    on_release=self.on_second_button_click)
        layout.add_widget(self.second_button)

        self.third_button = Button(text=current_lang[5],
                                   font_size=font_size,
                                   font_name=font,
                                   pos_hint={"center_x": 0.5, "center_y": 0.38},
                                   size_hint=(0.5, 0.1),
                                   background_normal=get_button_path(),
                                   on_release=self.on_third_button_click)
        layout.add_widget(self.third_button)

        self.back_button = Button(text=current_lang[6],
                                  font_size=font_size,
                                  font_name=font,
                                  pos_hint={"center_x": 0.5, "y": 0.1},
                                  size_hint=(0.5, 0.1),
                                  background_normal=get_button_path(),
                                  on_release=self.on_back_button_click)
        layout.add_widget(self.back_button)

        self.background = Image(source=get_background_path(),
                                keep_ratio=False,
                                allow_stretch=True
                                )
        self.add_widget(self.background)
        self.add_widget(layout)

    def on_back_button_click(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'main_menu'

    def on_first_button_click(self, instance):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'first_game'

    def on_second_button_click(self, instance):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'second_game'

    def on_third_button_click(self, instance):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'third_game'
