from turtle import Turtle
import time


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.lscore = 0
        self.rscore = 0
        self.scoreupdate()
    
    def scoreupdate(self):
        self.clear()
        self.goto(-290, 235)
        self.write(f"{self.lscore}", align= "center", font=("courier", 50, "normal"))
        self.goto(290, 235)
        self.write(f"{self.rscore}", align= "center", font=("courier", 50, "normal"))
    
    def l_point(self):
        self.lscore += 1
        self.scoreupdate()

    def r_point(self):
        self.rscore += 1
        self.scoreupdate()
    
    def game_reset(self):
        self.goto(0,0)
        self.clear()
        self.write("Restarting.....", align= "center", font=("courier", 30, "normal"))
        time.sleep(0.2)
        self.clear()
        self.scoreupdate()    