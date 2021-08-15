import turtle as t
from turtle import *

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
startingpos = [(0,0), (-20, 0), (-40, 0)]
segments = []
for i in startingpos:
    snake = Turtle(shape="square")
    snake.color("white")
    snake.goto(i)
    segments.append(snake)


screen.exitonclick()
