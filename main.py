#add gridlayout to home screen

import kivy
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button,ButtonBehavior
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.uix.label import Label
from kivy.config import Config
from kivy.core.audio import SoundLoader
from kivy.uix.slider import Slider

Config.set('graphics', 'resizable', True)

class StartWindow(Screen):
    pass

class HomeWindow(Screen):
    pass

class PracticeWindow(Screen):
    pass

class TestWindow(Screen):
    pass

class KeyboardWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("main.kv") #loads kv no matter filename

class Main(App):
    def build(self):
        Window.clearcolor = (0.1176,0.1294,0.2471, 1)
        return kv

if __name__ == "__main__":
    Main().run()
