from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_clkwise():
    newiheading = tim.heading() + 10
    tim.setheading(newiheading)


def move_anticlkwise():
    newheading = tim.heading() - 10
    tim.setheading(newheading)


def clear():
    tim.clear()
    tim.home()


screen.listen()
screen.onkey(move_forward, "f")
screen.onkey( move_backward, "b")
screen.onkey(move_clkwise, "c",)
screen.onkey(move_anticlkwise, "a",)
screen.onkey(clear, "h",)
screen.exitonclick()
