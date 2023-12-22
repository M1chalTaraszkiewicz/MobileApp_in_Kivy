from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from main_menu import MainMenu
from game_menu import GameMenu
from settings import Settings
from kivy.core.window import Window

class MyApp(App):
    def build(self):

        sm = ScreenManager()
        sm.add_widget(MainMenu(name='main_menu'))
        sm.add_widget(GameMenu(name='game_menu'))
        sm.add_widget(Settings(name='settings'))
        sm.current = 'main_menu'
        return sm


if __name__ == '__main__':
    Window.size = (405, 720)
    # Window.size = (1080, 1920)
    MyApp().run()
