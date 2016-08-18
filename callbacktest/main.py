from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class myLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(myLayout, self).__init__(**kwargs)

        btn = Button(text='Click')
        btn.bind(on_press=self.clk)

        self.add_widget(btn)

    def clk(self, obj):
        print('Hello world!')

class CallbacktestApp(App):
    def build(self):
        mL = myLayout()
        return mL

if __name__ == '__main__':
    CallbacktestApp().run()
