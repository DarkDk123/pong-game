from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, color , position):
        super().__init__()
        self.penup()
        self.color(color)
        self.shape("square") 
        self.shapesize(stretch_wid=10, stretch_len=1)       
        self.goto(position)
    
    def up(self):
        if self.ycor() < 200:
            self.new_y = self.ycor() + 30
            self.goto(self.xcor(), self.new_y)
    
    def down(self):
        if self.ycor() > -200:
            self.new_y = self.ycor() - 30 
            self.goto(self.xcor(), self.new_y)
        
