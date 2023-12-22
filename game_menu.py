from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from settings import get_background_path, get_button_path

class GameMenu(Screen):
    def __init__(self, **kwargs):
        super(GameMenu, self).__init__(**kwargs)
        layout = FloatLayout()

        self.back_button = Button(text='Back', pos_hint={"center_x": 0.5, "y": 0.1}, size_hint=(0.5, 0.1))
        self.back_button.background_normal = get_button_path()
        self.back_button.bind(on_release=self.on_back_button_click)
        layout.add_widget(self.back_button)

        self.first_button = Button(text='Hanged Man', pos_hint={"center_x": 0.5, "center_y": 0.62}, size_hint=(0.5, 0.1))
        self.first_button.background_normal = get_button_path()
        layout.add_widget(self.first_button)

        self.second_button = Button(text='Second', pos_hint={"center_x": 0.5, "center_y": 0.5}, size_hint=(0.5, 0.1))
        self.second_button.background_normal = get_button_path()
        layout.add_widget(self.second_button)

        self.third_button = Button(text='Third', pos_hint={"center_x": 0.5, "center_y": 0.38}, size_hint=(0.5, 0.1))
        self.third_button.background_normal = get_button_path()
        layout.add_widget(self.third_button)

        self.background = Image(source=get_background_path())
        self.add_widget(self.background)
        self.add_widget(layout)

    def on_back_button_click(self, instance):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'main_menu'

