from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.image import Image

from settings import get_background_path, get_button_path, current_lang, font, font_size


class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        layout = FloatLayout()

        self.play_button = Button(text=current_lang[0],
                                  font_size=font_size,
                                  font_name=font,
                                  pos_hint={"center_x": 0.5, "y": 0.5},
                                  size_hint=(0.5, 0.1),
                                  background_normal=get_button_path(),
                                  on_release=self.on_play_button_click)
        layout.add_widget(self.play_button)

        self.settings_button = Button(text=current_lang[1],
                                      font_size=font_size,
                                      font_name=font,
                                      pos_hint={"center_x": 0.5, "y": 0.38},
                                      size_hint=(0.5, 0.1),
                                      background_normal=get_button_path(),
                                      on_release=self.on_settings_button_click)
        layout.add_widget(self.settings_button)

        self.quit_button = Button(text=current_lang[2],
                                  font_size=font_size,
                                  font_name=font,
                                  pos_hint={"center_x": 0.5, "y": 0.1},
                                  size_hint=(0.5, 0.1),
                                  background_normal=get_button_path(),
                                  on_release=self.on_quit_button_click)
        layout.add_widget(self.quit_button)

        self.background = Image(source=get_background_path(),
                                keep_ratio=False,
                                allow_stretch=True
                                )
        self.add_widget(self.background)

        self.add_widget(layout)

    def on_play_button_click(self, instance):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'game_menu'

    def on_settings_button_click(self, instance):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'settings'

    def on_quit_button_click(self, instance):
        App.get_running_app().stop()

