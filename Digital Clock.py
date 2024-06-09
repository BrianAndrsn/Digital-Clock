from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window

import time

Window.size = (700, 300)

Builder.load_string("""

<Layout>
    ClockLabel:
        id: clock_label
        size_hint: 0.75, 1
        font_size: 120
        color: 'blue'
        markup: True        

""")

class Layout(BoxLayout):
    pass

class ClockLabel(Label):
    def __init__(self, **kwargs):
        super(ClockLabel, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)

    def update(self, *args):
        self.text = f"{time.strftime('%H:%M:%S A.M.')}"

class DigitalClock(App):
    def build(self):
        return Layout()

MyApp = DigitalClock()
MyApp.run()