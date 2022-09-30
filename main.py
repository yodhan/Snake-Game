from turtle import Screen
import time
from food import Food
from score import Score
from snake import Snake

screen=Screen()
screen.setup(width=800,height=800)
screen.bgcolor("grey")
screen.tracer(0)
snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
isTrue=True
while isTrue:
    snake.move()
    screen.update()
    time.sleep(0.1)

    #detecting collision distance method is used to compare distance
    #between two turtle onrturtle.distance(two turtle)

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.updatescore()
    if snake.head.xcor()<(-380) or snake.head.xcor()>380 or snake.head.ycor()<(-380) or snake.head.ycor()>(380):
        score.gameover()
        isTrue=False
    for seg in snake.res[1:]:
        if snake.head.distance(seg)<5:
            score.gameover()
            isTrue=False
screen.exitonclickes