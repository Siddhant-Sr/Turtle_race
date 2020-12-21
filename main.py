from turtle import Turtle, Screen
import random

race = False
screen = Screen()
screen.setup(width= 500, height= 400)
color = ["red", "yellow", "purple", "pink", "brown", "blue"]
y = [-70, -40, -10, 20, 50, 80]
bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter a color")
all_turtle = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y[turtle_index])
    all_turtle.append(new_turtle)

if bet:
    race = True


while race:
    for turtles in all_turtle:
        if turtles.xcor()>230:
            race =False
            winning_color = turtles.pencolor()
            if winning_color == bet:
                print(f"You've won! The {winning_color} turtle is the winner ")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner ")
        turtles.forward(random.randint(0,10))

screen.exitonclick()
