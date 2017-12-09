from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from toys import *

Builder.load_file('layout.kv')

class Controller(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Home(name='home'))
        return sm

Controller().run()
