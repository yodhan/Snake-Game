from turtle import Turtle,Screen, goto
import turtle
initialPositions=[(0,0),(-20,0),(-40,0)]
moveDist=10

class Snake:
    def __init__(self) -> None:
        self.res=[]
        self.createsnake()
        self.head=self.res[0]

    def createsnake(self):
        for i in initialPositions:
            self.createbody(i)

    def createbody(self,position):
        root=Turtle("square")
        root.penup()
        root.color("green")
        root.speed("fastest")
        root.goto(position)
        self.res.append(root)
    
    def extend(self):
        self.createbody(self.res[-1].position())

    def move(self):
        for i in range(len(self.res)-1,0,-1):
            nx=self.res[i-1].xcor()
            ny=self.res[i-1].ycor()
            self.res[i].goto(x=nx,y=ny)
        self.head.speed("fastest")
        self.head.forward(moveDist)

    
    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)      
