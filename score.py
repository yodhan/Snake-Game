from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.goto(0,350)
        self.hideturtle()
        self.updatescoreboards()
    
    def updatescoreboards(self):
        self.write(f"Score:{self.score}", align="center", font=("Arial",24,"normal"))
    
    def gameover(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=("Arial",28,"normal"))
    
    def updatescore(self):
        self.score+=1
        self.clear()
        self.updatescoreboards()