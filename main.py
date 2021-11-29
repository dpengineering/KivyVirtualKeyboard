from kivy.config import Config  # Keep these Config settings at the top
Config.set('kivy', 'keyboard_mode', 'systemanddock')  # virtual docked keyboard plus input from real keyboard
Config.set('kivy', 'keyboard_layout', 'simple')  # setting a custom keyboard layout from kivy/data/keyboards
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

SCREEN_MANAGER = ScreenManager()
MAIN_SCREEN_NAME = 'main'

Window.clearcolor = (1, 1, 1, 1)  # White


class KeyboardTestGUI(App):
    def build(self):
        return SCREEN_MANAGER


class MainScreen(Screen):
    txt_in = ObjectProperty(None)

    def action(self):
        print(self.txt_in.text)


Builder.load_file('main.kv')
SCREEN_MANAGER.add_widget(MainScreen(name=MAIN_SCREEN_NAME))

if __name__ == "__main__":
    KeyboardTestGUI().run()
