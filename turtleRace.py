from turtle import Turtle, Screen
import turtle as t
import random

screen = Screen()
screen.setup(500, 400)
bet = screen.textinput(title="Make your bet.", prompt="Which color turtle will win thw race? Make a guess: ")
colors = ['red', 'pink', 'green', 'blue', 'black', 'orange', 'purple']
y_position = [-150, -100, -50, 0, 50, 100, 150]
all_turtles = []
for i in range(0,7):
    new = Turtle(shape="turtle")
    new.penup()
    new.color(colors[i])
    new.goto(-230, y_position[i])
    all_turtles.append(new)

if bet:
    race_on = True

while race_on:
    for i in all_turtles:
        if i.xcor() > 230:
            race_on = False
            winner = i.pencolor()
            if winner == bet:
                print(f"You have won! The {winner} is the winner.")
            else:
                print(f"You have lost! The {winner} is the winner.")
        random_distance = random.randint(0,5)
        i.forward(random_distance)
        
screen.exitonclick()
