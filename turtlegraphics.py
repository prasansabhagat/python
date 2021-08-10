#turtle graphics: https://docs.python.org/3/library/turtle.html
#turtle colors: https://cs111.wellesley.edu/labs/lab01/colors
import turtle as t
from turtle import Turtle, Screen

# tim = Turtle()
# tim.shape("turtle")
# tim.color("red")
# tim.forward(180)
# tim.right(90)
# tim.forward(180)
# tim.right(90)
# tim.forward(180)
# tim.right(90)
# tim.forward(180)
   #a square#


# tim = Turtle()
# for i in range(0):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
   #dashed line#
import random
tim = Turtle()
# def color():
#    R = random.random()
#    G = random.random()
#    B = random.random()
#    return tim.color(R, G, B)
COLORS = ["blue", "black", "brown", "red", "yellow", "green", "orange", "beige", "turquoise", "pink"]

#for random color:
t.colormode(255)

def randomcolor():
   r = random.randint(0,255)
   g = random.randint(0, 255)
   b = random.randint(0, 255)
   randomcolor = (r, g, b)
   return randomcolor



directions = [0, 90, 180, 270]
# for i in range(3):
#    tim.color(random.choice(COLORS))
#    tim.forward(100)
#    tim.right(360/3)
   
# for i in range(4):
#    tim.color(random.choice(COLORS))
#    tim.forward(100)
#    tim.right(360/4)
   
# for i in range(5):
#    tim.color(random.choice(COLORS))
#    tim.forward(100)
#    tim.right(360/5)
# for i in range(6):
#    tim.color(random.choice(COLORS))
#    tim.forward(100)
#    tim.right(360/6)
# for i in range(7):
#    tim.color(random.choice(COLORS))
#    tim.forward(100)
#    tim.right(360/7)
# for i in range(8):
#    tim.color(random.choice(COLORS))
#    tim.forward(100)
#    tim.right(360/8)
# for i in range(9):
#    tim.color(random.choice(COLORS))
#    tim.forward(100)
#    tim.right(360/9)
# for i in range(10):
#    tim.color(random.choice(COLORS))
#    tim.forward(100)
#    tim.right(360/10)


# def draw(sides):
#    angle = 360 / sides
#    for i in range(sides):
#       tim.forward(100)
#       tim.right(angle)

# for i in range(3, 11):
#      tim.color(random.choice(COLORS))
#      draw(i)

for i in range(300):
      tim.width(10)
      tim.speed('fastest')
      tim.color(randomcolor())
      tim.forward(40)
      tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
      
