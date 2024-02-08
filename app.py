from kivy.app import App
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color

class CanvasExample4(Widget):
    repeat = 1
    count = 0
    text_height = 0
    last_x = 0
    first_letter_start_pos = dp(250)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.ellipse = Ellipse(pos=(dp(200), self.center_y), size=(dp(20), dp(20)))
            # self.rect = Rectangle(pos=self.ellipse.pos, )
        Clock.schedule_interval(self.update, 1/10)
    def on_size(self, *args):
        self.ellipse.pos = (self.first_letter_start_pos, self.center_y)

    def update(self, dt):
        x, y = self.ellipse.pos
        
        #Animation for F
        if self.repeat == 1 and y+dp(10)+self.ellipse.size[1] <= dp(400):
            y += dp(10)
        if self.repeat == 1 and y+dp(10)+self.ellipse.size[1] >= dp(400):
            if x+dp(10)+self.ellipse.size[0] <= dp(100)+self.first_letter_start_pos:
                x += dp(10)
                self.text_height = y
            else: 
                self.ellipse.pos = (self.first_letter_start_pos, self.center_y+(y-self.center_y)/2)
                self.repeat = 2
                return
        if self.repeat == 2 and x+dp(10)+self.ellipse.size[0] <= dp(100)+self.first_letter_start_pos:
            x += dp(10)
        if self.repeat == 2 and x+dp(10)+self.ellipse.size[0] > dp(100)+self.first_letter_start_pos:
            self.ellipse.pos = (x, self.center_y)
            self.repeat = 3
            return

        # Animation for A
        if self.repeat == 3 and y+dp(10)+self.ellipse.size[1] <= dp(400):
            x += dp(10)
            y += dp(20)
            self.count += 1
        if self.repeat == 3 and y+dp(10)+self.ellipse.size[1] > dp(400):
            self.ellipse.pos = (x-dp(10)*self.count/2, y-dp(20)*self.count/2)
            self.count = 0
            self.repeat = 4
            return
        if self.repeat == 4 and x+dp(10)+self.ellipse.size[0] <= dp(200)+self.first_letter_start_pos:
            self.count += 1
            x += dp(10)
        if self.repeat == 4 and x+dp(10)+self.ellipse.size[0] > dp(200)+self.first_letter_start_pos:
            self.ellipse.pos = (x-dp(10)*self.count/2, self.text_height)
            self.repeat = 5
            return
        if self.repeat == 5 and x+dp(10)+self.ellipse.size[0] <= dp(200)+self.first_letter_start_pos:
            x += dp(10)
            y -= dp(20)
        if self.repeat == 5 and x+dp(10)+self.ellipse.size[0] > dp(200)+self.first_letter_start_pos:
            self.ellipse.pos = (x, self.center_y)
            self.count = 0
            self.repeat = 6
            return 
        
        # Animation for B
        if self.repeat == 6 and y+dp(10)+self.ellipse.size[1] <= dp(400):
            y += dp(10)
            self.last_x = x
        if self.repeat == 6 and y+dp(10)+self.ellipse.size[1] > dp(400):
            if x+dp(10)+self.ellipse.size[0] <= dp(300)+self.first_letter_start_pos:
                x += dp(10)
            else:
                self.repeat = 7
                return
        if self.repeat == 7 and y-dp(10)-self.ellipse.size[1] >= (self.text_height-self.center_y)/2+self.center_y:
            y -= dp(10)
        if self.repeat == 7 and y-dp(10)-self.ellipse.size[1] < (self.text_height-self.center_y)/2+self.center_y:
            if x-dp(10)-self.ellipse.size[0] >= self.last_x:
                x -= dp(10)
                self.count += 1
            else:
                self.ellipse.pos = (x+dp(10)*self.count, y)
                self.count = 0
                self.repeat = 8
                return
        if self.repeat == 8 and y-dp(10)-self.ellipse.size[1] >= self.center_y:     
            y -= dp(10)
        if self.repeat == 8 and y-dp(10)-self.ellipse.size[1] < self.center_y: 
            if x-dp(10)-self.ellipse.size[0] >= self.last_x:
                x -= dp(10)
                self.count += 1
            else:
                self.ellipse.pos = (x+dp(10)*self.count, y)
                self.count = 0
                self.repeat =0
                return       
        self.ellipse.pos = (x, y)


class TheMainApp(App):
    def build(self):
        return CanvasExample4()

TheMainApp().run()