import kivy
from kivy.core.window import Window
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton

kivy.require('1.0.7')
import dir
from creditz import credit

Page_title = ['']


class DbPage(Screen, FloatLayout):
    def __init__(self, **kwargs):
        super(DbPage, self).__init__(**kwargs)
        self.padding = 20
        self.spacing = 10
        Window.size = (500, 300)
        with self.canvas.before:
            self.rect = Rectangle(source=dir.file('/res/wall.jpg'), size=Window.size, pos=self.pos)
        self.btn1 = Button(text='CREDIT', bold=True, size_hint=(.3, .2), pos_hint={'center_x': .3, 'center_y': .5},
                           background_color=(0, 1, 0, .8))
        self.btn1.bind(on_press=self.changeScreen)
        self.add_widget(self.btn1)

    def changeScreen(self, *args):
        self.manager.current = 'menu'


class EntryPage(Screen):
    mode = ''

    def __init__(self, **kwargs):
        super(EntryPage, self).__init__(**kwargs)
        self.padding = 20
        self.spacing = 10
        Window.size = (500, 300)
        with self.canvas.before:
            self.rect = Rectangle(source=dir.file('/res/wall.jpg'), size=Window.size, pos=self.pos)
        self.amount = TextInput(id='credit_amount', multiline=False, write_tab=False, size_hint=(.7, .1),
                                pos_hint={'center_x': .5, 'center_y': .8}, hint_text='Amount')
        self.add_widget(self.amount)
        self.recp = TextInput(id='credit_recp', multiline=False, write_tab=False, size_hint=(.7, .1),
                              pos_hint={'center_x': .5, 'center_y': .6}, hint_text='Name')
        self.add_widget(self.recp)
        self.purpose = TextInput(id='credit_purpose', multiline=False, write_tab=False, size_hint=(.7, .1),
                                 pos_hint={'center_x': .5, 'center_y': .4}, hint_text='Reason')
        self.add_widget(self.purpose)
        self.cash = CheckBox(id='Cash', size_hint=(.2, .1), pos_hint={'center_x': .15, 'center_y': .2})
        self.bank = CheckBox(id='Bank', size_hint=(.2, .1), pos_hint={'center_x': .8, 'center_y': .2})
        self.cash.bind(on_press=self.toggle)
        self.bank.bind(on_press=self.toggle)
        self.add_widget(self.cash)
        self.add_widget(self.bank)
        self.cash_L = Label(text='Cash', bold=True, size_hint=(.2, .1), pos_hint={'center_x': .23, 'center_y': .2})
        self.bank_L = Label(text='Bank', bold=True, size_hint=(.2, .1), pos_hint={'center_x': .88, 'center_y': .2})
        self.add_widget(self.cash_L)
        self.add_widget(self.bank_L)
        self.btn1 = Button(text='SUBMIT', bold=True, size_hint=(.3, .2), pos_hint={'center_x': .5, 'center_y': .1},
                           background_color=(0, 1, 0, .8))
        self.btn1.bind(on_press=self.store)
        self.add_widget(self.btn1)

    def changeScreen(self, *args):
        self.manager.current = 'db'

    def toggle(self, widget, *args):
        if widget.state == 'down':
            self.mode = widget.id

    def store(self, instance):
        credit.credit(self.amount.text, self.recp.text, self.purpose.text, self.mode, Page_title[-1])


class MenuPage(Screen):
    def __init__(self, **kwargs):
        super(MenuPage, self).__init__(**kwargs)
        box = FloatLayout
        box.padding = 20
        box.spacing = 10
        Window.size = (500, 300)
        with self.canvas.before:
            box.rect = Rectangle(source=dir.file('/res/wall.jpg'), size=Window.size, pos=self.pos)
        wel = Image(source=dir.file('/res/welcome.jpg'), size_hint=(1, .3), pos_hint={'top': .96})
        box.add_widget(self, wel)
        btn1 = Button(text='CREDIT', bold=True, size_hint=(.3, .2), pos_hint={'center_x': .3, 'center_y': .5},
                      background_color=(0, 1, 0, .8))
        btn1.bind(on_press=self.changeScreen)
        box.add_widget(self, btn1)
        btn2 = Button(text='DEBIT', bold=True, size_hint=(.3, .2), pos_hint={'center_x': .7, 'center_y': .5},
                      background_color=(1, 0, 0, .8))
        btn2.bind(on_press=self.changeScreen)
        box.add_widget(self, btn2)
        btn3 = Button(text='VAULT', bold=True, size_hint=(.3, .2), pos_hint={'center_x': .5, 'center_y': .25},
                      background_color=(.5, .5, .8, .8))
        btn3.bind(on_press=self.validate)
        box.add_widget(self, btn3)

    def validate(self, instance):
        print('worked!')

    def changeScreen(self, widget, *args):
        Page_title.append(widget.text)
        print(Page_title)
        self.manager.current = 'entry'


class StartUI(App):
    def build(self):
        m = ScreenManager(transition=WipeTransition())
        screen1 = MenuPage(name='menu')
        screen2 = EntryPage(name='entry')
        screen3 = DbPage(name='db')
        m.add_widget(screen1)
        m.add_widget(screen2)
        m.add_widget(screen3)
        return m


if __name__ == '__main__':
    StartUI().run()
