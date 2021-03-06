import kivy
kivy.require('1.2.1')

from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty


class Controller(FloatLayout):

    label_wid = ObjectProperty()
    info = StringProperty()

    def do_action(self):
        self.label_wid.text = 'Label after Press'
        self.info = 'New info text'

class ControllerApp(App):

    def build(self):
        return Controller(info='Hello World')


if __name__ == '__main__':
    ControllerApp().run()