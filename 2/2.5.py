from random import randint
import turtle


number_of_turtles = 100
steps_of_time_number = 1


pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]

for unit in pool:
    unit.shapesize(0.1)
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))
for x in range(100):
    for unit in pool:
        unit.speed(0)
        unit.forward(randint(-200,200))
        unit.left(randint(0,360))
    

   

