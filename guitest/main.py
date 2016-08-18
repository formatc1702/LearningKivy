from kivy.app        import App
from kivy.uix.widget import Widget
from kivy.clock      import Clock

from random          import randint
from time            import sleep

import serial

btstring = '/dev/tty.Dekoboko-0000-DevB'
bt = None

class GuiApp(App):
    def build(self):
        gui = RootWidget()
        Clock.schedule_interval(gui.update, 1.0 / 10.0)
        # gui.connect()
        return gui

class RootWidget(Widget):
    def build(self):
        try:
            print 'connecting...'
            bt = serial.Serial(btstring, 115200)
        except:
            print 'Failed to connect'
            exit()

    def update(self, dt):
        line = randint(0,100)
        # line = bt.readline()
        # print(line)


if __name__ == '__main__':
    GuiApp().run()
