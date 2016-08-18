from kivy.app        import App
from kivy.uix.widget import Widget
from kivy.clock      import Clock
from kivy.properties import StringProperty, NumericProperty

from random          import randint
from time            import sleep

import serial

# LALALALALALALALALALA

# btstring = '/dev/tty.Dekoboko-0000-DevB'
# bt = None

# class swLogging(Switch):
#     def callback(instance, value):
#         print('the switch', instance, 'is', value)

class GuiApp(App):
    def build(self):
        gui = RootWidget()
        Clock.schedule_interval(gui.update, 1.0 / 10.0)
        # gui.connect()
        gui.build() # necessary? correct? how to init labels etc otherwise?
        return gui


class RootWidget(Widget):

    status      = StringProperty  ()
    counter     = NumericProperty ()
    counter_str = StringProperty  ()

    def build(self):
        self.status      = 'start'
        self.counter     = 0
        self.counter_str = '0'
        # try:
        #     print 'connecting...'
        #     # bt = serial.Serial(btstring, 115200)
        # except:
        #     print 'Failed to connect'
        #     exit()

    def update(self, dt):
        line = randint(0,100)
        # line = bt.readline()
        # print(line)

    def hello(self):
        self.status = 'stop'
        self.counter += 1
        self.counter_str = str(self.counter)
        print("Hello world!")
        # gui.lb_status.text = 'tadaa'



if __name__ == '__main__':
    GuiApp().run()
