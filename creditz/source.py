from kivy.core.window import Window
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

import dir
from creditz.db import dbk


class ImageButton(ButtonBehavior, Image):
    pass


class VaultPage(Screen, FloatLayout, ButtonBehavior):
    fill = ...  # type: TextInput

    def __init__(self, **kwargs):
        super(VaultPage, self).__init__(**kwargs)
        self.padding = 20
        self.spacing = 10
        Window.size = (500, 300)
        with self.canvas.before:
            self.rect = Rectangle(source=dir.file('/res/wall.jpg'), size=Window.size, pos=self.pos)
        self.home = ImageButton(source=dir.file('/res/home_btn.jpg'), size_hint=(.15, .15), pos_hint={'center_y': .9,
                                                                                                'center_x': .9})
        self.home.bind(on_release=self.changeScreen)
        self.add_widget(self.home)
        self.btn1 = Button(text='SUMMARY', bold=True, size_hint=(.3, .15), pos_hint={'center_x': .3, 'center_y': .1},
                           background_color=(0, 1, 0, .8))
        self.btn1.bind(on_press=self.summary_gen)
        self.add_widget(self.btn1)
        self.btn2 = Button(text='ACCT BALANCE', bold=True, size_hint=(.3, .15), pos_hint={'center_x': .7, 'center_y': .1},
                           background_color=(0, 1, 0, .8))
        self.btn2.bind(on_press=self.adapt)
        self.add_widget(self.btn2)

    def changeScreen(self, *args):
        self.manager.current = 'menu'

    def adapt(self, instance, *args):
        try:
            a = VaultPage
            a.remove_widget(self, self.fill)
            a.remove_widget(self, self.btn1)
            a.remove_widget(self, self.fold)
        except:
            pass
        finally:
            self.fill = TextInput(id='fill', size_hint=(.5, .5), pos_hint={'center_x': .7, 'center_y': .5}, multiline=True,
                                  hint_text='Click Generate to view info', background_color=(1, 1, 1, .5), font_size=15)
            self.add_widget(self.fill)
            self.btn1 = Button(text='Generate', bold=True, size_hint=(.3, .15), pos_hint={'center_x': .2, 'center_y': .5},
                               background_color=(0, 1, 0, .8))
            self.btn1.bind(on_press=self.generate)
            self.add_widget(self.btn1)

    def generate(self, *args):
        x = dbk.analyze()
        statement = ''
        for i in x:
            if type(i) is str:
                statement += '%s' % i
                statement += '\n'
        self.fill.text = str(statement)

    def summary_gen(self, instance, *args):
        try:
            a = VaultPage
            a.remove_widget(self, self.fold)
            a.remove_widget(self, self.fill)
            a.remove_widget(self, self.btn1)

        except:
            pass
        finally:
            self.fold = TextInput(id='fold', size_hint=(.7, .6), pos_hint={'center_x': .5, 'center_y': .5},
                                  multiline=True,
                                  hint_text='Click Generate to view info', background_color=(1, 1, 1, .5))
            self.add_widget(self.fold)
            m = dbk.call_part()
            self.fold.text = m


'''
from creditz.credit import *
from creditz.debit import *
from creditz import summary as sum


def select(self):
    a = 0
    try:
        a = int(input('Credit OR Debit OR Summary OR View_Remaining_funds OR Exit (1 OR 2 OR 3 OR 4 OR Any_key)? : '))
        if a == 1:
            start_credit(self)
        elif a == 2:
            start_debit(self)
        elif a == 3:
            sum.get()
        elif a == 4:
            sum.balance()
        else:
            exit()
    except:
        select(self)


def exitz(self):
    return None


def start_credit(self):
    credit.entry_amount()


def start_debit(self):
    debit.entry_amount()
'''
