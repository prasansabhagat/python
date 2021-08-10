import random
import turtle as t
from turtle import Turtle, Screen

tim = Turtle()
t.colormode(255)

def randomcolor():
   r = random.randint(0, 255)
   g = random.randint(0, 255)
   b = random.randint(0, 255)
   randomcolor = (r, g, b)
   return randomcolor


for i in range(100):
    tim.color(randomcolor())
    tim.circle(100)
    tim.left(10)
    tim.speed("fastest")

screen = Screen()
screen.exitonclick()
