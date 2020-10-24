# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 20:03:10 2019

@author: Grivois
"""


from kjv_methods import Biblework
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.button import Button
import gesture_box as gesture
from kivy.properties import StringProperty

#KIVY_TEXT = sdl2



class Bibliomancy(Widget):
    
    pass

p = Biblework().logos()


    
class Swiper(gesture.GestureBox):
    pass

class Bibleworkscreen(Screen):
    
    info = StringProperty()
#    @property
    def plot(self):
        b = Biblework()
        l = b.logos()
        self.info = l[1]
        return l

    pass

class ScreenManagement(ScreenManager):
    pass

class Main_menu(Screen):

    pass

class About(Screen):
    pass

class Instructions(Screen):
    pass

class BackGround(Image):
    pass

class Help(Screen):
    pass

class BibliomancyApp(App): 
    def build(self):

        return ScreenManagement()
    
    
if __name__ == '__main__':
    BibliomancyApp().run()
