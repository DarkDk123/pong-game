from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("Red")
        self.penup()
        self.movedisx = 10
        self.movedisy = 10
    
    def move(self):
        self.new_x = self.xcor() + self.movedisx
        self.new_y = self.ycor() + self.movedisy
        self.goto(self.new_x, self.new_y)

    def bounce_y_ball(self):
        self.movedisy *= -1

    def bounce_x_ball(self):
        self.movedisx *= -1

    def reset_game(self):
        self.goto(0, 0)
        self.bounce_x_ball()
        
