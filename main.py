from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from main_menu import MainMenu
from game_menu import GameMenu
from settings import Settings
from first_game import FirstGame
from second_game import SecondGame
from third_game import ThirdGame
from kivy.core.window import Window


class MyApp(App):
    def build(self):
        self.title = "CustomizeTheApp"
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='main_menu'))
        sm.add_widget(GameMenu(name='game_menu'))
        sm.add_widget(Settings(name='settings'))
        sm.add_widget(FirstGame(name='first_game'))
        sm.add_widget(SecondGame(name='second_game'))
        sm.add_widget(ThirdGame(name='third_game'))
        sm.current = 'main_menu'
        return sm


if __name__ == '__main__':
    Window.size = (405, 720)
    # Window.size = (1080, 1920)
    MyApp().run()
