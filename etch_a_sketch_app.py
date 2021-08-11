from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_clkwise():
    tim.right(10)


def move_anticlkwise():
    tim.left(10)



screen.listen()
screen.onkey("q", move_forward)
screen.onkey("w", move_backward)
screen.onkey("e", move_clkwise)
screen.onkey("r", move_anticlkwise)
screen.exitonclick()
